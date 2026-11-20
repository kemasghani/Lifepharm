"""Replace the contents of an existing Shopify File (same filename) with a local image: staged upload -> fileUpdate(originalSource)."""
import sys, os, time, uuid, urllib.request
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from shopify import gql
store, path = sys.argv[1], sys.argv[2]
name = os.path.basename(path)
nodes = gql(store, 'query($q:String){files(first:10,query:$q){nodes{id ... on MediaImage{image{url}}}}}', {'q': f'filename:"{name}"'})['data']['files']['nodes']
match = [n for n in nodes if n.get('image') and n['image']['url'].split('?')[0].rsplit('/', 1)[-1] == name]
if not match:
    print(store, name, 'not found -> use files_upload.py'); sys.exit(2)
fid = match[0]['id']
t = gql(store, 'mutation($i:[StagedUploadInput!]!){stagedUploadsCreate(input:$i){stagedTargets{url resourceUrl parameters{name value}} userErrors{message}}}',
        {'i': [{'filename': name, 'mimeType': 'image/jpeg', 'resource': 'IMAGE', 'httpMethod': 'POST', 'fileSize': str(os.path.getsize(path))}]})['data']['stagedUploadsCreate']['stagedTargets'][0]
b = '----lp' + uuid.uuid4().hex
body = b''.join(f'--{b}\r\nContent-Disposition: form-data; name="{p["name"]}"\r\n\r\n{p["value"]}\r\n'.encode() for p in t['parameters'])
body += f'--{b}\r\nContent-Disposition: form-data; name="file"; filename="{name}"\r\nContent-Type: image/jpeg\r\n\r\n'.encode() + open(path, 'rb').read() + f'\r\n--{b}--\r\n'.encode()
urllib.request.urlopen(urllib.request.Request(t['url'], body, {'Content-Type': f'multipart/form-data; boundary={b}'}), timeout=120)
r = gql(store, 'mutation($f:[FileUpdateInput!]!){fileUpdate(files:$f){files{id fileStatus} userErrors{field message code}}}', {'f': [{'id': fid, 'originalSource': t['resourceUrl']}]})
print(store, name, r['data']['fileUpdate']['userErrors'] or 'update sent')
for _ in range(30):
    time.sleep(3)
    n = gql(store, 'query($id:ID!){node(id:$id){... on MediaImage{fileStatus image{url width height}}}}', {'id': fid})['data']['node']
    if n['fileStatus'] in ('READY', 'FAILED'):
        print(store, n['fileStatus'], n['image'] and n['image']['url'].split('?')[0].rsplit('/',1)[-1], n['image'] and (n['image']['width'], n['image']['height'])); break
