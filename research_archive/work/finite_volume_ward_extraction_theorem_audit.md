# Audit of finite-volume total Ward extraction

17 October 2026. Independent audit of finite_volume_ward_extraction_research.md. Sections 1--7 pass, subject to their stated small-period threshold and reference normalization. No substantive mathematical correction was found.

## Lift and Ward defect

The midpoint-diameter cutoff is invariant under slot permutations, reanchoring, translations and signed permutations. For D_N<=T=floor(N/16), fixing the first bond fixes every other lift uniquely. Each pair of selected lifts differs by at most 2T<N/2 in each coordinate, so its ordinary l1 distance equals its torus l1 distance. This proves both the simultaneous diameter assertion and the no-multiplicity periodization identity.

The polynomial-tail estimate spends half the original exponential and is valid with the stated B_m(mu). The inequality T>=N/32 holds in the stated N>=64 range.

Each Ward operation is a finite shift or coincident-slot embedding, with fixed color coefficients. It commutes with relative periodization. The lifted defect has diameter at most T+2. Since 2(T+2)<N/2 in the stated range, anchored lifts in its support are unique and their pair distances still equal torus distances. Thus injectivity really does convert the periodic defect equality into an absolute infinite lifted-kernel bound. This is stronger than a statement restricted to discrete Fourier momenta, and the note correctly uses that stronger fact.

## Finite coefficient and approximate cancellation

The short lift retains exact midpoint parity and hypercubic tensor forms. Defining beta_N=b_E/b_S cancels the transverse quadratic coefficient exactly. For the homogeneous classical reference, the separately proved exact periodization of q_M and its normalized infinite symbol supply b_S=1+exponentially small error; a normalized subsequential limit alone would not suffice.

One useful detail behind this reference comparison is that the short lifted periodization contains long-image contributions as well as the unwrapped head. Every such extra image is at original distance at least N-T, and its folded short moment is bounded by its original absolute moment. Consequently both missing tails and folded images are controlled by the same known infinite q_M exponential moment bound. No new N-dependent prefactor is required.

The degree-one quadratic Ward defect bounds the mass coefficient. The degree-three equation then bounds the remaining a and c coefficients after b_F=0, including the small sine-correction term proportional to the mass. The cubic degree-two equation bounds each linear tensor coefficient by the independent p_mu q_sigma monomials. The quartic degree-one equation then bounds its constant tensor; its quadratic-generator term uses the small residual mass times one sine factor. All constants are finite-dimensional and preserve the stated J dependence.

The real-ray Taylor estimates follow from the midpoint moments, with exact parity excluding other lower orders. They describe the lifted short part plus a separately bounded wrapping tail, not an exact zero-jet claim for a finite torus.

## Fixed-order tail localization

Selecting monomials by the diameter of their differentiated slots is unambiguous for a scalar monomial and reconstructs the total degree-n tail kernel after summing the original carriers. A nonzero selected monomial forces its original connected carrier to have size at least T/(C_d J). The fixed-degree Cauchy count and the split cardinality reserve then prove (6.2). The loss from a0 to a_out is explicit. Individual tail coefficients need not be invariant.

## Scope

The construction gives a definite finite-volume beta_N and exponentially small low-moment defects, not regulator consistency or convergence of beta_N. Accumulating finite-size errors in an RG sequence, localizing the principal spatial remainder, and controlling the coupling trajectory remain separate. No output edits or compilation were performed.
