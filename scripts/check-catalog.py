"""Check catalogue invariants and optionally GET every current/related destination."""
import json,pathlib,urllib.request,concurrent.futures,sys,re,hashlib
root=pathlib.Path(__file__).resolve().parents[1];apps=json.loads((root/'catalog.json').read_text())
assert len(apps)==42 and sorted(a['id'] for a in apps)==list(range(1,43))
assert len({a['title'] for a in apps})==42
for a in apps:
 for k in ['title','value','evidence','gap','acceptance','commercial','review_level','status']:assert a[k].strip(),(a['id'],k)
 for k in ['url','source_url','related_url']:
  assert not a[k] or a[k].startswith('https://'),(a['id'],k)
 assert not a['url'] or not a['url'].startswith('/apps/')
 assert not a['url'] or a['status'] not in ['Demo on request','Access restricted']
assert sum(bool(a['url']) for a in apps)==32
assert sum(a['status']=='Demo tested' for a in apps)==2
assert sum(a['status']=='Demo on request' for a in apps)==9
assert sum(a['status']=='Access restricted' for a in apps)==1
assert (root/'catalog-data.js').read_text()=='window.OECS_CATALOG = '+json.dumps(apps,indent=2,ensure_ascii=False)+';\n'
print('PASS: 42 unique assessments, 32 public launches, safe URLs, 9 unavailable editions, 1 restricted and synchronized browser data.')
if '--http' in sys.argv:
 urls=sorted({a[k] for a in apps for k in ['url','related_url'] if a[k]})
 def check(u):
  try:
   r=urllib.request.urlopen(u,timeout=30);b=r.read();s=b.decode('utf8','replace');t=re.search('<title>(.*?)</title>',s,re.S)
   return dict(url=u,status=r.status,final_url=r.url,title=t.group(1) if t else '',sha256=hashlib.sha256(b).hexdigest())
  except Exception as e:return dict(url=u,error=str(e))
 with concurrent.futures.ThreadPoolExecutor(max_workers=8) as e:results=list(e.map(check,urls))
 (root/'review/current-link-audit.json').write_text(json.dumps(results,indent=2)+'\n')
 for r in results:print(r.get('status',r.get('error')),r['url'])
 if any(r.get('status')!=200 for r in results):sys.exit(1)
 print('PASS: every unique launch and related destination responded HTTP 200. This does not prove app functionality.')
