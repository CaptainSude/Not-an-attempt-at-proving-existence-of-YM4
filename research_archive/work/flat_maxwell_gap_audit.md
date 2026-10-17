# Independent audit of the flat Maxwell gap note

16 October 2026. Audited `work/flat_maxwell_gap_research.md` in full, together with the relevant flat bridge formulas and the cited raw source passages. No repository or output file was changed. This is an internal mathematical audit, not an external certification of the Yang--Mills construction.

## Verdict and two conventions to state explicitly

I found no mathematical error in the normalized cochain identity, its weighted L2 contraction, the finite-patch positivity proof, the constant `gamma_loc=sigma(d,L)/3^d`, or the equality of the two flat quadratic energy infima. The small-periodic-torus argument also works.

Two conventions are necessary to read the proof correctly:

1. The patches in Section 6 are translated by **block-center lattice translations**, `y in L Z^d`, modulo the periodic coarse lattice. Arbitrary fine-unit translations need not preserve the given tree constraints and cannot be used in the argument.
2. A periodic lattice is the quotient of the oriented lattice cell complex. Bonds and plaquettes retain their direction and base-point labels, including multiplicities when a lifted patch wraps or when a very small quotient makes endpoints coincide. One must not replace this by a simple graph that discards repeated edges or faces. The standard periodic lattice gauge convention has the required interpretation.

The physical conclusion remains conditional on the stated identification of the actual full-block effective Hessian. The note does not establish the missing complex response, upper-bound or locality theorems. There is also a useful strengthening: once the physical action part is bounded below by curl energy, the exponential-gauge lower bound can be proved directly without a separate use of gauge invariance of that action part; see Section 6 below.

## 1. Two-form normalization and contraction

The audit uses exactly the physical potential convention `U_b=exp(i h A_b)`, with fine curl divided by `h` and coarse curl divided by `H=Mh`.

Expanding the coarse curl of the straight average gives

    (d_H Q_M^st A)_(mu nu)(y)
      = M^(-d-1)/(M h) sum_(x in B_M(y))
          [oriented sum of A on the M-by-M square boundary at x].

Discrete Stokes replaces the square-boundary sum by

    h sum_(r,s=0,...,M-1) (d_h A)_(mu nu)(x+r h e_mu+s h e_nu).

Thus the coefficient is exactly `M^(-d-2)`. There is no missing factor of `M` or `h`. This proves the displayed identity `(2.3)` with the sign convention in the note.

For each fixed component, the positive two-form kernel has row sum one. For each fixed fine plaquette label `z`, every ordered pair `(r,s)` determines exactly one block containing `x=z-rh e_mu-sh e_nu`. Consequently its column sum is

    M^2 M^(-d-2)=M^(-d).

Jensen followed by the column sum gives

    H^d sum_y |Q_M^(2) F(y)|^2
      <= H^d M^(-d) sum_z |F(z)|^2
      = h^d sum_z |F(z)|^2.

The calculation is componentwise, so summing over `mu<nu` adds no dimension factor. Complex values of `F` are allowed in this Hilbert-space inequality. On a compatible torus the same argument counts repeated summands with multiplicity; the unique-block statement refers to the partition of periodic fine sites. The analogous one-form calculation has `M` longitudinal indices and again column sum `M^(-d)`.

The centered odd-block semigroup assertion is correct. The bijections are independently

    a_(MN)=a_M+M a_N,
    r_(MN)=r_M+M r_N,

and, for two-forms, a second independent longitudinal index `s`. The order of the two sums introduces no additional weighting. This is an exact statement for the displayed straight averages, not for arbitrary nonlinear averaging maps.

## 2. Rooted versus straight constraints

The first-order contour calculation gives

    Q_M^flat=Q_M^st-D_H aT_h.

Its spacing factors check: `T_h` is `h` times the bond-potential path sum, and `D_H` divides by `Mh`. Consequently the endpoint-contour term has coefficient `M^(-d-1)`, the same physical normalization as the straight term.

For a scalar fine field `lambda`, exact telescoping gives

    Q_M^st D_h lambda = D_H mean_M(lambda),
    Q_M^flat D_h lambda = D_H restrict_to_centers(lambda).

Induction through nested blocks therefore gives

    Q_k^rooted A=Q_(L^k)^st A+D_1 Psi_k(A).

No bound on `Psi_k` is needed for the finite-volume variational comparison. Both directions of the correction in Section 4.2 have the correct sign:

* If `Qst A=B`, choose `lambda` with final-center values `-Psi_k(A)`. Then `Qroot(A+D_eta lambda)=B`.
* If `Qroot A=B`, then `Qst A=B-D_1 Psi_k(A)`. Choose the final block mean of `lambda` to equal `Psi_k(A)`. Then `Qst(A+D_eta lambda)=B`.

Both corrections preserve `d_eta A` exactly. This proves equality of energy infima even if no minimizer is known and even in the presence of torus harmonic modes: only an exact gradient discrepancy is corrected; no claim is made that all closed torus fields are gradients.

For an infinite-volume version, the admissible field class must be preserved. At each fixed `k`, the scalar maps are finite-range bounded maps on the appropriate L2 spaces, with constants allowed to depend on `k`. The center-value extension can be chosen zero off the prescribed centers, and the block-mean extension can be chosen blockwise constant. These choices preserve square summability. The note makes no uniform potential-norm or analytic-radius assertion, correctly.

The source distinction in Sections 4.1 and 8 is real and correctly retained. Raw I, lines 24355--24369, displays a corrected linear operator whose four correction brackets vanish at the identity, leaving the straight-string term. That does not by itself identify this operator with the uncorrected rooted constraint of a nonlinear minimizer.

## 3. Finite-patch positivity

The local matrix in Section 6 is positive definite for the stated rectangular patch. Its proof does not use a global gap or assume the desired eigenvalue positivity.

Every straight row for two neighboring block centers is supported in their two endpoint blocks: the transverse coordinates remain in the same block intervals, and the longitudinal string joins equal relative positions in the two consecutive intervals. Thus these rows genuinely depend only on `E_Omega`.

The kernel argument is valid:

1. The rectangular cubical complex has trivial first cohomology, so `d_Omega B=0` implies `B=D phi` on all its edges.
2. Every chosen rooted tree path telescopes; `T_0,Omega B=0` makes `phi` constant on each block.
3. For neighboring block constants `c_y,c_(y+L e_mu)`, each string integral is their difference. Hence its normalized straight row equals `(c_(y+L e_mu)-c_y)/L`.
4. The block-neighbor graph of the patch is connected. The constants agree, so `B=0`.

Therefore `sigma(d,L)>0`. A numerical eigenvalue calculation is unnecessary. The same scalar matrix acts on each orthonormal color component, so the gap does not deteriorate with color dimension.

The arbitrary sizes of the tree path rows only affect the finite number `sigma(d,L)`. They do not invalidate its strict positivity or its volume independence.

## 4. Overlap counts, including small tori

There is an exact count behind the conservative `3^d` bound. Fix an edge or plaquette and let `r` be the number of coordinate directions in which its vertices occupy two neighboring blocks instead of one. For an edge, `r` is zero or one. For a plaquette, `r` is zero, one or two.

In one coordinate, a single prescribed block belongs to three possible block-centered length-three patches. Two prescribed adjacent blocks belong to two. Consequently the number of translated patch occurrences is

    m(cell)=2^r 3^(d-r).

In particular, every edge has positive multiplicity and every plaquette has multiplicity at most `3^d`. Summing the patch inequality thus yields exactly the stated conservative bound

    ||B||^2 <= sigma^(-1) sum_p m(p)|dB(p)|^2
             <= 3^d sigma^(-1)||dB||^2.

There is no extra factor from orientations: each edge is counted in one chosen positive orientation and each plaquette once for `mu<nu`.

On a torus with `N_mu` blocks in coordinate `mu`, fix one lift of the target cell. Pairs consisting of a periodic patch center and an occurrence of the target cell in its lifted patch correspond bijectively to the covering-lattice patch centers containing that chosen lift, by translating the occurrence and center by the same period vector. Hence the same count `2^r 3^(d-r)` holds with multiplicity for every positive integer `N_mu`, including one or two. The constraint rows of a lifted patch are exactly periodic copies of the global aligned rows. Neither local path independence nor the matrix positivity proof is applied to the quotient torus; both are applied to the ordinary rectangular lifted patch. This avoids the torus-cohomology pitfall.

The infinite-volume passage is also correct for square-summable fields: all squared quantities are nonnegative, and the bounded overlap sum can be justified by Tonelli or monotone convergence over patch centers.

## 5. Wilson Hessian and actual source match

The Wilson normalization in Section 5 is correct. The linearized plaquette phase is `i t eta^2 d_eta A`; the normalized trace removes the order-two commutator contribution. Thus

    D^2 S_eta(1)[A,A]=eta^(d-4) eta^4 sum_p |d_eta A(p)|^2
                    =||d_eta A||_eta^2.

For an actual differentiable branch with the specified constraint, `Q_k L_k B=B`. If it is twice differentiable, the chain rule at the stationary fine configuration gives

    q_eff,k(B)=||d_eta L_k B||_eta^2>=||d_1 B||_1^2.

A first derivative and a quadratic Peano expansion suffice to obtain the quadratic coefficient, but not automatically a classical continuous Hessian; the note distinguishes these correctly. No uniform derivative bound on `L_k` is needed for this lower bound. The existence and differentiation of the branch must nevertheless be established for every scale at which the conclusion is used.

The stronger infimum identity `(5.3)` needs the indicated integrability of tangent-feasible directions and an actual minimizing comparison, not merely stationarity of an arbitrarily chosen branch. Section 7 does not need this stronger identity. Equality of the *abstract* rooted and straight quadratic infima from Section 4.2 cannot alone identify an unrelated nonlinear corrected branch with the actual effective action.

For the limited source check, CMP109 explicitly gives the constrained minimization and the separation of the Wilson term from the correction in (0.21)--(0.22), p.256; its fluctuation expansion is (2.6)--(2.11), pp.266--267. The raw transcription at II 73873--73910 and 73997--74000 identifies the associated reduced covariance and variables. These are consistent with the note's conditional match. They are not, by themselves, a new proof of the underlying analytic minimizer theorem or of a complex independent-current extension. Source: [Bałaban, CMP109](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf).

The action whose Hessian is bounded here is the constrained Wilson-action part `S_eta(U_k(V))`. It is not the complete logarithmic RG effective action including all corrections `E_k`. Similarly, vanishing of the physical current at the trivial field removes the physical current correction; identifying this with the deposited free-current carrier at `(1,0)` remains a definition/source interface. Holes, frozen bonds, mixed histories and alternative block normalizations are outside the argument as stated.

## 6. Direct final lower bound, with one fewer hypothesis

The constants in Section 7 agree with the bridge note. In fact the conclusion only needs the pointwise quadratic inequality `q(B)>=||dB||^2`, not the stronger identity `q(B+D lambda)=q(B)`.

For `B in ker Q^flat`, set

    xi=T B,
    B_T=B-D xi,
    B_0=B_T-D d^(-1) T_0 B_T.

The exact bridge identities give

    B_0 in ker Qst intersect ker T_0,
    d B_0=d B_T=d B,
    ||B_T|| <= (1+d_0 t_0)||B_0||.

Therefore, directly,

    q(B) >= ||dB||^2
          = ||dB_0||^2
          >= gamma_loc ||B_0||^2
          >= gamma_T ||B_T||^2.

Since `B=B_T+D xi` and `||D||<=d_0`, weighted Cauchy--Schwarz gives

    ||B||^2 <= (gamma_T^(-1)+d_0^2)
                  [gamma_T||B_T||^2+||xi||^2]
             <= (gamma_T^(-1)+d_0^2)[q(B)+||TB||^2].

This proves exactly `gamma_exp=1/(gamma_T^(-1)+d_0^2)`. The full physical Hessian does have the expected flat gauge invariance when its effective-action identification holds, but the lower-bound proof need not consume that extra fact.

Finally, if the pivot extension `K_flat` retains the independent coordinates literally, then `||K_flat z||>=||z||`. Thus the lower bound survives pullback with no extension-norm loss. This is specific to that coordinate convention; it would not apply unchanged after an arbitrary rescaling of the independent variables. As stated, the note does not infer an upper precision bound, complex covariance accretivity, exponential decay, or normalized source responses from this lower bound.

## Audit conclusion

The direct flat gap is a valid new conditional reduction in the stated full-block periodic setting. The geometry and normalization checks do not reveal a hidden volume or RG-level factor. The remaining qualification is the actual effective-Hessian/source identification, together with the independent analytic and locality inputs explicitly left open in the research note. The two small clarifications above concern the index set of patch translations and the periodic-cell convention; they do not require changing the claimed constant or the proof strategy.

## Addendum: combined candidate Sections 5--6

I subsequently checked Sections 5--6 of `work/ym4-flat-maxwell-candidate.tex`. The compact-lift construction is under a separate audit; conditional on its displayed all-field upper bound `q_M(B)<=C_d||B||^2`, the combination is correct:

    gamma_*=[(1+d_0t_0)^2/gamma_loc+d_0^2]^(-1),
    B_*=(C_d+t_0^2)K_*^2,
    gamma_* I <= A_(M,0) <= B_* I.

There is no need to pass the upper bound through the tree gauge bridge, because it already holds on every coarse field. The exact gradient invariance of the quadratic variational form follows in both directions from the onto scalar block-average map. It is not an unproved property of an arbitrary corrected nonlinear branch.

The stated inverse and complex perturbation inequalities check. For `||V||<=gamma_*/2`, accretivity gives `||A^(-1)||<=2/gamma_*`, and

    Herm(A^(-1))=A^(-*) Herm(A) A^(-1)
      >= [gamma_*/(2(B_*+gamma_*/2)^2)] I.

Complex symmetry is not needed for this particular algebraic implication. Obtaining the actual uniform norm bound on `V` is explicitly left conditional.

The finite-regulator implicit-function argument is valid with the stated hypotheses. In logarithmic coordinates the analytic averaging constraint has a surjective derivative, by the lift and root/straight correction. A fixed complement of its kernel and the ordinary implicit-function theorem correct `tA` by `O(t^2)` to a nonlinear feasible curve for each `QA=B`. Comparing action coefficients proves the variational identity when the actual branch minimizes against these curves. The frozen-gauge caveat correctly prevents silently using competitors that do not belong to the branch's gauge slice. No uniform radius follows from this argument.

Two corrections/clarifications were sent to the parent:

1. The candidate initially assumed only differentiability of `U_k` but wrote `t L_k B+O(t^2)` and called the coefficient a Hessian. Differentiability alone gives `t L_k B+o(t)`, sufficient for the quadratic Peano coefficient. A classical Hessian and the stated `O(t^2)` expansion require additional regularity, such as a C2/analytic branch. The original lower-bound note already made the distinction correctly.
2. If only the Wilson action is multiplied by `c>0` while the gauge penalty remains `||TB||^2`, the complete precision bounds are not obtained by multiplying both constants by `c`. Instead use

       gamma_*(c)=[(1+d_0t_0)^2/(c gamma_loc)+d_0^2]^(-1),
       B_*(c)=(c C_d+t_0^2)K_*^2.

   Multiplying both action and gauge penalty by the same constant does rescale the whole precision. The displayed unit-normalization constants are correct.
