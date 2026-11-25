"""Draft check of the quick add drawer at 390 and 1440: add a product, then list what the confirmation holds, its close button, focus and how it closes.

Adds one item to a throwaway cart. Usage: uv run --no-project --with playwright python tools/qa/quick_add_drawer_check.py <base_url> <theme_id or -> <tag> <outdir> [path]"""
import asyncio,sys,json
from playwright.async_api import async_playwright
base=sys.argv[1]; tid=sys.argv[2]; tag=sys.argv[3]; S=sys.argv[4]
async def main():
  async with async_playwright() as p:
    b=await p.chromium.launch(channel='chrome')
    for w,h,m in((390,844,True),(1440,900,False)):
      c=await b.new_context(viewport={'width':w,'height':h},device_scale_factor=2,is_mobile=m,has_touch=m); pg=await c.new_page()
      errs=[]; pg.on('pageerror',lambda e:errs.append(str(e)[:120]))
      if tid!='-': await pg.goto(f'{base}/?preview_theme_id={tid}',wait_until='domcontentloaded'); await pg.wait_for_timeout(1500)
      r=await pg.goto(base+(sys.argv[5] if len(sys.argv)>5 else '/'),wait_until='load'); await pg.wait_for_timeout(5000)
      th=await pg.evaluate('String(Shopify.theme.id)')
      btn=pg.locator("[aria-controls^=quick-buy-]").first
      await btn.evaluate('e=>e.click()'); await pg.wait_for_timeout(4000)
      await pg.screenshot(path=f'{S}/{tag}-{w}-1.png')
      await pg.evaluate("document.querySelector('quick-buy-drawer[open] button[type=submit]').click()"); await pg.wait_for_timeout(4500)
      await pg.screenshot(path=f'{S}/{tag}-{w}-2.png')
      o=await pg.evaluate("""()=>{const d=document.querySelector('quick-buy-drawer[open]'); if(!d) return {open:false, cart:document.querySelector('#cart-drawer')?.hasAttribute('open')};
        const c=d.shadowRoot.querySelector('[part=close-button]'), oc=d.shadowRoot.querySelector('[part=outside-close-button]'); const r=e=>{const b=e.getBoundingClientRect();return [b.x,b.y,b.width,b.height].map(Math.round).concat(getComputedStyle(e).display)};
        return {open:true, buttons:[...d.querySelectorAll('button,a,form')].map(e=>e.tagName+':'+e.textContent.trim().slice(0,30)), close:r(c), outside:r(oc), box:r(d.shadowRoot.querySelector('[part=content]')), active:document.activeElement.tagName, hs:document.documentElement.scrollWidth>innerWidth+1}}""")
      n=await pg.evaluate("fetch('/cart.js').then(r=>r.ok?r.json():{item_count:'http '+r.status}).then(c=>c.item_count).catch(e=>'err')")
      if o.get('open'):
        x,y,ww,hh,_=o['close'];
        await pg.mouse.click(x+ww/2,y+hh/2) if ww else await pg.keyboard.press('Escape')
        await pg.wait_for_timeout(1500); o['closed_by']=('cross' if ww else 'escape'); o['closed']=await pg.evaluate("!document.querySelector('quick-buy-drawer[open]')")
      print(tag,r.status,w,th,'cart',n,json.dumps(o),'errs',errs); await c.close()
    await b.close()
asyncio.run(main())
