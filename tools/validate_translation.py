#!/usr/bin/env python3
import sys,json,pathlib,re,hashlib
if len(sys.argv)!=2:
    raise SystemExit('usage: validate_translation.py /path/to/tolstoy-russian-md-audited')
ru=pathlib.Path(sys.argv[1]); en=pathlib.Path(__file__).resolve().parents[1]
rows=[json.loads(x) for x in (en/'translation_manifest.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
page_re=re.compile(r'<!--\s*vol\.\s*\d+,\s*p\.\s*[^>]+?-->')
fn_ref_re=re.compile(r'\[\^([^\]]+)\](?!:)')
fn_def_re=re.compile(r'^\[\^([^\]]+)\]:',re.M)
errors=[]; checked=0
for r in rows:
    ep=en/r['output_path']
    if not ep.exists(): continue
    rp=ru/r['source_ru_path']
    if not rp.exists(): errors.append((r['output_path'],'missing Russian source')); continue
    current=hashlib.sha256(rp.read_bytes()).hexdigest()
    if current!=r['source_ru_sha256']: errors.append((r['output_path'],'Russian source checksum changed'))
    rt=rp.read_text(encoding='utf-8'); et=ep.read_text(encoding='utf-8')
    if page_re.findall(rt)!=page_re.findall(et): errors.append((r['output_path'],'page-marker sequence differs'))
    # Definitions/references may be absent from body-only milestones, but if defs exist ensure references are not dangling.
    defs=set(fn_def_re.findall(et)); refs=set(fn_ref_re.findall(et))
    dangling=sorted(refs-defs)
    if dangling: errors.append((r['output_path'],f'dangling footnote refs: {dangling[:10]}'))
    checked+=1
print(f'English files checked: {checked:,}')
print(f'errors: {len(errors):,}')
for p,msg in errors[:100]: print('ERROR',p,msg)
raise SystemExit(1 if errors else 0)
