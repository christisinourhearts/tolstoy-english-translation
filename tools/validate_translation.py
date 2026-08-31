#!/usr/bin/env python3
import sys,json,pathlib,re,hashlib
if len(sys.argv)!=2:
    raise SystemExit('usage: validate_translation.py /path/to/tolstoy-russian-md-audited')
ru=pathlib.Path(sys.argv[1]); en=pathlib.Path(__file__).resolve().parents[1]
rows=[json.loads(x) for x in (en/'translation_manifest.jsonl').read_text(encoding='utf-8').splitlines() if x.strip()]
page_re=re.compile(r'<!--\s*vol\.\s*\d+,\s*p\.\s*[^>]+?-->')
fn_ref_re=re.compile(r'\[\^([^\]]+)\](?!:)')
fn_def_re=re.compile(r'^\[\^([^\]]+)\]:',re.M)
front_re=re.compile(r'^---\s*\n(.*?)\n---\s*\n',re.S)
def yaml_scalar(text,key):
    m=re.search(rf'(?m)^{re.escape(key)}:\s*["\']?([^"\'\n]+)["\']?\s*$',text)
    return m.group(1).strip() if m else None
errors=[]; warnings=[]; checked=0
seen_paths=set(); seen_ids=set()
for r in rows:
    if r['output_path'] in seen_paths: errors.append((r['output_path'],'duplicate output path in manifest'))
    seen_paths.add(r['output_path'])
    if r['id'] in seen_ids: errors.append((r['output_path'],'duplicate stable id in manifest'))
    seen_ids.add(r['id'])
    if r.get('translation_status')=='reviewed':
        if r.get('fidelity_audit_status') not in ('pass','passed'): errors.append((r['output_path'],'reviewed but fidelity audit is not pass'))
        if r.get('english_edit_status')!='complete': errors.append((r['output_path'],'reviewed but English edit is not complete'))
        if r.get('final_source_audit_status') not in ('pass','passed'): errors.append((r['output_path'],'reviewed but final source audit is not pass'))
        if r.get('coverage_audit_status') not in ('pass','p001_legacy_unstructured_pass'):
            errors.append((r['output_path'],'reviewed but coverage audit has not passed'))
    ep=en/r['output_path']
    if not ep.exists():
        if r.get('translation_status')=='reviewed': errors.append((r['output_path'],'reviewed row missing English file'))
        continue
    rp=ru/r['source_ru_path']
    if not rp.exists(): errors.append((r['output_path'],'missing Russian source')); continue
    current=hashlib.sha256(rp.read_bytes()).hexdigest()
    if current!=r['source_ru_sha256']: errors.append((r['output_path'],'Russian source checksum changed'))
    rt=rp.read_text(encoding='utf-8'); et=ep.read_text(encoding='utf-8')
    if page_re.findall(rt)!=page_re.findall(et): errors.append((r['output_path'],'page-marker sequence differs'))
    # Source and target should carry the exact source identity in front matter.
    fm=front_re.match(et)
    if not fm: errors.append((r['output_path'],'missing YAML front matter'))
    else:
        f=fm.group(1)
        sp=yaml_scalar(f,'source_ru_path')
        sh=yaml_scalar(f,'source_ru_sha256')
        if sp!=r['source_ru_path']: errors.append((r['output_path'],f'front-matter source_ru_path mismatch: {sp!r}'))
        if sh!=r['source_ru_sha256']: errors.append((r['output_path'],'front-matter source_ru_sha256 mismatch'))
    # Footnote definitions should preserve the source identifiers for complete/applicable apparatus.
    sdefs=set(fn_def_re.findall(rt)); edefs=set(fn_def_re.findall(et)); erefs=set(fn_ref_re.findall(et))
    dangling=sorted(erefs-edefs)
    if dangling: errors.append((r['output_path'],f'dangling footnote refs: {dangling[:10]}'))
    # A confirmed source erratum may require the English to restore a footnote that is
    # missing from the audited Markdown. Such exceptions must be declared exactly in
    # the manifest; they do not weaken footnote equality for any other unit.
    extra_defs=set(str(x) for x in (r.get('source_qa_extra_footnote_ids') or []))
    if extra_defs and r.get('source_qa_status')!='confirmed_erratum':
        errors.append((r['output_path'],'source_qa_extra_footnote_ids requires source_qa_status=confirmed_erratum'))
    expected_defs=sdefs|extra_defs
    if r.get('apparatus_translation_status') in ('translated','complete','not_applicable') and expected_defs!=edefs:
        errors.append((r['output_path'],f'footnote definition ids differ expected={sorted(expected_defs)} target={sorted(edefs)}'))
    # Cyrillic in English is a warning, not an error: some sources intentionally retain Russian tokens/quotes.
    body=front_re.sub('',et,count=1)
    if re.search(r'[А-Яа-яЁё]',body): warnings.append((r['output_path'],'Cyrillic remains in English body; verify intentional'))
    checked+=1
print(f'English files checked: {checked:,}')
print(f'errors: {len(errors):,}')
print(f'warnings: {len(warnings):,}')
for p,msg in errors[:100]: print('ERROR',p,msg)
for p,msg in warnings[:50]: print('WARNING',p,msg)
raise SystemExit(1 if errors else 0)
