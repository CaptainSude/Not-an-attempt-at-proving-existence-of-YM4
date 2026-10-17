from pathlib import Path
import hashlib,json,shutil,subprocess,zipfile,html,re
import pymupdf
ROOT=Path(__file__).resolve().parent.parent
BUNDLE=ROOT/"outputs"/"ym4-handoff-2026-10-17"
BUILD=ROOT/"work"/"handoff_build"
PIN="e392ef45013a581664bab76b90867170b30fe10e"
def sha(p):return hashlib.sha256(p.read_bytes()).hexdigest()
def write(rel,s):
    p=BUNDLE/rel;p.parent.mkdir(parents=True,exist_ok=True);p.write_text(s,encoding="utf-8")

def prepare_archive():
    excluded=[]
    for p in sorted((ROOT/"work").iterdir()):
        if not p.is_file():continue
        if p.suffix.lower() not in (".tex",".md",".txt",".ps1",".py",".json"):
            excluded.append({"path":str(p.relative_to(ROOT)),"reason":"Third-party PDF/image, transient compiler output, or downloaded web response"});continue
        if p.name.startswith(("luscher_weisz_","openaire_")) or p.name=="handoff_inventory_scan.json":
            excluded.append({"path":str(p.relative_to(ROOT)),"reason":"Full third-party extraction/metadata or redundant transient inventory"});continue
        dest=BUNDLE/"research_archive"/"work"/p.name
        dest.parent.mkdir(parents=True,exist_ok=True);shutil.copy2(p,dest)
    write("provenance/archive_exclusions.json",json.dumps(excluded,indent=2))
    for name in ("handoff_repository_source_map.json","handoff_notebook_catalogue.json","handoff_corrections_register.txt"):
        shutil.copy2(ROOT/"work"/name,BUNDLE/"provenance"/name)
    notebook_entries=json.loads((BUILD/"notebooks.json").read_text(encoding="utf-8"))
    catalogue=json.loads((ROOT/"work"/"handoff_notebook_catalogue.json").read_text(encoding="utf-8"))
    lookup={r["number"]:r for r in notebook_entries}
    for r in catalogue["notebooks"]:
        entry=lookup[r["ordinal"]]
        r["bundle_source"]=entry["source"];r["bundle_pdf"]=entry["pdf"]
        r["bundle_original_source"]=entry["source"].replace("main.tex","original.tex")
    write("provenance/notebook_catalogue_portable.json",json.dumps(catalogue,indent=2,ensure_ascii=False))
    write("provenance/notebook_source_manifest.json",json.dumps(notebook_entries,indent=2))
    repo=ROOT/"work"/"Yang--Mills-LLM-experiment"
    rev=subprocess.check_output(["git","-C",str(repo),"rev-parse","HEAD"],text=True).strip()
    assert rev==PIN
    state=subprocess.check_output(["git","-C",str(repo),"status","--porcelain"],text=True)
    assert not state.strip(),"Source checkout changed"
    tree=subprocess.check_output(["git","-C",str(repo),"ls-tree","-r","--long",PIN],text=True,encoding="utf-8")
    write("provenance/pinned_git_tree.txt",tree)
    write("provenance/repository_version.txt",
          f"Repository: https://github.com/ethanwsussman/Yang--Mills-LLM-experiment\n"
          f"Examined commit: {PIN}\nEvidence date: 17 October 2026\n"
          "Pinned checkout clean at packaging. Remote updates are not included.\n"
          "The original repository and third-party papers are not republished in this bundle.\n"
          "See source map for hashes and exact locators, and fetch script for retrieval.\n")
    for name in ("notebook_compilation.json","document_compilation.json"):
        shutil.copy2(BUILD/name,BUNDLE/"provenance"/name)
    return catalogue,notebook_entries

VERIFY=r'''from pathlib import Path
import hashlib,json,sys
root=Path(__file__).resolve().parent.parent
data=json.loads((root/"manifest.json").read_text(encoding="utf-8"))
errors=[]
for item in data["files"]:
    p=root/item["path"]
    if not p.is_file():errors.append("Missing "+item["path"]);continue
    if p.stat().st_size!=item["bytes"] or hashlib.sha256(p.read_bytes()).hexdigest()!=item["sha256"]:
        errors.append("Changed "+item["path"])
print("Checked",len(data["files"]),"files")
if errors:
    print("\n".join(errors));sys.exit(1)
print("All manifest hashes match.")
'''
FETCH=r'''from pathlib import Path
import subprocess,sys
PIN="e392ef45013a581664bab76b90867170b30fe10e"
if len(sys.argv)!=2:raise SystemExit("Usage: python fetch_repository.py NEW_DESTINATION")
dest=Path(sys.argv[1]).resolve()
if dest.exists():raise SystemExit("Destination exists; choose a new directory. Nothing changed.")
subprocess.run(["git","clone","--no-checkout",
 "https://github.com/ethanwsussman/Yang--Mills-LLM-experiment",str(dest)],check=True)
subprocess.run(["git","-C",str(dest),"checkout","--detach",PIN],check=True)
actual=subprocess.check_output(["git","-C",str(dest),"rev-parse","HEAD"],text=True).strip()
assert actual==PIN
print("Verified pinned checkout:",dest)
'''
COMPILE=r'''from pathlib import Path
import subprocess,shutil
root=Path(__file__).resolve().parent.parent
exe=shutil.which("pdflatex")
if not exe:raise SystemExit("Install TeX Live or MiKTeX with the packages named in the sources.")
for source in sorted((root/"documents").rglob("main.tex"))+sorted((root/"notebooks").rglob("main.tex")):
    out=root/"reproduction"/"_build"/source.parent.name
    out.mkdir(parents=True,exist_ok=True)
    for _ in range(3 if "documents" in source.parts else 2):
        subprocess.run([exe,"-no-shell-escape","-interaction=nonstopmode","-halt-on-error",
          "-output-directory="+str(out),str(source)],cwd=source.parent,check=True)
    shutil.copy2(out/"main.pdf",source.parent/"main.pdf")
print("PDFs rebuilt. PDF hashes may change with compiler version; original manifest is a delivery snapshot.")
'''

def main():
    catalogue,entries=prepare_archive()
    write("reproduction/verify_bundle.py",VERIFY)
    write("reproduction/fetch_repository.py",FETCH)
    write("reproduction/build_pdfs.py",COMPILE)
    write("reproduction/README.txt",
"""REPRODUCTION

Read PDFs with any PDF reader; read the sources with any text editor.
The sources are standalone and need no proprietary service.

Rebuild PDFs:
  python reproduction/build_pdfs.py
Requires Python 3, pdflatex, and the standard packages declared in the
sources (amsmath, amssymb, amsthm, geometry, fontenc, lmodern, microtype,
hyperref, booktabs, array, longtable, and xurl for the handoff documents).
The delivered PDFs were built with local MiKTeX. Shell escape is disabled.
The script uses each standalone main.tex and writes build files under
reproduction/_build. It does not delete source files.

Verify delivery:
  python reproduction/verify_bundle.py
This checks every recorded path, byte count and SHA-256. It does not
certify mathematical correctness. The manifest and checksum file
exclude themselves to avoid self-referential hashes.

Retrieve the original repository:
  python reproduction/fetch_repository.py NEW_DIRECTORY
This creates a new checkout, checks out the exact detached commit, and
verifies its identity. It refuses an existing destination.
See provenance/pinned_git_tree.txt and repository source map.

Source layout:
Each notebook original.tex is the exact assembled workspace source.
Its main.tex adds emergency line stretch, permits breaks in the commit
hash and splits two long displays in notebooks25/28. No mathematical
content has been changed. The corresponding main.pdf is built from it.
Historical scripts in research_archive/work may use original workspace
paths; the portable scripts in this directory are the reproduction route.
""")
    pages={str(p.relative_to(BUNDLE)).replace("\\","/"):len(pymupdf.open(p)) for p in BUNDLE.rglob("*.pdf")}
    assert len(pages)==42,(len(pages),"Expected3guides+39notebooks")
    write("provenance/pdf_pages.json",json.dumps(pages,indent=2))
    notes=len(list((BUNDLE/"research_archive"/"work").iterdir()))
    readme=f"""FOUR DIMENSIONAL YANG-MILLS RESEARCH HANDOFF
17 October 2026

START WITH documents/01-start-here/main.pdf or open index.html.

Contents:
  3 handoff documents
  39 mathematical proof notebooks in PDF and editable LaTeX
  {sum(pages.values())} PDF pages in total
  {notes} archived research, source, audit and reproducibility files
  Pinned repository provenance, exact locators, corrections and file hashes

The final new result is Notebook39: an exactly normalized replacement
for separated fixed boxes of the actual bare Wilson measure, with
exterior preservation and local coupling/source bounds.

FOUR-DIMENSIONAL CONTINUUM YANG-MILLS EXISTENCE IS NOT YET PROVED.
The principal remaining step is controlled complete-density/mixed-history
transfer for the actual constrained RG map, followed by observable
bounds, continuum reconstruction and nontrivial Yang-Mills identification.
The physical mass gap remains separate.

Reading documents:
  documents/01-start-here/main.pdf
  documents/02-research-dossier/main.pdf
  documents/03-notebook-catalogue/main.pdf

For the latest proof: notebooks/39-ym4-normalized-box-replacement/main.pdf
For the local positive drift: notebooks/37-ym4-positive-drift/main.pdf
For the full-measure bridge: notebooks/38-ym4-full-measure-bridge/main.pdf

Use the dossier and catalogue for current scope. Older archive checkpoints
may record superseded gaps or routes; they are historical evidence.
Internal audits and compilation do not certify the whole argument.

The examined source repository is pinned at {PIN}.
It explicitly claims an apparent R4 existence argument; the dossier
documents its narrower displayed conclusions and inconsistent proof-status
markers instead of erasing that claim. Original third-party documents
are linked and identified, not republished.

No documents have been sent or published externally.
Verify integrity with python reproduction/verify_bundle.py.
"""
    write("README.txt",readme)
    rows=[]
    for r in catalogue["notebooks"]:
        rows.append(f'<tr><td>{r["ordinal"]:02d}</td><td>{html.escape(r["title"])}</td>'
         f'<td><a href="{r["bundle_pdf"]}">PDF</a> · <a href="{r["bundle_source"]}">TeX</a> · '
         f'<a href="{r["bundle_original_source"]}">Original source</a></td></tr>')
    archived=sorted((BUNDLE/"research_archive"/"work").iterdir())
    research_links="".join(f'<li><a href="{p.relative_to(BUNDLE).as_posix()}">{html.escape(p.name)}</a></li>' for p in archived)
    write("index.html",f"""<!doctype html><html lang="en"><meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1"><title>Yang-Mills research handoff</title>
<style>body{{max-width:1100px;margin:48px auto;padding:0 24px;font:17px/1.6 system-ui;color:#17212e;background:#fff}}
h1,h2{{line-height:1.2}}a{{color:#1253a4}}table{{border-collapse:collapse;width:100%;font-size:15px}}
td,th{{border-bottom:1px solid #ddd;padding:12px;text-align:left}}th{{background:#eef2f6}}
.lead{{font-size:20px;max-width:900px}}small{{color:#526070}}details{{margin:24px 0}}li{{margin:5px 0}}</style>
<h1>Four-dimensional Yang-Mills research handoff</h1><small>17 October 2026 · Pinned research snapshot</small>
<p class="lead">A detailed record of the repository baseline, the local ultraviolet construction,
new full Wilson measure arguments, and the remaining route to continuum existence.</p>
<p><strong>Existence remains unproved.</strong> Notebook39 completes a normalized fixed-box
replacement theorem. The next major step is control of the actual multiscale mixed histories.</p>
<h2>Start here</h2><ol>
<li><a href="documents/01-start-here/main.pdf">Handoff guide</a> — result and reading order</li>
<li><a href="documents/02-research-dossier/main.pdf">Research dossier</a> — baseline, additions and remaining proof</li>
<li><a href="documents/03-notebook-catalogue/main.pdf">Annotated notebook catalogue</a> — dependencies and corrections</li>
</ol><p>{len(pages)} PDFs · {sum(pages.values())} pages · {notes} archived research files.
<a href="README.txt">Plain-text guide</a> · <a href="manifest.json">Manifest</a> ·
<a href="reproduction/README.txt">Reproduction instructions</a></p>
<h2>Proof notebooks</h2><table><thead><tr><th>No.</th><th>Title</th><th>Files</th></tr></thead><tbody>{''.join(rows)}</tbody></table>
<h2>Provenance and review</h2><ul>
<li><a href="provenance/handoff_repository_source_map.json">Pinned repository source map</a></li>
<li><a href="provenance/notebook_catalogue_portable.json">Structured notebook catalogue</a></li>
<li><a href="provenance/handoff_corrections_register.txt">Corrections register</a></li>
<li><a href="provenance/verification_record.txt">Verification record</a></li></ul>
<details><summary>Historical research archive ({notes} files)</summary>
<p>Historical checkpoints and draft paths can be superseded. Use the final dossier and catalogue for current status.</p>
<ul>{research_links}</ul></details></html>""")
    mapping={r["original"]:r["source"] for r in entries}
    mapping.update({f"work/{p.name}":p.relative_to(BUNDLE).as_posix() for p in archived})
    write("provenance/workspace_path_map.json",json.dumps(mapping,indent=2))
    files=[]
    for p in sorted(BUNDLE.rglob("*")):
        if not p.is_file() or p.name in ("manifest.json","SHA256SUMS.txt"):continue
        files.append({"path":p.relative_to(BUNDLE).as_posix(),"bytes":p.stat().st_size,"sha256":sha(p)})
    write("manifest.json",json.dumps({"schema_version":1,"date":"2026-10-17",
      "repository_commit":PIN,"status":"Research handoff; continuum existence unproved",
      "pdf_count":len(pages),"pdf_pages":sum(pages.values()),"files":files},indent=2))
    write("SHA256SUMS.txt","\n".join(f'{x["sha256"]}  {x["path"]}' for x in files)+"\n")
    # Verify every local HTML hyperlink before archiving.
    links=re.findall(r'href="([^"]+)"',(BUNDLE/"index.html").read_text())
    assert all((BUNDLE/x).is_file() for x in links if "://" not in x)
    archive=BUNDLE.with_suffix(".zip")
    with zipfile.ZipFile(archive,"w",zipfile.ZIP_DEFLATED,compresslevel=8) as z:
        for p in sorted(BUNDLE.rglob("*")):
            if p.is_file():z.write(p,Path(BUNDLE.name)/p.relative_to(BUNDLE))
    with zipfile.ZipFile(archive) as z:
        assert z.testzip() is None
        assert len(z.namelist())==len(files)+2
        for item in files:
            data=z.read(BUNDLE.name+"/"+item["path"])
            assert hashlib.sha256(data).hexdigest()==item["sha256"]
    print(json.dumps({"bundle":str(BUNDLE),"zip":str(archive),"zip_bytes":archive.stat().st_size,
                     "files":len(files),"pdfs":len(pages),"pages":sum(pages.values()),
                     "research_files":notes,"html_links":len(links),"zip_sha256":sha(archive)}),flush=True)
if __name__=="__main__":main()
