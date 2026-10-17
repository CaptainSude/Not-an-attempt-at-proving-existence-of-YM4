# Public edition and provenance

This is the public edition of the research handoff assembled on 17 October 2026, published with the project owner's authorization at [CaptainSude/Not-an-attempt-at-proving-existence-of-YM4](https://github.com/CaptainSude/Not-an-attempt-at-proving-existence-of-YM4).

## Preserved content

All 682 payload files listed in the original handoff manifest are included. All 42 mathematical/reading PDFs and every notebook's compiling and original assembled sources are byte-identical to that handoff. The repository contains 39 notebooks, 3 lead documents, and 539 historical research files.

The [original manifest](provenance/original_handoff_manifest.json) records the original handoff. The root [manifest](manifest.json) and [SHA256SUMS](SHA256SUMS.txt) record the public edition, including the navigation documents added for GitHub.

## Minimal changes for publication

The [change record](provenance/publication_changes.json) records original and public hashes for four edited payload files:

- One historical checkpoint's personal workspace path was replaced by a neutral placeholder.
- Two historical build scripts now find the TeX compiler on PATH instead of referring to a personal installation path.
- The plain-text guide's statement that nothing had yet been published was date-qualified and linked to this public edition.

No mathematical statement, proof, formula, or PDF was changed. The README, notebook index, contribution guide, open-problem map, publication record, and Git configuration files were added for readers.

The copied payload is selected from the original manifest. A subsequently extracted duplicate directory, transient build files, raw conversation history, local credentials, and unrelated workspace files are not part of the publication.

## Reading historical statements

Old notes retain their historical date, task status, abandoned routes, and next-task instructions. Statements such as "not yet published" or "no external publication authorized" describe the earlier session state. The later user instruction expressly authorizes this public edition.

The archive's internal reviews are not external peer review. See the [verification record](provenance/verification_record.txt) for the actual compilation and visual-review scope, and the [dossier](documents/02-research-dossier/main.pdf) for current mathematical status.

## Original project

The original public work is at [ethanwsussman/Yang--Mills-LLM-experiment](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment). The examined baseline is commit e392ef45013a581664bab76b90867170b30fe10e.

Its repository files and complete third-party papers are identified rather than republished here. The [source map](provenance/handoff_repository_source_map.json), pinned tree, and retrieval script support checking the exact baseline. Attribution to the original project does not imply its authors reviewed or endorsed this continuation.
