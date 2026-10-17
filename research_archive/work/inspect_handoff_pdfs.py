from pathlib import Path
import json, math, sys
import pymupdf as fitz
from PIL import Image,ImageDraw
ROOT=Path(__file__).resolve().parent.parent
BUNDLE=ROOT/"outputs"/"ym4-handoff-2026-10-17"
QA=ROOT/"work"/"handoff_build"/"visual"
QA.mkdir(parents=True,exist_ok=True)
documents_only="--documents-only" in sys.argv
prior=QA/"pdf_inspection.json"
records=([r for r in json.loads(prior.read_text(encoding="utf-8"))
          if not r["pdf"].startswith("documents/")]
         if documents_only and prior.exists() else [])
search_root=BUNDLE/"documents" if documents_only else BUNDLE
for pdf in sorted(search_root.rglob("*.pdf")):
    rel=pdf.relative_to(BUNDLE)
    key=pdf.parent.name
    folder=QA/key;folder.mkdir(exist_ok=True)
    doc=fitz.open(pdf)
    out_of_bounds=[];bad_text=[];blanks=[]
    thumbs=[]
    for i,page in enumerate(doc):
        txt=page.get_text()
        if len(txt.strip())<5:blanks.append(i+1)
        if "\ufffd" in txt or "\x00" in txt:bad_text.append(i+1)
        for block in page.get_text("dict")["blocks"]:
            for line in block.get("lines",[]):
                for span in line["spans"]:
                    x0,y0,x1,y1=span["bbox"]
                    if x0<20 or x1>page.rect.width-20 or y0<10 or y1>page.rect.height-10:
                        out_of_bounds.append({"page":i+1,"bbox":list(span["bbox"]),"text":span["text"]})
        pix=page.get_pixmap(matrix=fitz.Matrix(1.25,1.25),alpha=False)
        img=Image.frombytes("RGB",[pix.width,pix.height],pix.samples)
        img.save(folder/f"page-{i+1:03d}.png")
        img.thumbnail((330,440))
        thumb=Image.new("RGB",(350,475),"#e9edf2")
        thumb.paste(img,((350-img.width)//2,8))
        ImageDraw.Draw(thumb).text((12,454),f"{key}   p{i+1}",fill="black")
        thumbs.append(thumb)
    sheets=[]
    for first in range(0,len(thumbs),20):
        subset=thumbs[first:first+20]
        sheet=Image.new("RGB",(1400,475*math.ceil(len(subset)/4)),"white")
        for j,img in enumerate(subset):sheet.paste(img,((j%4)*350,(j//4)*475))
        target=folder/f"contact-{first//20+1:02d}.png";sheet.save(target)
        sheets.append(str(target))
    rec={"pdf":str(rel).replace("\\","/"),"pages":len(doc),
         "blank_pages":blanks,"replacement_chars":bad_text,"out_of_bounds":out_of_bounds,
         "contact_sheets":sheets}
    records.append(rec)
    print(json.dumps({"pdf":str(rel),"pages":len(doc),"bounds":len(out_of_bounds),"blank":blanks}),flush=True)
(QA/"pdf_inspection.json").write_text(json.dumps(records,indent=2),encoding="utf-8")
print("TOTAL",sum(r["pages"] for r in records),flush=True)
