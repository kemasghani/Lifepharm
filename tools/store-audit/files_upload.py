"""Upload new images to a store's Shopify Files (skips names that already exist):
stagedUploadsCreate -> multipart POST -> fileCreate -> poll READY.
Usage: STORE=uk [ALTS=alts.json] python3 tools/store-audit/files_upload.py img1.jpg img2.jpg
Files are store admin data shared by every theme, including live: upload only finished, approved images."""
import sys, os, time, json, uuid, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shopify import gql
STORE=os.environ.get('STORE','uk')
paths=sys.argv[1:]
# skip existing
names=[os.path.basename(p) for p in paths]
q=' OR '.join(f'filename:{n.rsplit(".",1)[0]}*' for n in names)
ex=gql(STORE,'query($q:String){files(first:50,query:$q){nodes{... on MediaImage{image{url}} fileStatus}}}',{'q':q})
existing={n['image']['url'].split('/')[-1].split('?')[0] for n in ex['data']['files']['nodes'] if n.get('image')}
print('existing:',existing)
todo=[p for p in paths if os.path.basename(p) not in existing]
inp=[{'filename':os.path.basename(p),'mimeType':'image/jpeg','resource':'IMAGE','httpMethod':'POST','fileSize':str(os.path.getsize(p))} for p in todo]
if not inp: sys.exit()
r=gql(STORE,'mutation($i:[StagedUploadInput!]!){stagedUploadsCreate(input:$i){stagedTargets{url resourceUrl parameters{name value}} userErrors{field message}}}',{'i':inp})
targets=r['data']['stagedUploadsCreate']['stagedTargets']
res=[]
for p,t in zip(todo,targets):
    b='----lp'+uuid.uuid4().hex; body=b''
    for prm in t['parameters']:
        body+=f'--{b}\r\nContent-Disposition: form-data; name="{prm["name"]}"\r\n\r\n{prm["value"]}\r\n'.encode()
    body+=f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="{os.path.basename(p)}"\r\nContent-Type: image/jpeg\r\n\r\n'.encode()+open(p,'rb').read()+f'\r\n--{b}--\r\n'.encode()
    req=urllib.request.Request(t['url'],body,{'Content-Type':f'multipart/form-data; boundary={b}'})
    print(os.path.basename(p),'upload',urllib.request.urlopen(req,timeout=120).status)
    res.append(t['resourceUrl'])
# optional alt text map: ALTS=path/to/alts.json with {"<filename without extension>": "alt text"}
alts=json.load(open(os.environ['ALTS'])) if os.environ.get('ALTS') else {}
files=[{'originalSource':u,'contentType':'IMAGE','alt':alts.get(os.path.basename(p).rsplit('.',1)[0],''),'filename':os.path.basename(p)} for p,u in zip(todo,res)]
r=gql(STORE,'mutation($f:[FileCreateInput!]!){fileCreate(files:$f){files{id fileStatus} userErrors{field message}}}',{'f':files})
print(json.dumps(r['data']['fileCreate']['userErrors']))
ids=[f['id'] for f in r['data']['fileCreate']['files']]
for _ in range(30):
    time.sleep(3)
    s=gql(STORE,'query($ids:[ID!]!){nodes(ids:$ids){... on MediaImage{fileStatus image{url}}}}',{'ids':ids})['data']['nodes']
    if all(n['fileStatus'] in ('READY','FAILED') for n in s):
        for n in s: print(n['fileStatus'], n['image'] and n['image']['url'])
        break
