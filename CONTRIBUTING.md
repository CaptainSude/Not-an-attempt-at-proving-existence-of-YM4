# Contributing mathematical work

The aim is to make the argument correct and complete. Corrections, counterexamples, independent checks, exact literature matches, and new proofs are all useful contributions.

Begin with the [handoff guide](documents/01-start-here/main.pdf), the [open problems](OPEN_PROBLEMS.md), and the [annotated catalogue](documents/03-notebook-catalogue/main.pdf). The catalogue states dependencies and current limitations. The [corrections register](provenance/handoff_corrections_register.txt) identifies superseded claims.

## Report a gap or error

Open an issue with:

1. The file, notebook number, theorem/lemma or equation, and page.
2. The exact claim under examination and the assumptions you are using.
3. The problematic implication, missing uniformity, normalization, or domain condition.
4. A counterexample, calculation, relevant source, or proposed repair where available.
5. Which downstream statements may be affected.

A concise, decisive objection is more useful than a general endorsement or rejection of the entire project.

## Contribute a proof or extension

Open a pull request with an editable source and an explanation of:

- The precise statement proved, including domains, quantifier order, constants, and uniformities.
- Which existing inputs it uses and which open obligation it advances.
- The argument and exact primary-source references.
- What remains conditional or outside its scope.

If a construction, coarse map, normalization, observable, or coupling extraction changes, explain how it connects to the rest of the argument. A theorem for a related model does not automatically repair this one.

Keep corrections traceable. Add a correction note and update affected dependencies rather than silently rewriting historical evidence. Distinguish an independent check from an AI-assisted review, and disclose material AI assistance in new contributions.

## Sources and verification

Each notebook has a standalone compiling source and an original assembled source. Historical files under research_archive preserve the research process; the final dossier and catalogue give the handoff's current scope.

The portable build and integrity scripts are in [reproduction](reproduction/README.txt). Build success is a typesetting check, not proof verification. The original snapshot manifest is retained under [provenance](provenance/original_handoff_manifest.json); the root manifest records this public edition.

Refer to the original project and the published literature for their contributions. Do not credit this continuation with ideas or results already present there. Proposed new statements should carry their exact hypotheses and evidence.
