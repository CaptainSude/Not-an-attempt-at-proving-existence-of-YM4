from pathlib import Path
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
