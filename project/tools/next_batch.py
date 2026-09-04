#!/usr/bin/env python3
import argparse,json,pathlib
p=argparse.ArgumentParser()
p.add_argument('--category')
p.add_argument('--max-words',type=int,default=1000)
p.add_argument('--min-words',type=int,default=0)
p.add_argument('--count',type=int,default=10)
p.add_argument('--include-flags',action='store_true')
a=p.parse_args()
root=pathlib.Path(__file__).resolve().parents[2]
rows=[json.loads(x) for x in (root/'project'/'translation_manifest.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
sel=[]
for r in rows:
    if r['translation_status']!='untranslated': continue
    if not a.include_flags and r.get('source_qa_status')=='confirmed_erratum': continue
    if a.category and r['category']!=a.category: continue
    wc=int(r.get('body_word_count_rough') or 0)
    if not (a.min_words<=wc<=a.max_words): continue
    if not a.include_flags and ('non_russian_or_mixed_source_language' in r.get('flags',[])): continue
    sel.append(r)
    if len(sel)>=a.count: break
for r in sel:
    print(f"{r['body_word_count_rough']:>6}  {r['category']:<16} {r['output_path']}  |  {r['title_ru']}")
