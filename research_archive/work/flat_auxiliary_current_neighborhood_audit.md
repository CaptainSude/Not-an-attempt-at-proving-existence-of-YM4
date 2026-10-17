# Independent audit of the flat auxiliary-current neighborhood

16 October 2026. Audited `flat_auxiliary_current_neighborhood_research.md`, Sections 1--7, against the completed independent audits of the full flat inverse and scalar source-gauge locality. **Pass within the stated homogeneous flat auxiliary-family scope.** No mathematical correction is needed. The full fine-inverse input has now passed independent audit, so the conditional status of that input can be removed when the statements are assembled with its theorem.

## 1. Norms, parameter, and source scope

The physical fine-cell L2 norms, rectangular weighted block-Schur norms, and fixed analytic transpose are compatible. The Schur norm is submultiplicative by the metric triangle inequality. Its constants do not involve the number of fine sites in a cell. For complex currents, every star in a parameter-dependent coefficient must mean the stipulated analytic transpose, rather than conjugation of the current; the note already states this convention.

The baseline G_0 bound follows from the completed full-inverse theorem. The identities q_0=q_M+aI and E_0=H_src supply the needed q_0 and extension bounds. The local straight average and its adjoint have fixed cell range and uniformly bounded physical-cell norms. The auxiliary perturbation estimate follows from the already audited factorization through Lambda, D Lambda, and bounded finite-incidence current coefficients. The derivative in the m_J term acts on its scalar legs, not on J. A common Schur exponent kappa must be chosen below the exponential rates of all baseline kernels. Once this has been done, no subsequent change of kappa is required for the stated algebra estimates.

The perturbation is the displayed Theta'_J family only. The additional nonlinear-constraint term in the full G_1^J, general nonflat backgrounds, retained histories, arbitrary boundary geometries, and source pointwise/Hölder norms are not obtained by this argument.

## 2. The explicit radius and both inverses

Write c=g b^2 q, e=g b q, and epsilon=[4 g theta(1+c)]^(-1). Then

    ||G_0 Theta'_J||_kappa < 1/[4(1+c)] <= 1/4,
    ||G_J||_kappa <= (4/3)g <= 2g,
    ||G_J-G_0||_kappa <= 2g^2 theta ||J||_infinity.

For W_J=QG_JQ*,

    ||q_0(W_J-W_0)||_kappa
       <=2q b^2 g^2 theta ||J||_infinity
       <c/[2(1+c)]<1/2.

Thus q_J=[I+q_0(W_J-W_0)]^(-1)q_0 exists with norm at most 2q. This inverse ordering is correct because W_J=W_0[I+q_0(W_J-W_0)]. Finally ||E_J||_kappa<=4e. The two Neumann series converge in the same Banach algebra uniformly in refinement and volume. For theta=0 the perturbation vanishes, as separately stated.

This argument works for arbitrary bounded complex fine-bond currents, not only finite-dimensional parameter slices. For each fixed refinement, the fine precision and its bounded perturbation are actual Hilbert-space operators; the algebra inverse is their operator inverse. In infinite volume, holomorphy is on the complex l-infinity current ball.

## 3. The exact quadratic correction

For B_0=G_0-E_0QG_0,

    ||B_0||_kappa<=g+e b g=g(1+c)=t_0,
    QB_0=B_0Q*=0,
    B_0 Delta_0=I-E_0Q.

The radius gives ||B_0 Theta'_J||_kappa<1/4. Applying B_0 to the current stationary equation gives

    E_J-E_0=B_0 Theta'_J E_J.

Multiplying the same equation by E_0* gives q_J=q_0-E_0*Theta'_J E_J. The flat source-gauge identity E_0*Theta'_J E_0=0 therefore yields exactly

    q_J-q_0=-E_0*Theta'_J
                  (I-B_0 Theta'_J)^(-1)
                  B_0 Theta'_J E_0.

Both the sign and the order of the noncommuting factors agree with the stationary equations. The bounds 2e^2 theta^2 t_0 ||J||_infinity^2 and 2t_0 theta e ||J||_infinity for the precision and extension corrections follow immediately. No analytic-radius shrink or Cauchy loss is hidden in these estimates.

## 4. Derivatives at a nonzero base current

The estimate ||B_J||_kappa<=2g(1+4c)=t is valid because ||E_JQG_J||_kappa<=8g^2b^2q. The identities for B_{J+K}, E_{J+K}, and q_{J+K} follow either from the constrained stationary equations or from the inverse quadratic form on ker Q. Its extension to all fine fields annihilates ran Q*, so the displayed fine-space operator identities are legitimate.

In particular,

    q_{J+K}=q_J-E_J*Theta'_K
                     (I-B_JTheta'_K)^(-1)E_J.

The degree-n term contains n current factors and n-1 constrained propagators. Polarizing it gives precisely the sum over the n! permutations, with no additional factorial. The extension derivative has n factors B_JTheta' and one final E_J. The bounds

    ||D^n q_J[J_1,...,J_n]||_kappa
       <=n!(4e)^2 theta^n t^(n-1) product_i ||J_i||_infinity,
    ||D^n E_J[J_1,...,J_n]||_kappa
       <=n!(4e)(t theta)^n product_i ||J_i||_infinity

are therefore correct for every n>=1 and every base current inside the stated ball. The increment neighborhood used to derive the identities need only be a neighborhood of that base current; the uniform derivative bounds follow directly from the uniform propagator bounds and do not presume a fixed larger ball around every base current. At J=0 the first precision derivative vanishes, consistently with the exact quadratic remainder.

## 5. Anchored derivative paths and exponent accounting

For a current supported in one cell x, every local coefficient vertex reads and writes a fixed neighboring-cell set of x and has norm O(||J_x||_infinity). Expand each Theta' into its four terms. Between two local coefficient vertices, all nonlocal factors form one product A B_J C*, with A,C among I, Lambda, D Lambda, on their appropriate Hilbert spaces. Its kappa-Schur norm is uniformly bounded, hence its block between cells x,y is bounded by C exp(-kappa d(x,y)). End factors A E_J satisfy the same statement.

There are only a fixed number of neighboring cells and four choices per insertion. Moving each neighboring-cell endpoint back to its source center costs at most exp(C kappa) per edge. These factors are absorbed into C_1^n, giving exactly the path sum in equation (5.1). Repeated source cells cause no problem. The sum over permutations already accounts for the factorial differentiation; expanding the four terms costs only an exponential in n.

The intermediate products are estimated in the weighted algebra before taking their blocks. Accordingly there is no borderline convolution of pointwise exponential estimates and no unaccounted polynomial in the separation. The path estimate uses the same kappa as the input algebra. If one subsequently sums its endpoint blocks against an exponential weight, a smaller endpoint-weight exponent must be used unless the algebra estimate itself is invoked; that additional summed pointed estimate is not claimed in (5.1).

The finite-volume proof is identical with periodic distance. Exact baseline periodization and finite-incidence source vertices give uniform algebra constants, including short periods and repeated geometric incidences. No large-volume separation assumption is used.

## 6. Fine derivatives and final status

The outside-factor resolvent identity in (6.1) is exact. At total fine derivative order at most two, every required baseline one-sided factor and sandwich has now been proved by the full-inverse theorem. Thus all those physical-cell L2 derivative sandwiches persist throughout the same current ball. Derivatives do not hit the current, and no pointwise fine-derivative estimate follows from this argument.

**Integration status: ready.** Together with the audited flat inverse, source-gauge scalar kernel, and local current vertex factorization, the note proves a uniform complex neighborhood for the fixed-flat auxiliary current family, an exact quadratic precision correction, factorial current derivatives, and anchored spatial-path locality. This remains an auxiliary homogeneous theorem; it is not the complete independent-current carrier or a nonflat Yang--Mills construction.
