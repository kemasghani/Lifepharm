"""What a Lighthouse result says, in a few lines. Shared by psi_run.py and lh_run.py."""

WEIGHTS = (('first-contentful-paint', 'FCP', 10), ('largest-contentful-paint', 'LCP', 25), ('total-blocking-time', 'TBT', 30), ('cumulative-layout-shift', 'CLS', 25), ('speed-index', 'SI', 10))


def summary(lh):
    lh = lh.get('lighthouseResult', lh); a = lh['audits']
    m = ((a.get('metrics') or {}).get('details') or {}).get('items', [{}])[0]
    cats = {k: round((v.get('score') or 0) * 100) for k, v in lh['categories'].items() if v.get('score') is not None}
    parts = ' · '.join(f"{label} {a[key].get('displayValue', '?')} ({round((a[key].get('score') or 0) * weight, 1)}/{weight})" for key, label, weight in WEIGHTS)
    observed = {k.replace('observed', ''): round(m[k]) for k in ('observedFirstPaint', 'observedFirstContentfulPaint', 'observedLargestContentfulPaint', 'observedDomContentLoaded', 'observedLoad') if isinstance(m.get(k), (int, float))}
    lcp = next((i for i in (((a.get('lcp-breakdown-insight') or {}).get('details') or {}).get('items') or []) if i.get('type') == 'table'), {})
    phases = {i.get('subpart', i.get('label')): round(i.get('duration', 0)) for i in lcp.get('items', [])}
    requests = ((a.get('network-requests') or {}).get('details') or {}).get('items') or []
    hinted = sum(1 for r in requests if r.get('transferSize') == 0 and r.get('resourceType') in ('Stylesheet', 'Font', 'Image'))
    return (f"   Lighthouse {lh.get('lighthouseVersion')} · {lh['configSettings'].get('formFactor')} · {lh.get('fetchTime', '')[:19]}\n"
            f"   scores    {cats}\n   metrics   {parts}\n   observed  {observed}\n   LCP parts {phases}\n"
            f"   weight    {round(sum(r.get('transferSize', 0) for r in requests) / 1024)} KB in {len(requests)} requests · {hinted} files already in cache (early hints)"
            + ''.join(f"\n   warning   {w[:150]}" for w in lh.get('runWarnings') or []))


def numbers(lh):
    """The figures worth comparing between runs."""
    lh = lh.get('lighthouseResult', lh); a = lh['audits']
    m = ((a.get('metrics') or {}).get('details') or {}).get('items', [{}])[0]
    return {'score': round((lh['categories']['performance'].get('score') or 0) * 100), 'FCP': round(m.get('firstContentfulPaint', 0)), 'LCP': round(m.get('largestContentfulPaint', 0)),
            'TBT': round(m.get('totalBlockingTime', 0)), 'SI': round(m.get('speedIndex', 0)), 'CLS': round(m.get('cumulativeLayoutShift', 0), 3),
            'seen FCP': round(m.get('observedFirstContentfulPaint', 0)), 'seen LCP': round(m.get('observedLargestContentfulPaint', 0))}
