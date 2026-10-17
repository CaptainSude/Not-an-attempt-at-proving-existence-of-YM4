from pathlib import Path
import re, subprocess, json, shutil
ROOT=Path(__file__).resolve().parent.parent
BUNDLE=ROOT/"outputs"/"ym4-handoff-2026-10-17"
BUILD=ROOT/"work"/"handoff_build"
LATEX=Path(shutil.which("pdflatex") or "pdflatex")
PREAMBLE=r"""\documentclass[11pt]{article}
\usepackage[margin=0.9in]{geometry}
\usepackage{amsmath,amssymb,amsthm,booktabs,longtable,array}
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{lmodern,microtype}
\usepackage{xurl}
\usepackage[colorlinks=true,linkcolor=blue,urlcolor=blue]{hyperref}
\providecommand{\hrbpath}[1]{\nolinkurl{#1}}
\providecommand{\hncpath}[1]{\nolinkurl{#1}}
\newcommand{\norm}[1]{\left\lVert#1\right\rVert}
\newtheorem{theorem}{Theorem}[section]
\newtheorem{lemma}[theorem]{Lemma}
\newtheorem{proposition}[theorem]{Proposition}
\newtheorem{corollary}[theorem]{Corollary}
\theoremstyle{remark}
\newtheorem{remark}[theorem]{Remark}
\setlength{\emergencystretch}{5em}
\setcounter{tocdepth}{2}
\author{Research handoff}
\date{17 October 2026}
"""
SPECS=[
("01-start-here","Four dimensional Yang--Mills research\\ handoff guide",
 ["handoff_start_here_body.tex"],False),
("02-research-dossier","Four dimensional Yang--Mills\\ research dossier",
 ["handoff_dossier_core.tex","handoff_repository_baseline.tex"],True),
("03-notebook-catalogue","Four dimensional Yang--Mills\\ annotated proof catalogue",
 ["handoff_notebook_catalogue.tex"],True),
]
def build():
    rows=[]
    for name,title,parts,toc in SPECS:
        if not all((ROOT/"work"/p).exists() for p in parts):
            print(f"Pending {name}");continue
        if name=="02-research-dossier":
            core=(ROOT/"work"/parts[0]).read_text(encoding="utf-8-sig")
            before,after=core.split(r"\section{The local construction added in this project}",1)
            baseline=(ROOT/"work"/parts[1]).read_text(encoding="utf-8-sig")
            body=before+"\n"+baseline+"\n"+r"\section{The local construction added in this project}"+after
        else:
            body="\n\n".join((ROOT/"work"/p).read_text(encoding="utf-8-sig") for p in parts)
        source=PREAMBLE+"\n\\title{"+title+"}\n\\begin{document}\n\\maketitle\n"
        if toc: source+="\\tableofcontents\n\\clearpage\n"
        source+=body+"\n\\end{document}\n"
        folder=BUNDLE/"documents"/name
        folder.mkdir(parents=True,exist_ok=True)
        (folder/"main.tex").write_text(source,encoding="utf-8")
        labels=re.findall(r"\\label\{([^}]+)\}",source)
        refs=re.findall(r"\\(?:eqref|ref)\{([^}]+)\}",source)
        assert len(labels)==len(set(labels)),f"Duplicate labels {name}"
        assert set(refs)<=set(labels),(name,set(refs)-set(labels))
        out=BUILD/name;out.mkdir(exist_ok=True)
        result=None
        for i in range(3):
            result=subprocess.run([str(LATEX),"--disable-installer","-no-shell-escape",
                 "-interaction=nonstopmode","-halt-on-error",f"-output-directory={out}",
                 str(folder/"main.tex")],cwd=folder,capture_output=True,text=True,
                 encoding="utf-8",errors="replace",timeout=100)
            if result.returncode: break
        (out/"compiler-output.txt").write_text(result.stdout+"\n"+result.stderr,encoding="utf-8")
        if result.returncode:
            print(json.dumps({"name":name,"ok":False,"error":result.stdout[-5000:]}),flush=True)
            continue
        shutil.copy2(out/"main.pdf",folder/"main.pdf")
        log=(out/"main.log").read_text(encoding="utf-8",errors="replace")
        warnings=[x for x in log.splitlines() if "Overfull" in x or "undefined" in x or "multiply defined" in x]
        row={"name":name,"ok":True,"warnings":warnings}
        rows.append(row);print(json.dumps(row),flush=True)
    (BUILD/"document_compilation.json").write_text(json.dumps(rows,indent=2),encoding="utf-8")
if __name__=="__main__":build()
