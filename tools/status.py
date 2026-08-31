#!/usr/bin/env python3
import json, collections, pathlib
root=pathlib.Path(__file__).resolve().parents[1]
rows=[json.loads(x) for x in (root/'translation_manifest.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
print(f'Documents: {len(rows):,}')
for field in ['category','translation_status','fidelity_audit_status','english_edit_status','final_source_audit_status','apparatus_translation_status']:
    print(f'\n{field}:')
    for k,v in collections.Counter(str(r.get(field,'')) for r in rows).most_common():
        print(f'  {k or "(blank)":28} {v:>6,}')
print('\nRough source words by translation status:')
for status in sorted({r['translation_status'] for r in rows}):
    n=sum(int(r.get('body_word_count_rough') or 0) for r in rows if r['translation_status']==status)
    print(f'  {status:28} {n:>12,}')
