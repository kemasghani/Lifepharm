"""Parse ./work/raw into ./work/exigo_parsed.json (run after crawl.py)."""
import os; os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'work'))
import re,html,json,os,glob
import xml.etree.ElementTree as ET
def txt(fragment, code=False):
    s=re.sub(r'<script.*?</script>|<style.*?</style>','',fragment,flags=re.S)
    s=re.sub(r'(?i)<br\s*/?>|</p>|</div>|</li>|</tr>|</h\d>','\n',s)
    s=re.sub(r'<[^>]+>','',s); s=html.unescape(s).replace('\xa0',' ')
    if not code: s=re.sub(r'[ \t]+',' ',s)
    lines=[l.rstrip() for l in s.split('\n')]
    out=[];blank=0
    for l in lines:
        if not l.strip():
            blank+=1
            if blank>1: continue
        else: blank=0
        out.append(l)
    return '\n'.join(out).strip('\n')
def tab(s,tid):
    m=re.search(r'id="%s">(.*?)(?=<div class="tab-pane|<footer|<!-- Footer|\Z)'%tid,s,re.S)
    return m.group(1) if m else ''
# enums from help pages
enum_pages={}
for f in glob.glob('raw/enums/*.html'):
    s=open(f,encoding='utf-8').read(); main=s[s.find('</aside>'):] if '</aside>' in s else s
    tm=re.search(r"<table class='[^']*helptable'>(.*?)</table>",s,re.S)
    vals=[]
    if tm:
        for row in re.findall(r'<tr>(.*?)</tr>',tm.group(1),re.S):
            cells=[txt(c).strip() for c in re.findall(r'<t[dh][^>]*>(.*?)</t[dh]>',row,re.S)]
            if any(cells): vals.append(' = '.join(c for c in cells if c))
    key=os.path.basename(f)[:-5]
    q=dict(kv.split('=',1) for kv in key.split('__') if '=' in kv)
    enum_pages[(q.get('op'),q.get('o'),q.get('p'))]=vals
def parse_io(seg,op):
    blocks=[];cur=None;section=None
    for m in re.finditer(r"<h4>([^<]*)</h4>|<h5 class='span12'>(.*?)</h5>|<div class='row-fluid tablebody'>(.*?)</div>",seg,re.S):
        if m.group(1) is not None: section=m.group(1).strip(); continue
        if m.group(2) is not None:
            cur={'section':section,'type':txt(m.group(2)),'rows':[]}; blocks.append(cur); continue
        row=m.group(3)
        pm=re.search(r"<span class='span4 property ?([^']*)'>(.*?)</span>(?=<span class='span3)",row,re.S)
        dm=re.search(r"<span class='span3 datatype'>(.*?)</span>(?=<span class='span5)",row,re.S)
        nm=re.search(r"<span class='span5 notes[^']*'>(.*)</span>\s*$",row,re.S)
        if not pm: continue
        indent=int((re.search(r'indented-(\d+)',pm.group(1)) or [0,0])[1]) if 'indented' in pm.group(1) else 0
        help_=None
        hm=re.search(r"href='doc/(EnumHelp|ListHelp)\.aspx\?([^']+)'",pm.group(2))
        if hm:
            q=dict(kv.split('=',1) for kv in html.unescape(hm.group(2)).split('&'))
            help_={'kind':'enum' if hm.group(1)=='EnumHelp' else 'company-list','values':enum_pages.get((q.get('op'),q.get('o'),q.get('p'))) if hm.group(1)=='EnumHelp' else None}
        r={'property':txt(pm.group(2)).strip(),'indent':indent,'datatype':txt(dm.group(1)).strip() if dm else '','notes':txt(nm.group(1)).strip() if nm else ''}
        if help_: r['lookup']=help_
        if cur is None: cur={'section':section,'type':'','rows':[]}; blocks.append(cur)
        cur['rows'].append(r)
    return blocks
def parse_op(path,name,category,hidden):
    s=open(path,encoding='utf-8').read()
    main=s[s.find('</aside>'):]
    dm=re.search(r'<div id="DetailView">\s*<h2>(.*?)</h2>(.*?)<ul class="nav nav-pills"',s,re.S)
    h=None; desc=''
    if dm: desc=txt(dm.group(2)); title=txt(dm.group(1))
    io=tab(s,'inputoutput'); blocks=parse_io(io,name)
    rest=tab(s,'rest'); pres=re.findall(r'<pre[^>]*>(.*?)</pre>',rest,re.S)
    rest_req=txt(pres[0],True) if pres else ''; rest_resp=txt(pres[1],True) if len(pres)>1 else ''
    rm=re.match(r'(GET|POST|PUT|DELETE|PATCH)\s+(\S+)',rest_req)
    soap=tab(s,'soap'); sp=re.findall(r'<pre[^>]*>(.*?)</pre>',soap,re.S)
    soap_req=txt(sp[0],True) if sp else ''; soap_resp=txt(sp[1],True) if len(sp)>1 else ''
    sa=re.search(r'SOAPAction:\s*"([^"]+)"',soap_req)
    samples={}
    for tid,label in [('restcsharp','C# REST client'),('csharp','C# SOAP client'),('vb','VB.Net'),('php','PHP'),('java','Java')]:
        seg=tab(s,tid); samples[label]=txt(seg,True)
    csv=tab(s,'csv'); csvt=txt(csv,True)
    return {'name':name,'category':category,'hidden_from_nav':hidden,'title':title if dm else name,'description':desc,
            'rest':{'method':rm.group(1) if rm else None,'url':rm.group(2) if rm else None,'request':rest_req,'response':rest_resp},
            'soap':{'action':sa.group(1) if sa else None,'request':soap_req,'response':soap_resp},
            'io':blocks,'samples':samples,'csv':csvt}
nav=json.load(open('nav.json'))
ops=[]
for c in nav:
    for h,_ in c['links']:
        if 'op=' in h: n=h.split('op=')[1]; ops.append(parse_op(f'raw/ops/{n}.html',n,c['category'],False))
for n in json.load(open('hidden.json')): ops.append(parse_op(f'raw/hidden/{n}.html',n,'Unlisted (WSDL only)',True))
# WSDL types
ns={'w':'http://schemas.xmlsoap.org/wsdl/','s':'http://www.w3.org/2001/XMLSchema'}
r=ET.parse('raw/wsdl.xml').getroot(); sch=r.find('w:types/s:schema',ns)
def fields(ct):
    out=[]
    base=None
    ext=ct.find('.//s:extension',ns)
    if ext is not None: base=ext.get('base')
    for e in ct.iter('{http://www.w3.org/2001/XMLSchema}element'):
        out.append({'name':e.get('name') or e.get('ref'),'type':(e.get('type') or '').split(':')[-1],'min':e.get('minOccurs','1'),'max':e.get('maxOccurs','1'),'nillable':e.get('nillable','false')})
    for a in ct.iter('{http://www.w3.org/2001/XMLSchema}attribute'):
        out.append({'name':'@'+a.get('name'),'type':(a.get('type') or '').split(':')[-1],'min':'1' if a.get('use')=='required' else '0','max':'1','nillable':'false'})
    return base,out
types={}
for ct in sch.findall('s:complexType',ns):
    b,f=fields(ct); types[ct.get('name')]={'base':(b or '').split(':')[-1] or None,'fields':f}
enums={st.get('name'):[e.get('value') for e in st.iter('{http://www.w3.org/2001/XMLSchema}enumeration')] for st in sch.findall('s:simpleType',ns)}
elements={}
for e in sch.findall('s:element',ns):
    t=e.get('type'); 
    if t: elements[e.get('name')]=t.split(':')[-1]
    else:
        b,f=fields(e.find('s:complexType',ns)) if e.find('s:complexType',ns) is not None else (None,[])
        elements[e.get('name')]={'fields':f}
pt=r.find('w:portType',ns); msgs={m.get('name'):[p.get('element') for p in m.findall('w:part',ns)] for m in r.findall('w:message',ns)}
wsdl_ops={}
for o in pt.findall('w:operation',ns):
    i=o.find('w:input',ns).get('message').split(':')[-1]; out=o.find('w:output',ns).get('message').split(':')[-1]
    doc=o.find('w:documentation',ns)
    wsdl_ops[o.get('name')]={'input':[x.split(':')[-1] for x in msgs.get(i,[])],'output':[x.split(':')[-1] for x in msgs.get(out,[])],'documentation':(doc.text or '').strip() if doc is not None else ''}
for op in ops:
    w=wsdl_ops.get(op['name'],{}); op['wsdl']=w
json.dump({'ops':ops,'types':types,'enums':enums,'elements':elements},open('exigo_parsed.json','w'),indent=1)
print('ops',len(ops),'types',len(types),'enums',len(enums))
print('missing rest',[o['name'] for o in ops if not o['rest']['method']][:20])
print('empty io',[o['name'] for o in ops if not o['io']][:20])
print('no desc',[o['name'] for o in ops if not o['description']][:20])
print('enum lookups without values',sum(1 for o in ops for b in o['io'] for r in b['rows'] if r.get('lookup',{}).get('kind')=='enum' and not r['lookup']['values']))
print('company-list fields',sum(1 for o in ops for b in o['io'] for r in b['rows'] if r.get('lookup',{}).get('kind')=='company-list'))
