from pathlib import Path
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
