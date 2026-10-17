# Contractive high-jet differences for the actual common-domain quantum step

17 October 2026. Research proof, for independent audit. This combines the actual common-domain macrostep with the coefficientwise fifth-order background estimate. The result is a Lipschitz estimate for two admissible inputs with the same coefficientwise jets through degree four. It is not an invariant-fiber theorem or a completed quantum induction.

All identities are finite compatible-regulator identities or the specified local holomorphic continuations of those germs. Constants are uniform in preceding homogeneous depth M and volume once the finite primitive, macro and grouping parameters have been fixed.

## 1. The inputs and the canonical output map

Use the same input and output J-cell graphs, scalar-coordinate radius b, and connected-carrier exponent a0=1/16 as in common_domain_macrostep_research.md. Fix a common activity index set H; missing activities in either input are padded by zero. Let

    E_j=sum_H E_(j,H),   ||E_j||_(a0;b)<=epsilon_bar,
    D=E_1-E_2,   D_H=E_(1,H)-E_(2,H),                    (1.1)

with each total E_j locally gauge invariant on its common original domain and using the stipulated logarithm branch. Assume

    D^n D_H(0)=0 for every H and n=0,1,2,3,4.            (1.2)

These are full total-degree tensors in all field coordinates of H, including mixed derivatives. Equal low jets of the summed extensive functional would not suffice.

The two exact macrostep integrals use the same classical action, physical stationary background, retained chart, covariance, cutoff, local measure factors and normalizations. In particular the precision is the exact classical action-plus-gauge Hessian; it is not shifted to an E-dependent quantum saddle.

We specify a compatible coefficient-valued output map

    F(E)=T E + Delta + Qdet + L(Q_E),                    (1.3)

where:

* T E is the connected core/tail family for E(a_p(w));
* Delta and Qdet are the fixed pivot and Gaussian determinant families;
* Q_E is the canonical joint family for E(f_1(w,xi))-E(a_p(w));
* L(Q_E) is the canonical strictly local Gaussian logarithm with exponent V_base+Q_E and the fixed precision.

Its scalar sum is exactly the correction E_next of the common-domain theorem, with that theorem's germ/orbit-density qualifications. The coefficient choices in (1.3) are fixed as follows; a claim about arbitrary decompositions of the same scalar functional is not made.

## 2. Compatibility of the support assignments

Choose one primitive reserve A_in large enough for the stronger inherited Gaussian exponent B=53/8 and tail exponent8. Let C_A,kappa0,r_A be its pre-gauge constants, fixed at the primitive ratio before R. Use one and the same supported family

    a_(p,i)(w)=sum_X a_(i;X)(w_X),   a_(i;X)(0)=0,        (2.1)

with its complete output-fiber maximum inside the support sum.

The actual fluctuation construction has

    f_lambda,i(w,xi)=sum_X [
          a_(i;X)(w_X)+d_(lambda;i;X)(w_X,xi|N(i))],
    d_(0;i;X)=0 termwise.                               (2.2)

Fix a common sufficiently large J, one support cutoff ell_tail, the same core criterion X subset B_(ell_tail)(i), the same enlarged core carrier K0(H)=N_(infinity,2)(pi_R H), and deterministic joining trees and carrier grouping. These choices can meet the stronger joint fluctuation budgets and therefore the weaker background budgets simultaneously. The core carrier is retained even where some of its sites are not read.

At fluctuation lambda=0, (2.2) is exactly (2.1), coefficient by coefficient, and its core and tail are independent of xi. The core/tail Taylor series of E_H is therefore the same series as in the background transport theorem at field-scaling parameter mu=1:

    U^fluct_(K,0)[E] = U^field_(K,1)[E] = (T E)_K.       (2.3)

There is no equality here inferred only after summing K. The two constructions use identical local coefficient functions, local multiindices, support occurrences and deterministic trees. Their proofs can use different target weights without changing these assignments.

For the high-jet proof, impose the additional final-radius condition

    L_H=R/(8 C_A)>=2,   b L_H<=r_A.                      (2.4)

Then a_p(mu w) has absolute family norm at most b/8 on |mu|<L_H. The shared core/tail split gives the background theorem's uniform family bound with the same halo constants. Its stronger joint counterpart uses b/4; the weaker background bound causes no conflict.

The maps E -> U_lambda[E], T and Q_E are linear in the input coefficient family. Taylor differentiation of E_H, multiplication by the fixed core/tail functions and grouping supports are all linear operations. In particular

    Q_(E1)-Q_(E2)=Q_D                                 (2.5)

as joint coefficient families, not merely as total functions.

For the Gaussian logarithm, retain all possible interaction carrier labels, including zero ones, rather than deleting them depending on E. Use the same deterministic forest/hull assignments, the same precision expansion, and the same convergent cluster-log branch. This defines L as one analytic coefficient-valued map on the common interaction neighborhood. The two endpoint families in (1.3) are evaluations of this one map.

## 3. The background difference is small in the same family norm

Apply high_jet_background_transport_research.md with the common choices above. For completeness, an individual core/tail summand of tail degree n contains D^n D_H(c_mu) and n tail factors. If n<=4, the first factor vanishes to degree at least 5-n in mu and the tails supply n powers. If n>=5, the tails themselves supply five powers. Thus each canonical carrier has a fifth-order zero, without cancellation between carriers.

The background core/tail bound on the field-scaling disk is

    ||U^field_mu[D]||_(a0;b)<=C0 R^d ||D||_(a0;b),
    C0=exp[a0 5^d 2^d+2d] S1,                           (3.1)

where S1=sum_(z in Z^d) exp(-|z|_1). Banach Schwarz at mu=1 gives, in dimension d=4,

    ||T D||_(a0;b) <= (C_H/R)||D||_(a0;b),
    C_H=C0(8 C_A)^5.                                    (3.2)

C_H is fixed before R, since the reserve A_in was fixed before R. In particular the J-dependent tail estimates have not reappeared in C_H. Equation (2.3) is what makes (3.2) apply to the background term of the actual output family (1.3).

## 4. The inherited fluctuation map is linear and bounded

Let the common-domain theorem's constants be fixed and put

    a_Q=16 C_T C_R gT/b,
    C_T=exp[B 5^d 2^d+2d] R^d S1.                       (4.1)

Here T is the actual retained link/color-ball threshold, not the background transport operator. The canonical joint-family estimate and (2.5) give

    ||Q_E||_B<=a_Q ||E||_(a0;b),
    ||Q_D||_B<=a_Q ||D||_(a0;b).                         (4.2)

This estimate does not require high-jet vanishing. It uses the actual pre-gauge field in the old radius-b domain and the fluctuation-scaling Cauchy disk. The additional zeros of D are used only in the background estimate.

Delta and Qdet in (1.3) are independent of E and cancel coefficientwise. The base exponent and precision also remain fixed. Therefore

    F(E1)-F(E2)
       =T D + L(Q_E2+Q_D)-L(Q_E2).                      (4.3)

## 5. A uniform Gaussian-log difference with the base retained

Let eta_*<=1 be the common positive threshold of the tunable strictly local Gaussian theorem. Let v bound the base exponent family in the stronger B norm. Strengthen the already allowed small-coupling budgets to

    v<=eta_*/(64e),
    a_Q epsilon_bar<=eta_*/(128e),
    e^3 tau(T)<=eta_*/4.                                 (5.1)

All precision/support-algebra conditions are unchanged. They were met by the final choice of b, independently of E.

If D=0, the difference is zero. Otherwise set

    q_D=a_Q ||D||_(a0;b),
    L_D=eta_*/(32e q_D).                                 (5.2)

Since ||D||<=2 epsilon_bar, (5.1) gives q_D<=eta_*/(64e) and L_D>=2. Interpolate only the inherited exponent:

    zeta -> L(Q_E2+zeta Q_D),       |zeta|<L_D.           (5.3)

It is unnecessary that E2+zeta D remain in the original bounded input class on this larger disk. The Gaussian theorem applies directly because its actual exponent norms obey

    ||V_base+Q_E2+zeta Q_D||_B
      <= (1/64+1/128+1/32)eta_*/e
       =7 eta_*/(128e)<eta_*/(8e).                      (5.4)

Equal-carrier exponentiation has multiplier norm at most exp(x)x with x the left side. As eta_*<=1, it is at most eta_*/8. Together with the tail quarter budget, the Gaussian connected-log norm is at most S1 eta_* on the whole disk. The same canonical coefficient family is holomorphic there, its precision does not move, and the cluster theorem fixes a common nonvanishing logarithm branch.

Apply Banach Cauchy with the contour integral before the anchored sum. Taking the difference at zeta=1 and zeta=0 gives

    ||L(Q_E1)-L(Q_E2)||_(a_G;b)
       <= S1 eta_*/(L_D-1)
       <=64e S1 q_D,
    a_G=1/2.                                            (5.5)

Since a_G>=a0, this also bounds the a0 norm. Substituting (4.1),

    ||L(Q_E1)-L(Q_E2)||_(a0;b)
       <= C_quant (gT/b)||D||_(a0;b),
    C_quant=1024e S1 C_T C_R.                            (5.6)

This proof retains both the original base exponent and Q_E2. It does not replace their exponential factor by one in a multiplier difference. It is valid for the actual canonical output log family, not merely a difference of extensive scalar logarithms. No endpoint branch ambiguity remains because both endpoints are evaluated in the same normally convergent analytic cluster expansion on (5.3).

## 6. The Lipschitz statement and the projected contraction

Combining (3.2), (4.3) and (5.6) proves

    ||F(E1)-F(E2)||_(a0;b)
       <= [C_H/R+C_quant gT/b] ||E1-E2||_(a0;b).         (6.1)

This is an estimate for the full compatible output families, despite the fact that their difference may acquire low field jets.

For the output coefficient family define the total-degree remainder by the dimension-free phase projections

    (P_n F_K)(w)=(1/(2pi)) integral_0^(2pi)
                      exp(-int) F_K(exp(it)w) dt,
    R_(>=5) F_K=F_K-sum_(n=0)^4 P_n F_K.                (6.2)

The circular product ball is unchanged, supports remain K, and each P_n has operator norm at most one. Thus

    ||R_(>=5)[F(E1)-F(E2)]||_(a0;b)
       <=6[C_H/R+C_quant gT/b]||D||_(a0;b).             (6.3)

To obtain a concrete factor one-half, choose a sufficiently large R=ell^s with

    R>=24 C_H,                                         (6.4)

in addition to the common-domain compression and amplitude requirements. Then choose common J and ell_tail satisfying both stronger joint and weaker background budgets. Choose the one final b also satisfying (2.4), all classical and theta-neighborhood bounds, and finally choose g and T(g) so that (5.1) and

    C_quant gT/b<=1/24                                  (6.5)

hold. T(g) may grow like a fixed multiple of sqrt(log(1/g)); all constants in (6.5) are fixed before g. This gives

    ||F(E1)-F(E2)||_(a0;b)<= (1/12)||D||_(a0;b),
    ||R_(>=5)[F(E1)-F(E2)]||_(a0;b)
                                      <= (1/2)||D||_(a0;b). (6.6)

The parameter order is noncircular and uniform in M and compatible volume. The same b is used at input and output. The numerical constants are deliberately conservative.

The map (1.3) uses a fixed common field-independent normalization. If each output is subsequently vacuum-normalized by subtracting every coefficient's value at zero, the unprojected difference estimate can cost another factor two. The projected estimate (6.3) is unchanged, because R_(>=5) already annihilates those constants.

## 7. Exact scope

The scalar sums in (4.3) are differences of the actual common-domain small-field quantum map, with its established analytic-germ or gauge-orbit density interpretation. The proof does not apply a rooted/pre-gauge equality separately to a nongauge-invariant extraction of either E_j. It first compares two admissible complete inputs; D is their coefficientwise difference, and all subsequent operator estimates refer to that exact difference.

The input equal-low-jet condition is coefficientwise and representation-sensitive. We have proved the existence of the explicit compatible canonical output families above with the stated norm bound, not a bound for every arbitrary localization of the same scalar output.

The full output difference can regenerate jets of degrees zero through four through the fluctuation integral. Thus F does not preserve the affine subspace of inputs with a prescribed set of low jets. Projecting the high-degree output is a bounded analytic operation but is not automatically gauge invariant; gauge transformations are nonlinear in potential coordinates. No gauge-invariant low-jet extraction, closed relevant/marginal flow, or invariant high-jet fiber has been constructed.

The estimate is therefore a genuine contractive response of the actual finite quantum step in equal-low-jet input directions, and a contraction after projecting its output to high field degree. It does not by itself supply a Banach fixed-point iteration on the admissible physical activities. Large fields, mixed histories, global measure consistency, extraction/coupling flow and continuum observables remain separate.
