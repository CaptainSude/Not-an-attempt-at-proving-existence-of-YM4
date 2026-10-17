# Flat covariance reconstruction: the gauge quotient and the actual reduced coordinates

16 October 2026. This note derives the flat quotient formulas, records the exact deposited coordinate definitions, and isolates the source assumptions under which a decay theorem for the Maxwell effective Hessian becomes a decay theorem for the actual flat fluctuation covariance. It does not duplicate the separate complex Fourier pole-cancellation proof, nor assert the independent-current perturbation theorem.

## 1. Distinguish the five operators

Use coarse physical spacing one, original fine spacing `eta=1/M`, with `M=L^k`. The fixed next-step blocking factor is `L`.

| Symbol in this note | Domain and meaning |
|---|---|
| `Q_M^st` | Original fine one-forms at spacing `eta` to unit-scale one-forms; the normalized straight-string average |
| `R_M` | Derivative of the original composed rooted group average from spacing `eta` to spacing one |
| `S_L=Q_L^flat` | Unit-scale one-forms to the next-scale datum at spacing `L`; the actual one-step fluctuation constraint |
| `T_L` | Unit-scale averaged rooted contour integrals within fixed `L`-blocks; the exponential gauge penalty is `||T_L B||^2/2` |
| `K_L` | The actual flat pivot-extension matrix from remaining unit-bond variables into `ker S_L` |

The repeated use of the letter `Q` in the source papers must not collapse these maps. The averaged Feynman propagator used below concerns the first map. The actual reduced fluctuation covariance at step `k` concerns the last three maps and the effective Hessian inherited from the first `k` steps.

The whole-lattice physical Hessian, under the differentiable-minimizer identification already stated in the flat Maxwell notes, is

\[
 q_M(B)=\inf_{Q_M^{\rm st}A=B}\|d_\eta A\|_\eta^2.
                                                               \tag{1.1}
\]

The proved energy-preserving gradient adjustment gives the same infimum with `R_M A=B`, for the full-block flat rooted composition. It does not identify `R_M` and `Q_M^st` as maps on potentials, and it supplies no bound for the gauge-adjusted potential itself.

## 2. Averaged Feynman propagator and the gauge quotient

First work in a nonzero coarse Fourier sector on a periodic lattice. There are finitely many fine alias modes in that sector. No fine harmonic zero mode occurs there.

Let `D_f` be the fine scalar gradient and `K_f=d_eta^*d_eta` the fine Maxwell precision. At the flat reference, the discrete Hodge identity is

\[
 K_f+D_fD_f^*=\mathcal L_f I,
\]

where `mathcal L_f=-Delta_eta` is the positive scalar lattice Laplacian. The adjoints use the fine physical volume measure. Let

\[
 G_F=\mathcal L_f^{-1}I,
 \qquad \overline G_M=Q_M^{\rm st}G_F(Q_M^{\rm st})^*.
                                                               \tag{2.1}
\]

The averaging adjoint in (2.1) is the adjoint from unit counting measure to fine `eta^d` volume measure. It is not the unweighted transpose of the discrete averaging matrix.

Let `D_c` be the unit-scale gradient. The exact scalar cochain identity is

\[
 Q_M^{\rm st}D_f=D_cQ_M^{(0)},                       \tag{2.2}
\]

where `Q_M^(0)` is the centered scalar block average. Its scalar right inverse exists, for example by blockwise constant extension. Thus fine gradients map onto all coarse gradients.

### 2.1 Variational proof of the quotient formula

Fine Hodge decomposition separates an arbitrary one-form into a transverse part and a gradient. The Maxwell energy is the Feynman quadratic form on the transverse part, and deleting the gradient leaves the coarse constraint unchanged modulo a coarse gradient by (2.2). Conversely, a coarse gradient discrepancy can be corrected by a fine gradient without changing Maxwell energy. Therefore

\[
 q_M(B)=\inf_{\sigma}
       \inf_{Q_M^{\rm st}A=B+D_c\sigma}
                             \langle A,G_F^{-1}A\rangle.
                                                               \tag{2.3}
\]

This equality can also be proved without naming a gauge: minimizing the Feynman energy over a coarse-gradient equivalence class removes any fine gradient that increases its energy, while surjectivity in (2.2) recovers an exactly feasible Maxwell field.

For each fixed coarse datum `b`, constrained Gaussian minimization gives

\[
 \inf_{QA=b}\langle A,G_F^{-1}A\rangle
                  =\langle b,\overline G_M^{-1}b\rangle.
\]

Indeed the minimizer is `G_F Q^* overline G_M^-1 b`, whose average is `b`; subtracting it from any other feasible field makes the cross term vanish. Thus

\[
 q_M(B)=\inf_\sigma
       \langle B+D_c\sigma,\overline G_M^{-1}(B+D_c\sigma)\rangle.
                                                               \tag{2.4}
\]

In a nonzero Fourier sector write `d=d(k)` for the coarse gradient column and `H=overline G_M^-1`. Eliminating the scalar `sigma` gives the full-space precision

\[
 \boxed{\quad
 q_M=H-Hd(d^*Hd)^{-1}d^*H.
 \quad}                                               \tag{2.5}
\]

Equivalently, with `P=I-d(d^*d)^-1d^*`, the quotient covariance on the coarse transverse subspace is

\[
 C_{\rm physical}=(P\overline G_MP)|_{\operatorname{ran}P},
\]

and its inverse on that subspace, extended by zero on gradients, is (2.5). One way to check the latter identity is the dual constrained-minimization characterization of the inverse quadratic form; another is multiplying the block Schur complement in the decomposition `ran P plus span d`.

It is generally incorrect to replace (2.5) by `overline G_M^-1`, or by `P overline G_M^-1 P`. Conditioning a gauge-fixed potential on a particular representative is different from minimizing over the gradient representative.

At coarse momentum zero the preceding Feynman inverse must not be used blindly. The fine constant potential `A=B` has zero Maxwell energy and average `B`, so the correct effective Hessian is `q_M(0)=0` on every constant one-form/color component. These are the harmonic modes, distinct from periodic exact gradients. A mass regulator may be used for intermediate Feynman formulas if its limit is checked; the explicit zero-mode definition is simpler here.

## 3. Exact alias representation, including the longitudinal weight

The fine Fourier variable is the physical momentum `p`, and fine aliases of a coarse momentum `k` are `p=k+2pi n` lying in the fine Brillouin zone. Use the fine and coarse normalized modes of equal physical volume, so no extra `M^-d` appears in an alias sum.

For centered odd `M`, define

\[
 r_M(p_\nu)={\sin(p_\nu/2)\over M\sin(p_\nu/(2M))}
\]

with continuous values at removable zeros. The symbol for the `mu`-component average is

\[
 q_{M,\mu}(p)
 =e^{i(M-1)p_\mu/(2M)}r_M(p_\mu)\prod_\nu r_M(p_\nu).
                                                               \tag{3.1}
\]

The factor in direction `mu` occurs **twice**: once from the centered block average and once from the longitudinal string average. Replacing this by a scalar block average common to all one-form components loses the actual tensor weight.

The fine Laplacian symbol is

\[
 \lambda_\eta(p)=4M^2\sum_\nu\sin^2(p_\nu/(2M)).
\]

Because the Feynman propagator is diagonal in one-form components, (2.1) is diagonal too:

\[
 (\overline G_M)_{\mu\nu}(k)
 =\delta_{\mu\nu}\sum_{p=k+2\pi n}
                  {|q_{M,\mu}(p)|^2\over\lambda_\eta(p)}.
                                                               \tag{3.2}
\]

For complex continuation, the real-axis product `|q(p)|^2` must be replaced by the analytic product `q(p)q(-p)` with the correct component convention; it must not be continued as a complex modulus. The phase in (3.1) cancels in that product.

An independent normalization check is

\[
 q_{M,\mu}(p)\,M(e^{ip_\mu/M}-1)
       =(e^{ik_\mu}-1)\prod_\nu r_M(p_\nu),           \tag{3.3}
\]

which is exactly (2.2) in Fourier variables. The longitudinal string average telescopes against the fine gradient. The alias sum in (3.2) uses the volume adjoint: each fine normalized Fourier mode is sent to its coarse normalized mode with coefficient `q`, so composing with the adjoint yields precisely the sum of squared coefficients.

The analytic continuation and uniform pole-cancellation bounds for (2.5)--(3.2) are being proved separately. This note does not infer exponential decay from the real-axis spectral bounds alone.

## 4. What the source's G1 formula actually says

The deposited source algebra, raw III around lines 36350--36357, states

\[
 G_1^{-1}=\Delta_1+DRD^*+Q^*aQ,
 \qquad H_1=G_1Q^*(QG_1Q^*)^{-1},
\]
\[
 QH_1=I,\qquad RD^*H_1=0.
                                                               \tag{4.1}
\]

Consequently, on the stated source constraint space,

\[
 H_1^*\Delta_1H_1=(QG_1Q^*)^{-1}-a.                 \tag{4.2}
\]

The proof is direct: insert `Delta1=G1^-1-DRD*-Q*aQ`, use the last two identities, and pair the equation `G1^-1 H1=Q*(QG1Q*)^-1` with `H1`. No Feynman-gauge replacement is used in this computation.

Raw II around 9090--9100 identifies this same quadratic form with the action part of the fluctuation Hessian. Raw I around 13583--13655 records the analogous operators `Delta_a`, `G0`, `(QG0Q*)^-1` and the normalized minimizing map, including the distinction between physical-volume and scale-normalized coarse variables.

In particular the source `G1` is not, by notation alone, `(-Delta_eta)^-1 I`. It contains the source's gauge projector `R` and an averaging penalty. Under the actual variational identification of its Hessian, (4.2) equals the Maxwell quotient (2.5) at flatness. Then the source average satisfies `QG1Q*=(q_M+a)^-1`; it is a different object from the Feynman average (3.2), which is used before taking the coarse gauge quotient.

### 4.1 Primary-source scope

CMP109, Section 2, expands the action around its constrained critical configuration, adds the quadratic exponential-gauge term, linearizes the next averaging constraint and eliminates pivot coordinates. Its formulas (2.11)--(2.13) identify the reduced Gaussian covariance. [Primary PDF](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), pp.266--268.

No usable original CMP99b PDF or local extraction was found in this workspace during this pass. Its metadata identifies *Propagators for lattice gauge theories in a background field*, CMP 99 (1985), 389--434, DOI [10.1007/BF01240355](https://doi.org/10.1007/BF01240355). Therefore the exact CMP99b operator formulas and quantitative estimates above are treated as deposited transcriptions, not as newly verified original-page quotations. The flat variational reconstruction avoids importing its quantitative covariance theorem; it still needs the independently identified minimizer/constraint definitions.

## 5. The actual reduced coordinates at the flat reference

Raw II, `8.2:not-small-field-step`, around lines 73860--74020, records the operations of CMP109. The integration variable at unit scale is first written relative to the critical configuration, the nonlinear averaging constraint is linearized by a change beginning at quadratic order, the coupling is scaled out, and the pivot variables are eliminated. Denote the final remaining Gaussian vector by `z` to avoid the source's repeated use of `B`.

At `(U,J)=(1,0)`, the following facts apply:

* The critical configuration is the trivial one, and the action is stationary there.
* The linearized effective action on the full unit bond field is `q_M`; current-times-second-chart-derivative corrections vanish.
* The gauge-fixing Hessian is `T_L^*T_L` with coefficient one in the quadratic form before its overall Gaussian factor `1/2`.
* The differential of the nonlinear constraint-straightening change is the identity. Its quadratic correction cannot change the stationary Hessian.
* Haar and change-of-variable factors belong to the interaction exponent after coupling rescaling; they do not change the order-zero flat Gaussian precision.
* The actual linear pivot extension is `B=K_L z`, with `z` precisely the nonpivot unit bonds.

Therefore, under the finite-level minimizer identification and these recorded source operations, the flat Gaussian precision and covariance are

\[
 \boxed{\quad
 A_{M,L}=K_L^*[q_M+T_L^*T_L]K_L,
 \qquad C^{(k)}(1)=A_{M,L}^{-1}.
 \quad}                                               \tag{5.1}
\]

This is the reconstruction relevant to the fixed Gaussian cutoff coordinates. It uses the gauge-quotient **precision** `q_M`, followed by the actual next-step constraint and local gauge penalty. Simply treating (3.2) as the reduced fluctuation covariance would be incorrect.

The source carrier permits independent `J` away from the physical minimizing pair. Formula (5.1) only identifies its value at `(1,0)` when its displayed definitions specialize to the physical quadratic term there. It supplies no response bound in a free `J` direction.

## 6. Exact locality of the fixed-L matrices K_L and T_L

These matrices concern one unit-scale step, not the large refinement factor `M`. Their ranges and all elementary norms therefore depend only on the fixed `d,L`.

Raw I around 46960--47000 specifies the next-step operators by the first derivatives of the actual contour and averaging maps. It defines the kernel convention

\[
 (S_L B)(c)=\sum_b L^{-d}Q^{\flat}(c,b)B(b),
\]

and the pivot kernel coefficient `pi_c=Qflat(c,b0(c))`. At flatness `pi_c=I`, while the **discrete matrix coefficient** of the pivot in `S_L` is `L^-d I`. Its extension coefficient on nonpivot columns is consequently

\[
 K_L(b_0(c),b)=-Q^{\flat}(c,b)
                  =-L^d(S_L)(c,b),                  \tag{6.1}
\]

and `K_L` is the identity on retained nonpivot rows. This agrees exactly with the flat pivot construction already audited. Confusing the normalized kernel with the discrete matrix coefficient would introduce a spurious factor `L^d`.

Each `T_L` row uses contours entirely within one `L`-block. Each `S_L` row uses only the two endpoint blocks of its coarse bond: two endpoint-contour terms plus the translated straight strings. Thus each pivot row in (6.1) reads only those two blocks. No inverse on an extended lattice is hidden inside `K_L`; the pivot coefficient matrix is diagonal at flatness.

Let `h_L=d(L-1)`, `n_L=L^d`, and `r_L=1+2h_L/L`. The audited absolute row/column sums give

\[
 \|T_L\|_{\rm Schur}\le\max(h_L,n_L-1),
\]
\[
 \|K_L\|_{\rm Schur}\le
              K_*:=1+L^d(2d+2)r_L,                  \tag{6.2}
\]

where the Schur norm is the maximum of the absolute block row sum and column sum. These bounds are deliberately conservative. The sharper Hilbert-space bound remains

\[
 \|K_L\|_{2\to2}^2\le1+L^{2d}(2d+2)r_L^2.
\]

Give each bond coordinate its basepoint or midpoint and each contour output its target site; either fixed convention has uniformly bounded offsets. One may safely take range constants `R_T=3dL`, `R_K=3dL`. With the exponentially weighted Schur norm,

\[
 \|T_L\|_m\le e^{mR_T}\max(h_L,n_L-1),
 \qquad \|K_L\|_m\le e^{mR_K}K_*.                   \tag{6.3}
\]

The transpose has the same weighted Schur bound. The two-block geometry and incidence bounds persist on periodic lattices with the proper seam-cell multiplicity, and in the complete-block incident-bond convention audited previously. They do not justify an arbitrary altered pivot scheme.

## 7. Conditional transfer of a q_M decay theorem

Suppose the separate Fourier argument establishes, uniformly in `M` and periodic volume,

\[
 \|q_M\|_m\le K_q
\]

for a fixed positive exponential weight exponent `m`, in a precise pointwise-kernel/weighted-Schur sense. Multiplication of weighted Schur matrices and (5.1)--(6.3) then imply

\[
 \|A_{M,L}\|_m
 \le\|K_L\|_m^2\bigl(K_q+\|T_L\|_m^2\bigr).        \tag{7.1}
\]

The flat Maxwell lower-bound and gauge-bridge notes supply `A_{M,L}>=gamma_exp I`, uniformly in `M` and volume, in these same retained nonpivot coordinates. Consequently a weighted-resolvent/Combes--Thomas argument can use the uniform gap and (7.1) to derive exponential decay of `A_{M,L}^-1`, at a possibly smaller fixed exponent. This is a legitimate route to the actual flat covariance after the q-decay hypothesis is proved. The gap alone was insufficient; the missing locality input is precisely the `q_M` bound, not a hidden nonlocality of `K_L` or `T_L`.

When grouping retained coordinates into fixed cells for a Gaussian theorem, the number of coordinates per cell is bounded in terms of `d,L` and the Lie-algebra dimension. The cell grouping and the metric conversion are fixed independently of `M`; hence (7.1) and the gap retain scale-independent constants.

## 8. Remaining source and analytic obligations

1. Identify the actual whole-lattice effective action with the stated C^2 constrained-minimizer branch and the exact normalized averaging operation. The existing flat notes supply the chain-rule and variational consequences once this source match is supplied; they do not reprove the nonlinear minimizer theorem.
2. Complete and independently audit the uniform complex-strip/weighted-kernel argument for the quotient precision `q_M`. Real-axis bounds and the alias formula alone do not prove exponential decay.
3. Check thermodynamic or periodic-regulator identification using the actual finite-volume operator, rather than replacing it with an unrelated infinite-volume symbol.
4. Establish the small weighted perturbation or directional-response bounds of the **actual complex independent-current precision** near `(1,0)`. Flat locality does not supply these derivative bounds.
5. Preserve the actual retained cutoff coordinates. The use of a gauge adjustment to identify a variational Hessian does not authorize moving the sharp real integration domain.
6. General retained histories, multiple active scales, different boundary/pivot conventions and arbitrary nonflat reference backgrounds remain outside this whole-lattice flat identification unless separately checked.

The constructive source match obtained here is therefore specific: the Maxwell gauge quotient reconstructed from the averaged Feynman propagator is the physical flat Hessian, and the actual reduced Gaussian is obtained by adding the fixed local averaged-contour penalty and applying the fixed local next-step pivot extension. No quantitative property of the old source G1 is being silently substituted for a property of the Feynman propagator, or conversely.
