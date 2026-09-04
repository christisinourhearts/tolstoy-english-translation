#!/usr/bin/env python3
import json, pathlib, sys, hashlib
root=pathlib.Path(__file__).resolve().parents[2]
manifest=[json.loads(x) for x in (root/'project'/'translation_manifest.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
errors=[]; checked=0
for r in manifest:
    if r.get('coverage_audit_status')!='pass':
        continue
    checked += 1
    safe=r['id'].replace('::','__').replace('/','_')+'.json'
    cp=root/'project'/'qa'/'coverage'/safe
    if not cp.exists():
        errors.append((r['output_path'],'missing structured coverage record')); continue
    try: rec=json.loads(cp.read_text(encoding='utf-8'))
    except Exception as e:
        errors.append((r['output_path'],f'invalid coverage JSON: {e}')); continue
    if rec.get('source_path')!=r['source_ru_path']:
        errors.append((r['output_path'],'coverage source_path disagrees with manifest'))
    if rec.get('source_sha256')!=r['source_ru_sha256']:
        errors.append((r['output_path'],'coverage source hash disagrees with manifest'))
    if rec.get('result')!='PASS':
        errors.append((r['output_path'],f"coverage result is {rec.get('result')!r}, expected PASS"))
    if rec.get('coverage_method')!='exhaustive_source_to_target_pass':
        errors.append((r['output_path'],'unexpected/missing coverage method'))
    if rec.get('every_substantive_source_passage_checked') is not True:
        errors.append((r['output_path'],'coverage does not certify every source passage checked'))
    if rec.get('known_omissions') not in ([],0):
        errors.append((r['output_path'],'coverage record contains known omissions'))
    if rec.get('known_unsupported_additions') not in ([],0):
        errors.append((r['output_path'],'coverage record contains unsupported additions'))
print(f'coverage records checked: {checked:,}')
print(f'errors: {len(errors):,}')
for p,msg in errors[:100]: print('ERROR',p,msg)
raise SystemExit(1 if errors else 0)
