#!/usr/bin/env python3
import sys,json,pathlib,hashlib
if len(sys.argv)!=2:
    raise SystemExit('usage: check_source.py /path/to/tolstoy-russian-md-audited')
ru=pathlib.Path(sys.argv[1]); root=pathlib.Path(__file__).resolve().parents[1]
rows=[json.loads(x) for x in (root/'translation_manifest.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
missing=[]; changed=[]
for r in rows:
    p=ru/r['source_ru_path']
    if not p.exists(): missing.append(r['source_ru_path']); continue
    h=hashlib.sha256(p.read_bytes()).hexdigest()
    if h!=r['source_ru_sha256']: changed.append((r['source_ru_path'],r['source_ru_sha256'],h))
print(f'checked: {len(rows):,}')
print(f'missing: {len(missing):,}')
print(f'changed: {len(changed):,}')
for x in missing[:50]: print('MISSING',x)
for x,old,new in changed[:50]: print('CHANGED',x,old,new)
raise SystemExit(1 if missing or changed else 0)
