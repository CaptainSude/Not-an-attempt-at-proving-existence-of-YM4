# Not an attempt at proving existence of YM4

**A continuation of the public Yang–Mills work of Levent and his collaborators, released in [ethanwsussman/Yang--Mills-LLM-experiment](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment), hosted by Ethan Sussman.**

The title and repository description are humorous. The goal is serious: advance that program toward a rigorous existence argument for a nontrivial four-dimensional Yang–Mills quantum theory, and ultimately investigate the mass gap.

This repository makes the research available so other mathematicians can inspect it, correct it, and carry it further. **It does not yet contain a completed continuum existence proof or a mass-gap proof.** It contains a developed local ultraviolet construction, finite Wilson-measure results, and a detailed account of the remaining steps.

## Start here

| Read | Purpose |
| --- | --- |
| **[Handoff guide — 3 pages](documents/01-start-here/main.pdf)** | Results, boundaries, and reading order |
| **[Research dossier — 21 pages](documents/02-research-dossier/main.pdf)** | Original project, our additions, and the unfinished existence argument |
| **[Annotated catalogue — 42 pages](documents/03-notebook-catalogue/main.pdf)** | Every notebook's results, assumptions, dependencies, and limitations |
| **[Complete notebook and archive index](INDEX.md)** | Direct links to every PDF, source, and historical research file |
| **[Open problems](OPEN_PROBLEMS.md)** | Concrete targets for continuing the work |
| **[Contributing](CONTRIBUTING.md)** | How to report an error or contribute an argument |

The handoff contains **39 mathematical notebooks and 3 reading documents: 42 PDFs, 622 pages**, with editable LaTeX sources and **539 archived research, calculation, and internal-review files**. Use GitHub's **Code → Download ZIP** to download the entire repository. The [HTML index](index.html) can also be opened locally after downloading.

## What this continuation adds

The dossier and catalogue give the precise hypotheses; the following is an orientation.

- **Local classical analysis:** constrained minimizers, localized inverse operators, refinement estimates, and nonlinear response control near the trivial gauge orbit.
- **Actual local quantum integration:** the chosen constrained coarse map, Haar and Jacobian factors, gauge insertion, retained windows, analytic domains, and finite Ward extraction.
- **Local ultraviolet evolution:** a positive determinant drift and arbitrarily long finite weak homogeneous histories, under the stated upstream working inputs. See [Notebook 37](notebooks/37-ym4-positive-drift/main.pdf).
- **Full finite-measure tools:** exact positive history operators, normalized bare Wilson plaquette bounds, fixed-box conditional tails, and local defect estimates. See [Notebook 38](notebooks/38-ym4-full-measure-bridge/main.pdf).
- **A completed normalized fixed-box replacement argument:** an operation on separated fixed boxes of the actual bare Wilson measure that preserves the exterior marginal and partition mass, accounts for removed configurations, and bounds changes to bounded local observables and connected cumulants independently of distant boxes. See [Notebook 39](notebooks/39-ym4-normalized-box-replacement/main.pdf).

These are written research arguments, not independently certified results. Many earlier modules depend on other modules. Internal reviews, successful compilation, and correct file hashes have their stated scopes; none certifies the whole mathematical chain.

The final replacement theorem concerns **fixed boxes in the bare measure**. It has not been extended to arbitrary growing components, nonlinear coarse-average fibers, or general effective actions after renormalization.

## What remains for existence

The first major unfinished theorem is **complete-density transfer for the actual renormalization map**: control all admissible good and bad regions, their conditional normalizations, and their mixed histories, with estimates that survive iteration and with the same effective coupling extraction.

The subsequent obligations are uniform renormalized observable/source estimates, a common continuum hierarchy, reflection positivity and full Euclidean covariance on that hierarchy, reconstruction, and a quantitative nontriviality and Yang–Mills identification argument. A physical mass gap is a further infrared problem.

See [the open-problem map](OPEN_PROBLEMS.md) and **Sections 6–7 of the dossier** for the precise research program and a concrete next deliverable. The remaining work is substantial; the purpose of this publication is to make it inspectable and tractable for contributors.

## Relationship to the original project

The baseline examined is [upstream commit e392ef45013a581664bab76b90867170b30fe10e](https://github.com/ethanwsussman/Yang--Mills-LLM-experiment/tree/e392ef45013a581664bab76b90867170b30fe10e). Later upstream developments may go beyond that snapshot.

The original repository explicitly reports an apparent four-dimensional existence argument. Our dossier records that claim, its displayed theorem scope, and the unreconciled proof-status statements in the deposited files. It distinguishes material from the original project, published mathematical inputs, our subsequent arguments, conditional reductions, and open interfaces. Our project-specific additions are not blanket claims of novelty relative to the literature.

Original repository files and full third-party papers are identified and linked rather than republished. The [source map](provenance/handoff_repository_source_map.json) supplies hashes and exact locations, and the [retrieval script](reproduction/fetch_repository.py) can fetch the examined upstream commit.

## Research provenance and corrections

This continuation was developed in a user-directed, AI-assisted Codex research session and is published by [CaptainSude](https://github.com/CaptainSude). The internal mathematical audits were part of that research process; they are not external peer review. Credit to the original project does not assign its authors responsibility for this continuation's arguments.

The [corrections register](provenance/handoff_corrections_register.txt) records 41 corrections and scope clarifications. Historical checkpoints and unsuccessful routes are retained in [the research archive](research_archive/work); use the final dossier and catalogue to determine their current status. An old file saying a step is unfinished or giving a next task may have been superseded.

Each notebook contains a PDF, its compiling source, and the original assembled source. All delivered mathematical PDFs and notebook sources are unchanged from the handoff. The [publication record](PUBLICATION.md) documents the small public-copy edits to machine paths and navigation.

## Reproduce and verify

Read the PDFs with any PDF reader. To verify the published snapshot, run:

~~~sh
python reproduction/verify_bundle.py
~~~

To rebuild the PDFs with Python 3 and a suitable TeX installation:

~~~sh
python reproduction/build_pdfs.py
~~~

The [reproduction guide](reproduction/README.txt) lists requirements. PDF byte hashes may change after rebuilding with another compiler. The [manifest](manifest.json) and [checksums](SHA256SUMS.txt) describe the delivered snapshot, not mathematical validity.

**Corrections, independent audits, exact literature matches, and new arguments are welcome through issues and pull requests.** Please identify the notebook, theorem or equation, hypotheses, and the precise contribution.
