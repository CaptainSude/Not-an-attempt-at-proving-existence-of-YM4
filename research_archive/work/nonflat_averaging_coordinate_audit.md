# Independent audit of the nonflat averaging coordinate conversion

Audited `nonflat_averaging_coordinate_research.md`, §§1–6, against the stated deposited source bridge and direct noncommutative differentiation. Verdict: passes. No mathematical correction found. The multilevel trajectory hypothesis in its §6 is now supplied by the separately saved candidate `nonflat_reference_averages_research.md`, subject to the latter's independent audit.

## 1. Noncommutative endpoint order

Write g=g^V(U), a=a(U), a0=a(V), and k=g^(-1)a a0^(-1), so a=g k a0. Substituting this equality at both endpoints gives

    C_1(U) C_1(V)^(-1)
      =a0_-^(-1) k_-^(-1) C_V(U)
           M(V) k_+ M(V)^(-1) a0_-.

This is exactly (2.2). In particular the endpoint matrices are neither commuted nor treated as a multiplicative mean cocycle. C_V(U) in (1.5) agrees with the corrected middle increment obtained by rearranging Raw I 47082–47086. The fixed-reference specialization (1.6) agrees with Raw I 24313–24325 at reference 1.

At U(s)=exp(isB)V, k(0)=1 and its left derivative is eta^1-eta^V=Z_V. The left derivative of k_-^(-1) C_V(U) Ad_M k_+ is therefore LQB-Z_-+Ad_M Z_+=LQB-d_MZ. This verifies the sign in (2.4). Independently differentiating the rooted identity gives LQflat=d_M rbar+LQ, hence (2.6), consistent with the direct derivative of C_1.

## 2. Jacobians and physical factor

For arbitrary complex matrices in the stated logarithm ball, differentiation of the exponential proves

    (1/i) d exp(i(X+sK))/ds|0 exp(-iX)=J_X K,
    J_X=integral_0^1 Ad(exp(itX)) dt.

The inverse-Jacobian formula for the logarithm is therefore correctly used in (3.3). Its expansion gives the displayed first-order endpoint defect (3.4), including its sign. The two-contour example is appropriately described only as an algebraic diagnostic, not as unproved realizable lattice data.

For an ordinary physical variation K, the fine left-increment coefficient is h J_(hA)K. The coarse coefficient is Lh J_(LhF_h(A)) DF_h(A)K. Substitution into (2.4), division by Lh, and right composition by J_(hA)^(-1) give exactly (4.1). The endpoint factor is 1/L, not 1/(Lh), and it has no additional h; its smallness comes from Z_V itself. The order Ad(a_-) J_coarse DF_h J_fine^(-1) is correct.

## 3. Norms and scope

All contour operators are finite fixed-L local coefficient matrices. On the common complex ball their transport products and logarithm Jacobians are uniformly bounded; Z_1=0 and local analyticity give coefficient size C_L h||A||. Physical column sums acquire the fixed ratio L^d only. Consequently bounded-field, physical-adjoint bounded-field and physical L2 norms are uniformly controlled, with no refinement-dependent path-trace estimate. The endpoint difference d_M is bounded between the coarse site and coarse bond spaces by fixed incidence. Together with the previously proved corrected derivative estimate, this verifies (5.4).

The local Cauchy remark about additional background derivatives is sound when read for the one-step map in the unit-angle variable hA. Multiplication over the actual ordinary backgrounds requires their independent uniform physical amplitude bound. The note does not conflate that product with the derivative of the fixed-reference multilevel map and correctly excludes nonflat minimization or inverse stability.

As throughout this research sequence, the coordinate identification is verified against the explicit deposited bridge, not independently against a newly inspected original CMP98 PDF. That source limitation is stated accurately.
