"""Crawl https://api.exigo.com/3.0/ into ./work/raw (run from docs/exigo-api/tools).
Fetches: docs home + nav, WSDL, every menu method page, every WSDL-only method page,
and every EnumHelp page (needs a Referer header, otherwise HTTP 500)."""
import json,os,re,html,time,urllib.request,concurrent.futures as cf
import xml.etree.ElementTree as ET
BASE='https://api.exigo.com/3.0/'
W=os.path.join(os.path.dirname(os.path.abspath(__file__)),'work'); os.chdir(os.makedirs(W,exist_ok=True) or W)
for d in ('raw/ops','raw/hidden','raw/enums'): os.makedirs(d,exist_ok=True)
def get(url,path,referer=None):
    if os.path.exists(path) and os.path.getsize(path)>2000: return open(path,encoding='utf-8').read()
    h={'User-Agent':'Mozilla/5.0 (docs crawler)'}
    if referer: h['Referer']=referer
    for i in range(4):
        try:
            data=urllib.request.urlopen(urllib.request.Request(url,headers=h),timeout=60).read().decode('utf-8','replace')
            open(path,'w',encoding='utf-8').write(data); return data
        except Exception as e: err=e; time.sleep(2*(i+1))
    print('FAIL',url,err); return ''
home=get(BASE,'raw/home.html'); get(BASE+'ExigoApi.asmx?WSDL','raw/wsdl.xml')
nav=home[home.find('id="apimethodsnavigation"'):]; nav=nav[:nav.find('</aside>')]
cats=[{'category':html.unescape(m.group(1).strip()),'links':re.findall(r"href='([^']+)'>([^<]+)</a>",m.group(2))}
      for m in re.finditer(r'<li>\s*<a href="#" class="navlink ignore"><i class="[^"]*"></i>([^<]+)</a>\s*<ul class="subnav">(.*?)</ul>',nav,re.S)]
json.dump(cats,open('nav.json','w'),indent=1)
navops=[h.split('op=')[1] for c in cats for h,_ in c['links'] if 'op=' in h]
ns={'w':'http://schemas.xmlsoap.org/wsdl/'}
wsdl_ops=[o.get('name') for o in ET.parse('raw/wsdl.xml').getroot().find('w:portType',ns).findall('w:operation',ns)]
hidden=sorted(set(wsdl_ops)-set(navops)); json.dump(hidden,open('hidden.json','w'))
with cf.ThreadPoolExecutor(6) as ex:
    list(ex.map(lambda n: get(BASE+'ExigoApi.asmx?op='+n,f'raw/ops/{n}.html'),navops))
    list(ex.map(lambda n: get(BASE+'ExigoApi.asmx?op='+n,f'raw/hidden/{n}.html'),hidden))
links=set()
for f in [f'raw/ops/{n}.html' for n in navops]+[f'raw/hidden/{n}.html' for n in hidden]:
    links|=set(re.findall(r"href='(doc/EnumHelp\.aspx\?[^']+)'",open(f,encoding='utf-8').read()))
def fetch_enum(l):
    l=l.replace('&amp;','&'); op=re.search(r'op=([^&]+)',l).group(1)
    name=re.sub(r'[^A-Za-z0-9_=&.-]','_',l.split('?')[1]).replace('&','__')
    return get(BASE+l,f'raw/enums/{name}.html',referer=BASE+'ExigoApi.asmx?op='+op)
with cf.ThreadPoolExecutor(6) as ex: list(ex.map(fetch_enum,sorted(links)))
cd={}
for blk in re.findall(r'<div class="media-body">(.*?)<ul class="methodlist',home,re.S):
    h=re.search(r'<h3 class="media-heading">(.*?)</h3>',blk,re.S); name=html.unescape(re.sub('<[^>]+>','',h.group(1))).strip()
    ps=[re.sub(r'\s+',' ',html.unescape(re.sub('<[^>]+>','',p))).strip() for p in re.findall(r'<p(?: class="(?!hidden-desktop)[^"]*")?>(.*?)</p>',blk,re.S)]
    cd[name]=' '.join(p for p in ps if p and p!='View Methods')
json.dump(cd,open('cat_desc.json','w'),indent=1)
v=re.search(r'<small>\s*(v[\d.]+)\s*</small>',open(f'raw/ops/{navops[0]}.html',encoding='utf-8').read())
open('version.txt','w').write(v.group(1) if v else '')
print('menu ops',len(navops),'wsdl-only',len(hidden),'enum pages',len(links))
