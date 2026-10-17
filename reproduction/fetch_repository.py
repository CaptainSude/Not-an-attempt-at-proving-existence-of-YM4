from pathlib import Path
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
