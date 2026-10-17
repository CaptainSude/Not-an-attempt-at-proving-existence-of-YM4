# Spatially canceled low kernels under a classical background

17 October 2026. Research proof for independent audit. Dimension four throughout. The conclusion is a connected-activity norm estimate, not just an extensive scalar estimate. The inputs are total-kernel moments and coherent complete-field support families. This note does not yet identify the resulting relocalization with a finite-volume quantum extraction.

## 1. Precise inputs

The current lattice is Z^4. A coordinate consists of a site, positive bond direction and color; their finite internal dimension is denoted v. For n=2,3,4 let K_n be a translation-invariant, symmetric n-linear kernel. Anchor its first site at x and write the remaining sites as x+r_2,...,x+r_n. Internal indices are retained in every sum. Set m=sum_{j=2}^n |r_j|_1 and suppose

    sup_(first internal index) sum_(others,r_2,...,r_n)
            exp(sigma m) |K_n(0,r_2,...,r_n)|
        <= epsilon b^(-n),                              (1.1)

for some fixed sigma>0. A change in the definition of epsilon can absorb separate constants for the three orders. Both sigma and epsilon can depend on a fixed old grouping J. A connected activity norm supplies (1.1), with smaller sigma, by fixed-order Cauchy and exponential tree length; for n<=4, m is at most three times a spanning-tree length.

Assume the following componentwise anchored moment cancellations:

* every anchored momentum jet of K_2 through total degree three vanishes: sum_r r^gamma K_2(r)=0 for every multiindex |gamma|<=3;
* sum_(r,s) K_3(r,s)=0, sum r_rho K_3(r,s)=0 and sum s_rho K_3(r,s)=0;
* sum_(r,s,t) K_4(r,s,t)=0.

The total Ward extraction gives stronger cancellations, so these hypotheses hold for its residual infinite kernels. Site-tail rather than midpoint coordinates are used here. Multiplication by the analytic midpoint phases preserves the orders of vanishing.

Fix an integer endpoint ratio L, h=1/L, and an analytic background map a(w) on the radius-b ball of final-lattice bond fields. Its current sites have physical spacing h. Assume the coherent complete-field strict families of the pgh theorem: for each final unit-cell root i and a fixed enlarged collar,

    a|_i=sum_(X nonempty) a_(i,X)(w_X),    a_(i,X)(0)=0,
    sup_i sum_X exp(kappa tau({i} union X)+A|X|)
                 ||a_(i,X)||_(C^(1,alpha),b)
       <= C_* b h.                                     (1.2)

Physical derivatives are used in this norm. The coefficients are restrictions of one global assignment, and all maxima and first-gradient Hölder quotients on the collar are inside the support sum. Increase the fixed collar size, if necessary, to contain all points at current distance <=L and the fixed coordinate paths between them; this only changes C_* by a fixed factor. The spatial exponent can be decreased by a fixed factor to pass between neighboring collar roots. No L-dependent increase is involved.

The construction of such families on finite regulators is the pgh theorem. The following estimate applies on the infinite lattice whenever families (1.2) have been obtained, for example by an independently justified infinite-volume subsequence. It also applies to explicitly periodized infinite kernels and coherent periodized families, with sums and paths interpreted on their lifts. It does not treat an arbitrary finite torus kernel as if it already had the exact lifted moment cancellations.

## 2. Claim and parameter order

Let P_n(a)=K_n(a,...,a)/n!. For an initially compactly supported final field w, use the normally convergent substituted expressions below to define these functionals. Vacuum constants are absent. Fix target connected-carrier exponent a_0>0 and set c=a_0+1. Choose J once so that

    2c/J <= kappa,             A >= 4c.                 (2.1)

These are the same kind of spatial/cardinality budgets as the previously proved joint-carrier lemma. They can be imposed along with the already required fixed-step grouping conditions. There are constants C and L_0, depending on sigma,J,C_*,a_0,alpha and the fixed internal dimension but not on L,b,volume or preceding refinement, such that for L>=L_0 one can construct connected activities B_H on final J-cells with

    sum_H B_H(w_H)=sum_(n=2)^4 P_n(a(w)),
    sup_I sum_(H contains I) exp(a_0 |H|) ||B_H||_b
        <= C epsilon L^(-alpha).                       (2.2)

The construction is linear in the kernels. Individual B_H need not be gauge invariant. The identity is of vacuum-normalized analytic functionals on compactly supported fields, and hence of their local analytic interactions. In particular it does not assert convergence of an unnormalized infinite total energy at a constant nonzero field.

The constant C is fixed AFTER J and BEFORE L. Setting L=R^q with fixed R,J, and choosing finite q afterward, can therefore make the right-hand coefficient as small as desired. Whether the complete quantum recursion admits this reorganization is a subsequent question.

## 3. Exact algebra before estimating

Write a(x) as the vector of all positive direction/color components at x; all the following matrix/tensor formulas include these indices.

For n=2 use an exponentially summable Laurent factorization, which does not require the matrix K_2(r) to be symmetric at each displacement. Write

    F(z)=sum_r K_2(r) z^r,       d_rho^+(z)=z_rho-1,
    d_rho^-(z)=z_rho^(-1)-1.

The exponential kernel bound makes F holomorphic on a product annulus. Its momentum jets through degree three vanish, so its complex-coordinate jets through degree three at z=(1,...,1) vanish as well. Define the ordered divided difference

    B_j F(z)=
      [F(1,...,1,z_j,...,z_d)
        -F(1,...,1,1,z_(j+1),...,z_d)]/(z_j-1).

The quotient is removable at z_j=1 and

    F(z)-F(1)=sum_j (z_j-1) B_j F(z).

For a Laurent monomial z^r, its quotient in coordinate j is a sum of |r_j| monomials, each of absolute exponent length at most |r|_1. Thus for 0<sigma'<sigma the combined absolute matrix-row Wiener norm obeys

    sup_row sum_(j,column,r) exp(sigma'|r|_1)
                         |(B_j F)_(row,column)(r)|
       <= [e(sigma-sigma')]^(-1) ||F||_sigma.

The j sum is inside the row supremum; no interchange of suprema and order sums is used. The local Taylor series also shows that vanishing jets of orders <k for F imply vanishing jets of orders <k-1 for every B_j F. Apply the identity twice, first at exponent 3sigma/4 and then at sigma/2. With

    H_(rho,tau)=B_tau B_rho F,
    Htilde_(rho,tau)(z)=-z_rho H_(rho,tau)(z),

we obtain

    F(z)=sum_(rho,tau)
             d_rho^-(z) Htilde_(rho,tau)(z) d_tau^+(z),
    Htilde_(rho,tau)(1)=0,                              (3.1a)

and the combined kernel bound

    sup_row sum_(rho,tau,column,r) exp((sigma/2)|r|_1)
                   |Htilde_(rho,tau)(r)_(row,column)|
       <= [16 exp(sigma/2)/(e^2 sigma^2)]
                      epsilon b^(-2).                (3.1b)

In fact Htilde has vanishing jets through degree one. Multiplication by z_rho costs at most exp(sigma/2). No symmetry of the individual matrices Htilde is required.

Integration by parts transfers one difference to each field. The zero sum of Htilde gives the exact quadratic identity

    P_2(a)=1/2 sum_(x,r,rho,tau)
        [D_rho a(x)]^T Htilde_(rho,tau)(r)
                [D_tau a(x+r)-D_tau a(x)].             (3.1)

Here d_rho^- is the bilinear adjoint of the positive difference d_rho^+. For compactly supported fields the identity is immediate; the normally convergent substituted fields are handled by the exponential majorants below. No positivity of K_2 is assumed.

For the cubic calculation set

    ell_r(x)=sum_rho r_rho D_rho a(x),
    R_r(x)=a(x+r)-a(x)-ell_r(x),                       (3.2)

where D_rho is the positive unscaled current difference. Only first-gradient Hölder regularity is used in (3.1): both field factors already carry a first difference, and the second factor is their Hölder difference. The cubic Taylor remainder in (3.2) uses that same regularity.

For n=3, use an anchored expression

    P_3(a)=1/6 sum_(x,r,s)
          K_3(r,s)[a(x),a(x+r),a(x+s)].                 (3.3)

Replace each shifted factor by a(x)+ell+R. The zeroth moment cancels the a,a,a term. The first moments cancel the a,ell,a and a,a,ell terms. Retain the six remaining terms: the two with one R and no ell, the ell,ell term, the two ell,R terms, and the R,R term, each with the unshifted a as its first argument.

For n=4 subtract the product with all four factors at x using its zeroth moment. Telescope the difference of the three shifted-factor product and the anchor product. Each of the resulting three terms contains one difference a(x+r_j)-a(x), and three endpoint or anchor factors. This identity does not introduce derivatives of the kernel.

These cancellations are performed in the total kernels BEFORE any triangle inequality or final carrier assignment. No coefficientwise Ward identity is used.

## 4. Near displacements and complete-field estimates

Split each of the exact residual summands from Section 3 into m<=L and m>L. This split is made AFTER the moment cancellations. Neither restricted kernel is asserted to have zero moments.

For m<=L the anchor, all endpoints and the chosen coordinate paths fit in one fixed final-unit collar. Coherent coefficients in (1.2) obey, in the rooted weighted family norm,

    |a| <= C b h,
    |ell_r| <= C b h^2 |r|_1,
    |a(x+r)-a(x)| <= C b h^2 |r|_1,
    |R_r| <= C b h^(2+alpha) |r|_1^(1+alpha).           (4.1)

The last line follows from the oriented discrete Taylor identity, with a negative traversal using the positive difference at its lower endpoint. Each inequality here is an inequality for the sum of weighted norms of coefficients; it is not inferred from a bound for the scalar sum. All factors can be rooted at the anchor's final unit cell. Multiplying at most four families glues their rooted trees and preserves their support weight, because both tree length and union cardinality are subadditive.

For the quadratic identity (3.1), the complete collar bound gives

    |D_rho a(x)| <= C b h^2,
    |D_tau a(x+r)-D_tau a(x)|
                     <= C b h^(2+alpha) |r|_1^alpha.

Thus its rooted coefficient product is bounded by

    C b^2 h^(4+alpha) |r|_1^alpha.                     (4.2)

It is summed with the exponentially summable Htilde kernel in (3.1b), rather than with K_2 directly. This changes only the fixed sigma-dependent constant and replaces the available decay exponent by sigma/2.

For the cubic residual the six terms are bounded by

    C b^3 h^(4+alpha) (1+m)^6.                         (4.3)

Indeed the leading a,a,R term has h^(4+alpha); a,ell,ell has h^5, which is no larger for 0<alpha<1 and h<=1; the other terms carry still higher powers. A fixed polynomial of degree six bounds all the displacement powers. The quartic telescoping gives

    C b^4 h^5 (1+m).                                  (4.4)

After the weighted kernel sums (3.1b) and (1.1), the factors b^n cancel. Fixed displacement moments cost only fixed powers of sigma^(-1). The resulting rooted contributions per original anchor are at most C epsilon h^(4+alpha), C epsilon h^(4+alpha) and C epsilon h^5 respectively.

## 5. Connected carriers and the anchor count

This is the norm step. For every product coefficient, retain its final-unit anchor i_0 and all endpoint roots actually used. For a near summand these are just i_0; the complete collar controls the other evaluations. For a far summand use the finitely many endpoint roots and any neighbor roots needed for D a(x). There are at most a fixed number n_0 of these roots, independently of L and the displacements.

Project the finite root set and each field-factor terminal set {root} union X to final J-cells. For each projected terminal set choose a deterministic short macro connecting graph supplied by the established projection lemma. Their connected union is the carrier H, including the anchor. Fine Steiner lengths bound these chosen macro graphs; the carrier need not contain the full projection of an arbitrarily chosen fine tree. The projection/tree inequality gives

    |H|<=1+T,
    T <= (2/J)[tau(roots)+sum_occ tau({root} union X)]
                   +4[n_0+sum_occ |X|].               (5.1)

The harmless fixed n_0 term can be retained even for a near summand. If z belongs to H and j(x) is the final J-cell containing x/L, then dist(z,j(x))<=T. Therefore

    exp(a_0|H|) 1_(z in H)
       <= exp(a_0) exp(-dist(z,j(x))) exp(c T).         (5.2)

Condition (2.1) pays the attached-tree and support-cardinality weights from (1.2). The remaining fixed exp(4c n_0) is part of C. For near summands the root-joining tree has bounded length, also paid by C. Finally

    sum_(x in Z^4) exp(-dist(z,j(x))) <= (JL)^4 S_1,
    S_1=sum_(y in Z^4) exp(-|y|_1).                    (5.3)

Each final J-cell contains exactly (JL)^4 current anchor sites (up to the same harmless centered-boundary convention). The finite internal first-index count multiplies this by a fixed v. Equations (4.2)-(5.3) give C J^4 epsilon L^(-alpha) for degrees two and three, and C J^4 epsilon L^(-1) for degree four. The entire anchor factor has now been displayed; there is no additional output-coordinate count.

## 6. Far displacements

For m>L use the exact residual formulas of Section 3, estimating each endpoint at its own root. For the cubic and quartic terms this gives

    |a| <= C b h,   |ell_r| <= C b h^2 m,
    |R_r| <= C b h(1+hm),                             (6.1)

in the corresponding separate-root family product norm. This uses a fixed number of endpoint factors, not a carrier containing every current site of a long path. The root tree length satisfies

    tau(roots) <= C_d(m/L+1).                          (6.2)

After (5.2), its additional weight is at most C exp(C' m/(JL)). For the quadratic term, both first differences in (3.1) have separate-root family bounds C b h^2, even for far endpoints. Its product is therefore bounded by C b^2 h^4. The cubic product is bounded by C b^3 h^3(1+m)^2, and the quartic by C b^4 h^4.

Use the common decay exponent sigma_* = sigma/2, valid for Htilde and for the original cubic/quartic kernels. Increase L_0 so that C'/(JL)<=sigma_*/4. These rough bounds then suffice.

Use one half of sigma_* to absorb the root-tree weight and the fixed polynomial. The remaining tail gives exp(-sigma_* L/4). After (5.3), the three far contributions are bounded by

    C J^4 epsilon (L+2) exp(-sigma_* L/4)
           <= C' epsilon L^(-alpha),    L>=L_0.        (6.3)

The last C' is finite and independent of L. Equations (5.3),(6.3) complete (2.2). Every estimate is an absolute majorant; regrouping by H is therefore legitimate and yields holomorphic coefficients on the same open b-ball, with the displayed b-supremum bound.

For compactly supported w, a coefficient vanishes unless its variable support meets that compact support, since each field factor vanishes at zero. The anchored output bound then implies absolute convergence of the total sum, bounded by a constant times the number of final J-cells meeting that support. Moreover, if K is the compact support, every nonzero field coefficient has tau({i} union X)>=dist(i,K). Equation (1.2) gives exponential spatial decay of a(w) and its first differences. Thus the original quadratic sum is absolutely convergent too, and truncation/exhaustion justifies the integration by parts with no boundary term. This verifies the stated interpretation of the scalar identity.

## 7. What has been established and what is still an interface

Subject to the explicit coherent-family and exact infinite-kernel hypotheses, (2.2) supplies bounded connected localization of the canceled total low-degree functional. It is stronger than power counting of its scalar value and does not rely on invariant individual carriers. It is linear in the total kernels, with all spatial constants fixed before L.

For an actual residual analytic activity E-beta S, one can split its coefficients into Taylor orders <=4 and >=5. The sum of the former has the kernels just treated, its total first-order term is zero, and its vacuum is subtracted. Notebook28 transports the coefficientwise >=5 remainder with an inverse-L bound, provided its field-scaling domain is chosen after L. The two separate localizations then give a candidate full classical contraction in a representation that is allowed to change.

The following are not established by this note: a canonical finite-torus extraction with wrapping control; an infinite-volume limit of the full quantum measure; equality of sequential and direct cutoff integrals; boundedness of a complete quantum map on a quotient of representations; the coupling trajectory; or the full existence theorem. The classical scalar semigroup permits using L=R^q for a gauge-invariant total input, but does not remove these interfaces.
