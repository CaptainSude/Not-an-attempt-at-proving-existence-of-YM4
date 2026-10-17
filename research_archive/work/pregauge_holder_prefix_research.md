# Hölder-regular ordinary prefixes and supported pre-gauge fields

17 October 2026. Proof module for independent audit. All identities are on finite compatible periodic regulators. No compilation or output edit. This strengthens the bounded-output pre-gauge result using the existing ordinary trajectory and classical support theorems; it does not prove a quantum extraction contraction.

## 1. Inputs and scales

Fix the primitive odd ratio ell and 0<alpha<1. Let N=ell^(k+s)=MR, R=ell^s, eta=N^-1 and h=ell^k eta=R^-1. Physical coordinates have next-coarse spacing one. Write

    P_h(A)=(ih)^-1 log M_ell^k(exp(i eta A)).             (1.1)

The established ordinary-trajectory theorem supplies rho>0 and K<infinity, independent of k,s and volume, such that P_h is holomorphic from the complex supremum ball ||A||<rho into bounded physical h-lattice potentials, P_h(0)=0, and ||P_h(A)||<=K||A||. Its dependency radius is at most c_ell h in physical coordinates. Its constants depend on the primitive ell, not the endpoint ratio R. On nested centered compatible lattices it obeys

    P_h(T_z A)=T_z P_h(A),       z in h Z^d.             (1.2)

Translation by h preserves every earlier partition because h is an integer multiple of every earlier spacing. Translation by arbitrary fine offsets is not asserted.

Use physical nearest-neighbor gradients and the complete norm

    ||A||_(N_alpha,eta)=||A||_infinity
                +||nabla_eta A||_infinity+[nabla_eta A]_alpha. (1.3)

For periodic fields use the shortest periodic physical distance and consistent lifted bond orientations. Equivalent fixed-collar versions have uniform constants. Tori with short periods are treated by their periodic lifts, counting incidences with multiplicity. Output gradients in N_alpha,h use spacing h.

## 2. Uniform C^(1,alpha) estimate

On a smaller supremum ball, Cauchy gives constants K1,K2 independent of h such that ||DP_h||_(infinity->infinity)<=K1 and ||D^2P_h||_(infinity,infinity->infinity)<=K2. Suppose ||A||_(N_alpha,eta)<=b with b sufficiently small. Let T_h denote translation by h e_mu. Since h/eta is an integer,

    nabla_h A=(T_h A-A)/h

is an average of fine gradients. Consequently its supremum and physical alpha-Hölder seminorm are bounded by those of nabla_eta A. Covariance (1.2) and the fundamental theorem of calculus give

    nabla_h P_h(A)
      =integral_0^1 DP_h(A+t(T_h A-A)) nabla_h A dt.      (2.1)

This proves ||nabla_h P_h(A)||<=K1 b. To estimate the Hölder seminorm, translate by z in hZ^d. After using (1.2) for the differentiated map, subtract the two versions of (2.1). The change in the direction contributes at most

    K1 ||T_z nabla_h A-nabla_h A|| <= C K1 b |z|^alpha.

The change in the derivative operator contributes at most

    K2 ||T_z(A+t(T_h A-A))-(A+t(T_h A-A))||
          ||nabla_h A|| <= C K2 b^2 |z|.

Here the interpolated input is `(1-t)A+t T_hA`, whose first-gradient supremum is at most b. For |z|<=1 the last term is bounded by C K2 b^2 |z|^alpha. For larger |z| the already proved gradient supremum suffices. Therefore

    ||P_h(A)||_(N_alpha,h)<=C(b+b^2).                    (2.2)

All line segments stay in the common complex supremum ball; the proof is equally valid for complex potentials. At each finite regulator this is a holomorphic map between finite-dimensional normed spaces. Its bound on a fixed N_alpha ball, followed by Banach-valued Cauchy on that ball, gives refinement-uniform derivative bounds into N_alpha,h. No claim about an infinite-volume nonlinear map is needed to justify those bounds.

The proof uses only aligned translation covariance and uniform bounded-potential holomorphy. It does not differentiate an ordinary-average physical adjoint or sum its coordinate entries.

## 3. Application to the selected ordinary representative

The existing corrected minimizer and explicit ordinary transfer give

    A_o,N(w)=T_N(A_c,N(w)),
    ||A_o,N(w)||_(N_alpha,eta)<=C_o||w||_infinity,        (3.1)

on a complex product ball independent of N and volume. Define

    a_p(w)=h P_h(A_o,N(w)),
    V_p=exp(i a_p)=M_ell^k(exp(i eta A_o,N(w))).          (3.2)

Thus a_p is the same pre-root-gauge representative already constructed, rather than the source's gauge-zero field. Applying (2.2) gives

    ||a_p(w)||_(N_alpha,h)<=C h ||w||_infinity.          (3.3)

In current-unit coordinates let Delta_mu be the unscaled difference between adjacent h-lattice sites. Then

    ||a_p||_infinity <= C b h,
    ||Delta_mu a_p||_infinity <= C b h^2,
    ||Delta_nu Delta_mu a_p||_infinity <= C b h^(2+alpha). (3.4)

The last bound follows from the alpha-Hölder difference of nabla_h a_p, multiplied by h. It is not a uniform classical C² estimate. More generally, for an integer current-lattice shift z,

    |Delta_mu a_p(x+z)-Delta_mu a_p(x)|
          <= C b h^(2+alpha) |z|^alpha                 (3.5)

when the physical distance h|z| is at most one; for larger shifts the gradient supremum gives the same upper bound after enlarging C. Distances and translations in (3.5) are interpreted through compatible periodic lifts.

All constants in (3.3)–(3.5) are independent of M,R and auxiliary grouping J. They may depend on the fixed primitive ratio, alpha and the group. The scalar radius used here is fixed before R and J.

## 4. Strict supports in complete Hölder output fibers

Fix an admissible positive spatial exponent kappa from the classical support theorem and any finite cardinality reserve a>=0. Support labels i,X refer to final physical unit cells. For every output root i let E_(h,i) consist of the complete h-lattice fields restricted to a fixed enlarged physical collar of i, with its local N_alpha,h norm. Enlarge collars once to include all difference endpoints. This norm includes the supremum of every component and every required Hölder quotient in the collar. It is taken **before** the sum over X.

For the input use the established smooth partition of unity and Banach spaces of complete eta-fields supported in enlarged cells. Their reconstruction has a uniform norm C_rec; no arbitrary sharply restricted Hölder field is extended. The composite

    F_h=P_h o T_N                                         (4.1)

is uniformly holomorphic from a fixed N_alpha,eta ball into E_(h,i), by Section2 and the ordinary transfer theorem. Its row depends only on a fixed finite number N0 of input physical cells in a fixed radius r0 about i. These constants are independent of h because P_h has physical range O(h), while T_N has fixed physical range. The output collar contains O(R^d) bonds but it is one Banach output fiber, not a coordinate sum.

Expand F_h after smooth reconstruction in homogeneous degree n. Cauchy and polarization bound each degree-n multilinear coefficient by K(e/rho1)^n. Summing over the at most N0 possible input cell labels in each slot, and paying the rooted spatial star, yields

    v_n <= K [e C_rec N0 exp(kappa r0)/rho1]^n =K c^n,
           n>=1.                                       (4.2)

The constants do not depend on output dimension. These are the same mixed-insertion bounds as the existing finite-range Banach vertex lemma, now with the stronger output norm from Section2.

The corrected minimizer already has a strict complete-field family with arbitrary prescribed reserve a and norm at most C_a r. Substitute it into (4.2). Joining the rooted support trees and taking unions preserves the norm because graph Steiner length is subadditive under gluing at the slot roots and

    exp(a |union_q X_q|)<=product_q exp(a |X_q|).

The resulting majorant is `sum_(n>=1) K(c C_a r)^n`, bounded by `2Kc C_a r` once c C_a r<=1/2. Consequently there are r_a,C'_a independent of M,R and volume and strict families

    a_p|_i=sum_(nonempty X) a_(p;i,X)(w_X),
    a_(p;i,X)(0)=0,
    sup_i sum_X exp[kappa tau({i} union X)+a|X|]
                   ||a_(p;i,X)||_(E_(h,i);r)
            <= C'_a h r,          0<r<=r_a.             (4.3)

Choose one global Taylor expansion after the same smooth partition and one global grouping by the union of input variable supports. Only then restrict the resulting complete output coefficients to the collars. Thus a_(p;i,X) is the restriction of one global coefficient a_(p;X); overlapping collar representations agree. The local-row bounds above estimate this global assignment and do not require independently chosen decompositions at each output root.

The coefficient sums converge in the complete local Hölder output norm and agree with (3.2). The max/Hölder quotient is inside the support sum. There is no factor R^d from counting fine output values. The linear supported part and the nonlinear remainder satisfy the corresponding bounds C'_a h r and C'_a h r², after reducing r_a once. Every displayed angle-difference estimate in Section3 also holds termwise after summing the weighted family norms, by applying the corresponding bounded difference map to E_(h,i). For paths crossing several collars, use these coherent complete coefficients and telescoping; a fixed starting-root spatial weight can be compared along the path by the usual exponential distance factor. This last comparison must be budgeted if a path-weighted carrier norm is subsequently used.

This claim is a finite-regulator support theorem. Its coefficients may retain dependence on the fixed regulator and baseline. It does not assert volume consistency. For any fixed a the radius is uniform in M,R; increasing a may shrink that radius.

## 5. Exact spatial Taylor remainder

On the current unit lattice use D_nu f(v)=f(v+e_nu)-f(v). Choose a fixed shortest coordinate path Gamma from x to y. Every traversed edge has a positive-coordinate lower endpoint v(e), a direction nu(e) and a traversal sign s(e). Telescoping gives the exact identity

    f(y)-f(x)=sum_nu(y_nu-x_nu)D_nu f(x)+Rem_xy(f),
    Rem_xy(f)=sum_(e in Gamma)s(e)
                 [D_(nu(e))f(v(e))-D_(nu(e))f(x)].       (5.1)

A negative traversal uses the positive difference at its lower endpoint, not at its traversal initial point. For n=|x-y|_1, (3.5) gives

    |a_p(y)-a_p(x)|<=C b h² n,
    |Rem_xy(a_p)|<=C b h^(2+alpha)n^(1+alpha).          (5.2)

The more elementary bound n² sup|D²f| is also valid. These identities apply componentwise to a bond potential, keeping its orientation label fixed. For a periodic winding path use its lifted displacement; no nonexistent global affine function on a torus is asserted. The same inequalities apply to the strict families in (4.3), in collars enlarged by the path or using their global summed bounds.

Thus the scale pattern used in CMP109 pp285–288, (4.17)–(4.18) and (4.30), is available for this particular pre-gauge representative without assuming C² regularity. This is an independent derivation in explicit positive-bond conventions.

## 6. Scope and the noncircular-constant warning

The prefix and complete-field support constants above are fixed by the primitive ell, alpha and a prescribed support reserve before choosing R or J. They genuinely provide the factors R^-1, R^-2 and R^(-2-alpha).

By contrast, extracting coordinate kernels from a quantum activity family carried on J-cells gives constants depending on the cell dimension D~J^d and the current-distance conversion J. Fixed-order Cauchy and cardinal decay make those constants finite, but do not make them independent of J. Since the common-domain construction chooses J after R, the formal power count `C(J) R^-alpha` does not yet establish a noncircular contraction. A separate norm/extraction argument must control that dependence, change the parameter order, or obtain the necessary scale gain in a norm with already fixed constants.

This note proves regularity and support estimates. It does not classify low-degree gauge-invariant kernels, supply their Ward-compatible local counterterms, prove a beta-function sign, or close a quantum induction.
