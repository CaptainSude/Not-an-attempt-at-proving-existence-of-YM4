# Interactions at the enlarged cutoff: a proved fixed-cell module and the remaining multi-cell interface

Research note, 16 October 2026. This note separates elementary estimates proved here from source statements and from model interfaces that have not been independently closed. The deposited repository is read-only. No claim of a Yang--Mills construction or of a complete interacting cutoff-transfer theorem is made.

## 1. Conclusions and status

1. A uniformly bounded analytic function of the **physical field** `z=gB`, whose first three Taylor coefficients of degrees 0, 1 and 2 vanish, obeys a sharp cubic Schwarz bound. With an action prefactor `g^-2`, this gives both `O(g R |B|^2)` stability on `|B|<=R` and `O(gR^3)` cutoff sup norm. The constants must be local and summable before summing interaction labels.
2. The full fluctuation exponent `P^(k)` is not generally cubic in the fluctuation field. In the displayed deposited formula its change-of-variables Jacobian can start linearly in `gB`. A full-exponent bound by `C gR |B|^2` alone is therefore unjustified. The weaker local sup bound `O(gR^3)` still follows for `R>=1`, together with an additive-constant quadratic stability bound.
3. For interactions confined to **disjoint fixed-dimensional cells**, the Gaussian defect proof extends exactly. The small parameter is a Gaussian tail plus the uniform local interaction weight. It gives an analytic, exponentially mark-local logarithm and a quantitative `O(v)` bound on its difference from the pure Gaussian cutoff logarithm. Under the already stated small-local-precision hypotheses, the same argument gives strict background-local activities.
4. The deposit already contains the essential larger-radius calculation: raw II, `5.2:lem-complex-localisation`, proof Step 3, lines 11178--11195, uses `g(T^C)^3` for the cubic terms and `gT^C` for the merely vanishing terms. It then chooses the coupling ceiling after the activity target. This is a conditional source match, not an independently checked completion of the full argument.
5. Actual localized interactions can meet several, overlapping cells. The fixed-cell theorem does not cover this case. A naive regrouping into large disjoint blocks can lose summability through powers of block size at unrestricted branching vertices. The first remaining cluster interface is a verified use of the specialized CMP116 interaction resummation at the enlarged domain, or a new endpoint-level hypergraph estimate with explicit weighted local hypotheses.

## 2. A physical-field Schwarz lemma

Let `Y` be a finite collection of fluctuation coordinates, and let `A` denote allowed background variables. Write

\[
 \|z\|_{\infty,Y}=\max_{b\in Y}\|z_b\|,
 \qquad \|B\|_{2,Y}^2=\sum_{b\in Y}\|B_b\|^2.
\]

Assume `F_Y(A,z)` is holomorphic on the complex physical-field ball `||z||_infty,Y<r0`, uniformly on the specified background domain, and

\[
 \sup_{A,\|z\|_{\infty,Y}<r_0}|F_Y(A,z)|\le a_Y,
 \qquad D_z^jF_Y(A,0)=0\quad(j=0,1,2).                 \tag{2.1}
\]

Here the ball is balanced; a product of complex coordinate balls also suffices. Neither its radius nor `a_Y` is allowed to shrink or grow with the cutoff unless that dependence is explicitly accounted for.

**Lemma.** For `||z||_infty,Y<r0`,

\[
 |F_Y(A,z)|\le a_Y r_0^{-3}\|z\|_{\infty,Y}^3.         \tag{2.2}
\]

**Proof.** For `z!=0`, put `u=z/||z||_infty,Y`. The one-variable function `f(w)=F_Y(A,r0 w u)/a_Y` maps the unit disk to its closed unit disk and vanishes to order at least three at zero. Iterating Schwarz's lemma gives `|f(w)|<=|w|^3`. Limits cover non-strict bounds; `a_Y=0` is trivial. There is no dimension factor or combinatorial number of Taylor monomials. The same argument proves the order-`m` version. ∎

For real `B` with `||B||_infty,Y<=R` and `gR<r0`, define the scaled cubic action remainder

\[
 W_Y(A,B)=g^{-2}F_Y(A,gB).
\]

Then

\[
 |W_Y(A,B)|
 \le {a_Y\over r_0^3}g\|B\|_{\infty,Y}^3
 \le {a_Y\over r_0^3}gR\|B\|_{2,Y}^2,
 \qquad \|W_Y\|_{\mathrm{cutoff},\infty}
 \le {a_Y\over r_0^3}gR^3.                            \tag{2.3}
\]

If `sup_b sum_{Y contains b} a_Y <= a_*`, summing the first inequality gives

\[
 \sum_Y|W_Y(A,B)|
 \le {a_*\over r_0^3}gR\sum_b\|B_b\|^2.             \tag{2.4}
\]

Thus, against a real reference density with quadratic exponent at least `c||B||_2^2`, the cubic action is absorbable whenever `a_*gR/r0^3<c`. This is an absolute-value estimate, so it also bounds the modulus of a complex interaction factor. It does not identify the actual Yang--Mills covariance or its required complex domain.

More generally, a term `g^-r F_Y(gB)` vanishing to order `m` has cutoff norm at most `a_Y g^(m-r) R^m/r0^m`. A weighted local coefficient norm such as

\[
 \mathcal A_{a,\kappa}
 =\sup_b\sum_{Y\ni b}e^{a|Y|+\kappa\ell(Y)}a_Y<\infty \tag{2.5}
\]

therefore transfers to the identical weighted norm of cutoff sup bounds, multiplied by `g^(m-r)R^m/r0^m`. Merely having an extensive global analytic bound for the sum of the `F_Y` does not imply (2.5).

If the physical argument is `gCB`, or is an analytic nonlinear response to `gB`, one must also supply uniform response bounds and a local support expansion. The statement is not obtained by renaming that argument `gB`. A fixed operator bound may be incorporated in `r0`; a nonlocal response requires its own localization estimate.

## 3. Why the entire fluctuation exponent is not cubic

The exact displayed exponent in raw II, `8.2:eq-small-field-step-3`, around lines 73910--73940, includes the following types. The table records the scaling in the physical argument `z=gCB` schematically; a uniformly bounded response operator is understood only where explicitly supplied.

| Term | Prefactor | First possible physical-field order | Cutoff scale |
|---|---:|---:|---:|
| Change-of-variables `Tr log(I-h D Dtilde)` | 1 | 1 | `gR` |
| Haar log density | 1 | 2 | `g^2 R^2` |
| Current paired with cubic `Dtilde_3` | `g^-2` | 3 | `gR^3` |
| Gauge-fixing cubic remainder `G_3` | `g^-2` | 3 | `gR^3` |
| Cross term between `z` and `Dtilde(z)` | `g^-2` | 3 | `gR^3` |
| Quadratic term in `Dtilde(z)` | `g^-2` | 4 | `g^2R^4` |
| Curvature-action remainder | `g^-2` | 3 | `gR^3` |

This uses the specified quadratic start of `Dtilde` and cubic start of the action remainder; it is not a proof of all needed coefficient bounds. Prior effective-action increments are separate terms and need their own induction norm and vanishing estimates.

For `R>=1` and `gR<=1`, every displayed cutoff scale is at most a constant times `gR^3`. Hence uniform localized coefficient estimates imply, for a fixed cell or local label,

\[
 \sup_{\mathrm{cutoff}}|V_Y|\le C_YgR^3.              \tag{3.1}
\]

However, a term with nonzero linear Taylor coefficient cannot obey `|V_Y(B)|<=C gR||B||^2` as `B` tends to zero. A safe local quadratic envelope has an additive constant. For example, the linear term satisfies

\[
 C_Yg\|B\|\le {C_Yg\over2}(1+\|B\|^2),
\]

and, after combining the orders above on the cutoff, one may use

\[
 |V_Y(B)|\le \widetilde C_Yg(1+R)(1+\|B\|_{2,Y}^2), \tag{3.2}
\]

with the localized constants summable. Constants per local label are not a single volume-independent constant after summing all labels. Possible odd cancellations under a Gaussian expectation do not repair a false pointwise quadratic bound.

If `u_Y=sup_cutoff |V_Y|<=1`, then

\[
 v_Y:=\sup_{\mathrm{cutoff}}|e^{V_Y}-1|
 \le e^{u_Y}-1\le 2u_Y.                              \tag{3.3}
\]

Thus the cubic estimate supplies the interaction parameter used next.

## 4. Exact theorem for disjoint fixed-dimensional cells

Let the cells form a finite set `Lambda` in a lattice. Each cell carries `D` real fluctuation coordinates, with `D` fixed. A cell can contain several original lattice variables, but its size and the induced metric constants must be uniformly bounded.

Use exactly the covariance assumptions of `gaussian_cutoff_cluster_research.md`:

\[
 C(A)^T=C(A),\qquad \operatorname{Herm}C(A)\ge\lambda I,
 \qquad\|C(A)\|\le\Lambda_0,
\]
\[
 \|C_{ij}(A)\|\le J_{ij}=J_{ji},\qquad
 A_\kappa=\sup_i\sum_{j\ne i}e^{\kappa d(i,j)}J_{ij}<\infty.
                                                               \tag{4.1}
\]

The covariance is holomorphic in the complex background on a fixed domain. The normalized complex Gaussian density uses the analytic square-root determinant branch on the accretive cone. Let

\[
 \chi_i(x_i)=\mathbf1_{\{\|x_i\|_2\le R\}}.
\]

Suppose `V_i(A,x_i)` depends on the fluctuation in its own cell only, is measurable in real `x_i`, and is holomorphic in the allowed background for every real `x_i` on the cutoff. Assume uniformly

\[
 \sup_{A,\|x_i\|\le R}|e^{V_i(A,x_i)}-1|\le v.
                                                               \tag{4.2}
\]

For strict background locality below, require additionally that `V_i` reads only the background in its own cell. The mark-local statement itself needs only uniform holomorphy, not local background dependence.

Define whole-real-space multipliers

\[
 q_i(A,x_i)=\chi_i(x_i)e^{V_i(A,x_i)}-1
 =-\mathbf1_{\{\|x_i\|>R\}}+
       \chi_i(x_i)(e^{V_i(A,x_i)}-1).                 \tag{4.3}
\]

The values of `V_i` outside the cutoff are never needed; (4.3) defines `q_i=-1` there. In particular,

\[
 |q_i(A,x_i)|\le\mathbf1_{\{\|x_i\|>R\}}+v,
\]
\[
 Z_V(A)=\mathbb E_{C(A)}\prod_i(1+q_i)
 =\mathbb E_{C(A)}\left[\left(\prod_i\chi_i\right)
                                      e^{\sum_iV_i}\right]. \tag{4.4}
\]

Set

\[
 \delta=\lambda/2,\quad V_*=8\Lambda_0^2/\lambda,\quad
 K_G=(2V_*/\lambda)^{D/2},\quad
 p_R=2^{D/2}e^{-R^2/(4V_*)},
\]
\[
 \beta=K_G(p_R+v),\qquad
 B_0=8e^2A_\kappa/\delta,\qquad
 \beta_*={1\over2e^2\max(1,B_0)}.                   \tag{4.5}
\]

**Theorem.** If `beta<=beta_*`, the normalized integral has a convergent logarithm

\[
 \log Z_V(A)=\sum_{X\ne\varnothing}U_V(X;A),
\]

holomorphic in the background, with the branch defined by the convergent polymer expansion, and

\[
 \sup_i\sum_{X\ni i}e^{\kappa\ell(X)+|X|}
                              \|U_V(X;\cdot)\|_\infty\le2e^2\beta. \tag{4.6}
\]

The constants are volume-independent. `X` in this theorem is a set of marked cells; background locality requires the additional hypotheses in Section 6.

### Proof: density domination, forest factorization and the logarithm

At a BKAR partition-mask interpolation, every covariance is a convex combination of block-diagonal principal submatrices and still obeys (4.1). A perturbation of operator norm at most `delta` therefore has

\[
 \operatorname{Herm}M\ge\lambda I/2,
 \quad\|M\|\le2\Lambda_0,
 \quad\operatorname{Herm}M^{-1}\ge V_*^{-1}I,
 \quad |\det M|\ge(\lambda/2)^{D|S|}.
\]

Its density modulus is bounded by `K_G^|S|` times the density of independent real cell Gaussians of covariance `V_* I`. Consequently, for every marked set `S`,

\[
 \left|\int p_M(x_S)\prod_{i\in S}q_i(A,x_i)\,dx_S\right|
 \le K_G^{|S|}\prod_{i\in S}
       \mathbb E_{V_*I}\bigl[\mathbf1_{\{\|G_i\|>R\}}+v\bigr]
 \le\beta^{|S|}.                                    \tag{4.7}
\]

The single-cell tail estimate uses exponential Markov with parameter `1/(4V_*)`, giving `P(||G_i||>R)<=p_R`. Uniform Gaussian domination also proves holomorphy of these integrals in `A`. Sharp indicators remain fixed; no derivative is taken of them or of the possibly nonsmooth real-field multiplier.

For a tree `T` on `n>=2` marked cells, write `d_i` for the degrees and permit independent complex changes in the covariance edge parameters of radii

\[
 r_{ij}={\delta\over\max(d_i,d_j)J_{ij}}.
\]

Every resulting block row and column perturbation has sum at most `delta`, so (4.7) holds on the full product polydisc. Cauchy and `d^d<=e^d d!` give

\[
 |\partial_T f_S|
 \le\beta^n(e^2/\delta)^{n-1}
                         \prod_i d_i!\prod_{ij\in T}J_{ij}. \tag{4.8}
\]

The multipliers `q_i` do not depend on the covariance interpolation parameters. Once a forest mask disconnects its covariance into blocks, the product of the cell-local multipliers factorizes over exactly the same components. BKAR therefore gives exact cumulant activities

\[
 \zeta(S)=\sum_{T\text{ tree on }S}\int\partial_T f_S(s^T(t))\,dt
\]

for nonsingletons, with the usual singleton moment. Expanding the product in (4.4) yields a hard-core gas of disjoint marked sets, exactly as in the Gaussian-only proof.

The degree count is

\[
 \sum_{T\text{ on }[n]}\prod_i d_i!
 =(n-2)!\binom{3n-3}{n-2},\qquad
 {1\over(n-1)!}\sum_T\prod_i d_i!\le8^{n-1}.
\]

Leaf sums of the weighted edges in (4.8) now imply

\[
 \sup_i\sum_{S\ni i}\|\zeta(S)\|_\infty e^{\kappa\ell(S)+\alpha|S|}
 \le {\beta e^\alpha\over1-B_0\beta e^\alpha}.        \tag{4.9}
\]

With `alpha=2`, the Kotecky--Preiss criterion for weighted activities `|zeta(S)|exp(kappa ell(S)+|S|)` and size function `|S|` holds under (4.5). The rooted Mayer estimate, grouped by the union `X` of the overlapping marked polymers, proves (4.6). This is the same exact forest and logarithm argument, with the single replacement of the Gaussian tail parameter by `K_G(p_R+v)`. ∎

## 5. Quantitative stability relative to the Gaussian cutoff logarithm

The previous theorem gives total smallness `O(tail+v)`. It also gives a genuine Lipschitz comparison `O(v)` without dividing by an uncontrolled Gaussian cutoff probability.

Let `tau=K_G p_R`. Suppose

\[
 \tau\le\beta_*/4,\qquad K_Gv\le\beta_*/4.           \tag{5.1}
\]

For complex `t`, interpolate the **bounded local multipliers**, not the exponent:

\[
 q_i(t)=-\mathbf1_{\mathrm{bad},i}
                  +t\chi_i(e^{V_i}-1).
\]

At `t=0` the partition function is the pure Gaussian cutoff probability; at `t=1` it is `Z_V`. For `v>0` put

\[
 \rho={\beta_*\over2K_Gv}\ge2.
\]

On `|t|<=rho`, the parameter is at most `tau+rho K_Gv<=3beta_*/4`. Thus the canonical mark-local activity vector `U(t)` is analytic in this disk, with weighted rooted norm at most `M=2e^2 beta_*`. Banach-valued Cauchy estimates give coefficient bounds `||U_n||<=M rho^-n`. It follows that

\[
 \boxed{\quad
 \sup_i\sum_{X\ni i}e^{\kappa\ell(X)+|X|}
             \|U_V(X)-U_0(X)\|_\infty
 \le {M\over\rho-1}
 \le 8e^2K_Gv.\quad}                               \tag{5.2}
\]

Here `U_0` is the canonical pure-cutoff activity representation coming from the same forest and Mayer expansion. The case `v=0` is immediate. The logarithms in this comparison use the convergent expansion's branches. This proves the desired interaction correction estimate for disjoint cells, including complex backgrounds.

The proof can be stated in the Banach space of bounded holomorphic activities, taking the background supremum in the norm. Local uniform convergence on background subdomains gives the same conclusion if an open domain has no attained boundary supremum.

## 6. Compatibility with the strict-background-locality expansion

Assume, in addition, **all** hypotheses and smallness conditions of `gaussian_cutoff_locality_research.md`: a fixed background-independent gapped baseline, the small weighted decomposition of the precision into locally background-dependent terms, the product background domain, and its fixed constants. Also require `V_i` to read only background coordinates in cell `i` and to satisfy (4.2) there.

For a marked set `S`, the additional multiplier `chi_i(e^{V_i}-1)` is an element of the rooted support algebra `B_S`, supported on `{i}`. Since `i` is already a root, its support length is zero and its algebra norm is at most `v`. The defect multiplier is background-independent. Therefore the full multiplier product has algebra norm bounded pointwise by

\[
 \prod_{i\in S}(\mathbf1_{\mathrm{bad},i}+v).
\]

The already derived marginal-density majorant in that algebra is

\[
 \|p_M(x_S)\|_{\mathcal B_S}
 \le\widehat K_G^{|S|}p_{2V_*I}(x_S),\qquad
 \widehat K_G=(8V_*/\lambda)^{D/2}.                  \tag{6.1}
\]

Thus replace its previous tail parameter by

\[
 \widehat\beta=
 \widehat K_G\left(2^{D/2}e^{-R^2/(8V_*)}+v\right). \tag{6.2}
\]

All further arguments in the support algebra are unchanged: covariance-forest factorization is still an identity in the formal local source variables; multiplication of the local interaction factors is compatible with it; no source component unconnected to a nonempty mark can occur. Mark-set compatibility remains disjointness of the **marks**, not of the enlarged background supports.

Use the locality note's constants here, in particular its `delta=lambda/4`, edge majorant, `B0`, and smallness ceiling `widehat beta<=[2e^2 max(1,B0)]^-1`. Its connected-hull construction then gives exact activities `E_{Lambda,H}(A|H)` with

\[
 \sup_b\sum_{H\ni b}e^{a_*|H|}\|E_{\Lambda,H}\|_\infty
 \le2e^2 S_{\kappa/2}\widehat\beta,
\]
\[
 a_*=\min(1/2,\kappa/4),\qquad
 S_{\kappa/2}=\sum_{z\in\mathbb Z^d}e^{-(\kappa/2)|z|}. \tag{6.3}
\]

The same interpolation as Section 5 proves an interaction-difference norm bounded by `8e^2 S_{kappa/2} widehat K_G v`, under the corresponding quarter-budget hypotheses. This is a proved extension of that abstract theorem, conditional on its hypotheses. It is not verification of those hypotheses for the gauge measure.

All earlier scope caveats remain: the finite-volume coefficient can depend on the whole background-independent baseline `C_{0,Lambda}`; variable background locality does not imply consistency between volumes. The product background domain is a substantive assumption, and symmetry of each chosen activity is not automatic from an asymmetric hull convention.

## 7. Parameter order with distinct radii

Put

\[
 L_g=\log g^{-2},\qquad R(g)=A_1L_g^{p_0},\qquad
 P(g)=C_1L_g^{p_1},\qquad p_1<p_0.
\]

For every fixed finite `q`,

\[
 gR(g)^q=A_1^q e^{-L_g/2}L_g^{qp_0}\longrightarrow0.
                                                               \tag{7.1}
\]

If the primitive local coefficients and covariance constants are fixed first, (2.3), (3.3) and the fixed-cell theorem give a correction of order `gR^3`, hence `g(log g^-2)^(3p0)`. One may choose the coupling ceiling `gamma=gamma(epsilon)` afterwards so that simultaneously `gR<r0`, `gR<=1`, the cluster budget holds, and this correction is at most any prescribed `epsilon`. To make the ceiling uniform for every `0<g<=gamma`, note that `e^-L/2 L^s` is decreasing once `L>2s`; alternatively use its eventual supremum directly.

When `p0>1/2`, the Gaussian tail is smaller than any prescribed fixed `g L_g^q` scale for sufficiently small `g`:

\[
 \log\left({K e^{-cA_1^2L_g^{2p_0}}\over gL_g^q}\right)
 =\log K-cA_1^2L_g^{2p_0}+L_g/2-q\log L_g\to-\infty.
\]

The fixed constant in an `O(gR^3)` inequality is independent of a later target `epsilon`; the ceiling enforcing an absolute `epsilon` budget can depend on it. These are different claims.

Nothing here requires `R<=P`, and in fact `R/P` diverges. A hypothesis such as `gP<=epsilon1` does **not** by itself imply `gR<=epsilon1`. A physical holomorphy domain of fixed radius permits the larger `R`, but the separate ceiling `gR<r0` must be checked. If the only available analytic domain were the unscaled fluctuation domain `|B|<P(g)`, the Schwarz argument would not extend it to `R(g)`.

## 8. Source map: what is present, and what remains conditional

The primary-source descriptions in this section are deliberately narrow. Precise local constants and norms must be read from the original formulas, not reconstructed from imperfect text extraction.

**CMP109.** Pages 266--270 separate the pure-action linear cancellation, the order-zero quadratic Gaussian part and higher action terms. The resulting `P^(k)` also includes the change-of-variables and Haar logarithms. Section 3 states analyticity and the localization program for the full fluctuation potential. This supports separating cubic action remainders from the entire exponent. [Primary PDF](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf).

**CMP116.** Pages 10--11, formulas (1.37)--(1.40) and Lemma 2, localize a representative cubic contribution and express the potential as a field-dependent quadratic form plus a bounded remainder. The dependence relevant here is in the physical fluctuation variable. Pages 16--17 use a separate conditional Gaussian/quadratic-form argument and resummation for the interaction; that argument is not replaced by the elementary fixed-cell theorem above. [Primary PDF](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf).

**Deposited algebra and local statements.** At pinned commit `e392ef45013a581664bab76b90867170b30fe10e`, the following locations are useful:

| File/location | Relevant content | Status for the present task |
|---|---|---|
| raw I, `4.5:def-higher-order-functional`, around 14156--14200 | Explicit cubic higher-order functional, with `D` quadratic and `D3` cubic; subsequent gradient bound has a fixed analytic field radius. | Algebra supports the cancellation order. Weighted norm and response/localization bounds remain separate. |
| raw I, `4.7:prf-unit-share`, around 30480--30770 | Inventory of unit localization bounds and their induction weights. | Provides a proposed source of local summable coefficients; not replaced by a global analytic bound. |
| raw I, `4.17:thm-transfer-seam`, around 53410 | Transfers interior CMP116 inputs and treats boundary-crossing CMP119 domains separately. | Requires its geometry, domain and residual hypotheses. Whole-lattice interior terms must not be assigned a boundary-only domain without justification. |
| raw II, `5.2:lem-fluctuation-potential`, around 3160--3210 | Physical variable `mathsf A=gB`, cubic quadratic-kernel pieces and bounded pieces vanishing at zero. | Matches the split used above, with histories and local norms still part of the hypotheses. |
| raw II, `5.2:lem-complex-fluctuation`, around 3530 onward | Proposed complex fluctuation integration under localized potential and domain hypotheses. | A candidate source for the multi-cell interaction module; its hypotheses at the modified cutoff need independent matching. |
| raw II, `5.2:lem-complex-localisation`, around 10944--11220 | Locality, complex domain `|mathsf B|<T^C`, weighted potential bound, and conditional history decomposition. | Already contains the larger-log-radius estimate; does not remove the need to audit its imported domain and local norm inputs. |
| raw II, `8.2:eq-small-field-step-3`, around 73910--73940 | Exact displayed exponent with Jacobian, Haar, current, gauge-fixing, action terms and previous effective-action increment. | Shows why full `P^(k)` need not be cubic. |
| raw II, `8.2:lem-box-exponent`, around 74700 onward | Assumes a uniform tube bound for localized terms and includes a coupling-flow hypothesis. | Cannot be used as an independent proof of the same coupling-flow input it assumes. |

Most directly, `5.2:lem-complex-localisation`, proof Step 3, states the cubic-piece estimate

\[
 C(M,\kappa_1)g_k(T^{\mathbb C})^3e^{-\kappa_Vd_k(Y)},
\]

uses vanishing plus physical-domain analyticity to bound the other pieces by `2g_kT^C/epsilon1` times their inherited bound, and bounds the quadratic gauge term by `C L^4 r(C1g_kT^C)^2`. It observes that these tend to zero with the coupling ceiling because `T^C` is a fixed polynomial of `log g_k^-2`. Step 4 chooses that ceiling after the activity target.

The domain calculation is not an assertion that `T^C` fits inside a smaller logarithmic radius. Its first step defines

\[
 \theta_k^{\mathbb C}=K_Rg_kT^{\mathbb C}/\alpha_{*,k},
 \qquad \mathsf w^{\mathbb C}=1/\theta_k^{\mathbb C}-1,
\]

so that `(1+mathsf w^C)K_Rg_kT^C=alpha_{*,k}`, then invokes physical response containment. This is the appropriate kind of interface. It still requires verifying the response theorem, its complex background chart, its admissible histories and the local coefficient estimates without circular use of the desired closure statement.

The first independently unverified source package is therefore concrete: the localized primitive terms and responses must obey fixed physical-field holomorphy and summable bounds on the exact complex domains used by the modified-cutoff integration, uniformly in scale and admitted history. Once that package is supplied, the one-variable Taylor estimate is elementary. For genuine multi-cell potentials a second, separate package is the interacting Gaussian resummation described next.

## 9. Multi-cell interactions: exact rewriting, but no claimed cluster theorem

Let the actual potential be `sum_Y V_Y(A,B_Y)`, where the finite sets `Y` may overlap and have unbounded size. Suppose each term is defined and bounded when all its cells are inside the cutoff. Define

\[
 \chi_Y=\prod_{i\in Y}\chi_i,\qquad
 w_Y(A,B_Y)=\chi_Y(e^{V_Y(A,B_Y)}-1),
\]

setting it equal to zero elsewhere. Then the exact identity is

\[
 \left(\prod_{i\in\Lambda}\chi_i\right)e^{\sum_YV_Y}
 =\left(\prod_{i\in\Lambda}\chi_i\right)
                                      \prod_Y(1+w_Y). \tag{9.1}
\]

If some cell is outside its cutoff both sides vanish; if every cell is inside, every `chi_Y=1` and the identity reduces to the product of exponentials. Moreover,

\[
 \|w_Y\|_\infty\le e^{u_Y}-1,
 \qquad u_Y=\sup_{\mathrm{cutoff}}|V_Y|.              \tag{9.2}
\]

The real integration domain is fixed, and the extension remains holomorphic in background variables under the stated local bounds. Expanding the first factor of (9.1) into defect marks gives an additional useful exact cancellation: a bad mark in `Y` annihilates any product containing `w_Y`.

These facts do **not** reduce (9.1) to Section 4. Interaction factors join several Gaussian blocks. Forest factorization across a partition is false unless every chosen interaction hyperedge lies inside a partition component. One must first account for this hypergraph connectivity, including overlap families and the powers paid for their support sizes.

In particular, grouping an overlapping family into a disjoint molecule `S` creates a variable-dimensional Gaussian block of size `D|S|`. A crude covariance-edge norm bound is a sum over endpoints and can contribute a factor `|S|` for every edge incident on that molecule. A vertex of degree `d` may therefore cost `|S|^d`. The degree-adapted Cauchy estimate already carries `d!`, which can cancel the child-label factorial in the tree enumeration. There is no resulting general bound by `C^|S|` from a single factor `e^-a|S|` when `d` is unrestricted. Merely declaring the new molecules to be blocks does not prove a convergent expansion.

A plausible primitive hypothesis is the small weighted norm

\[
 \sup_i\sum_{Y\ni i}e^{a|Y|+\kappa\ell(Y)}
                                     (e^{u_Y}-1)\ll1, \tag{9.3}
\]

with enough reserve to pay the complex-density dimensional prefactor. But this note does not prove that (9.3), covariance accretivity and exponential decay alone suffice through the proposed molecule-BKAR construction. A valid proof would need, for example, an endpoint-level forest allocation controlling degrees at individual fixed cells, or the stronger analytic derivative estimates used in an interaction-specific constructive expansion.

For the deposited Yang--Mills problem, the precise next target is to verify the CMP116 interaction integration/resummation, including its complex Gaussian operator and determinant estimates, with localized coefficients bounded on the enlarged `T^C` domain and the correct history norm. It is legitimate to use that specialized theorem if its hypotheses match; it is not legitimate to infer this match from the fixed-cell result or from `R/P` notation.

## 10. What this closes

The physical-radius issue is resolvable without forcing the auxiliary logarithmic radius to contain the cutoff. A uniform fixed physical-field analytic domain and the actual Taylor cancellations give the desired `gR^q` smallness, with the coupling ceiling chosen last. This conclusion is already reflected in a specific deposited proof step.

There is also a complete joint Gaussian-plus-interaction theorem for disjoint fixed-dimensional cells, including a quantitative analytic comparison of logarithms and compatibility with the small-local-precision background-locality mechanism. The full Yang--Mills multi-cell interaction remains outside that theorem; its next required estimate and the failure of a naive large-block extension are explicit above.
