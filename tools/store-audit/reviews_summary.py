"""Store-wide review summary for the checkout "Rating and guarantee" block (D-114).

Reads Stamped's per-product metafields (stamped.reviews_average, stamped.reviews_count) on every ACTIVE
product of a store, and writes one weighted summary to the shop as the app-owned JSON metafield
`$app:reviews` / `summary`: {"average": 4.862, "count": 1111, "products": 12, "customers": 1110, "updated_at": "..."}.
`customers` is the number of customers with at least one order in that Shopify store (developer's choice,
2026-11-28, D-115): imported accounts that never ordered here are not counted.
Only ACTIVE products count, so unlisted copies that share a product's reviews (the staging "IBO
Auto-Delivery" products) are not counted twice. Stamped has no store-wide total of its own, and checkout
extensions cannot read product metafields beyond the cart, so this summary is what the block shows.

Usage: python3 tools/store-audit/reviews_summary.py [--write] [us uk eu staging]
Without --write it only prints. Re-run after reviews change (planned: daily, see docs/tech-debt.md).
"""
import sys, os, json, datetime
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shopify import gql

PRODUCTS = '''query($a:String){ products(first:100, after:$a, query:"status:active"){
  pageInfo{ hasNextPage endCursor }
  nodes{ title status
    a: metafield(namespace:"stamped", key:"reviews_average"){ value }
    c: metafield(namespace:"stamped", key:"reviews_count"){ value } } } }'''
SET = '''mutation($m:[MetafieldsSetInput!]!){ metafieldsSet(metafields:$m){
  metafields{ namespace key value } userErrors{ field message code } } }'''


def num(field):
    try:
        return float(field['value']) if field and field.get('value') else 0.0
    except ValueError:
        return 0.0


def summary(store):
    total = weighted = 0.0
    products = 0
    after = None
    while True:
        page = gql(store, PRODUCTS, {'a': after})['data']['products']
        for p in page['nodes']:
            if p['status'] != 'ACTIVE':
                continue
            count, average = num(p['c']), num(p['a'])
            if count > 0 and 0 < average <= 5:
                total += count
                weighted += average * count
                products += 1
        if not page['pageInfo']['hasNextPage']:
            break
        after = page['pageInfo']['endCursor']
    buyers = gql(store, '{ c: customerSegmentMembers(first: 1, query: "number_of_orders > 0") { totalCount } }')
    return {
        'customers': int(buyers['data']['c']['totalCount']),
        'average': round(weighted / total, 3) if total else 0,
        'count': int(total),
        'products': products,
        'updated_at': datetime.datetime.now(datetime.timezone.utc).strftime('%Y-%m-%dT%H:%M:%SZ'),
    }


def main():
    args = [a for a in sys.argv[1:] if not a.startswith('--')]
    write = '--write' in sys.argv
    for store in args or ['us', 'uk', 'eu', 'staging']:
        s = summary(store)
        line = f"{store}: {s['average']} from {s['count']} reviews over {s['products']} products, {s['customers']} customers"
        if not write:
            print(line, '(dry run)')
            continue
        if not s['count']:
            print(line, 'skipped: no reviews found')
            continue
        shop_id = gql(store, '{ shop { id } }')['data']['shop']['id']
        r = gql(store, SET, {'m': [{'ownerId': shop_id, 'namespace': '$app:reviews', 'key': 'summary',
                                    'type': 'json', 'value': json.dumps(s)}]})['data']['metafieldsSet']
        print(line, 'written' if not r['userErrors'] else r['userErrors'])


if __name__ == '__main__':
    main()
