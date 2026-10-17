REPRODUCTION

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
