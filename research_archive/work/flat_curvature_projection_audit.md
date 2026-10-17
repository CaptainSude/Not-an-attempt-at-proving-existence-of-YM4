# Independent audit: the curvature projection and fixed-constraint perturbations

16 October 2026. Audited Sections 8–10 of `flat_curvature_response_research.md` against the independently checked full inverse and scalar source-gauge identities. **Pass: no mathematical correction found.** The result is a theorem for the homogeneous flat linear constraint kept fixed. It does not identify the response of the actual nonflat Yang–Mills Hessian.

## 1. Inputs and constrained inverse

Write `C=d_curl`, `L=D*D`, `Q=Q_M^st`, and retain the scalar average `Q_0`, source orthogonal projection `R`, and scalar inverse `G'`. The required exact identities are

    QD=d_coarse Q_0,  Q_0 G'R=0,  L G'R=R.

The audited positive fine operator and its inverse are

    A_a=C*C+D R D*+Q*aQ,  G_0=A_a^-1.

For fixed positive `a` (source normalization `a=1`), the normalized extension `H=G_0Q*q_aux` is the source-gauge Maxwell minimizer and

    q_aux=(QG_0Q*)^-1=q_M+aI,  QH=I,  RD*H=0.

Set `Gamma=G_0-H q_aux^-1 H*`. Direct multiplication gives `QGamma=Gamma Q*=0` and `Gamma A_a=I-HQ`. Thus `Gamma` is the inverse of the restricted positive form on `ker Q`, extended by zero on its orthogonal complement `ran Q*`. Surjectivity of `Q`, supplied by the bounded right inverse `H`, makes this decomposition legitimate also in infinite volume. The proof does not assume that `H` is the orthogonal right inverse in the unweighted fine field norm.

## 2. Gauge-removal test proves the projection identity

Let `K=closure(C ker Q)` and `zeta=Gamma C*f`. The constrained Euler equation is

    <C zeta-f,C xi>+<R D*zeta,R D*xi>=0,  xi in ker Q.

Define `r=R D*zeta` and `lambda=G'r=G'Rr`. The audited source identities yield `Q_0 lambda=0` and `L lambda=r`. Therefore `xi=Dlambda` is feasible, `Cxi=0`, and `R D*xi=Rr=r`. This test gives `||r||^2=0` exactly. There is no illicit commutation of `G'` with `R`, no assumption that all feasible fields satisfy the gauge, and no use of a bound on the individual fine derivative uniform in `M`.

The remaining equation says that `Czeta` is in `K` and `f-Czeta` is orthogonal to `K`. Hence

    P_K=C Gamma C*.

At each fixed refinement, all difference operators are bounded on the physical fine Hilbert space. The same argument therefore applies on compatible finite tori and on the homogeneous infinite lattice. The closure in `K` creates no existence issue because the constructed `Czeta` already realizes the orthogonal projection.

## 3. Locality and the inverse actually used

With `F=CH`,

    P_K=C G_0 C* - F q_aux^-1 F*.

The first term uses exactly the two-fine-derivative sandwich proved in the full inverse note. The second uses the local minimizing curl and `q_aux^-1=QG_0Q*`, whose locality follows from bounded finite-range averaging. There is no inversion of the massless physical precision `q_M`.

For the cell-Schur norm taking the maximum of exponentially weighted row and column sums, multiplication is submultiplicative and taking adjoints preserves the norm. Thus

    ||P_K||_kappa <= ||C G_0 C*||_kappa
                    + ||F||_kappa^2 ||QG_0Q*||_kappa =: p.

Choose `p>=1`. All norms use physical fine volume inside each cell. Compatible torus periodization and periodic distance retain the constants already established in the input theorems.

## 4. Exact analytic domain and derivatives

The identity

    q(V)=q_M+F* V (I+P_K V)^-1 F

is holomorphic for `p ||V||_kappa<1`, by a Neumann series in the weighted algebra. On the real selfadjoint slice this condition implies `||V||<1`, so the formula agrees with minimizing the positive curvature form `I+V` over `QA=B`. Off that slice it is a holomorphic continuation, not a complex infimum. Both insertions in the equivalent quadratic Schur term are `V`, not `V*`.

The first two weighted estimates and the all-order formula in Sections 9–10 follow directly from this series. At order `n`, there are `n-1` factors of `P_K`, a sign `(-1)^(n-1)`, and a sum over all `n!` orders of the directions. For insertions supported in single cells, the pointed matrix block has exactly two end legs from `F`, and the successive source-cell links from `P_K`; no uncontrolled sum over fine sites arises because each such factor is a cell Hilbert-space operator. Repeated source cells are allowed. The stated path exponential and constants check.

The equality `||sum_x V_x||_kappa=sup_x||V_x||` is correct for the disjoint cell-diagonal decomposition. It must not be used for overlapping supports without a separate bound. The note properly keeps varying `Q`, covariant derivatives, gauge projection, lower-order terms, and physical currents outside this theorem.

## 5. Deliverable

The accompanying `flat_curvature_projection_fragment.tex` contains a compact theorem and proof with independent label prefix `curv-`. It uses the physical precision `q_M` and the distinct penalized precision `q_aux=q_M+aI` throughout.
