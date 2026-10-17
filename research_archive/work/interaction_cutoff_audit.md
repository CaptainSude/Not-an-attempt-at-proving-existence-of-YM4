# Independent audit of the fixed-cell interaction extension

16 October 2026. Audited Sections 2--7 of `interaction_cutoff_research.md` against the Gaussian marked-cluster and support-algebra proofs. The mathematical argument passes under its stated hypotheses. One expectation-bracket typo in (4.4) was reported to the author and corrected: the exponential of the interaction sum belongs inside the expectation.

## 1. Physical-radius estimates

The order-three Schwarz bound is dimension-independent on the stated balanced physical-field ball. Restricting to the complex line through the given field and iterating the scalar Schwarz lemma proves it with precisely the displayed constant. The passage from the pointwise cubic estimate to the local quadratic envelope and the summable global envelope is valid.

The distinction between the cubic action remainder and the full fluctuation exponent is necessary. A merely linear Jacobian term cannot satisfy a purely quadratic pointwise bound near zero. The additive-constant envelope in Section 3 handles it. With R>=1 and gR<=1, the listed scales are all bounded by a fixed local constant times gR^3. These statements remain conditional on the localized primitive coefficient and response bounds explicitly listed in the note.

## 2. Gaussian domination and the tree bound

For the complex tree polydisc, delta=lambda/2 gives Herm M>=lambda/2 and ||M||<=2 Lambda_0. Thus Herm M^{-1}>=lambda/(8 Lambda_0^2)=1/V_*. The determinant bound produces exactly the density prefactor

    K_G=(2V_*/lambda)^(D/2)

per marked cell, relative to independent real Gaussians of covariance V_* I. Integrating the pointwise multiplier bound bad+v gives beta=K_G(p_R+v), with p_R=2^(D/2) exp[-R^2/(4V_*)]. All these constants are conservative and correct.

The local multipliers are held fixed while differentiating covariance interpolation parameters. Their fluctuation dependence is confined to one marked cell, so a block-diagonal covariance causes exact factorization over the marked components. Arbitrary background dependence does not obstruct this scalar factorization when that background is treated as a fixed parameter. Uniform holomorphy and the pointwise bounds justify integration and the final background-holomorphic activities.

The degree-adapted radius delta/[max(d_i,d_j)J_ij] bounds every row and column perturbation by delta. Its inverse-radius product is bounded by (e^2/delta)^(n-1) times the product of degree factorials and covariance edges. The stated tree identity and the conservative factor 8 then give (4.9). Spending alpha=2 yields the claimed weighted logarithm estimate 2e^2 beta under beta<=beta_*.

## 3. Interaction difference and Cauchy budget

Interpolating the bounded multiplier, rather than the exponent, is legitimate and gives the desired endpoints. Under the two quarter-budget assumptions, rho=beta_*/(2K_Gv)>=2 and the full polydisc parameter is at most 3beta_*/4. The canonical activity vector is therefore analytic with a common weighted norm bound M=2e^2 beta_*.

Cauchy gives ||U_n||<=M rho^(-n). Summing n>=1 gives M/(rho-1), and rho>=2 yields

    M/(rho-1) <= 2M/rho = 8e^2 K_G v.

There is no missing factorial, no division by a possibly small cutoff probability, and no branch mismatch: both logarithms are taken from the same convergent expansion. The background supremum can be included in the Banach norm because the common estimates are uniform over that domain. Absolute convergence of the forest and Mayer majorants establishes Banach-valued analyticity rather than merely pointwise analyticity.

## 4. Strict background support

Under the additional locality theorem hypotheses, the interaction part of q_i has background support {i}. For a marked set S containing i, its rooted attachment length is zero, so its support-algebra norm is at most v. The bad-cell term has empty background support. Consequently multiplication by the local interaction factors preserves the pointwise algebra norm bound by the product of bad+v.

The full marginal density is already expanded in the rooted support algebra. Its determinant and inverse majorant can therefore be multiplied by those factors before integration. Replacing the pure tail by widehat beta in (6.2) is correct. The remaining forest factorization remains an identity of the canonical source series. Compatibility is disjointness of marked sets, even if covariance perturbation terms have overlapping background supports.

The connected-hull regrouping is the same bounded linear map for every value of the multiplier interpolation parameter. Hence the interaction-difference estimate survives that regrouping with precisely the additional factor S_{kappa/2}. No separate unmarked source cluster appears: every interaction factor is attached to a nonempty mark by construction.

Section 6 must use the locality theorem's baseline constants, in particular delta=lambda/4, rather than silently retaining the larger delta from Section 4. The note explicitly says this, and its constants are consistent with that instruction. If the covariance and baseline estimates have been stated using different numerical lambda,Lambda_0 values, they must first be reconciled or renamed before applying the formulas.

## 5. Marks cannot be moved to unrelated supports

The strict-locality conclusion relies substantively on the assumption that V_i reads background in its own marked cell. A mark labels the fluctuation variables integrated in the marginal; it cannot simply be relocated to the support of an arbitrary background dependence.

There is an elementary obstruction to dropping this assumption. Take independent scalar Gaussians C=I on N cells, a common sharp cutoff, one background variable A_j in the unit disk, and V_i(A,x_i)=v A_j for every i. All fixed-cell interaction bounds and the mark-local theorem hold. Nevertheless

    log Z_V = N log P(|G|<=R) + N v A_j.

Any holomorphic strictly background-local representation must place all A_j dependence in activities whose support contains j. Evaluating at A_j=r and -r, then taking r upward to one, shows that their total supremum norm is at least N|v|. Thus no volume-independent support norm rooted at j is possible. This failure occurs even with diagonal covariance and arbitrarily small fixed v.

A limited extension is available without changing the fluctuation theorem: if V_i still depends only on fluctuation x_i but its background support is a specified finite set Y_i, one must pay the rooted attachment factor exp[kappa ell_{ {i} }(Y_i)] in its support-algebra norm. A uniform bound on v_i times that factor can replace v in the same proof. A uniformly bounded background collar is one such case. This is not a theorem for an interaction depending jointly on fluctuations in multiple cells; those factors destroy the single-cell forest factorization and remain outside the audited result.

## 6. Parameter order and scope

The larger logarithmic cutoff is compatible with a fixed physical-field analytic radius because gR^q tends to zero for every fixed finite q. The constants must be fixed before the final coupling ceiling is chosen. The note correctly does not deduce gR small from a bound involving the smaller auxiliary radius P, and does not confuse a global extensive analytic bound with a summable local coefficient norm.

The abstract fixed-cell module, including its interaction-difference and strict-support extensions, is proved by the displayed argument. Its application to the actual gauge model still requires the indicated primitive local holomorphy, response, covariance, domain and coordinate hypotheses. No full multi-cell interaction theorem was audited or inferred.
