# Total-kernel Ward extraction through field degree four

17 October 2026. Research proof for independent audit. This proves the low-momentum algebra for the **total** kernels, including their nonlinear Ward relation. It does not claim a coefficientwise gauge identity or a bounded localization of the subtracted functional. All constants in the preliminary kernel bound retain the fixed auxiliary grouping size.

## 1. Statement and exact scope

Consider a compact connected simple matrix gauge group with Hermitian Lie-algebra coordinates and a fixed invariant positive trace form. The main application is SU(2). Suppose a sequence of finite cubic periodic regulators carries analytic total corrections E_N with:

* local gauge invariance on a common neighborhood of zero, including its infinitesimal analytic Ward identity;
* output-unit translations and the full signed-permutation group;
* reality on real fields;
* connected activity representations on a fixed cell partition, with a common positive cardinality exponent and analytic radius.

The symmetry inputs are precisely those established for the actual local macrostep sector in composite_macrostep_symmetry_research.md. They concern the summed functional, not its chosen carrier coefficients. The global measurable completion and uncontrolled complement are not included.

Let S_N be an analytic gauge-invariant, spatially invariant real reference with S_N(0)=DS_N(0)=0. Assume its kernels through degree four obey the same kind of uniform fixed-order spatial-moment bounds, and that its limiting midpoint Hessian has normalization

    Gamma_2^S(p)=|p|^2 I-p p^T+O(|p|^4).                (1.1)

The standard normalized Wilson action is one such reference. The actual homogeneous classical action S_(MR) is another: its exact Hessian is the previously constructed q_(MR), and flat_covariance_decay_research.md Section 10 / Notebook07 proves (1.1) uniformly in MR. The classical strict-support theorem supplies its higher-kernel bounds. Ellipticity alone would not imply (1.1).

There is a joint subsequence of the total kernels of E_N and S_N, through field degree four, on which the infinite-lattice kernels exist and have exponentially summable spatial moments. Write their midpoint Fourier vertices as Gamma_n^E and Gamma_n^S, with momenta summing to zero. There is a real scalar beta such that the residual vertices

    Gamma_n^F=Gamma_n^E-beta Gamma_n^S

satisfy, near simultaneous zero momentum,

    Gamma_2^F(p)=O(|p|^4),
    Gamma_3^F(p1,p2,p3)=O((max_j |pj|)^3),
    Gamma_4^F(p1,p2,p3,p4)=O((max_j |pj|)^2).           (1.2)

Thus every total-kernel Taylor coefficient with field degree n=2,3,4 and momentum degree at most 4-n agrees with beta times the reference. The one-point kernel is zero, and the vacuum term is unrestricted.

This is an exact extraction theorem for these limiting kernels. The selected subsequence and beta need not be unique. It does not assert an exact continuous-momentum identity for a finite torus, whose winding terms can survive. A finite-volume localization with uniform wrapping-error estimates remains a separate step.

For a semisimple product, the quadratic invariant form has one coefficient beta_a per simple ideal. The proof applies after subtracting a family of gauge-invariant references whose normalized Hessians are the individual simple-ideal Maxwell blocks. A one-coupling rebase is immediate for a simple group, or when those coefficients coincide; it is not asserted for a general product with distinct coefficients.

## 2. Fixed-order kernels and passage to an infinite kernel

Here are the quantitative hypotheses actually supplied by the present activity class. Let H be connected in a cell graph, with at most D scalar field coordinates per cell, and suppose

    sup_I sum_(H contains I) e^(a0 |H|) ||E_H||_b
       <= epsilon.                                      (2.1)

For fixed n, scalar coordinate Cauchy on one H gives

    sum_(i1,...,in in H) |D^n E_H(0)[ei1,...,ein]|
       <= (D|H|+n)^n b^(-n) ||E_H||_b.                 (2.2)

For example, the exact sum of Taylor monomial counts is
n! binom(D|H|+n-1,n), bounded by the displayed expression.
Fixing the first coordinate can only decrease this sum. If a derivative is nonzero, its coordinates lie in H, so their graph Steiner length is at most |H|-1. Consequently for 0<sigma<a0,

    sup_i1 sum_(i2,...,in)
       e^(sigma tau(i1,...,in)) |K_n(i1,...,in)|
    <= b^(-n) epsilon
       sup_(m>=1) (Dm+n)^n e^(-(a0-sigma)m).             (2.3)

The scalar/color indices are included in these sums. Fixed spatial moments are absorbed by a further fixed exponent loss. Passing from cells of side J to unit sites changes the exponent and constants by fixed J-dependent factors. In particular (2.3) is not a claim of a constant chosen before J.

Global constant gauges imply K_1=0 separately at every bond: the covector there annihilates all Lie commutators, and a semisimple Lie algebra is its own commutator algebra.

Translation invariance lets us anchor the first coordinate at the origin. On exhausting cubic tori, every fixed tuple of displacements has bounded coefficients. A diagonal subsequence for the finite number of tensor orders n<=4, and simultaneously for the reference, gives infinite-lattice kernels. Fatou and a smaller exponent preserve (2.3). The exponential tails also permit termwise Fourier differentiation of any fixed order.

Hessian symmetry generalizes to permutation symmetry of all n slots. Translation, signed permutations and global adjoint covariance pass at every fixed tuple. The differentiated Ward identities below also pass: they involve finite nearest-neighbor shifts and lower kernels with coinciding bond slots, not an uncontrolled nonlocal operation. Alternatively one may test them first against finitely supported fields and gauges, use exponential summability, and then exhaust their supports.

The resulting Fourier vertices are analytic near the simultaneous origin. No convergence of the total infinite-volume functional is claimed: a nonzero vacuum density already prevents such an unnormalized total sum from converging.

## 3. Exact logarithmic gauge generator and the low Ward identities

Write U_b=exp(i A_b) and take the gauge transformation

    U_b(t)=exp(i t lambda_(b_-)) U_b exp(-i t lambda_(b_+)),
    (d lambda)_b=lambda_(b_+)-lambda_(b_-).

With ad_A X=[A,X], differentiation of the exponential chart gives

    delta_lambda A
      = i[lambda_-,A]-f(i ad_A)d lambda,
    f(z)=z/(1-exp(-z))
        =1+z/2+z^2/12+O(z^4).                          (3.1)

Thus

    delta_lambda A=-d lambda+L_lambda(A)+Q_lambda(A,A)
                         +O(A^4 lambda),
    L_lambda(A)_b=(i/2)[lambda_-+lambda_+, A_b],
    Q_lambda(A,B)_b=(1/24)(
       [A_b,[B_b,d lambda_b]]+[B_b,[A_b,d lambda_b]]).
                                                               (3.2)

The remainder is fourth order in A, not third: the cubic Bernoulli coefficient vanishes. Only the displayed orders are needed.

Since K_1=0, the coefficients of

    DE(A)[delta_lambda A]=0

at field degrees one, two and three give

    K_2(A,d lambda)=0,
    K_3(A,A,d lambda)=2 K_2(A,L_lambda(A)),
    K_4(A,A,A,d lambda)
       =3 K_3(A,A,L_lambda(A))
          +6 K_2(A,Q_lambda(A,A)).                    (3.3)

Polarizing yields the exact mixed identities

    K_3(A,B,d lambda)
       =K_2(A,L_lambda(B))+K_2(B,L_lambda(A)),           (3.4)

    K_4(A,B,C,d lambda)
       =K_3(A,B,L_lambda(C))
         +K_3(A,C,L_lambda(B))
         +K_3(B,C,L_lambda(A))
         +2K_2(A,Q_lambda(B,C))
         +2K_2(B,Q_lambda(A,C))
         +2K_2(C,Q_lambda(A,B)).                        (3.5)

All these are identities of the total kernels. Subtracting only K_2 would generally destroy (3.4)-(3.5). Subtracting beta times an exactly gauge-invariant reference preserves every identity.

These equations are independently derived from (3.1), rather than copied from damaged OCR. The published counterparts are Bałaban, CMP109 (1987), equations (4.9)-(4.15), pp.283-284; its later full-action subtraction is (4.38)-(4.45), pp.291-292. The source's stronger coefficientwise orbit hypotheses are not imported here.

The original article was checked through its [public primary copy](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf): (4.9) uses the same Bernoulli gauge generator, and the paragraph after (4.45) explicitly describes cancellation against the full action subtraction. Our tensor factors and midpoint formulas are derived here, not inferred from the OCR.

## 4. Midpoint Fourier conventions, parity, and generator phases

For b=(x,x+e_mu), use the Fourier representation

    A_mu(x)=integral exp(i p.(x+e_mu/2)) a_mu(p) dp.

For scalar site gauges use exp(i k.x) lambda(k). On the surface
p1+...+pn=0 define Gamma_n so that the multilinear functional is
the integral of Gamma_n times the n midpoint Fourier fields.
Anchoring its first bond makes the phase

    exp(i sum_(j=2)^n pj.(xj+e_(mu_j)/2-e_(mu_1)/2)).
                                                               (4.1)

Only a neighborhood of zero momentum is needed. Midpoint vertices can be quasiperiodic under a 2pi shift in a single momentum; this causes no local analytic difficulty.

The three Fourier ingredients in (3.2) are explicit:

    (d lambda)_mu: 2i sin(k_mu/2) lambda(k),
    L_lambda(A)_mu: i cos(k_mu/2)[lambda(k),a_mu(p)],
    Q_lambda(A,B)_mu:
       (i/12) sin(k_mu/2)
       ([a_mu(p),[b_mu(q),lambda(k)]]
        +[b_mu(q),[a_mu(p),lambda(k)]]).
                                                               (4.2)

The output momenta are respectively k, p+k and p+q+k. In particular L has a bounded analytic coefficient at zero momentum, while Q has one power of the gauge momentum. There is no singular phase or inverse gradient in these formulas.

Under full spatial inversion a midpoint bond field transforms as
a_mu(p) -> -a_mu(-p). Consequently the total vertices satisfy

    Gamma_n(-p1,...,-pn)=(-1)^n Gamma_n(p1,...,pn).       (4.3)

This is the reason Gamma_3 has only odd homogeneous momentum terms and Gamma_2,Gamma_4 only even ones. It would not have this phase-free form in uncentered tail coordinates.

## 5. Quadratic extraction and its normalization

The audited symmetry note gives the following argument. The limiting
Hessian obeys

    Gamma_2(p) hat p=0,  hat p_mu=2 sin(p_mu/2).

At p=t e_mu, continuity implies Gamma_2(0)e_mu=0, hence
Gamma_2(0)=0. This uses continuous momenta of the limiting kernel;
finite periodic momenta do not suffice.

Global color covariance makes each simple-ideal Hessian proportional
to its invariant color inner product. Reflections and permutations
restrict its degree-two spatial part to

    (P_2)_(mu mu)=A p_mu^2+B sum_(nu != mu) p_nu^2,
    (P_2)_(mu nu)=C p_mu p_nu, mu != nu.

The degree-three Ward relation P_2(p)p=0 gives A=0 and C=-B.
Reality makes beta=B real. Thus

    Gamma_2^E(p)=beta (|p|^2 I-p p^T)+O(|p|^4).         (5.1)

The reference normalization (1.1) gives the residual bound

    Gamma_2^F(p)=O(|p|^4).                              (5.2)

One may define beta by

    beta=(1/2) partial_(p_nu)^2
                   (Gamma_2^E)_(mu mu)(0), mu != nu,   (5.3)

in a trace-orthonormal color direction. The value is independent
of the distinct coordinate pair. Its absolute bound is one half
the corresponding second spatial moment.

## 6. The cubic marginal polynomial is forced by the Hessian

Apply (3.4) to the residual F=E-beta S and take three plane-wave
arguments with momenta tp,tq,tk, p+q+k=0. Formula (4.2) shows that
the right side is O(t^4), by (5.2). By inversion parity,

    Gamma_3^F(tp,tq,tk)=t P_1(p,q,k)+O(t^3).             (6.1)

The left side of (3.4) contracts the last vector index with
2i sin(tk/2)=it k+O(t^3). Its degree-two coefficient therefore
vanishes. Permutation symmetry gives the same conclusion for
each slot:

    p_mu (P_1)_(mu nu rho)=0,
    q_nu (P_1)_(mu nu rho)=0,
    k_rho (P_1)_(mu nu rho)=0.                          (6.2)

These identities hold for each choice of color indices. The
color commutators on the right side are harmless because their
Hessian coefficient is already O(t^4).

Here is the required elementary polynomial lemma, with no appeal
to a continuum cohomology classification. Eliminate k=-p-q and
write an arbitrary degree-one tensor as

    (P_1)_(mu nu rho)
       =sum_sigma A_(mu nu rho;sigma) p_sigma
                    +B_(mu nu rho;sigma) q_sigma.

In the first equation of (6.2), the mixed monomials
p_mu q_sigma have independent coefficients. They force every
B_(mu nu rho;sigma)=0. In the second equation the monomials
q_nu p_sigma are independent and force every A_(mu nu rho;sigma)=0.
Thus P_1=0. No antisymmetric exception survives, and the third
identity is not even needed.

Combining this with (6.1) proves

    Gamma_3^E-beta Gamma_3^S=O((max_j |pj|)^3).          (6.3)

The proof does not assume a separately invariant cubic functional.
It derives its leading coefficient from the nonlinear total Ward
identity after the full reference subtraction.

## 7. The quartic marginal tensor is forced as well

Apply (3.5) to the residual and scale all four momenta by t.
The terms with K_3 and L are O(t^3), by (6.3) and the bounded
cosine coefficient in (4.2). The terms with K_2 and Q are O(t^5),
by (5.2) and the sine factor in (4.2).

Write the constant quartic tensor as P_0. Inversion parity gives

    Gamma_4^F(tp1,...,tp4)=P_0+O(t^2).

The degree-one left side of the Ward identity is consequently
the contraction of P_0 with the arbitrary last gauge momentum p4.
It must vanish. The first three momenta can always be chosen to
sum to -p4, so p4 is unrestricted. It follows componentwise that
P_0=0. Therefore

    Gamma_4^E-beta Gamma_4^S=O((max_j |pj|)^2).            (7.1)

This completes (1.2). In particular there is no independent
constant quartic tensor left over after the correct quadratic
coefficient has been subtracted from an exactly invariant
reference. The conclusion concerns the integrated total kernel;
it does not select a unique density modulo lattice divergences.

## 8. Meaning of the full Wilson completion

For the standard Wilson reference, the marginal continuum
polynomial can be displayed explicitly. In Hermitian conventions,
put

    f_(mu nu)=partial_mu A_nu-partial_nu A_mu,
    F_(mu nu)=f_(mu nu)+i[A_mu,A_nu].

The engineering-degree-four polynomial is

    (1/2) sum_(mu<nu) tau(F_(mu nu)^2)
      =(1/2) sum tau(f_(mu nu)^2)
         +i sum tau(f_(mu nu)[A_mu,A_nu])
         -(1/2) sum tau([A_mu,A_nu]^2).                 (8.1)

This normalization follows directly from a plaquette. Give each
bond the angle t A evaluated at its midpoint on a lattice with
physical spacing t. Its four-exponential product is
I+i t^2 F_(mu nu)+O(t^3); the normalized Wilson density
1-(1/2)tau(P+P^{-1}) is
(t^4/2)tau(F_(mu nu)^2)+O(t^5).
Thus the cubic one-derivative and quartic zero-derivative terms
in (8.1) are precisely the lower jets forced by (6.3),(7.1).

No explicit Wilson expansion is required for the general reference
theorem. In particular any exact invariant analytic reference
with (1.1), including S_(MR), has these same marginal total
vertices by applying the theorem to the difference of the two
references.

For the actual classical reference the scalar rebasing identity is

    exp[-g^(-2) S_(MR)+E]
      =exp[-(g^(-2)-beta) S_(MR)+(E-beta S_(MR))].        (8.2)

The vacuum may be subtracted separately. Equation (8.2) is an
algebraic identity, not a proof that g^(-2)-beta remains positive
or has the asymptotically-free drift required for iteration.

## 9. Quantitative remainders and the unresolved norm step

For an anchored n-point kernel put xi_j=x_j+e_(mu_j)/2, the bond midpoint (not its tail), and define the absolute moment

    T_(n,m)=sup_(first bond/color index)
       sum_(other indices)
       (sum_(j=2)^n |xi_j-xi_1|_1)^m
                           |K_n(i1,...,in)|.            (9.1)

Apply this to the residual kernels, bounded by the moments of E
plus |beta| times those of S. The phase (4.1), Taylor's integral
remainder along a real simultaneous momentum ray, and the
vanishing terms already proved give componentwise bounds

    |Gamma_2^F(p)| <= T_(2,4) ||p||_infinity^4/4!,
    |Gamma_3^F(p1,p2,p3)|
       <= T_(3,3) (max_(j>=2)||pj||_infinity)^3/3!,
    |Gamma_4^F(p1,p2,p3,p4)|
       <= T_(4,2) (max_(j>=2)||pj||_infinity)^2/2!.
                                                               (9.2)

Finite color/vector row sums introduce only their fixed dimensions.
The exponential estimate (2.3) makes these moments finite. It
also justifies the analytic expansions and all Ward operations
above without taking a formal derivative of an unsummable series.

These constants can depend strongly on the old grouping J and
on its physical range. The current common-domain construction
chooses J after R. Consequently multiplying an estimate with
C(J) by R^{-alpha} is not, by itself, a contraction argument.
No such claim is made here.

The remaining construction work is now more precise:

1. Localize the canceled total low-degree functional into connected
   coefficients with the needed norm, without imposing false
   coefficientwise gauge identities.
2. Control finite-period wrapping terms, or construct a consistent
   infinite-volume correction. A subsequential kernel classification
   does not supply a unique finite-volume counterterm map.
3. Prove a scale gain in a norm whose spatial-moment constants are
   fixed in the correct parameter order, rather than allowing
   an uncontrolled C(J) to defeat that gain.
4. Establish the sign, size and accumulated trajectory of the
   actual beta and the remaining activity under repeated steps.

The proof discharges the finite Taylor Ward classification of
the total infinite kernels through engineering degree four.
It does not discharge these localization, regulator and
renormalization-flow obligations.

The moment cancellations also hold in ordinary tail-anchored Fourier coordinates. Passing from midpoint to tail vertices multiplies each component by an analytic nonzero phase. Such multiplication cannot lower its vanishing order. Thus the residual ordinary vertices have all jets through degrees 3, 2 and 1 zero for n=2, 3 and 4 respectively. In particular the weaker anchored moments needed for quadratic second-order, cubic first-order and quartic zeroth-order spatial subtractions vanish.
