# Remove the classical irrelevant contribution from the coupling coordinate

17 October 2026. Root research candidate for independent audit. This is a consequence of the uniformly contractive classical block on a fixed countable joint system. It does not evaluate the remaining determinant coefficient or prove its sign.

## 1. Uniform classical system

Use Q_j, S_j, beta_j, P_j=I-S_j beta_j and T_j from the extracted recurrence. Let X_j=ker beta_j and A_j=P_(j+1)T_j restricted to X_j. The actual identity T_j S_j=S_(j+1) holds. Assume ||A_j||<=B with B>=1, and every consecutive q-step product on X_j has norm<=theta<1, uniformly in j. These are supplied by the fixed-q classical contraction. Then an n-step product U_(j,n)=A_(j+n-1)...A_j, with U_(j,0)=I, satisfies

    ||U_(j,n)|| <= B^(q-1) theta^floor(n/q).             (1.1)

All spaces have the same inner radius b and carrier weight. The original beta has norm<=C_beta b^-2; the reference has norm<=C_S b²; and the one-step unprojected T has norm<=B_T, uniformly in j.

Define the classical marginal leakage functional on X_j by

    ell_j(e)=beta_(j+1)(T_j e),
    ||ell_j||<=C_beta B_T b^-2.                        (1.2)

No claim ell_j=0 is needed.

## 2. A bounded linear correction

The series

    k_j(e)=sum_(n>=0) ell_(j+n)(U_(j,n)e)              (2.1)

converges absolutely in the dual norm, with

    ||k_j|| <= C_k b^-2,
    C_k=C_beta B_T B^(q-1) q/(1-theta).               (2.2)

It obeys exactly

    k_j=ell_j+k_(j+1) A_j.                            (2.3)

This is the unique uniformly bounded family solving (2.3): the difference of two such families applied to e equals its n-step transported value, which tends to zero by (1.1). The uniqueness is relative to this fixed future classical system; it is not uniqueness across regulator subsequences.

Define a new normalized marginal functional on Q_j by

    beta_hat_j(x)=beta_j(x)+k_j(P_j x).                (2.4)

It has beta_hat_j(S_j)=1 and norm at most (C_beta+C_k p)b^-2, where ||P_j||<=p. Writing x=s S_j+e with e=P_j x,

    T_j x=(s+ell_j(e))S_(j+1)+A_j e.

Equation (2.3) therefore proves the exact identity

    beta_hat_(j+1) T_j = beta_hat_j.                   (2.5)

The associated full-reference projection P_hat_j=I-S_j beta_hat_j is bounded independently of b. This is a coordinate change in the marginal/irrelevant decomposition, not a newly asserted Ward classification: beta_j remains the original local Maxwell coefficient.

For clarity the two irrelevant spaces are explicitly conjugate. The map J_j:X_j -> ker beta_hat_j,

    J_j(e)=e-k_j(e)S_j,

is bounded independently of b and has inverse P_j restricted to ker beta_hat_j. Direct calculation gives T_j J_j=J_(j+1) A_j. No new physical field transformation is performed.

## 3. Exact density coordinate and its drift

The actual normalized density at stage j is exp[-gamma_j S_j+e_j] with beta_j(e_j)=0. Put

    gamma_hat_j=gamma_j-k_j(e_j),
    e_hat_j=e_j-k_j(e_j)S_j.

Then -gamma_hat_j S_j+e_hat_j=-gamma_j S_j+e_j exactly. On the O(b²) amplitude envelope, |gamma_hat_j-gamma_j|<=C_k C_int, a uniform finite constant. Thus sufficiently large inverse couplings remain positive under the coordinate change, although the physical Gaussian map still uses g_j=gamma_j^-1/2.

Write the actual output F_j,g(e)=T_j e+G_j,g(e). Original extraction sets gamma_(j+1)=gamma_j-beta_(j+1)(F_j,g(e_j)) and e_(j+1)=P_(j+1)F_j,g(e_j). Applying (2.4)-(2.5) gives exactly

    gamma_hat_(j+1)=gamma_hat_j-
                     beta_hat_(j+1)(G_j,g_j(e_j)).    (3.1)

The classical leakage has disappeared from the scalar equation by a bounded change of coordinate. This is not a sign calculation.

On the envelope ||e_j||<=C_int b², the fixed-coupling quantum Lipschitz estimate gives

    |beta_hat_(j+1)(G_j,g(e_j)-G_j,g(0))|
      <= (C_beta+C_k p) C_quant C_int (gT/b).          (3.2)

For fixed b, this tends to zero along the prescribed T(g). In particular the leading small-g adapted drift is independent of the inherited irrelevant amplitude up to a controlled vanishing error, even though the original beta_j(T_j e_j) need not be small.

## 4. The remaining leading coefficient

If the independently checked fixed-threshold parity estimate is available on the common outer radius rho, the zero-input quantum force tends uniformly to

    D_j=Delta_j+Qdet_j

in the outer activity quotient, with error O(tau(T)+g²T^6). The total D_j is invariant as the limit of the actual invariant zero-input totals with T=T(g), so its total first jet vanishes. Removing constant/linear coefficient sectors of the difference before restricting to b yields an inner representative bounded by C b² rho^-2[tau(T)+g²T^6]. Consequently define

    b0_j=beta_hat_(j+1)(D_j).

Equations (3.1)-(3.2) then give

    gamma_hat_j-gamma_hat_(j+1)
      =b0_j+O(tau(T)+g²T^6+gT/b),                    (4.1)

uniformly in j on the fixed geometry and amplitude envelope. Constants may depend on b,rho and the chosen geometry; b is fixed before g tends to zero. A sufficient next theorem is a positive lower bound on b0_j (or a suitable positive block drift) with its actual determinant/pivot normalization. This note does not prove that theorem.

The fixed-system/countable-parameter scope remains. Continuity in the coupling for an endpoint-shooting construction, finite-regulator uniform histories, all other field sectors and sourced continuum estimates are separate obligations. The coordinate change neither supplies them nor identifies different classical local-limit systems.
