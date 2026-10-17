# Deposited Wilson action, pairing and Hessian coordinates

Evidence-bound check of `theorem_0_complete_account_raw_I.tex` at pinned commit e392ef45013a581664bab76b90867170b30fe10e. This verifies the deposited conventions; it does not claim a fresh comparison with the original CMP99b/CMP102b typesetting.

## 1. Action and physical pairing

The relevant explicit passages are:

* I:450–455 uses independent oriented-link coordinates, with reversed links defined by inversion, and fixes normalized trace tr(1)=1. I:464–467 defines A(U)=sum_p[1-Re tr U(partial p)], summing each unoriented plaquette once. I:474–479 puts the coupling factor g_0^(-2) outside this action in the Boltzmann density.
* I:3882–3885 realizes the Lie algebra as Hermitian traceless matrices with inner product tr(Y_1Y_2), again with normalized trace.
* I:12756–12760 explicitly gives bilinear trace pairings with measure eta^d on the finest lattice and ell_j^d on the coarse layer; analytic adjoints coincide with those bilinear transposes.
* I:43103–43107 again defines the constrained-minimization Wilson action on a domain X as sum_(p subset X) Re tr(1-partial U(p)). There is no coupling factor in this displayed minimization action.

Accordingly, in the actual dimension d=4, the action in `nonflat_wilson_inverse_research.md` and `wilson_nonlinear_force_research.md`,

    eta^(d-4) sum_(positive plaquettes p)
       [1-(1/2)tr(P_p+P_p^(-1))],

matches the deposited coupling-free Wilson action on the real slice. Choosing one orientation/base for each square identifies its positive-plaquette sum with the deposit's unoriented sum. Its analytic extension near SU(N) is the displayed forward/reverse expression. There is no additional factor two, N, g^(-2), or eta^(d-4) in d=4. Fine variation pairings are exactly eta^4 sum tr(B_eC_e) in independent positive-bond coordinates. The deposit's positive-coordinate convention appears at I:452, I:589, and explicitly as “positively oriented fine bond, or simply a bond” at I:38158–38161.

These facts also fix the flat Hessian directly: a variation exp(i eta A) has plaquette linear angle i eta^2 dA; the quadratic action is (1/2)eta^4 sum_p tr((dA)_p^2). Thus its physical-pairing Hessian is d^T d with coefficient one. A general-dimension extension with eta^(d-4) is our explicit normalization, not an additional claim about a different-dimensional source convention.

## 2. Which Hessian the source calls Delta

I:15471–15478 defines Delta as the symmetric quadratic coefficient in the expansion of the lattice action about a background. The coordinate is made explicit at I:15643–15648:

    mathsf A(exp(i eta A)U_0)
      =mathsf A(U_0)+<A,J>+(1/2)<A,Delta A>+V_0(A),

with V_0 cubic. The same left-multiplication coordinate appears at I:14135 in the definition of V_0, and in the gauge-coordinate expansion at I:13693–13705.

It follows that the deposited Delta is the Hessian in the simultaneous left exponential fluctuation about U_0: mixed directions are exp(i eta(sB+tC))U_0. This is precisely the chart used for the explicit Hessian in `nonflat_wilson_inverse_research.md`. At U_0=1 it is also the ordinary global-potential chart of the nonlinear force note.

At a nonzero global potential A_0, however, the ordinary Hessian of A->S(exp(i eta A)) is generally different. Let V=exp(i eta A_0) and define the local coordinate conversion

    B_(A0)(delta)=(i eta)^(-1)
                    log[exp(i eta(A_0+delta))exp(-i eta A_0)].

Then DB_(A0)(0)H=J_(eta A0)H, where J_X H=integral_0^1 Ad(exp(itX))H dt. The exact chain rule is

    D^2 S_ord(A_0)[H,K]
      =<J_(eta A0)H, Delta_V J_(eta A0)K>
          +<J(V),D^2 B_(A0)(0)[H,K]>.

The second term involves the background current. It must not be dropped merely because the connection is small. The ordinary-coordinate nonlinear force/minimizer proof and the left-exponential nonflat inverse proof therefore have their respective, explicitly stated coordinates. They concern the same normalized action but not identical Hessian matrices away from the flat point.

## 3. Consequence and remaining limits

At the deposited-transcription level the action prefactor, physical pairing, trace normalization, and left-exponential chart required for the explicitly normalized homogeneous Wilson calculation are matched. The ordinary-coordinate force proof is also an exact calculation for that action in d=4. This removes the previously open numerical-prefactor/chart-reading issue in that restricted setting.

It does not verify every graded source curl notation against the transported curl used in the Hessian proof, nor identify a mixed retained-history effective Hessian with the bare homogeneous Wilson Hessian. It does not establish the source's own nonlinear minimizing gauge, nonlinear gauge-orbit coverage, or source weak-norm estimates. Original-paper verification remains separate from this direct check of the pinned deposit.
