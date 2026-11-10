import json,re,os,datetime
os.chdir(os.path.join(os.path.dirname(os.path.abspath(__file__)),'work'))
OUT=os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.makedirs(OUT+'/operations',exist_ok=True)
d=json.load(open('exigo_parsed.json')); ops=d['ops']; types=d['types']; enums=d['enums']
cats_desc=json.load(open('cat_desc.json')); version=open('version.txt').read().strip()
TODAY='2026-11-11'
DOC='https://api.exigo.com/3.0/ExigoApi.asmx?op='
def cell(x): return (x or '').replace('|','\\|').replace('\n','<br>').strip()
def slug(c): return re.sub(r'[^a-z0-9]+','-',c.lower()).strip('-')
order=[]
for o in ops:
    if o['category'] not in order: order.append(o['category'])
cat_file={c:f'{i+1:02d}-{slug(c)}.md' for i,c in enumerate(order)}
def anchor(n): return n.lower()
def enum_vals(r):
    lk=r.get('lookup')
    if lk and lk['kind']=='enum':
        v=lk.get('values') or enums.get(r['datatype']) or enums.get(r['datatype'].replace('[]',''))
        return v
    base=r['datatype'].replace('[]','')
    if base in enums: return enums[base]
    return None
def short(desc,n=180):
    t=re.sub(r'\s+',' ',desc or '').strip()
    return t if len(t)<=n else t[:n].rsplit(' ',1)[0]+'…'
def rest_path(o):
    u=o['rest']['url']
    if not u: return None
    return re.sub(r'^https?://[^/]+','',u)
def csv_supported(o): return 'supports CSV output' in (o['csv'] or '')
def fence(lang,body):
    body=body.strip('\n')
    tick='````' if '```' in body else '```'
    return f'{tick}{lang}\n{body}\n{tick}\n'
TITLES={'C# Rest Client','C# Soap Client','VB.Net','PHP','Java','CSV'}
NOTE_RE=re.compile(r'^(Install Nuget|Note:|This method)',re.I)
def split_header(body):
    lines=body.split('\n'); notes=[]; i=0
    while i<len(lines):
        t=lines[i].strip()
        if not t or t in TITLES: i+=1; continue
        if NOTE_RE.match(t): notes.append(t); i+=1; continue
        break
    code=lines[i:]
    if code: code[0]=code[0].lstrip()
    return ' '.join(notes), '\n'.join(code).strip('\n')
def op_md(o):
    L=[]
    L.append(f'### {o["name"]}\n')
    if o['description']: L.append('\n'.join('> '+l if l.strip() else '>' for l in o['description'].split('\n'))+'\n')
    rp=rest_path(o)
    L.append('| | |\n|---|---|')
    L.append(f'| Category | {o["category"]}{" (not listed in the docs menu, documented in WSDL + method page)" if o["hidden_from_nav"] else ""} |')
    L.append(f'| REST | {"`"+o["rest"]["method"]+" "+rp+"`" if rp else "Not available (docs: “Rest call not available for this method yet”) — use SOAP"} |')
    L.append(f'| SOAP action | `{o["soap"]["action"] or "https://api.exigo.com/"+o["name"]}` |')
    w=o.get('wsdl') or {}
    if w: L.append(f'| WSDL elements | `{", ".join(w.get("input",[]))}` → `{", ".join(w.get("output",[]))}` |')
    L.append(f'| CSV output | {"Yes — `GET https://api.exigo.com/3.0/csv/?method="+o["name"]+"&ApiLoginName=…&ApiPassword=…&ApiCompany=…`" if csv_supported(o) else "No"} |')
    L.append(f'| Source | {DOC}{o["name"]} |\n')
    for sec in ('Input Properties','Output Properties'):
        blocks=[b for b in o['io'] if b['section']==sec]
        if not blocks: continue
        L.append(f'#### {"Input" if sec.startswith("Input") else "Output"}\n')
        for b in blocks:
            L.append(f'**`{b["type"]}`**\n')
            if not b['rows']:
                L.append('_No properties._\n'); continue
            L.append('| Property | Type | Notes |\n|---|---|---|')
            for r in b['rows']:
                pre='&nbsp;&nbsp;'*r['indent']+('↳ ' if r['indent'] else '')
                notes=cell(r['notes'])
                ev=enum_vals(r)
                if ev: notes=(notes+'<br>' if notes else '')+'**Values:** '+', '.join(f'`{v}`' for v in ev)
                if r.get('lookup',{}).get('kind')=='company-list': notes=(notes+'<br>' if notes else '')+'**Lookup:** company-specific list (see company-lists.md)'
                L.append(f'| {pre}`{cell(r["property"])}` | `{cell(r["datatype"])}` | {notes} |')
            L.append('')
    if o['rest']['request'] and 'not available' not in o['rest']['request'].lower():
        L.append('#### REST example\n')
        L.append(fence('http',o['rest']['request'])); L.append(fence('http',o['rest']['response']))
    L.append('<details><summary>SOAP 1.1 request / response</summary>\n')
    L.append(fence('xml',o['soap']['request'])); L.append(fence('xml',o['soap']['response'])); L.append('</details>\n')
    for label,lang in [('C# REST client','csharp'),('C# SOAP client','csharp'),('VB.Net','vbnet'),('PHP','php'),('Java','java')]:
        body=o['samples'].get(label,'')
        if body.strip():
            note,code=split_header(body)
            L.append(f'<details><summary>{label}</summary>\n')
            if note: L.append('_'+note+'_\n')
            L.append(fence(lang,code)); L.append('</details>\n')
    if o['csv'].strip():
        note,code=split_header(o['csv'])
        L.append('<details><summary>CSV</summary>\n')
        if note: L.append('_'+note+'_\n')
        if code.strip(): L.append(fence('text',code))
        L.append('</details>\n')
    L.append('---\n')
    return '\n'.join(L)
# category files
for c in order:
    co=[o for o in ops if o['category']==c]
    H=[f'# Exigo API — {c}\n',f'API version {version}. Crawled {TODAY} from https://api.exigo.com/3.0/. Back to [index](../README.md).\n']
    if cats_desc.get(c): H.append(cats_desc[c]+'\n')
    if c.startswith('Unlisted'): H.append('These operations exist in the WSDL and have full method pages, but are **not linked from the docs menu**. They may be internal, legacy or limited to specific companies. Confirm with Exigo before relying on them.\n')
    H.append('| Operation | REST | Summary |\n|---|---|---|')
    for o in co:
        rp=rest_path(o); H.append(f'| [{o["name"]}](#{anchor(o["name"])}) | {"`"+o["rest"]["method"]+" "+rp+"`" if rp else "SOAP only"} | {cell(short(o["description"]))} |')
    H.append('\n---\n')
    open(f'{OUT}/operations/{cat_file[c]}','w').write('\n'.join(H)+'\n'.join(op_md(o) for o in co))
# enums.md
E=[f'# Exigo API — Enums\n','Back to [index](README.md). Source: WSDL `simpleType` enumerations (authoritative names) plus the per-property value lists from the docs (`EnumHelp`).\n','## WSDL enumerations\n']
for n in sorted(enums): E.append(f'### {n}\n\n'+', '.join(f'`{v}`' for v in enums[n])+'\n')
E.append('## Property → enum values (as listed on each method page)\n\n| Operation | Object | Property | Type | Values |\n|---|---|---|---|---|')
for o in ops:
    for b in o['io']:
        for r in b['rows']:
            if r.get('lookup',{}).get('kind')=='enum':
                E.append(f'| [{o["name"]}](operations/{cat_file[o["category"]]}#{anchor(o["name"])}) | `{b["type"]}` | `{r["property"]}` | `{r["datatype"]}` | {", ".join(f"`{v}`" for v in (enum_vals(r) or []))} |')
open(f'{OUT}/enums.md','w').write('\n'.join(E)+'\n')
# company lists
C=['# Exigo API — Company-specific lookup fields\n','Back to [index](README.md).\n',
   'These properties take IDs whose valid values are configured per Exigo company (for example warehouses, ship methods, price types, currencies, countries, customer types/statuses, rank IDs, periods). The docs expose them through `doc/ListHelp.aspx`, which **requires an Exigo developer login** (API login name, password, company), so the values are not public. For LifePharm, read them from our Exigo instance with these credentials, or use the list operations in the API (for example `GetWarehouses`, `GetShipMethods`, `GetCountryRegions`, `GetRankQualifications`) where available.\n',
   '## Fields by property\n','| Property | Type | Used in (operation · object) |\n|---|---|---|']
from collections import defaultdict
cl=defaultdict(list)
for o in ops:
    for b in o['io']:
        for r in b['rows']:
            if r.get('lookup',{}).get('kind')=='company-list': cl[(r['property'],r['datatype'])].append(f'[{o["name"]}](operations/{cat_file[o["category"]]}#{anchor(o["name"])}) · `{b["type"]}`')
for (p,t),uses in sorted(cl.items()):
    u=sorted(set(uses)); C.append(f'| `{p}` | `{t}` | {", ".join(u)} |')
open(f'{OUT}/company-lists.md','w').write('\n'.join(C)+'\n')
# types.md
T=[f'# Exigo API — Data types (WSDL)\n','Back to [index](README.md). All {n} complex types from `https://api.exigo.com/3.0/ExigoApi.asmx?WSDL`. `min=0` means optional; `max=unbounded` means array. Enum types are in [enums.md](enums.md).\n'.format(n=len(types))]
T.append('| Type | Fields |\n|---|---|')
for n in sorted(types): T.append(f'| [{n}](#{n.lower()}) | {len(types[n]["fields"])} |')
T.append('')
for n in sorted(types):
    t=types[n]; T.append(f'### {n}\n'+(f'Extends `{t["base"]}`.\n' if t['base'] else ''))
    if not t['fields']: T.append('_No fields._\n'); continue
    T.append('| Field | Type | min | max | nillable |\n|---|---|---|---|---|')
    for f in t['fields']: T.append(f'| `{f["name"]}` | `{f["type"]}` | {f["min"]} | {f["max"]} | {f["nillable"]} |')
    T.append('')
open(f'{OUT}/types.md','w').write('\n'.join(T)+'\n')
# README
listed=[o for o in ops if not o['hidden_from_nav']]; hidden=[o for o in ops if o['hidden_from_nav']]
rest_n=sum(1 for o in ops if rest_path(o)); csv_n=sum(1 for o in ops if csv_supported(o))
R=[f'# Exigo Web Services API — knowledge base\n',
f'Full crawl of **https://api.exigo.com/3.0/** (API version **{version}**), done {TODAY}. Every menu category and sub-menu method was read, plus every method that exists in the WSDL but is not linked in the menu. Nothing was summarised away: each operation file keeps the full input/output tables, enum values, REST and SOAP examples and all code samples (C# REST, C# SOAP, VB.Net, PHP, Java, CSV).\n',
'## Coverage\n',
f'| Item | Count |\n|---|---|\n| Operations in WSDL | {len(ops)} |\n| Listed in docs menu | {len(listed)} (18 categories) |\n| Unlisted but documented (WSDL only) | {len(hidden)} |\n| Operations with REST endpoint | {rest_n} |\n| SOAP-only operations | {len(ops)-rest_n} |\n| Operations with CSV output | {csv_n} |\n| Complex types (WSDL) | {len(types)} → [types.md](types.md) |\n| Enums (WSDL) | {len(enums)} → [enums.md](enums.md) |\n| Company-specific lookup fields | {len(cl)} distinct → [company-lists.md](company-lists.md) |\n',
'Not publicly readable (needs an Exigo developer login): `doc/ChangeLog.aspx` (“Changes”) and `doc/ListHelp.aspx` (company-specific value lists).\n',
'## Transports and authentication\n',
'Exigo exposes the same operations over three transports:\n',
'**1. REST (JSON)** — `https://{company}-api.exigo.com/3.0/{resource}`\n',
'```http\nPOST https://yourcompany-api.exigo.com/3.0/orders HTTP/1.1\nContent-Type: application/json\nAuthorization: Basic base64Encoded(yourlogin@yourcompany:yourpassword)\n```\n',
'- HTTP Basic auth where the user name is `login@company`.\n- JSON property names are camelCase versions of the documented PascalCase properties (`CustomerID` → `customerID`).\n- Not every operation has a REST route; SOAP-only operations are marked in the index.\n- .NET helper: NuGet package `Exigo.Api.Client` (`new ExigoApiClient("company","login","password")`, async methods such as `CreateOrderAsync`).\n',
'**2. SOAP 1.1 / 1.2** — `POST https://api.exigo.com/3.0/ExigoApi.asmx`, namespace `http://api.exigo.com/`, `SOAPAction: "https://api.exigo.com/{Operation}"`. WSDL: `https://api.exigo.com/3.0/ExigoApi.asmx?WSDL`.\n',
'Every SOAP call carries an `ApiAuthentication` header:\n',
'| Field | Type | Notes |\n|---|---|---|\n| `LoginName` | string | API login |\n| `Password` | string | API password |\n| `Company` | string | Exigo company key |\n| `Identity` | string | optional |\n| `RequestTimeUtc` | dateTime | schema marks it required (minOccurs=1); the docs samples leave it as a placeholder |\n| `Signature` | string | optional; the public docs do not describe a signing scheme |\n',
'**3. CSV (read operations)** — `GET https://api.exigo.com/3.0/csv/?method={Operation}&ApiLoginName=…&ApiPassword=…&ApiCompany=…&{params}`; supported only where the method page says so.\n',
'## Conventions seen across the docs\n',
'- Request/response objects are named `{Operation}Request` / `{Operation}Response`; SOAP result element is `{Operation}Result`.\n- Customers can be addressed by `CustomerID` (Int32) **or** `CustomerKey` (string); sending both raises an exception.\n- Many write operations “can participate in a transaction” — wrap them with `ProcessTransaction` to commit atomically (e.g. create customer + order + auto-order).\n- Optional properties are marked “Optional.” in Notes; WSDL `min=0` fields are optional, `max=unbounded` are arrays.\n- Fields with a lookup marker take company-configured IDs (see company-lists.md).\n',
'## Categories\n','| # | Category | Operations | Description |\n|---|---|---|---|']
for i,c in enumerate(order):
    R.append(f'| {i+1} | [{c}](operations/{cat_file[c]}) | {sum(1 for o in ops if o["category"]==c)} | {cell(cats_desc.get(c,""))} |')
R.append('\n## All operations\n')
R.append('| Operation | Category | REST | Summary |\n|---|---|---|---|')
for o in sorted(ops,key=lambda x:x['name'].lower()):
    rp=rest_path(o)
    R.append(f'| [{o["name"]}](operations/{cat_file[o["category"]]}#{anchor(o["name"])}) | {o["category"]} | {"`"+o["rest"]["method"]+" "+rp+"`" if rp else "SOAP only"} | {cell(short(o["description"],140))} |')
R.append('\n## Machine-readable data\n\n`exigo-api.json` holds the same crawl as structured data (operations with I/O tables, enum values, REST/SOAP examples and samples; WSDL types and enums) for code generation or tooling.\n')
R.append('## Refreshing this crawl\n\nThe crawler and parser live in `docs/exigo-api/tools/`. Run `python3 tools/crawl.py && python3 tools/parse.py && python3 tools/gen.py`. Note: `doc/EnumHelp.aspx` returns HTTP 500 unless a `Referer` header pointing at the method page is sent.\n')
open(f'{OUT}/README.md','w').write('\n'.join(R)+'\n')
json.dump({'source':'https://api.exigo.com/3.0/','version':version,'crawled':TODAY,'operations':ops,'types':types,'enums':enums},open(f'{OUT}/exigo-api.json','w'),indent=1)
print('ok',len(order),'categories')
