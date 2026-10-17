# Exact first free-current response at the flat source gauge

16 October 2026. This note proves finite-regulator identities for the free-current family displayed in the deposit at Raw I:13720–13740. The background and averaging maps are fixed at `U=1`; the current `J` varies independently. No field equation or divergence bound is imposed on `J`. These identities do not supply a uniform neighborhood, a response estimate, or the corresponding theorem for the full physical precision.

## 1. Definitions, adjoints, and source coordinates

Use the real finite periodic flat scalar gradient `D`, positive scalar Laplacian `L=D^*D`, and fine Maxwell bond precision `K=d^*d`, so `KD=0`. The same algebra extends by the fixed bilinear transpose when parameters are complexified. Let `Q=Q_M^st` be the one-form source constraint and `Q_0` the scalar centered block average. Their exact identity is

\[
 QD=d_cQ_0.
                                                               \tag{1.1}
\]

The flat source match and the scalar projection are checked in `flat_minimizer_source_gauge_research.md`. In particular,

\[
 G'=(L+Q_0^*a'Q_0)^{-1},\quad
 P=G'Q_0^*(Q_0G'^2Q_0^*)^{-1}Q_0G',\quad R=I-P,
\]
\[
 Q_0G'R=0,\qquad LG'R=R,
\qquad \Lambda=G'RD^*,\quad\Lambda^*=DRG'.         \tag{1.2}
\]

The star is the adjoint for the actual lattice measures at the real reference, continued bilinearly; `G'` and `R` are symmetric, but they need not commute. In particular `G'R` must not be replaced by `RG'`.

Let

\[
 \Delta_a=K+DRD^*+Q^*aQ,\qquad G_0=\Delta_a^{-1},
\]
\[
 q_0=(QG_0Q^*)^{-1},\qquad E_0=G_0Q^*q_0,
 \qquad H_0=E_0\ell^{-1}.
                                                               \tag{1.3}
\]

Thus `QE_0=I`, whereas the source-scaled map satisfies `QH_0=ell^-1`. The scalar `ell` can be a fixed diagonal scale multiplication; its position is not silently commuted through other coarse maps.

At the homogeneous flat reference, `q_0=q_M+a`: the coarse inverse includes the fixed averaging penalty, whereas `q_M` is the unpenalized Maxwell quotient. That penalty is constant on each affine constraint fiber, so `E_0` remains the same source-gauge Maxwell minimizing extension. The fixed penalty changes none of the current derivatives below. Define

\[
 \widetilde G_0=G_0-E_0QG_0.
                                                               \tag{1.4}
\]

At the source flat gauge,

\[
 RD^*E_0=0,\qquad\Lambda E_0=0,
                                                               \tag{1.5}
\]

and the same equations hold with `H_0`. These follow either from the identified gauge-selected Maxwell minimizer or directly from the source flat propagator identities. The averaging penalty in (1.3) is constant on each affine constraint fiber, so it does not alter that minimizer.

## 2. The current carrier under consideration

Raw I:13699–13713 defines the linear-in-current maps `j_J,k_J,m_J` through the second-order gauge BCH terms. They obey `k_J=j_J^*`, and `m_J` is symmetric. Raw I:13725–13731 gives

\[
 \Theta'_J=k_J\Lambda+\Lambda^*j_J+\Lambda^*m_J\Lambda,
\]
\[
 G_\pi^J=(\Delta_a-\Theta'_J)^{-1},\qquad
 q_J=(QG_\pi^JQ^*)^{-1},\qquad
 E_J=G_\pi^JQ^*q_J,\qquad H^J=E_J\ell^{-1}.
                                                               \tag{2.1}
\]

The inverse description agrees with the displayed Neumann series wherever it converges, and in finite dimensions the family is analytic near `J=0`. The existence of a scale-uniform neighborhood is not assumed or proved in this note.

For a direction `j` in current space, write `Theta'_j` and `mathfrak j_j` for the corresponding linear maps. Equations (1.5) and (2.1) give

\[
 \Theta'_jE_0=\Lambda^*\mathfrak j_jE_0,
 \qquad E_0^*\Theta'_jE_0=0.                       \tag{2.2}
\]

The first equality retains one nonzero term. It does not assert `Theta'_jE_0=0`.

## 3. The auxiliary coarse precision has no linear current term

Differentiate the inverse and the coarse inverse at zero:

\[
 \dot G_\pi[j]=G_0\Theta'_jG_0,
\]
\[
 \dot q[j]
 =-q_0QG_0\Theta'_jG_0Q^*q_0
 =-E_0^*\Theta'_jE_0=0.                            \tag{3.1}
\]

This cancellation holds for every independent current direction. It uses only the flat source gauge and the displayed factorization of `Theta'`; it uses neither a nonlinear Ward identity at nonzero current nor a condition such as `D^*j=0`.

The normalized extension derivative in any stationary quadratic inverse family is

\[
 \dot E[j]=\widetilde G_0\Theta'_jE_0.
                                                               \tag{3.2}
\]

Here it can also be obtained directly from `dot q=0` as `G_0Theta'_jE_0`. The agreement will be explicit in the next section.

## 4. The extension response is exactly a fine gradient

Put

\[
 Z=G'RG'.
                                                               \tag{4.1}
\]

It is symmetric positive semidefinite at the real reference. For any scalar forcing `f`, let `lambda=Zf`. Then (1.2) implies

\[
 Q_0\lambda=0,\qquad L\lambda=RG'f.
\]

Therefore, using `KD=0`, (1.1), and `R^2=R`,

\[
 \Delta_aD\lambda
 =DRL\lambda+Q^*a\,d_cQ_0\lambda
 =DRG'f=\Lambda^*f,
\qquad QD\lambda=0.
                                                               \tag{4.2}
\]

Invert `Delta_a` and use the second identity to conclude

\[
 \boxed{\quad G_0\Lambda^*=\widetilde G_0\Lambda^*=DZ.\quad}
                                                               \tag{4.3}
\]

Combining (2.2), (3.2), and (4.3) proves

\[
 \boxed{\quad
 \dot E[j]=DG'RG'\mathfrak j_jE_0,
 \qquad
 \dot H[j]=DG'RG'\mathfrak j_jH_0.
 \quad}                                                       \tag{4.4}
\]

In particular, `Q dot E=0` and `d dot E=0`. This is a genuine change of potential, but only a pure gauge change to first order. It need not preserve the source gauge: generally `RD^*dot E=RG' mathfrak j_jE_0` is nonzero. This agrees with the explicit warning at Raw I:13774 that `RD_U^*H^J=0` is neither asserted nor used for free current.

There is also the exact identity `Lambda DZ=Z`, since `LZ=RG'`. Thus with `Pi=I-DLambda`,

\[
 \Pi\dot E[j]=0.
                                                               \tag{4.5}
\]

No locality norm for `Z` is imported by these algebraic statements. Its localized bounds are a separate scalar problem.

## 5. Optional second derivative: current independence does not follow

Because `Theta'_J` is linear in `J`, the inverse family gives at any nearby `J`

\[
 Dq_J[j]=-E_J^*\Theta'_jE_J.
\]

Differentiate once more at zero and use (2.2), (4.4), and `Lambda DZ=Z`:

\[
 \boxed{\quad
 D^2q_0[j_1,j_2]
 =-(\mathfrak j_{j_1}E_0)^*Z(\mathfrak j_{j_2}E_0)
  -(\mathfrak j_{j_2}E_0)^*Z(\mathfrak j_{j_1}E_0).
 \quad}                                                       \tag{5.1}
\]

For a real current direction repeated twice this is negative semidefinite. It need not vanish. Thus (3.1) is a first-order cancellation, not independence of `q_J` from the current. The scale-normalized source `H^J=E_J ell^-1` retains the rightmost `ell^-1`; the unscaled coarse inverse `q_J` in (5.1) uses `E_0` as displayed.

## 6. The full source family retains a first-order contribution

Raw I:13733–13739 separately defines `Theta_J` from the quadratic nonlinear-constraint remainder `C^(2)` and then

\[
 G_1^J=[\Delta_a-\Theta'_J-\Pi^*\Theta_J\Pi]^{-1}.
                                                               \tag{6.1}
\]

At zero current, `Theta_0=0`, while its first derivative `Theta^{[1]}_j` is obtained by keeping the explicit current in

\[
 \langle A,\Theta^{[1]}_j A\rangle
     =2\langle H_0 C^{(2)}(\ell A),j\rangle.
                                                               \tag{6.2}
\]

The derivative of `H^J` inside this definition is multiplied by the zero base current and does not enter (6.2). Since `Pi E_0=E_0`, the corresponding full coarse inverse has derivative

\[
 D\big[(QG_1^JQ^*)^{-1}\big]_{J=0}[j]
      =-E_0^*\Theta^{[1]}_jE_0.                    \tag{6.3}
\]

No cancellation proved above forces this remaining term to vanish. It contains the actual constraint-curvature contribution. Subsequent pivot/gauge reduction and any background response must be tracked in the full precision separately. In particular, (3.1) must not be reported as vanishing of the physical Gaussian precision's current derivative.

The concrete result is narrower and useful: the `Theta'_J` part of the auxiliary coarse inverse starts at quadratic order in current, and its minimizing extension has the explicit pure-gradient first response (4.4). This isolates one part of the current response without assuming nonflat Ward identities or a uniform analytic current-carrier theorem.
