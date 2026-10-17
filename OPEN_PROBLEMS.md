# Continuing the existence argument

The aim is a nontrivial four-dimensional Yang–Mills quantum theory. The full continuum existence theorem remains open in this project.

Read [the dossier](documents/02-research-dossier/main.pdf), especially Sections 6 and 7.2, alongside the [annotated catalogue](documents/03-notebook-catalogue/main.pdf). The labels below match that dossier. They describe the present route; another construction could replace some interfaces.

## First target: H2, complete-density transfer

The local homogeneous construction and the fixed-box Wilson estimates must be connected to the complete density of the **same** renormalization map.

A concrete next deliverable is a theorem for one collared component with the actual averaged constraint. It should state:

1. The component geometry, admissible exterior fields, gauge or transition data, and compact conditional integral.
2. The constrained background, retained variables, and complete Jacobian.
3. An exactly normalized replacement or good/remainder identity preserving the fine measure when components are summed.
4. A bound in the actual norm used by the complete-density induction, uniform in the required geometries and scale ages.
5. Compatibility with neighboring regions, subsequent scales, observable sources, and coupling extraction.

Two routes are described in the dossier: match every relevant hypothesis of the published complete-density induction to the chosen map, or prove a direct replacement theorem for it. Weak coupling in our local recursion does not automatically establish the coupling hypothesis of a different construction.

[Notebook 38](notebooks/38-ym4-full-measure-bridge/main.pdf) and [Notebook 39](notebooks/39-ym4-normalized-box-replacement/main.pdf) provide an independent bare-measure entry point. Their fixed geometry is a substantive restriction. Exact positive history identities do not themselves give a summable bound over every history.

## H3: renormalized observable and source estimates

Specify the intended gauge-invariant observable algebra. Establish estimates uniform in mesh and volume for the actual interacting measure, including the distributional growth needed at all orders.

A useful first target is renormalized action density on reflected separated test supports. The source domain, numerator, denominator, counterterms, and complementary-region bounds must belong to the same construction.

The bounded-observable cumulant comparison in Notebook 39 is not automatically uniform for renormalized observables whose supremum norms grow with the cutoff.

## H4: one compatible continuum hierarchy

Construct a common limit for the required mixed observables, with compatible normalizations, products, subtractions, and any necessary contact extensions.

Background analyticity and compactness of effective interactions do not alone give the required compactness of physical correlation distributions. Separated correlations must be extended or the chosen reconstruction route must explain precisely why particular extensions are unnecessary.

## H5: positivity, rotations, and reconstruction

Pass reflection positivity from the same finite positive measures to the chosen limiting observable algebra. Establish full Euclidean covariance; lattice symmetry by itself is insufficient.

The earlier notebooks provide conditional reflection/rotation mechanisms. Their model-dependent uniformity and source hypotheses still need verification. Check the exact regularity and positivity assumptions of the reconstruction theorem used. Vacuum uniqueness or clustering requires its own argument if included in the target.

## H6: nontriviality and Yang–Mills identification

Prove a quantitative witness that survives the common continuum limit and gives nonzero physical content. A positive ultraviolet coefficient alone is insufficient.

The observable algebra, tensor structure, and short-distance normalizations must identify the limit as the intended Yang–Mills theory. Non-Gaussian scalar correlations alone do not establish interaction: composites of a free field can already be non-Gaussian.

## H7: mass gap and group scope

A physical mass gap requires an infrared estimate for the reconstructed Hamiltonian in the same continuum theory. A constrained Gaussian or auxiliary elliptic gap is not that estimate.

The upstream local construction principally targets SU(2). The general SU(N) bare-measure statements do not extend every earlier construction input to all compact simple groups.

## Independent review is also a contribution

Useful audits can focus on:

- Nonlinear domains, collars, constraints, and uniformity constants in the local construction.
- The actual determinant normalization and transfer from structural limits to finite histories.
- Matching published hypotheses to the exact map rather than matching terminology.
- The probability inputs and gauge-invariant windows in Notebooks 38–39.
- The original repository's unresolved version/proof-status crosswalk.

Record the exact statement checked, assumptions retained, and any counterexample or corrected proof. See [CONTRIBUTING.md](CONTRIBUTING.md).
