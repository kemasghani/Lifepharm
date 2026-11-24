"""End-to-end SEO check of a store's draft theme (or its live theme with --live). Read-only.

The categories, their weights and several rules (FAQ rich results retired, which AI crawler decides which
claim, llms.txt carries no weight) follow the claude-seo audit skill v2.6.2 by AgriciDaniel (MIT),
https://github.com/AgriciDaniel/claude-seo. That skill's own fetchers use plain HTTP, which the storefront
answers with 429 and which cannot open a draft theme, so this check drives a real browser instead (L-059).

What it reads on a sample of each page type (home, collections, products, pages, policy):
  Technical SEO      status, canonical, robots meta, lang, viewport, hreflang, security headers, robots.txt, sitemap
  On-Page SEO        title, meta description, h1, heading order, Open Graph, duplicate titles and descriptions
  Content Quality    word count of the main content (thin pages), trust pages (about, contact, policies)
  Schema             JSON-LD that parses; Organization, WebSite, Product (offers, brand, rating), BreadcrumbList
  Performance        lab LCP, CLS, TTFB, page weight, DOM size at 390 wide, unthrottled (not field data)
  AI Search Readiness search crawlers allowed in robots.txt, content present without JavaScript
  Images             alt attribute, width and height, lazy loading of the LCP image

Usage: uv run --no-project --with playwright python tools/seo/seo_check.py [us uk eu] [--live] [--out DIR]
       Writes <DIR>/seo-<store>.json (default tools/seo/reports, git-ignored). Set LP_CHROME if system Chrome is not installed.
       Exit code 1 when a Critical or High finding exists."""
import asyncio, json, os, re, sys
from playwright.async_api import async_playwright

STORES = {
    'uk': ('https://uk.lifepharm.com', '189821452674'),
    'us': ('https://shop.lifepharm.com', '193373995317'),
    'eu': ('https://europe.lifepharm.com', '168919728345'),
}
WEIGHTS = {'Technical SEO': 22, 'Content Quality': 23, 'On-Page SEO': 20, 'Schema': 10, 'Performance': 10, 'AI Search Readiness': 10, 'Images': 5}
DEDUCT = {'Critical': 25, 'High': 12, 'Medium': 6, 'Low': 2, 'Info': 0}
PRODUCTS = ['laminine', 'omega', 'cellnergy-wellness', 'lamiderm-apex-smart-serum']
SEARCH_BOTS = ['OAI-SearchBot', 'Claude-SearchBot', 'PerplexityBot', 'Googlebot', 'Bingbot']
UA = 'Mozilla/5.0 (iPhone; CPU iPhone OS 17_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Mobile/15E148 Safari/604.1'
LAUNCH = {'executable_path': os.environ['LP_CHROME']} if os.environ.get('LP_CHROME') else {'channel': 'chrome'}
LIVE = '--live' in sys.argv
OUT = sys.argv[sys.argv.index('--out') + 1] if '--out' in sys.argv else os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports')

VITALS = r"""(() => { window.__lp = { lcp: 0, lcpEl: null, cls: 0 };
  try { new PerformanceObserver(l => { for (const e of l.getEntries()) { window.__lp.lcp = e.startTime; const el = e.element;
      window.__lp.lcpEl = el ? { tag: el.tagName, loading: el.getAttribute('loading'), priority: el.getAttribute('fetchpriority'), src: (el.currentSrc || el.src || '').split('/').pop().split('?')[0].slice(0, 60) } : null; } }).observe({ type: 'largest-contentful-paint', buffered: true }); } catch (e) {}
  try { new PerformanceObserver(l => { for (const e of l.getEntries()) if (!e.hadRecentInput) window.__lp.cls += e.value; }).observe({ type: 'layout-shift', buffered: true }); } catch (e) {} })()"""

PAGE = r"""async () => {
  const q = s => document.querySelector(s), qa = s => [...document.querySelectorAll(s)];
  const meta = n => (q(`meta[name="${n}"]`) || q(`meta[property="${n}"]`) || {}).content || '';
  const main = q('main') || document.body;
  const words = t => (t.replace(/\s+/g, ' ').trim().match(/\S+/g) || []).length;
  const ld = [], ldErrors = [];
  for (const s of qa('script[type="application/ld+json"]')) { try { const v = JSON.parse(s.textContent); (Array.isArray(v) ? v : (v['@graph'] || [v])).forEach(x => ld.push(x)); } catch (e) { ldErrors.push(String(e).slice(0, 80)); } }
  const imgs = qa('img').filter(i => !i.closest('#preview-bar-iframe, #stamped-main-widget, .stamped-review-product'));
  const heads = qa('h1,h2,h3,h4,h5,h6').filter(h => h.getBoundingClientRect().height > 0 || h.tagName === 'H1').map(h => Number(h.tagName[1]));
  let skips = 0; for (let i = 1; i < heads.length; i++) if (heads[i] - heads[i - 1] > 1) skips++;
  const links = qa('a[href]'), internal = links.filter(a => a.hostname === location.hostname);
  let raw = ''; try { raw = await fetch(location.pathname + location.search, { credentials: 'include' }).then(r => r.text()); } catch (e) {}
  const rawDoc = raw ? new DOMParser().parseFromString(raw, 'text/html') : null;
  const rawMain = rawDoc ? (rawDoc.querySelector('main') || rawDoc.body) : null;
  if (rawMain) rawMain.querySelectorAll('script,style,noscript,template').forEach(n => n.remove());
  const nav = performance.getEntriesByType('navigation')[0] || {};
  const res = performance.getEntriesByType('resource');
  const origin3p = new Set(res.map(r => { try { return new URL(r.name).hostname; } catch (e) { return ''; } }).filter(h => h && !h.endsWith('lifepharm.com') && !h.endsWith('shopify.com') && !h.endsWith('shopifycdn.com')));
  return {
    theme: window.Shopify && Shopify.theme ? String(Shopify.theme.id) : null, url: location.href, lang: document.documentElement.lang || '',
    title: document.title || '', description: meta('description'), canonical: (q('link[rel="canonical"]') || {}).href || '', robots: meta('robots'),
    viewport: meta('viewport'), hreflang: qa('link[rel="alternate"][hreflang]').map(l => l.hreflang + ' ' + l.href),
    og: { title: meta('og:title'), description: meta('og:description'), image: meta('og:image'), url: meta('og:url'), type: meta('og:type') }, twitter: meta('twitter:card'),
    h1: qa('h1').map(h => h.innerText.replace(/\s+/g, ' ').trim().slice(0, 70)), headingSkips: skips, headings: heads.length,
    words: words(main.innerText || ''), rawWords: rawMain ? words(rawMain.textContent || '') : null, rawHasTitle: rawDoc ? !!(rawDoc.title || '').trim() : null,
    ld, ldErrors, rawLd: rawDoc ? rawDoc.querySelectorAll('script[type="application/ld+json"]').length : null,
    images: imgs.length, noAltAttr: imgs.filter(i => !i.hasAttribute('alt')).length, emptyAlt: imgs.filter(i => i.getAttribute('alt') === '').length,
    noSize: imgs.filter(i => !(i.getAttribute('width') && i.getAttribute('height')) && !i.closest('svg')).length,
    eagerBelow: imgs.filter(i => i.getAttribute('loading') !== 'lazy' && i.getBoundingClientRect().top + scrollY > innerHeight * 2).length,
    links: links.length, internal: internal.length, emptyLinks: links.filter(a => !(a.textContent || '').trim() && !a.getAttribute('aria-label') && a.getAttribute('aria-hidden') !== 'true' && !a.querySelector('img[alt]:not([alt=""]), svg[aria-label], svg title')).length,
    hashLinks: links.filter(a => a.getAttribute('href') === '#').length, mixed: res.filter(r => r.name.startsWith('http://')).length,
    dom: document.getElementsByTagName('*').length, blocking: qa('head script[src]:not([async]):not([defer]):not([type="module"])').length,
    ttfb: Math.round(nav.responseStart || 0), load: Math.round(nav.loadEventEnd || 0), transfer: Math.round(res.reduce((a, r) => a + (r.transferSize || 0), nav.transferSize || 0) / 1024), requests: res.length, thirdParties: origin3p.size,
    lcp: Math.round(window.__lp ? window.__lp.lcp : 0), lcpEl: window.__lp ? window.__lp.lcpEl : null, cls: window.__lp ? Math.round(window.__lp.cls * 1000) / 1000 : null,
    hscroll: document.documentElement.scrollWidth > innerWidth + 1,
    nav: [...new Set(internal.map(a => a.pathname.replace(/\/$/, '') || '/'))] }; }"""

SITE = r"""async () => { const get = async p => { try { const r = await fetch(p); return { status: r.status, text: (await r.text()).slice(0, 200000) }; } catch (e) { return { status: 0, text: '' }; } };
  const products = await fetch('/products.json?limit=250').then(r => r.json()).then(d => d.products.map(p => p.handle)).catch(() => []);
  return { robots: await get('/robots.txt'), sitemap: await get('/sitemap.xml'), llms: await get('/llms.txt'), products }; }"""


def kind(path):
    for prefix, name in (('/products/', 'product'), ('/collections/', 'collection'), ('/pages/', 'page'), ('/policies/', 'policy'), ('/blogs/', 'blog')):
        if path.startswith(prefix): return name
    return 'home' if path in ('/', '') else 'other'


def types(ld):
    out = []
    for item in ld:
        t = item.get('@type') if isinstance(item, dict) else None
        out += t if isinstance(t, list) else [t] if t else []
    return out


def robots_blocks(text, bot):
    """True when robots.txt disallows the whole site for this user agent (its own group, else the * group)."""
    groups, agents, in_rules = {}, [], False
    for line in text.splitlines():
        line = line.split('#')[0].strip()
        if ':' not in line: continue
        key, value = [x.strip() for x in line.split(':', 1)]
        key = key.lower()
        if key == 'user-agent':
            if in_rules: agents, in_rules = [], False
            agents.append(value.lower()); groups.setdefault(value.lower(), [])
        elif key in ('allow', 'disallow'):
            in_rules = True
            for agent in agents: groups[agent].append((key, value))
    rules = groups.get(bot.lower(), groups.get('*', []))
    return ('disallow', '/') in rules and ('allow', '/') not in rules


def findings_for(store, base, pages, site):
    F = []
    def add(cat, sev, text, affected=None, total=None):
        share = (len(affected) / total) if affected is not None and total else 1
        F.append({'category': cat, 'severity': sev, 'finding': text, 'pages': affected or [], 'share': round(share, 2)})
    def where(test, group=None):
        rows = [p for p in pages if (group is None or p['kind'] in group)]
        return [p['path'] for p in rows if test(p)], len(rows)
    host = base.split('//')[1]
    # A page whose canonical names another page on this store declares itself a copy; it is judged as that page, not twice.
    def copy_of(p): return bool(p['canonical']) and host in p['canonical'] and p['canonical'].split(host)[1].split('?')[0].rstrip('/') != p['path'].rstrip('/')
    copies = [p['path'] for p in pages if copy_of(p)]
    if copies: F.append({'category': 'Technical SEO', 'severity': 'Info', 'finding': 'Page names another page as its canonical (a declared copy, left out of the on-page checks)', 'pages': copies, 'share': 0})
    pages = [p for p in pages if not copy_of(p)]

    # Technical SEO
    a, n = where(lambda p: p['status'] != 200); a and add('Technical SEO', 'High', 'Page does not answer 200', a, n)
    a, n = where(lambda p: not p['canonical']); a and add('Technical SEO', 'High', 'No canonical link', a, n)
    a, n = where(lambda p: p['canonical'] and host not in p['canonical']); a and add('Technical SEO', 'High', 'Canonical points at another host', a, n)
    a, n = where(lambda p: 'noindex' in p['robots'].lower(), ('home', 'product', 'collection', 'page')); a and add('Technical SEO', 'Critical' if LIVE else 'Info', 'robots meta says noindex' + ('' if LIVE else ' (draft preview; confirm on the live theme)'), a, n)
    a, n = where(lambda p: not p['lang']); a and add('Technical SEO', 'Medium', 'html element has no lang', a, n)
    a, n = where(lambda p: 'width=device-width' not in p['viewport']); a and add('Technical SEO', 'High', 'No mobile viewport meta', a, n)
    a, n = where(lambda p: p['mixed'] > 0); a and add('Technical SEO', 'Medium', 'Resources loaded over http', a, n)
    a, n = where(lambda p: p['hscroll']); a and add('Technical SEO', 'Medium', 'Sideways scroll at 390 wide', a, n)
    a, n = where(lambda p: not p['hreflang']); a and add('Technical SEO', 'Medium', 'No hreflang links, while the same English pages are served on shop., uk. and europe.lifepharm.com', a, n)
    a, n = where(lambda p: not p['headers'].get('strict-transport-security')); a and add('Technical SEO', 'Low', 'No Strict-Transport-Security header', a, n)
    a, n = where(lambda p: not p['headers'].get('x-content-type-options')); a and add('Technical SEO', 'Low', 'No X-Content-Type-Options header', a, n)
    robots = site['robots']['text'] if site['robots']['status'] == 200 else ''
    if not robots: add('Technical SEO', 'High', 'robots.txt does not answer 200')
    elif 'sitemap:' not in robots.lower(): add('Technical SEO', 'Medium', 'robots.txt names no sitemap')
    if site['sitemap']['status'] != 200 or '<sitemap' not in site['sitemap']['text']: add('Technical SEO', 'High', 'sitemap.xml is missing or lists no child sitemaps')
    for bot in ('Googlebot', 'Bingbot'):
        if robots and robots_blocks(robots, bot): add('Technical SEO', 'Critical', f'robots.txt blocks {bot} from the whole site')

    # On-Page SEO
    a, n = where(lambda p: not p['title'].strip()); a and add('On-Page SEO', 'Critical', 'No title', a, n)
    a, n = where(lambda p: 0 < len(p['title']) < 25); a and add('On-Page SEO', 'Low', 'Title shorter than 25 characters', a, n)
    a, n = where(lambda p: len(p['title']) > 65); a and add('On-Page SEO', 'Low', 'Title longer than 65 characters (cut in results)', a, n)
    a, n = where(lambda p: not p['description'].strip(), ('home', 'product', 'collection', 'page')); a and add('On-Page SEO', 'High', 'No meta description', a, n)
    a, n = where(lambda p: 0 < len(p['description']) < 70, ('home', 'product', 'collection', 'page')); a and add('On-Page SEO', 'Low', 'Meta description shorter than 70 characters', a, n)
    a, n = where(lambda p: len(p['description']) > 165, ('home', 'product', 'collection', 'page')); a and add('On-Page SEO', 'Low', 'Meta description longer than 165 characters (cut in results)', a, n)
    for field, label in (('title', 'title'), ('description', 'meta description')):
        seen = {}
        for p in pages:
            if p[field].strip(): seen.setdefault(p[field].strip(), []).append(p['path'])
        dup = [x for v in seen.values() if len(v) > 1 for x in v]
        dup and add('On-Page SEO', 'Medium', f'The same {label} on more than one page', dup, len(pages))
    a, n = where(lambda p: len(p['h1']) == 0); a and add('On-Page SEO', 'High', 'No h1', a, n)
    a, n = where(lambda p: len(p['h1']) > 1); a and add('On-Page SEO', 'Medium', 'More than one h1', a, n)
    a, n = where(lambda p: p['headingSkips'] > 2); a and add('On-Page SEO', 'Low', 'Heading levels skip (for example h2 to h4) more than twice', a, n)
    a, n = where(lambda p: not p['og']['title'] or not p['og']['image']); a and add('On-Page SEO', 'Medium', 'Open Graph title or image missing (link previews)', a, n)
    a, n = where(lambda p: not p['twitter']); a and add('On-Page SEO', 'Low', 'No twitter:card', a, n)
    a, n = where(lambda p: p['emptyLinks'] > 3); a and add('On-Page SEO', 'Low', 'More than three links with no text or label', a, n)

    # Content Quality (what a script can measure; E-E-A-T needs a reader)
    a, n = where(lambda p: p['words'] < 150, ('product', 'page')); a and add('Content Quality', 'Medium', 'Thin page: fewer than 150 words of main content', a, n)
    a, n = where(lambda p: p['words'] < 300, ('product',)); a and add('Content Quality', 'Low', 'Product page under 300 words', [x for x in a], n)
    paths = set(x for p in pages for x in p['nav'])
    for label, pattern in (('About or company page', r'/pages/(about|company)'), ('Contact page', r'/pages/contact'), ('Refund policy', r'/policies/refund-policy|/pages/.*(refund|return)'), ('Privacy policy', r'/policies/privacy-policy|/pages/.*privacy'), ('Terms of service', r'/policies/terms-of-service|/pages/.*terms')):
        if not any(re.search(pattern, x) for x in paths): add('Content Quality', 'Medium', f'{label} is not linked from the sampled pages (trust signal)')

    # Schema
    a, n = where(lambda p: p['ldErrors']); a and add('Schema', 'High', 'JSON-LD that does not parse', a, n)
    home = [p for p in pages if p['kind'] == 'home']
    if home:
        t = types(home[0]['ld'])
        'Organization' in t or add('Schema', 'Medium', 'Homepage has no Organization schema', ['/'], 1)
        'WebSite' in t or add('Schema', 'Low', 'Homepage has no WebSite schema', ['/'], 1)
        org = next((x for x in home[0]['ld'] if isinstance(x, dict) and x.get('@type') == 'Organization'), None)
        if org and not org.get('sameAs'): add('AI Search Readiness', 'Low', 'Organization schema lists no sameAs profiles (brand entity signal)', ['/'], 1)
        if org and not org.get('logo'): add('Schema', 'Low', 'Organization schema has no logo', ['/'], 1)
    prods = [p for p in pages if p['kind'] == 'product']
    def product(p):
        nodes = [x for x in p['ld'] if isinstance(x, dict) and x.get('@type') in ('Product', 'ProductGroup')]
        if not nodes: return None
        merged = {}
        for node in nodes: merged.update(node)  # nodes that share an @id describe one product
        return merged
    def offers(x):
        o = x.get('offers') or (x.get('hasVariant') or [{}])[0].get('offers') if x else None
        return (o[0] if isinstance(o, list) and o else o) or {}
    a = [p['path'] for p in prods if not product(p)]; a and add('Schema', 'High', 'Product page has no Product schema', a, len(prods))
    a = [p['path'] for p in prods if product(p) and not (offers(product(p)).get('price') or offers(product(p)).get('lowPrice')) ]; a and add('Schema', 'High', 'Product schema has no price in offers', a, len(prods))
    a = [p['path'] for p in prods if product(p) and not offers(product(p)).get('priceCurrency')]; a and add('Schema', 'High', 'Product schema has no priceCurrency', a, len(prods))
    a = [p['path'] for p in prods if product(p) and not offers(product(p)).get('availability')]; a and add('Schema', 'Medium', 'Product schema has no availability', a, len(prods))
    a = [p['path'] for p in prods if product(p) and not product(p).get('brand')]; a and add('Schema', 'Low', 'Product schema has no brand', a, len(prods))
    a = [p['path'] for p in prods if product(p) and not (product(p).get('image') or (product(p).get('hasVariant') or [{}])[0].get('image'))]; a and add('Schema', 'Medium', 'Product schema has no image', a, len(prods))
    a = [p['path'] for p in prods if product(p) and not product(p).get('aggregateRating')]; a and add('Schema', 'Medium', 'Product schema has no aggregateRating (no review stars in results)', a, len(prods))
    a = [p['path'] for p in prods if product(p) and not (product(p).get('sku') or product(p).get('gtin') or product(p).get('gtin13') or product(p).get('mpn') or (product(p).get('hasVariant') or [{}])[0].get('sku'))]; a and add('Schema', 'Low', 'Product schema has no sku or gtin', a, len(prods))
    a, n = where(lambda p: 'BreadcrumbList' not in types(p['ld']), ('product', 'collection')); a and add('Schema', 'Low', 'No BreadcrumbList schema', a, n)
    a, n = where(lambda p: 'FAQPage' in types(p['ld'])); a and add('Schema', 'Info', 'FAQPage schema present: Google retired FAQ rich results for all sites on 2026-05-07, so it earns no rich result', a, n)
    a, n = where(lambda p: 'HowTo' in types(p['ld'])); a and add('Schema', 'Info', 'HowTo schema present: rich results removed in 2023', a, n)

    # Performance (lab, 390 wide, unthrottled)
    a, n = where(lambda p: p['lcp'] > 4000); a and add('Performance', 'Critical', 'Lab LCP above 4.0 s', a, n)
    a, n = where(lambda p: 2500 < p['lcp'] <= 4000); a and add('Performance', 'High', 'Lab LCP between 2.5 and 4.0 s', a, n)
    a, n = where(lambda p: (p['cls'] or 0) > 0.25); a and add('Performance', 'Critical', 'Lab CLS above 0.25', a, n)
    a, n = where(lambda p: 0.1 < (p['cls'] or 0) <= 0.25); a and add('Performance', 'High', 'Lab CLS between 0.1 and 0.25', a, n)
    a, n = where(lambda p: p['ttfb'] > 800); a and add('Performance', 'Medium', 'Server response (TTFB) above 800 ms', a, n)
    a, n = where(lambda p: p['transfer'] > 3000); a and add('Performance', 'Medium', 'Page weight above 3 MB', a, n)
    a, n = where(lambda p: p['dom'] > 3000); a and add('Performance', 'Medium', 'More than 3,000 DOM elements', a, n)
    a, n = where(lambda p: 1500 < p['dom'] <= 3000); a and add('Performance', 'Low', 'More than 1,500 DOM elements', a, n)
    a, n = where(lambda p: p['blocking'] > 3); a and add('Performance', 'Low', 'More than three render-blocking scripts in the head', a, n)
    a, n = where(lambda p: p['thirdParties'] > 15); a and add('Performance', 'Medium', 'More than 15 third-party hosts', a, n)
    a, n = where(lambda p: p['lcpEl'] and p['lcpEl']['tag'] == 'IMG' and p['lcpEl']['loading'] == 'lazy'); a and add('Performance', 'High', 'The LCP image is lazy-loaded', a, n)
    a, n = where(lambda p: p['lcpEl'] and p['lcpEl']['tag'] == 'IMG' and p['lcpEl']['priority'] != 'high' and p['lcpEl']['loading'] != 'lazy'); a and add('Performance', 'Low', 'The LCP image has no fetchpriority="high"', a, n)

    # AI Search Readiness
    for bot in ('OAI-SearchBot', 'Claude-SearchBot', 'PerplexityBot'):
        if robots and robots_blocks(robots, bot): add('AI Search Readiness', 'High', f'robots.txt blocks {bot} (the crawler behind that assistant\'s search citations)')
    a, n = where(lambda p: p['rawWords'] is not None and p['words'] > 150 and p['rawWords'] < p['words'] * 0.6); a and add('AI Search Readiness', 'Medium', 'Less than 60% of the main text is in the HTML before JavaScript runs (many AI crawlers do not run it)', a, n)
    a, n = where(lambda p: p['rawLd'] is not None and len(p['ld']) > 0 and p['rawLd'] == 0); a and add('AI Search Readiness', 'Medium', 'JSON-LD is only added by JavaScript', a, n)
    add('AI Search Readiness', 'Info', 'llms.txt ' + ('is present' if site['llms']['status'] == 200 else 'is absent') + ' (reported only: it carries no weight for Google)')

    # Images
    total = sum(p['images'] for p in pages) or 1
    no_alt = sum(p['noAltAttr'] for p in pages)
    if no_alt: add('Images', 'Medium' if no_alt / total > 0.05 else 'Low', f'{no_alt} of {total} images have no alt attribute', [p['path'] for p in pages if p['noAltAttr']], len(pages))
    no_size = sum(p['noSize'] for p in pages)
    if no_size / total > 0.1: add('Images', 'Medium', f'{no_size} of {total} images have no width and height (layout shift)', [p['path'] for p in pages if p['noSize']], len(pages))
    a, n = where(lambda p: p['eagerBelow'] > 5); a and add('Images', 'Low', 'More than five images far below the fold are not lazy-loaded', a, n)
    empty = sum(p['emptyAlt'] for p in pages)
    add('Images', 'Info', f'{empty} of {total} images carry an empty alt (right for decoration beside its text; a reader must judge)')
    return F


def score(findings):
    out = {}
    for cat in WEIGHTS:
        lost = sum(DEDUCT[f['severity']] * (0.5 + 0.5 * f['share']) for f in findings if f['category'] == cat)
        out[cat] = max(0, round(100 - lost))
    out['overall'] = round(sum(out[c] * w for c, w in WEIGHTS.items()) / 100)
    return out


async def check(browser, store):
    base, tid = STORES[store]
    ctx = await browser.new_context(viewport={'width': 390, 'height': 844}, user_agent=UA, device_scale_factor=2, is_mobile=True)
    await ctx.add_init_script(VITALS)
    page = await ctx.new_page()

    async def read(path):
        response = await page.goto(base + path, wait_until='load', timeout=90000)
        await page.wait_for_timeout(2500)
        data = await page.evaluate(PAGE)
        headers = {k.lower(): v for k, v in response.headers.items()}
        data.update({'path': path, 'kind': kind(path), 'status': response.status, 'headers': {k: headers.get(k) for k in ('strict-transport-security', 'x-content-type-options', 'x-frame-options', 'content-security-policy', 'x-robots-tag')}})
        return data

    if not LIVE:
        await page.goto(f'{base}/?preview_theme_id={tid}', wait_until='domcontentloaded'); await page.wait_for_timeout(1500)
    home = await read('/')
    site = await page.evaluate(SITE)
    nav = home['nav']
    picks = ['/collections/all'] + [p for p in nav if p.startswith('/collections/') and p != '/collections/all'][:1]
    picks += [f'/products/{h}' for h in PRODUCTS if h in site['products']] or [f'/products/{h}' for h in site['products'][:4]]
    picks += [p for p in nav if p.startswith('/pages/')][:6] + ['/policies/refund-policy']
    pages = [home]
    for path in dict.fromkeys(picks):
        try: pages.append(await read(path))
        except Exception as error: print(f'  skipped {path}: {str(error)[:80]}')
    await ctx.close()
    theme_ok = LIVE or all(p['theme'] == tid for p in pages)
    findings = findings_for(store, base, pages, site)
    return {'store': store, 'base': base, 'mode': 'live' if LIVE else f'draft {tid}', 'theme_ok': theme_ok, 'scores': score(findings), 'findings': findings,
            'pages': [{k: v for k, v in p.items() if k not in ('nav', 'ld')} | {'schema': types(p['ld'])} for p in pages],
            'site': {'robots_status': site['robots']['status'], 'sitemap_status': site['sitemap']['status'], 'child_sitemaps': site['sitemap']['text'].count('<sitemap>'), 'llms_status': site['llms']['status'], 'products': len(site['products']),
                     'search_bots_blocked': [b for b in SEARCH_BOTS if site['robots']['text'] and robots_blocks(site['robots']['text'], b)]}}


async def main():
    stores = [a for a in sys.argv[1:] if a in STORES] or list(STORES)
    os.makedirs(OUT, exist_ok=True)
    serious = 0
    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True, **LAUNCH)
        for store in stores:
            report = await check(browser, store)
            json.dump(report, open(os.path.join(OUT, f'seo-{store}.json'), 'w'), indent=1, ensure_ascii=False)
            s = report['scores']
            print(f"\n== {store} ({report['mode']}{'' if report['theme_ok'] else ', WRONG THEME SERVED'}) · {len(report['pages'])} pages · score {s['overall']}/100")
            print('   ' + ' · '.join(f'{c} {s[c]}' for c in WEIGHTS))
            order = ['Critical', 'High', 'Medium', 'Low', 'Info']
            for f in sorted(report['findings'], key=lambda f: order.index(f['severity'])):
                serious += f['severity'] in ('Critical', 'High')
                n = len(f['pages'])
                print(f"   {f['severity']:8} {f['category']:20} {f['finding']}" + (f"  [{n} page{'s' if n != 1 else ''}: {', '.join(f['pages'][:3])}{' ...' if n > 3 else ''}]" if n else ''))
        await browser.close()
    sys.exit(1 if serious else 0)

asyncio.run(main())
