"""axe-core (WCAG 2.2 AA and best practices) on six pages at 1440 and 390, every violating node printed once. Read-only.

Usage: npm pack axe-core --ignore-scripts && tar xzf axe-core-*.tgz, then: uv run --no-project --with playwright python tools/qa/axe_check.py <axe.min.js> <base_url>
Known and accepted: brand orange text (client decision, TD-042), sold-out cards and the decorative step numbers."""
import asyncio,json,sys
from playwright.async_api import async_playwright
B=sys.argv[2].rstrip('/'); P=['/','/collections/all','/products/laminine','/pages/science','/pages/contact','/pages/company']
SRC=open(sys.argv[1]).read()
async def main():
  agg={}
  async with async_playwright() as p:
    b=await p.chromium.launch(channel='chrome')
    for w,m in((1440,False),(390,True)):
      c=await b.new_context(viewport={'width':w,'height':900},is_mobile=m,has_touch=m); pg=await c.new_page()
      for u in P:
        r=await pg.goto(B+u,wait_until='domcontentloaded',timeout=90000); await pg.wait_for_timeout(3000)
        H=await pg.evaluate('document.body.scrollHeight')
        for y in range(0,H,700): await pg.evaluate(f'scrollTo(0,{y})'); await pg.wait_for_timeout(120)
        await pg.evaluate('scrollTo(0,0)'); await pg.wait_for_timeout(3000)
        await pg.evaluate(SRC)
        res=await pg.evaluate("axe.run(document,{runOnly:['wcag2a','wcag2aa','wcag21a','wcag21aa','wcag22aa','best-practice']})")
        print(w,u,r.status,{v['id']:(v['impact'],len(v['nodes'])) for v in res['violations']})
        for v in res['violations']:
          for n in v['nodes']: agg.setdefault((v['id'],v['impact'],v['help']),{}).setdefault(n['target'][0] if isinstance(n['target'][0],str) else str(n['target'][0]),(w,u,n['html'][:170],(n.get('failureSummary') or '')[:330].replace('\n',' ')))
      await c.close()
    await b.close()
  for k,v in sorted(agg.items(),key=lambda x:str(x[0][1])):
    print('\n##',k,len(v))
    for t,x in list(v.items())[:300]: print('   ',t[:110],'|',x[0],x[1],'|',x[2],'|',x[3] if k[0] in('color-contrast','target-size') else '')
asyncio.run(main())
