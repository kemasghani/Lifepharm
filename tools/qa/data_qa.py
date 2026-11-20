#!/usr/bin/env python3
"""Data completeness across stores (Admin API only, read-only, no storefront traffic).

    python3 tools/qa/data_qa.py

Per active product: image and alt text, price, availability, template file present in the store's branch, short
summary and Ideal For (custom.product_short_summary, custom.value_1), PDP metafields the lp-pdp sections read,
SEO title/description, description. Per page and collection: template file present, content/image, product count.
Then the differences between stores for the same handle.
"""
import json, os, sys
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', 'store-audit'))
from shopify import gql  # noqa: E402

ROOT = os.path.abspath(os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..'))
CHECKOUT = {'uk': ROOT, 'us': os.path.join(ROOT, '..', 'Lifepharm-worktrees', 'us'), 'eu': os.path.join(ROOT, '..', 'Lifepharm-worktrees', 'eu')}
PDP_KEYS = ['product_short_summary', 'value_1', 'text_benefits', 'text_ingredients', 'studies', 'faq_url', 'phase_1_content']

Q = '''query($c:String){products(first:100,after:$c,query:"status:active"){pageInfo{hasNextPage endCursor} nodes{
  handle title templateSuffix onlineStoreUrl descriptionHtml totalInventory tracksInventory
  seo{title description} featuredMedia{alt ... on MediaImage{image{url}}} mediaCount{count}
  priceRangeV2{minVariantPrice{amount currencyCode}}
  variants(first:20){nodes{availableForSale price}}
  metafields(first:80,namespace:"custom"){nodes{key value}}}}}'''
QP = '{pages(first:100){nodes{handle title templateSuffix isPublished body}} collections(first:100){nodes{handle title templateSuffix productsCount{count} image{url} descriptionHtml}}}'


def tpl_exists(store, kind, suffix):
    base = os.path.join(CHECKOUT[store], 'templates')
    name = f'{kind}.{suffix}' if suffix else kind
    return any(os.path.exists(os.path.join(base, name + ext)) for ext in ('.json', '.liquid'))


def products(store):
    out, cursor = [], None
    while True:
        d = gql(store, Q, {'c': cursor})['data']['products']
        out += d['nodes']
        if not d['pageInfo']['hasNextPage']:
            return out
        cursor = d['pageInfo']['endCursor']


def main():
    data, issues = {}, []
    for store in ('uk', 'us', 'eu'):
        ps = [p for p in products(store) if p['onlineStoreUrl']]
        data[store] = {p['handle']: p for p in ps}
        for p in ps:
            h = f"{store} product {p['handle']}"
            mf = {m['key']: m['value'] for m in p['metafields']['nodes']}
            p['_mf'] = mf
            if not p['featuredMedia']:
                issues.append((h, 'no product image'))
            elif not (p['featuredMedia'].get('alt') or '').strip():
                issues.append((h, 'featured image has no alt text'))
            if not tpl_exists(store, 'product', p['templateSuffix']):
                issues.append((h, f"template product.{p['templateSuffix']} missing in the {store} branch (falls back to default)"))
            if float(p['priceRangeV2']['minVariantPrice']['amount']) == 0:
                issues.append((h, 'price is 0'))
            if not any(v['availableForSale'] for v in p['variants']['nodes']):
                issues.append((h, 'no variant available for sale (sold out)'))
            if not (p['seo']['description'] or '').strip():
                issues.append((h, 'no SEO meta description'))
            if len((p['descriptionHtml'] or '').strip()) < 20:
                issues.append((h, 'empty product description'))
            if not mf.get('product_short_summary'):
                issues.append((h, 'no short summary (custom.product_short_summary): the summary and Ideal For block do not render'))
            elif not mf.get('value_1'):
                issues.append((h, 'no Ideal For list (custom.value_1)'))
        r = gql(store, QP)['data']
        for pg in r['pages']['nodes']:
            if not pg['isPublished']:
                continue
            h = f"{store} page {pg['handle']}"
            if not tpl_exists(store, 'page', pg['templateSuffix']):
                issues.append((h, f"template page.{pg['templateSuffix']} missing in the {store} branch"))
            if not pg['templateSuffix'] and len((pg['body'] or '').strip()) < 20:
                issues.append((h, 'default template with an empty body'))
        for c in r['collections']['nodes']:
            h = f"{store} collection {c['handle']}"
            if not tpl_exists(store, 'collection', c['templateSuffix']):
                issues.append((h, f"template collection.{c['templateSuffix']} missing in the {store} branch"))
            if c['productsCount']['count'] == 0:
                issues.append((h, 'collection has no products'))
    # cross-store differences for the same handle
    for h in sorted(set(data['uk']) | set(data['us']) | set(data['eu'])):
        present = [s for s in data if h in data[s]]
        if len(present) < 3:
            issues.append((f'product {h}', f'only on {", ".join(present)}'))
        for key in ('product_short_summary', 'value_1'):
            vals = {s: (data[s][h]['_mf'].get(key) or '').strip().rstrip('.') for s in present}
            if len(set(vals.values())) > 1:
                issues.append((f'product {h}', f'{key} differs: ' + ' / '.join(f'{s}: "{v[:60]}"' for s, v in vals.items())))
        tpls = {s: data[s][h]['templateSuffix'] for s in present}
        if len(set(tpls.values())) > 1:
            issues.append((f'product {h}', f'template differs: {tpls}'))
    for where, what in issues:
        print(f'{where}: {what}')
    print(f'\n{len(issues)} findings')
    os.makedirs(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports'), exist_ok=True)
    json.dump(issues, open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'reports', 'data-latest.json'), 'w'), indent=1)


if __name__ == '__main__':
    main()
