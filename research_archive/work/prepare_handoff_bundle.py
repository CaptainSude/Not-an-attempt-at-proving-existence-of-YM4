"""Portable snapshot of authored notebooks. No mutation of original proofs."""
from pathlib import Path
import re, json, shutil, hashlib, subprocess, time, sys

ROOT = Path(__file__).resolve().parent.parent
BUNDLE = ROOT / "outputs" / "ym4-handoff-2026-10-17"
BUILD = ROOT / "work" / "handoff_build"
LATEX = Path(shutil.which("pdflatex") or "pdflatex")

def digest(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()

def prepare():
    for rel in ("documents", "notebooks", "research_archive", "provenance", "reproduction"):
        (BUNDLE/rel).mkdir(parents=True, exist_ok=True)
    BUILD.mkdir(parents=True, exist_ok=True)
    entries = []
    for src in sorted((ROOT/"outputs").rglob("*.tex")):
        if BUNDLE in src.parents:
            continue
        data = src.read_text(encoding="utf-8-sig")
        match = re.search(r"Notebook\s+(\d+)\s*:", data)
        if not match:
            continue
        num = int(match.group(1))
        short = src.parent.name if src.name == "main.tex" else src.stem
        folder = BUNDLE/"notebooks"/f"{num:02d}-{short}"
        folder.mkdir(parents=True, exist_ok=True)
        target = folder/"main.tex"
        shutil.copy2(src, folder/"original.tex")
        rendered = data.replace(r"\begin{document}",r"\setlength{\emergencystretch}{5em}"+"\n"+r"\begin{document}",1)
        sha="e392ef45013a581664bab76b90867170b30fe10e"
        rendered=rendered.replace(r"\texttt{"+sha+"}",r"\texttt{"+r"\allowbreak ".join(sha[i:i+10] for i in range(0,len(sha),10))+"}")
        if num==25:
            rendered=rendered.replace(
                r"A_{\mathrm o,N}(w)=T_N(A_{\mathrm c,N}(w)),\qquad",
                r"\begin{aligned} A_{\mathrm o,N}(w)&=T_N(A_{\mathrm c,N}(w)),\qquad",1)
            rendered=rendered.replace(
                r"U_N(w)=e^{i\eta A_{\mathrm o,N}(w)},\qquad",
                r"U_N(w)=e^{i\eta A_{\mathrm o,N}(w)},\\",1)
            rendered=rendered.replace(
                r"M_L^{k+s}(U_N(w))=e^{iw},\qquad",
                r"M_L^{k+s}(U_N(w))&=e^{iw},\qquad",1)
            rendered=rendered.replace(
                r"\label{sv-ordinary-minimizer}",r"\end{aligned}"+"\n"+r"\label{sv-ordinary-minimizer}",1)
        if num==28:
            rendered=rendered.replace(
                r"V_p(W)=\mathcal M_\ell^k U_{MR}(W),\qquad",
                r"\begin{aligned} V_p(W)&=\mathcal M_\ell^k U_{MR}(W),\qquad",1)
            rendered=rendered.replace(
                r"V^\star(W)=V_p(W)^{u(W)},\qquad P_R(V^\star)=1,",
                r"V^\star(W)=V_p(W)^{u(W)},\\"+"\n"+r"P_R(V^\star)&=1,",1)
            rendered=rendered.replace(
                r"\label{cdm-background}",r"\end{aligned}"+"\n"+r"\label{cdm-background}",1)
        target.write_text(rendered,encoding="utf-8")
        pdf_path=folder/"main.pdf"
        if pdf_path.exists(): pdf_path.unlink()
        entries.append(dict(number=num, original=str(src.relative_to(ROOT)).replace("\\","/"),
                            source=str(target.relative_to(BUNDLE)).replace("\\","/"),
                            pdf=str((folder/"main.pdf").relative_to(BUNDLE)).replace("\\","/"),
                            original_source_sha256=digest(src),
                            source_sha256=digest(target),
                            layout_changes="Emergency paragraph stretch; breakable commit hash; displays split in25/28. No mathematical content change."))
    nums=[r["number"] for r in entries]
    if len(nums)!=len(set(nums)):
        raise RuntimeError("Duplicate notebook numbers")
    entries.sort(key=lambda r:r["number"])
    (BUILD/"notebooks.json").write_text(json.dumps(entries,indent=2),encoding="utf-8")
    print(json.dumps({"prepared":len(entries),"numbers":nums,"bundle":str(BUNDLE)}))

def compile_one(entry):
    src=BUNDLE/entry["source"]
    out=BUILD/f"latex-{entry['number']:02d}"
    out.mkdir(exist_ok=True)
    start=time.time()
    logs=[]
    for k in range(2):
        cmd=[str(LATEX),"--disable-installer","-no-shell-escape","-interaction=nonstopmode",
             "-halt-on-error",f"-output-directory={out}",str(src)]
        proc=subprocess.run(cmd,cwd=src.parent,capture_output=True,text=True,
                            encoding="utf-8",errors="replace",timeout=100)
        logs.append(proc.stdout+"\n"+proc.stderr)
        if proc.returncode:
            (out/"compiler-output.txt").write_text("\n".join(logs),encoding="utf-8")
            return {"number":entry["number"],"ok":False,"error":logs[-1][-5000:]}
    pdf=out/"main.pdf"
    shutil.copy2(pdf,BUNDLE/entry["pdf"])
    log=(out/"main.log").read_text(encoding="utf-8",errors="replace")
    warnings=[line for line in log.splitlines()
              if ("Overfull" in line or "undefined" in line or "multiply defined" in line)]
    return {"number":entry["number"],"ok":True,"seconds":round(time.time()-start,2),
            "pdf_sha256":digest(pdf),"warnings":warnings}

def compile_all():
    entries=json.loads((BUILD/"notebooks.json").read_text(encoding="utf-8"))
    records=[]
    for entry in entries:
        target=BUNDLE/entry["pdf"]
        if target.exists():
            records.append({"number":entry["number"],"ok":True,"existing":True,
                            "pdf_sha256":digest(target)})
            continue
        try:
            result=compile_one(entry)
        except Exception as exc:
            result={"number":entry["number"],"ok":False,"error":str(exc)}
        records.append(result)
        print(json.dumps(result),flush=True)
        (BUILD/"notebook_compilation.json").write_text(json.dumps(records,indent=2),encoding="utf-8")
    (BUILD/"notebook_compilation.json").write_text(json.dumps(records,indent=2),encoding="utf-8")

if __name__=="__main__":
    if sys.argv[1:]==["prepare"]: prepare()
    elif sys.argv[1:]==["compile"]: compile_all()
    else: raise SystemExit("Use prepare or compile")
