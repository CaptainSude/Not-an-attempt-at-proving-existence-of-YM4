# Independent audit of the full flat constraint-current argument

16 October 2026. Independently inspected the deposited source passages, derived the physical-scale and measure factors, and read all ten sections of `flat_full_constraint_current_research.md`. **Pass for the mathematical implication and its stated deposited-coordinate identification.** The refinement is `M=L^j` for fixed odd `L`, the final physical scale is one, the background is identity, and the norms are weighted physical-cell L2 operator norms. This is not an independent verification of every original CMP98 definition, nor a theorem for nonflat or retained-history carriers.

## 1. The selected map and the actual source coefficient

Raw I:24320–24325 explicitly composes the corrected double-bar operation. At flat reference the intermediate reference backgrounds are all identity, so the same fixed one-step map is used at every scale. The displayed linearization at I:24344–24369 reduces to the normalized straight-string average, not the rooted average. The higher-level coefficient entering the earlier current term is matched to this corrected remainder at I:26985–26988. This is separate from the later pivot chart's `C^(2)=Phi^flat_2` at I:46978.

The apparent missing input-coordinate definition is resolved within the deposit by I:47076–47087. Together with the explicit `e^{iB}V` input of `Phi^flat,Phi^g` at I:46965–46973, it gives at `V=1`

    exp(i F_L(X;c))
       =exp(-i alpha_-(X)) exp(i phi(X;c)) exp(i alpha_+(X)).

This is exactly the research note's equation (2.1a). The BCH coefficient in (2.1b) has the correct signs: with `X1=-alpha_-`, `X2=phi`, and `X3=alpha_+`, the logarithm divided by i contributes `(i/2)([X1,X2]+[X1,X3]+[X2,X3])`. In particular the two endpoint quadratic terms and three commutators cannot be dropped. Finite local analyticity near the identity gives a finite coefficient constant for this fixed-L map; no bound as L tends to infinity is used.

The source scale is explicit at I:12664–12669: `ell_j=L^j eta`, with multiplication by `ell_j` on the retained layer and corresponding fine region. Thus in the homogeneous final-scale-one case, `ell=1` and `H^J=E_J`. Replacing ell by the fine spacing would be incorrect. Under the stated source identification, the full symmetric form is exactly

    <A,Theta_J B>_eta=2<C_j^(2)(A,B), E_J^T J>_1.

All these source checks use the deposited transcriptions. The note correctly distinguishes this from a fresh verification of the inaccessible original article.

## 2. Physical scaling of the one-step jet

The physical input angle at spacing h is hA; the output angle at spacing Lh is Lh times its physical potential. Therefore

    F_h(A)=(Lh)^-1 F_L(hA)
          =Q_h A+(h/L) C_L(A,A)+O(A^3).

The h/L factor is exact, not a heuristic dimension estimate. C_L denotes the homogeneous quadratic coefficient, so polarization and the chain rule introduce no extra factor two. At each fixed finite depth the composite jet exists near zero; the argument does not assume a depth-uniform nonlinear chart merely to extract that jet.

The one-step paired form estimate correctly has constant `K_L N_L L^(d-1) h`. Indeed the coarse measure is `(Lh)^d`, the quadratic scaling is h/L, and the product of the two input physical norms supplies h^d after Cauchy–Schwarz. The finite fixed-step bond-incidence multiplicity is N_L. This computation neither compares a large-block sup norm to an L2 norm nor hides a factor M^d.

## 3. Both contraction statements and the chain rule

The normalized straight-string average has row sum one. Each oriented fine bond occurs in exactly L strings when one counts all coarse centers, centered block starts, and longitudinal offsets. Its ordinary column sum is therefore L^-d. Multiplication by the coarse/fine volume ratio L^d gives physical-adjoint row sum one. Positivity and Jensen then yield precisely

    ||Q_h A||_(2,Lh)<=||A||_(2,h),
    ||Q_h^* w||_infinity<=||w||_infinity.

The counting remains true on short compatible tori when repeated images are counted with their covering multiplicity. It is componentwise, so Lie algebra fibers do not change the contraction.

Equation (5.1) is the exact quadratic chain rule. Move the suffix average onto w by its physical adjoint and apply its sup contraction; apply the prefix's L2 contraction to both input legs. This leaves the factor

    sum_(t=0)^(j-1) L^(t-j)=(1-L^-j)/(L-1).

Thus (5.3) is uniform in j and compatible volume. At j=0 the map is identity and the quadratic coefficient is zero. No claim for all odd M, rather than the selected powers of L, is needed or made.

## 4. Operator locality and bounded currents

The bounded paired form defines a complex-linear fine operator by the fixed bilinear transpose convention; allowing all complex test vectors gives the stated Hilbert operator norm as well. Its finite physical range follows either from the deposited two-final-block support or from summing a fixed one-step reading radius over the same geometric spacings. The radius controlling the distance between the two input cells may be enlarged by a fixed factor; the note leaves its R_* free to include this enlargement.

For a finite-range cell kernel, each block norm is bounded by the global Hilbert norm. The number of possible neighboring cells, multiplied by `exp(kappa R_*)`, therefore gives (6.3). This is a cell count independent of refinement, not a count of fine variables in a cell. Periodic distance and the previously retained multiplicities cover small tori.

For a bounded fine current, a unit physical cell contains d units of oriented-bond volume, so its L2 norm is at most `sqrt(d)||J||_infinity` in the note's fiber convention. The transpose Schur row of E_J then gives (7.1). The infinite-volume sum is absolutely convergent cellwise and needs no global L2 hypothesis on J. The map `(E,J)->E^T J` is bounded from the weighted rectangular algebra times fine l-infinity into coarse l-infinity; hence w_J and Theta_J are holomorphic. Theta_J is finite range in its potential arguments even though its coefficients depend nonlocally, with controlled decay, on J. The note states this distinction explicitly.

## 5. Full inverse radius and derivatives

The fixed flat projection `Pi=I-DLambda` has a uniform weighted bound from the scalar four-derivative theorem. Thus

    ||Psi_J||_kappa
      <=[theta+4||Pi||_kappa^2 sqrt(d) e tau_kappa] ||J||_infinity.

Taking the minimum of the auxiliary radius and `[4g xi(1+c)]^-1` controls both the full fine inverse and the coarse inverse in the same order as the audited auxiliary proof. The estimates `2g,2q,4e` for the full inverse, coarse precision, and normalized extension follow. The perturbation is now nonlinear in J, but a bounded holomorphic perturbation is sufficient for these Neumann inverses.

The total-two-fine-derivative bounds follow from the outside-factor resolvent identity. No fine derivative of J is introduced. The auxiliary exact derivative chains cannot be copied verbatim because derivatives of Psi_J now also occur; the note correctly declines to do so. Its warning about the branched source geometry is also correct: a source can propagate to a coefficient cell before two potential legs separate, so the previous auxiliary ordered path bound is not automatic.

At zero current the first derivative formula (1.3) is exact. It retains only the derivative of Theta_J since the auxiliary term cancels and `Pi E_0=E_0`. One wording refinement was sent to the author: the displayed formula shows that this derivative is **not forced to vanish by the auxiliary cancellation**; saying it is “generally not zero” would additionally require an explicit nonzero datum or an independent nonvanishing argument. This wording does not affect any estimate or existence result in the note.

## 6. Conclusion and limits

No substantive mathematical correction was found. The proof supplies the missing physical-cell form bound for the selected corrected quadratic vertex, and therefore the full homogeneous flat current neighborhood. The path-concentration objection is correctly addressed: arbitrary macroscopic rooted-path formulas are not the iterated fixed-L quadratic coefficient being estimated here.

The independent source check is at the deposited-coordinate level, using the explicit bridge and earlier-current coefficient identification above. No assertion about nonflat covariance, mixed histories, arbitrary boundaries, pointwise/Hölder carriers, the nonlinear minimizing map beyond its quadratic jet, or an interacting continuum limit follows. Those restrictions are retained in the note.

## 7. Additional audit: the stronger fine sup-row estimate

The stronger `T_w:l-infinity->l-infinity` claim is also valid, but it should be proved from the fixed-step coefficients, not inferred from the L2 bound.

Write the finite one-step coefficient as

    C_L(A,B)(c)=sum_(b,b' in D_L(c)) c_(c;b,b')[A(b),B(b')],

where each bilinear tensor has norm bounded by a fixed `K_coeff`. Let `m_L=max_c #D_L(c)`. For the one-step symmetric operator associated to twice the paired form, the physical matrix coefficient carries the factor

    2 (Lh)^d h^-d (h/L)=2 L^(d-1) h.

For a fixed input/output row b, at most N_L output bonds c can contribute and each supplies at most m_L other fine bonds b'. The coefficient contraction with w is bounded by `K_coeff ||w||_infinity`. Consequently

    ||T_(h,w)||_(infinity->infinity)
      <=2 L^(d-1) N_L m_L K_coeff h ||w||_infinity.

This is an absolute matrix-row estimate with a fixed fiber norm; all color constants can be included in K_coeff. It is valid for complex coefficients and for short tori with covering multiplicity.

The quadratic composition formula implies exactly

    T_w=sum_t P_t^* T_(h_t,w_t) P_t,
    P_t=Q_(0:t),  w_t=Q_(t+1:j)^* w.

Both P_t and its **physical** adjoint have fine sup operator norm at most one, as shown by their nonnegative normalized row sums. The suffix also gives `||w_t||_infinity<=||w||_infinity`. Therefore

    ||T_w||_(infinity->infinity)
      <=[2 L^(d-1) N_L m_L K_coeff/(L-1)] ||w||_infinity,

uniformly in j and compatible volume. The same argument with absolute row norms proves a uniform absolute kernel-row bound, which is stronger than a bound relying on cancellations in the operator norm. Since the final kernel has fixed physical cell range, an exponential cell weight changes this by at most `exp(kappa R_*)`. The symmetric bilinear form also supplies the corresponding transpose/column statement. This additional result is compatible with, but not a substitute for, the separately needed pointwise estimates on the outer inverse propagators.
