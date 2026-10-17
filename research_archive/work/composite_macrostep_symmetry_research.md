# Exact macrostep symmetries and the quadratic infrared tensor

17 October 2026. Research proof for independent audit. This note concerns the actual composite constraint, direct-\(R\) internal contour gauge and retained-link/color-ball sector of the common-domain macrostep. It does not identify different gauge sectors, change the regulator, or prove a continuum limit.

## 1. Setting and the source property actually used

Fix an odd primitive ratio \(\ell\), \(R=\ell^s\), and centered nested blocks. In current unit coordinates the final centers are \(R\mathbb Z^d\). Use cubic periodic regulators with periods divisible by the required \(R,J\) blocks, with the distinct local lifted interfaces specified in the geometry proof. A cofinal source family can be retained by choosing the sufficiently large grouping \(J\) to be a power of \(\ell\). Arbitrary rectangular tori have only the coordinate permutations preserving their side lengths.

The local input maps are precisely those of composite_macrostep_geometry_research.md: all coordinate-order shortest root contours; their selected analytic group mean; the ordinary primitive average and its \(s\)-fold composition \(F_R\); and the independent direct-\(R\) root-contour map \(P_R\). The selected mean must obey the source's permutation axiom, in addition to the endpoint covariance and arithmetic differential already used in the geometry proof.

This is an actual source property. Bałaban, CMP 109 (1987), pp.252–254 defines the enlarged contour family, explains its role in lattice symmetry, and states permutation invariance as (0.7). The implicit equation (0.10) is one admissible realization, not the definition of every permitted mean. Reality in (0.9) is not by itself a charge-conjugation axiom. [Primary article, pp.252–254](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf).

The action/density being integrated must have the asserted spatial symmetries on the common small domain. Bare Wilson does. The homogeneous classical action inherits them from its defining ordinary constraint and the comparison of minima in the same small class. An arbitrary gauge-invariant inherited functional need not be spatially invariant; spatial invariance is an additional input preserved by the step below.

The group and color form are as in the preceding notes. The main \(SU(2)\) application needs no extra charge-conjugation assumption. For more general groups the precise extra condition is stated in Section 5.

## 2. Which spatial transformations are exact?

Let
\[
 {\cal G}_R=\{x\longmapsto Sx+Rn:
       n\in\mathbb Z^d,\quad S\text{ a signed coordinate permutation}\}.
 \tag{2.1}
\]
On a compatible cubic torus these are exact geometric automorphisms of the entire nested block hierarchy. At each primitive level a transformed contour is another contour in the same coordinate-order family. Permutation invariance of the mean gives the corresponding transformed \(P\). Products and logarithms are conjugated or oriented as the transformed paths require. Thus every primitive average, its composition \(F_R\), and the separate \(P_R\) commute with (2.1) on their common analytic domains.

There is no hidden orientation assumption in this statement. Write a primitive positively oriented output as
\[
 F=\exp\!\left\{N^{-1}\sum_x
                   \log(U_xT^{-1})\right\}T .
\]
For the reversed coarse bond the transported strings and reference are \(U_x^{-1},T^{-1}\), after reindexing starting sites. On the common logarithm branch,
\[
 \log(U_x^{-1}T)
       =-\operatorname{Ad}_{T^{-1}}\log(U_xT^{-1}),
 \qquad F_{\rm reverse}=F^{-1}.
 \tag{2.2}
\]
Consequently the positive-bond convention does not break reflections. The selected centerline interface pivots are preserved as unoriented bonds under (2.1); internal contours remain internal. Short periodic volumes use the distinct lifted interfaces of the geometry note, not a collapsed unoriented edge set.

After rescaling the final centers by \(R\), the translations in (2.1) are **all unit translations of the output lattice**. The signed permutations give its full hypercubic point group. Coordinate reflections through both output site planes and output link planes occur: \(x_\mu\mapsto -x_\mu+nR\). This is discrete lattice symmetry, not arbitrary \(O(d)\) symmetry.

Current unit translations not divisible by \(R\) are not symmetries of the fixed block sector. A concrete failure already occurs in the absolute contour penalty. On a large periodic lattice take a pure gauge with a small site phase \(t\) at one block root and zero at every other site. Its penalty is
\[
 (R^d-1)\,q(e^{it}),\qquad
 q(U)=1-\tfrac12\tau(U+U^{-1}).
\]
Translate that phase by one current unit into a nonroot site. The penalty is now \(q(e^{it})\). Endpoint covariance makes this calculation exact, independently of the contour prescription. Thus current unit-translation invariance cannot be inferred for the fixed gauge insertion or sector. This causes no loss of output unit-translation symmetry, whose current lift is \(R\) units.

## 3. The relative chart and sharp cutoff under reflections

The nontrivial point is the transformation of left-relative Lie coordinates. If
\[
 U_b=e^{iB_b}V_b ,
\]
then reversing the orientation gives exactly
\[
 U_b^{-1}
   =e^{-i\operatorname{Ad}_{V_b^{-1}}B_b}V_b^{-1}.
 \tag{3.1}
\]
It is generally incorrect to replace the relative field by merely \(-B_b\). For a fixed real background \(V\), (3.1) is a fixed real orthogonal linear map of the color coordinates. A spatial transformation therefore gives a permutation of bonds combined with these orthogonal maps. Denote the resulting map on retained coordinates by \(D_{S,V}\); its absolute Jacobian is one.

If \(V'=SV\), the transformed full relative field solves the \(V'\) constraint whenever the original solves the \(V\) constraint. Its retained coordinates are \(D_{S,V}z\). Uniqueness of the small pivot solution proves
\[
 \Phi_{V'}(D_{S,V}z)
       ={\cal R}_{S,V}\Phi_V(z),
 \tag{3.2}
\]
where \({\cal R}_{S,V}\) is the corresponding full-bond relative transformation. The retained set is preserved because the pivot set is preserved. Hence the actual window
\[
 \prod_{b\ {\rm retained}}1_{\{|z_b|\le gT\}}
 \tag{3.3}
\]
is invariant, with its original linkwise color norm. No complex transformation of a sharp indicator is involved. A coordinate cube in an arbitrary color basis would not have this property; neither would arbitrary bond-dependent thresholds.

The physical background also transforms correctly. \(SV_*(W)\) is feasible for the transformed coarse datum, has \(P_R=1\), and has the same constrained classical value and stationarity. The common small-domain uniqueness theorem gives
\[
 V_*(SW)=S V_*(W).
 \tag{3.4}
\]
For the homogeneous classical action itself, the same argument can be made at its defining fine minimization: the ordinary hierarchy, fine Wilson action and the small global norm class are permuted isometrically. This proves equality of the values without requiring an arbitrarily selected gauge representative to be covariant.

Every factor in the exact chart integral is now accounted for. Haar is invariant under inverses and conjugation. The relative coarse constraint transforms linearly by a coarse orthogonal map. Its pivot derivative transforms by the corresponding coarse and pivot matrices. For a reversed bond both matrices have determinant \((-1)^{\dim\mathfrak g}\), with the adjoint determinants equal to one, so their determinant ratio is unchanged. Bond permutations simply relabel the factors. The nonlinear pivot derivative has the same transformation. Thus both the background delta determinant and the normalized straightening determinant transform correctly.

The action plus absolute gauge penalty in the chart obeys
\[
 T_{SV}(D_{S,V}z)=T_V(z).
\]
Because \(D_{S,V}\) is independent of \(z\), constant, linear and quadratic Taylor terms transform separately. The centered extension on the independent background ball therefore has the same covariance identity; the omitted linear term is not silently assumed zero off the physical branch. The Hessian obeys an orthogonal congruence, so the normalized Gaussian and its determinant transform correctly. The reference flat determinant is the same scalar normalization on both sides.

Changing retained variables by \(D_{S,V}\) proves equality of the **actual total small-field integrals** for real arguments in the common small domain. Equality extends holomorphically to the common complex germ. Equality of logarithms additionally uses the proved nonvanishing cluster domain and the compatible branch, fixed at the common base point. Mere analyticity of an integral would not suffice.

The inherited pre-gauge representation does not need to transform term by term. Its complete insertion agrees with the rooted integral on a nonempty common domain, and the inherited total is assumed spatially invariant there. Holomorphic uniqueness carries the resulting total symmetry to the common-domain continuation. This does not assert symmetry of an individual nongauge-invariant activity.

## 4. Auxiliary grouping and global completions

The auxiliary \(J\) grouping is a reorganization of the retained product window and of exact finite integrals. It changes neither (3.3) nor the scalar total. The fixed \(J\)-cell carrier grid, deterministic hulls and joining trees may obscure unit output translations and signed permutations **at coefficient level**. Their sum nevertheless has the symmetry just proved. No symmetry of a chosen carrier assignment is needed for the Hessian of the sum.

This conclusion uses the actual linkwise window. Adding genuine restrictions on grouped Euclidean norms or any asymmetric extra indicator requires a separate check. Grouping cannot be used to erase such restrictions.

There is a different limitation outside the analytic sector. The measurable completion in the composite integral note selects an ordered reference contour and a fallback value. That construction is gauge equivariant, but a spatial transformation can change the selected reference and the good-set test. The supplied proof does not establish its global spatial equivariance. We therefore claim the above symmetry for the actual local sector and its common-domain analytic continuation, not for an arbitrary global completion of the blocking map or its uncontrolled complement.

There is an exact way to repair an asymmetric sector decomposition if it becomes necessary. For a finite spatial group, transform the sector and its complement together and average the resulting decompositions. Each transformed gauge insertion retains its exact orbit normalization. When the blocking map and input measure are equivariant, the average is a new positive decomposition of the same pushforward, with a symmetric small part and matching complement. It does not say the original small part was unchanged. If the blocking completion itself is asymmetric, averaging its conjugated kernels defines a new symmetric Markov blocking kernel, not the original deterministic map. Restoring current-unit translations similarly requires block-origin averaging with the origin retained as part of the blocking data. None of these changes is made or needed for the local theorem above.

## 5. Charge conjugation

For \(SU(2)\), complex conjugation is the constant inner automorphism
\[
 U\longmapsto\overline U=(i\sigma_2)U(i\sigma_2)^{-1}.
\]
It is consequently already included in constant gauge covariance of the total integral, selected mean, color balls and classical action. Thus charge conjugation is exact for the stated \(SU(2)\) construction on the same domains.

For \(SU(N)\), its holomorphic complexification is
\[
 {\cal C}(U)=(U^{-1})^T,\qquad {\cal C}_{\rm Lie}(A)=-A^T.
\]
The latter is an orthogonal real color map. The implicit Federbush realization \(\sum_j\log(U_jP^{-1})=0\) commutes with \({\cal C}\): apply the automorphism to the equation and use the local uniqueness of its small solution. Products, inverses, the chosen logarithm, Wilson plaquettes, Haar and the color-ball windows then commute with \({\cal C}\), and the same integral proof applies if the inherited total is charge-conjugation invariant.

For an otherwise unspecified selected mean satisfying only the properties used in the geometry module, automorphism covariance under this outer automorphism has not been verified. It must be supplied, or the explicit admissible realization must be chosen. Reality of the mean is insufficient as a proof. No assertion that two different means or cut sectors give identical integrals is made.

## 6. From analytic connected activities to a quantitative Hessian bound

Here and below the Hessian is that of the **summed output correction**, not of a single carrier coefficient. Suppose on a compatible output torus
\[
 F(w)=\sum_{H\ {\rm connected}}F_H(w_H),\qquad
 \sup_I\sum_{H\ni I}e^{a_0|H|}\|F_H\|_b\le\epsilon.
 \tag{6.1}
\]
The labels \(I,H\) are \(J\)-cells of the output unit lattice, and \(\|\cdot\|_b\) is the supremum on a scalar-coordinate polydisc of radius \(b\). If the available domain is instead a color Euclidean ball, use the contained scalar polydisc and replace \(b\) accordingly. There are at most \(D=d(\dim\mathfrak g)J^d\) scalar bond coordinates per cell. The norm and parameters are uniform in volume and preceding depth; \(J\) is fixed.

Let \(i=(x,\mu,a)\) denote an oriented bond/color coordinate, \(\xi_i=x+e_\mu/2\) its midpoint, and \(K_{ij}=\partial_i\partial_jF(0)\). Cauchy's estimate gives
\[
 |\partial_i\partial_jF_H(0)|\le2b^{-2}\|F_H\|_b.
 \tag{6.2}
\]
A connected \(H\) containing the cells of both coordinates satisfies
\[
 |\xi_i-\xi_j|_1\le J(|H|+d)
 \tag{6.3}
\]
with periodic shortest distance on a torus. Set \(\mu_0=a_0/(2J)\). Sum first over \(j\) in \(H\), then over \(H\) containing the cell of \(i\). Equations (6.1)–(6.3) give
\[
 \sup_i\sum_j e^{\mu_0|\xi_i-\xi_j|_1}|K_{ij}|
 \le {\cal M}:=
 \frac{2D e^{a_0d/2}}{b^2}\epsilon
              \sup_{n\ge1}n e^{-a_0n/2}.
 \tag{6.4}
\]
This proof needs no symmetry of the decomposition. It supplies a uniformly summable bound for the actual kernel. Additional fixed local contributions to \(F\) can be added with their own finite row bounds.

## 7. Ward identity and the infinite-kernel limit

Assume \(F\) has the local coarse gauge invariance already established for the complete integral and is real on real small fields, as for the physical positive density with its real logarithm. The algebraic conclusions also hold for complex inputs, but then the coefficient \(\beta\) below can be complex. For a compact semisimple group, constant gauges imply \(DF(0)=0\), since the adjoint representation has no invariant covector. Differentiating local gauge invariance once in the gauge parameter and once in a field direction then gives
\[
 K D=0,
 \tag{7.1}
\]
where \(D\) is the output unit-lattice gradient. The nonlinear derivative of the gauge generator is multiplied by \(DF(0)\) and hence disappears. This is an exact finite-regulator identity in position space.

Finite periodic momenta alone do **not** imply \(K_N(0)=0\). Small gauge-invariant winding contributions are not excluded by that argument. To make a continuous-momentum statement, take an exhausting sequence of compatible cubic tori and use (6.4). For every fixed bond displacement the kernel entries are bounded; a diagonal subsequence yields an infinite-lattice kernel. The exponential bound passes by Fatou. Translation covariance, signed permutations, Hessian symmetry and the finite-difference identity (7.1) pass at each fixed displacement. Thus the limiting kernel has all these properties and is exponentially summable.

This is existence of a subsequential **kernel** limit only. It establishes neither a probability-measure limit, uniqueness of the kernel, nor a continuum limit.

For a simple Lie algebra, constant adjoint invariance makes each spatial block of this kernel a scalar multiple of the invariant color inner product. For a semisimple product there is one such tensor per simple ideal; cross terms between distinct ideals vanish. The following formulas concern one simple factor.

Use the midpoint Fourier convention
\[
 \widetilde K_{\mu\nu}(p)
 =\sum_{r\in\mathbb Z^d} k_{\mu\nu}(r)
       e^{ip\cdot(r+(e_\nu-e_\mu)/2)},\qquad
 \widehat p_\mu=2\sin(p_\mu/2).
 \tag{7.2}
\]
Exponential summability makes the symbol analytic near zero. Position-space (7.1) gives, now for every real \(p\),
\[
 \widetilde K(p)\widehat p=0.
 \tag{7.3}
\]
At \(p=t e_\mu\ne0\) this annihilates \(e_\mu\); continuity gives \(\widetilde K(0)=0\). Full inversion gives \(\widetilde K(-p)=\widetilde K(p)\). Real Hessian symmetry then makes the symbol real symmetric for real \(p\), with no odd Taylor terms. Midpoint coordinates are essential to the phase-free signed-permutation transformation law.

## 8. The justified quadratic classification

Signed reflections and coordinate permutations constrain the homogeneous degree-two part to
\[
 (K_2)_{\mu\mu}(p)=A p_\mu^2+
                  B\sum_{\nu\ne\mu}p_\nu^2,\qquad
 (K_2)_{\mu\nu}(p)=C p_\mu p_\nu\quad(\mu\ne\nu).
 \tag{8.1}
\]
Indeed reflection in coordinate \(j\) changes exactly the tensor indices equal to \(j\); diagonal entries therefore contain only squares, and off-diagonal entries only the product of their two indexed coordinates. Permutations identify the coefficients shown. The cubic part of (7.3) is \(K_2(p)p=0\). Its coefficients give \(A=0\) and \(C=-B\). Hence, with a real scalar \(\beta=B\),
\[
 \widetilde K(p)
   =\beta\bigl(|p|^2I-pp^T\bigr)+O(|p|^4)
   =\beta\bigl(|\widehat p|^2I-\widehat p\widehat p^T\bigr)
                                                   +O(|p|^4).
 \tag{8.2}
\]
This uses full coordinate permutations, not just axis reflections. For example different coefficients for the six plaquette orientations in four dimensions give a local, gauge-invariant, translation- and axis-reflection-invariant action with several quadratic coefficients. Without the permutations the single-\(\beta\) conclusion is false.

There is a quantitative remainder. Define the moments of the limiting spatial kernel by
\[
 M_n=\max_\mu\sum_{\nu,r}
 |r+(e_\nu-e_\mu)/2|_1^n\,|k_{\mu\nu}(r)|.
 \tag{8.3}
\]
Equation (6.4) implies \(M_n\le{\cal M}[n/(e\mu_0)]^n\) for \(n>0\). The \(p_\nu^2\) coefficient of a diagonal entry gives \(|\beta|\le M_2/2\). For real \(p\) with \(r_p=\|p\|_\infty\le1\), the even Taylor remainder for cosine gives
\[
 \|\widetilde K(p)-K_2(p)\|_{\rm op}
                         \le M_4 r_p^4/24.
 \tag{8.4}
\]
Also \(|2\sin(t/2)-t|\le|t|^3/24\); summing the diagonal and off-diagonal differences in a row gives
\[
 \|\widetilde K(p)
     -\beta(|\widehat p|^2I-\widehat p\widehat p^T)\|_{\rm op}
 \le \left(\frac{M_4}{24}+\frac d6|\beta|\right)r_p^4.
 \tag{8.5}
\]
Real symmetry permits the row bound to control the operator norm. These estimates do not require a choice of analytic interpolation of finite-volume discrete momenta.

## 9. What this does and does not supply for extraction

For the \(SU(2)\) construction with symmetric complete input, centered cubic regulators, all source contour permutations and the actual retained color balls, there is no local hypercubic obstruction from the composite constraint, its separate contour gauge, the pivot chart or auxiliary grouping. The actual total correction has the symmetries required for (8.2), after the explicitly stated kernel-limit step.

The proven obstructions are narrower but real: current unit translations do not preserve the fixed macro sector; arbitrary asymmetric indicators or input densities are not repaired by grouping; and the chosen measurable large-field completion has not been shown spatially equivariant. General outer charge conjugation needs a property of the selected mean. None of these can be removed by claiming equality of different gauge-fixed sectors.

The scalar \(\beta\) is a coefficient of the **quadratic correction kernel**. Symmetry determines neither its sign nor asymptotic freedom. The required flat classical normalization is available beyond mere ellipticity: flat_covariance_decay_research.md Section 10 (Notebook07) derives \(q_{M,\mathrm{mid}}(p)=|p|^2I-pp^T+O(|p|^4)\) uniformly in \(M\) from the explicit alias formula. With the separately proved identification of this variational \(q_M\) as the Hessian of the homogeneous classical minimum \(S_M\), this supplies its quadratic normalization in that scope. Ellipticity alone would not have supplied it. A recursive interacting running-coupling construction still needs the nonlinear extraction and stability steps below.

One may subtract \(\beta\) times the normalized standard Wilson plaquette functional, whose midpoint Hessian is \(|\widehat p|^2I-\widehat p\widehat p^T\), to obtain the quadratic \(O(p^4)\) remainder (8.5). This is a gauge-invariant scalar subtraction, but it is not yet a localized nonlinear extraction theorem. Its relation to the chosen \(S_M\), the necessary Ward-compatible higher field jets, finite-volume winding terms, stable norms for the extracted activities and the relevant/marginal flow remain to be proved. The coefficientwise high-field-jet contraction from Notebook28 does not by itself fill these gaps.
