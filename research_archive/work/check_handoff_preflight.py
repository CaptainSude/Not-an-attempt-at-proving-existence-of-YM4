from pathlib import Path
import json,hashlib,re
ROOT=Path(__file__).resolve().parent.parent
BUNDLE=ROOT/"outputs"/"ym4-handoff-2026-10-17"
BUILD=ROOT/"work"/"handoff_build"
rows=json.loads((BUILD/"notebooks.json").read_text(encoding="utf-8"))
assert len(rows)==39
for row in rows:
    source=BUNDLE/row["source"]
    original=source.parent/"original.tex"
    assert original.read_bytes()==(ROOT/row["original"]).read_bytes(),row["number"]
for name,count in (("notebook_compilation.json",39),("document_compilation.json",3)):
    results=json.loads((BUILD/name).read_text(encoding="utf-8"))
    assert len(results)==count
    assert all(r["ok"] and not r["warnings"] for r in results)
for source in list((BUNDLE/"documents").rglob("main.tex"))+list((BUNDLE/"notebooks").rglob("main.tex")):
    tex=source.read_text(encoding="utf-8")
    assert not re.search(r"\\(?:input|include|includegraphics|bibliography)\s*\{",tex),source
    labels=re.findall(r"\\label\{([^}]+)\}",tex)
    refs=re.findall(r"\\(?:eqref|ref)\{([^}]+)\}",tex)
    assert len(labels)==len(set(labels)),source
    assert set(refs)<=set(labels),(source,set(refs)-set(labels))
qa=json.loads((BUILD/"visual"/"pdf_inspection.json").read_text(encoding="utf-8"))
assert len(qa)==42
assert sum(r["pages"] for r in qa)==622
assert all(not r["blank_pages"] and not r["out_of_bounds"] for r in qa)
portable=[{k:v for k,v in row.items() if k!="contact_sheets"} for row in qa]
(BUNDLE/"provenance"/"pdf_layout_checks.json").write_text(json.dumps(portable,indent=2),encoding="utf-8")
print("PASS:39 exact original sources,42 standalone compilations, labels/references,622 pages, no blank/out-of-bounds pages.")
