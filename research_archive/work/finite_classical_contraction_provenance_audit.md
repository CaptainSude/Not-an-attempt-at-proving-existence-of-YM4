# Independent audit of finite-regulator classical contraction

17 October 2026. Auditor: provenance. Full read of `finite_classical_contraction_research.md`, compared with the finite Ward extraction, repaired low-kernel spatial proof, coherent prefix bounds, actual reference transport and high-jet transport. No outputs edited and no compilation.

## Result

The proof passes under its stated actual finite-background and symmetry inputs. In particular, it proves an exact finite normalized-total relocalization at the SAME output carrier exponent a0 and field radius b. It does not use the optional old-scale tail localization that loses carrier exponent. The degree-dependent factors are preserved and cancel correctly. The error remains explicit as C_err(J)(L^2+L+1)exp[-c(J)LN]. No mathematical correction was requested.

One notation clarification was sent to the author: in (5.5), tau_N is measured on final unit cells, whereas the distance in (5.6)-(5.8) is measured on the final J-cell graph. The proof uses exactly this distinction; making it explicit prevents the factor 1/J or the anchor count from being misread.

## 1. Finite spaces, references and degree grading

At every fixed regulator there are finitely many connected carriers and coordinates. Equality of normalized analytic totals is a closed linear kernel, so the stated finite quotient is legitimate. Connected torus carriers obey D_P<=C J|H| even when they wind: a spanning tree of the carrier supplies paths of at most |H|-1 cell edges. The fixed-order coordinate counts are polynomial in |H| and can be absorbed by a portion of the input cardinal weight. This gives the displayed exponential total-kernel bounds without a factor of the torus volume.

The fixed-rho classical reference can be projected coefficientwise to degrees at least two because only its TOTAL linear jet is required to vanish. The geometric phase bound gives C_S b^2 uniformly in the actual finite reference. Its finite Hessian is the exact periodization of q_M, so both discarded long q_M coefficients and long images folded into short displacements are exponentially small. The ratio defining beta_(M,Q) therefore has a uniformly nonzero denominator for Q>=Q0(J) and normalizes the actual finite reference exactly. This is not an identification of the whole nonlinear reference with a periodized infinite action.

The projection norm C_ext=1+C_beta C_S retains beta's b^(-2) factor and cancels it using the proved reference bound. For an already extracted class, choose a near-minimal representative F directly; its total is invariant even though its individual coefficients need not be. This gives every fixed-degree kernel bound with the same representative amplitude epsilon.

In the degree-n Ward equation only degrees 2 through n occur. With b<=1, their estimates are bounded by C epsilon b^(-n), so delta_n=C epsilon b^(-n)e^(-cP) is correct separately for n=2,3,4. In particular the quadratic repair is not assigned the spurious b^(-4) factor from a common ungraded error. The lower-degree errors entering cubic and quartic coefficient elimination are bounded by the corresponding graded delta_3 and delta_4. This is sufficient for every later cancellation of b powers.

## 2. Symmetric lift and finite-range jet repair

The diameter cutoff is symmetric under all field-slot permutations and reanchoring. For cutoff P/16, anchoring the first bond determines every short lift uniquely, and pairwise lifted distances agree with torus distances. Thus the kernel equals periodization of the short lift plus the literal large-diameter tail, with no hidden multiplicity.

The finite Ward operators only shift/merge nearby slots. Their short lifted defects have diameter at most T0+2 and lie in the injective periodization range. Exact finite Ward identities therefore bound the continuous lifted Fourier defects, not merely their values at discrete torus momenta. The finite-dimensional Maxwell/cubic/quartic comparisons give the claimed graded small jets. Multiplication by midpoint phases and the analytic p-to-z change have fixed derivative constants, so the same finite orders of tail-coordinate Laurent jets are small.

Subtracting the Taylor polynomial in z-1 through orders 3,1,0 for degrees 2,3,4 gives fixed finite-range Laurent coefficients of size C delta_n. Slot symmetrization does not reintroduce low jets: the original lifted kernel is symmetric, and each transformed residual is the original vanishing residual composed with an analytic monomial change fixing z=1. Such composition preserves vanishing order. The transformed polynomial still has bounded finite range, because both the order and number of slots are fixed. Averaging only changes fixed constants.

The corrected kernels consequently have exact moments needed by the spatial proof and uniform exponential row norms. Identity (4.5) is exact for the finite polynomial: the periodized correction and the original wrapping tail are retained. Neither is incorrectly asserted to satisfy a separate Ward identity.

## 3. Periodic spatial algebra

For the corrected quadratic kernel, the ordered Laurent divided differences have the same exponentially weighted row bound as on the infinite lattice; they are operations on the lifted relative symbol. The sum over derivative directions remains inside the row norm. Two divisions give the stated 16 exp(sigma/2)/(e^2 sigma^2) bound, and the corrected jets ensure Htilde(1)=0.

Evaluation of the relative kernel on the actual periodic field is exactly evaluation of its periodization, including repeated finite slots. Periodic summation by parts has no boundary term, so (5.3) is exact. The cubic discrete Taylor identities use integer displacements in a periodic lift, not an assumed affine function on the torus. Their constant and first-moment cancellations are therefore still valid. The quartic telescope uses only the exact zeroth moment. No summability of a periodic field on the infinite lattice is assumed.

The coherent complete-field coefficient norm is the right hypothesis for all near estimates: field values, positive differences and gradient Hölder quotients are controlled before the support sum. Negative traversals evaluate a positive difference at its lower endpoint. Thus near products have the same b^n L powers as in the checked infinite spatial proof. One global coefficient assignment makes overlapping collar restrictions compatible; independent rootwise decompositions would not suffice.

For far displacements the polynomial factors in the cubic remainder are absorbed by the remaining exponential kernel decay. The quadratic difference product supplies b^2/L^4, the cubic rough product b^3/L^3 times fixed displacement powers, and the quartic product b^4/L^4. After the anchor sum these yield at most C epsilon(L+2)e^(-sigma L/8). The constants are fixed after J and before L, as required.

## 4. Unchanged carrier weight and wrapping errors

The output carrier joins projected endpoint roots and the projected strict background supports. Its graph can be chosen directly at the output scale; it need not contain every vertex of an unnecessarily long projected fine tree. The projection estimate (5.5) and rerooting (5.6) pay all attachments using the arbitrary fixed classical cardinal reserve A and spatial exponent kappa. They do not spend the inherited input exponent a0.

Each final J-cell contains exactly (JL)^4 input current anchor sites. For a torus, choosing one shortest coordinate representative for each macrocell makes its exponential distance sum at most the corresponding infinite S1. Hence the anchor bound is uniform in the regulator, with no additional winding factor.

For a general endpoint product, a root-joining tree has final-unit length at most C_n(D_P/L+1). Its output-cardinality and rerooting cost is therefore at most C exp[C'_n(a0+1)D_P/(JL)]. Taking L sufficiently large AFTER fixing J places that coefficient below mu/4. The remaining kernel exponential can retain exp(-mu T0/2) on the large-diameter tail. This is the critical same-a0 argument.

Multiplying n background factors supplies (b/L)^n; the anchor count supplies (JL)^4. With the graded tail bound C epsilon b^(-n), the field-radius factors cancel exactly and the residual scale is C(J)epsilon L^(4-n)e^(-cP). The finite-range jet correction has the same graded amplitude and is handled by the same endpoint construction. Thus n=2,3,4 give precisely L^2,L,1, at the original output a0. No exponent-losing old-scale carrier argument is used.

All regroupings are normally convergent analytic coefficient sums on the same b ball. The resulting family represents the ENTIRE finite polynomial, including its error terms, rather than merely matching its low kernels.

## 5. Full total and the finite operator estimate

Coefficientwise homogeneous projection has norm at most one, so the order-at-least-five remainder has norm at most six times the input norm. The high-jet theorem applies with the same fixed J and larger endpoint L: compression improves, tail conditions remain those of the fixed grouping, and only the final common radius must be reduced for the larger dilation disk. Its contribution is 6 C_high epsilon/L.

The total linear sector is zero by semisimplicity and stays zero after finite substitution. The constant sector is removed only by normalized-total convention. Combining all exact polynomial identities with the high-order remainder gives an exact representative of the finite normalized classical output.

Applying this to a near-minimal representative of P_in[E], then applying P_out and taking quotient infima, gives the displayed C_ext^2 bound. The actual reference identity makes P_out T P_in=P_out T, so intermediate finite projections telescope even though each stage has a different period and its own beta ratio. No identity beta_out T=beta_in is needed.

The parameter order is sound: fix J and its spatial/tail constants, choose an allowed large L=R^q, choose a sufficiently large compatible N0 for the residual exponential term, and finally choose b within every common domain and b<=min(1,rho/2). The principal constants do not deteriorate when b is reduced.

The theorem closes the finite CLASSICAL relocalization issue on these regulators. It does not automatically verify the intervening actual quantum budgets, identify sequential sharp cutoffs with a one-shot cutoff, prove a running-coupling sign, or construct the remaining field sectors and continuum observables. The saved scope is accurate.

## Fragment fidelity

The complete `finite_classical_contraction_fragment.tex` was read against the passed note. It preserves the actual finite reference ratio, graded defects, finite-range symmetrized repair, periodic Laurent/IBP identities, degree-wise b powers, same-a0 endpoint localization, high-jet domain and fixed-J parameter order. The requested metric distinction is explicit at the carrier and rerooting displays. Its added finite-domain gauge-path paragraph is also sound: the actual finite equality construction supplies a near-identity connecting gauge; the endpoint link equation then bounds its logarithmic edge increments; a strict L>C_g C_A margin keeps the interpolating links in the input domain. It does not infer a small gauge solely from small edge increments. The final theorem and telescope have the same meanings and constants as the audited research. No fidelity correction was found and no compilation was performed.
