# Constant Cartan curvature as a determinant-comparison test background

17 October 2026. Scoped research result. Sections 1–3 are exact local lattice identities. Section 4 gives a precise polynomial-jet extension/uniqueness lemma and its application under the already available fixed-endpoint exponential Taylor-kernel hypotheses. This is not an analytic periodic family of nonzero constant flux, a globally bounded background, or a completed determinant comparison.

## 1. A commuting affine connection is exactly Wilson stationary

Use unit-lattice positive bond angles. Fix a Cartan subalgebra and matrices \(B_{\mu\nu},c_\mu\) in it, with \(B_{\mu\mu}=0\), and put
  \[
  a_\mu(x)=c_\mu+\sum_\nu B_{\mu\nu}x_\nu,\qquad
  U_\mu(x)=e^{ia_\mu(x)}.
  \tag{1.1}
  \]
All products commute. The oriented plaquette is the constant matrix
  \[
  U_{\mu\nu}(x)=e^{iF_{\mu\nu}},\qquad
  F_{\mu\nu}=B_{\nu\mu}-B_{\mu\nu}.
  \tag{1.2}
  \]
For example \(B_{\mu\nu}=-F_{\mu\nu}/2\) gives the symmetric affine gauge proposed by the parent.

The full Wilson first variation vanishes, including non-Cartan link variations. One can see this without restricting the variation to the Abelian subgroup: the left derivative on a bond is the Lie-algebra projection of the sum of transported oriented plaquette sine terms. For each transverse direction, the two incident plaquettes give opposite terms. Their constant plaquette matrices agree after transport because every background link commutes with every \(F_{\mu\nu}\). They cancel before taking the trace or Lie-algebra projection. Thus the local Euler equation is exactly zero at each bond.

This statement is local on the infinite lattice. It also holds on a finite region at bonds with complete neighboring plaquettes. It does not assert vanishing of boundary forces for an arbitrary finite-box truncation of (1.1).

## 2. The actual ordinary centered average preserves the affine family

The source formula used here is precisely the one in work/composite_macrostep_geometry_research.md, Section 1. Let \(r=x-y\) be a displacement in the centered \(\ell\)-block. For each coordinate-order contour \(\Gamma:y\to y+r\),
  \[
  U(\Gamma)=\exp\{i[r\cdot a(y)+q_\Gamma(B,r)]\},
  \tag{2.1}
  \]
where \(q_\Gamma\) is independent of \(y\). Negative oriented steps use the inverse link and obey the same identity. The selected local group mean is endpoint-equivariant. Its value on a tuple in the fixed maximal torus remains in that torus: conjugating every input by any torus element fixes the tuple, and conjugation equivariance therefore makes the output commute with the entire torus.

Consequently, without assuming the selected mean is exactly logarithmic arithmetic,
  \[
  P_\ell(U;y,y+r)
    =e^{i r\cdot a(y)}p_\ell(B,r).
  \tag{2.2}
  \]
The same \(p_\ell(B,r)\) occurs at \(y+\ell e_\mu\). In the ordinary-average path product
  \[
  U_x=P_\ell(y,x)\,U([x,x+\ell e_\mu])\,
                  P_\ell(y+\ell e_\mu,x+\ell e_\mu)^{-1},
  \]
it cancels exactly. Since \(B_{\mu\mu}=0\),
  \[
  U_x=e^{i\ell a_\mu(y)}
       \exp\!\left\{i\ell\sum_\nu
                  (B_{\mu\nu}-B_{\nu\mu})r_\nu\right\}.
  \tag{2.3}
  \]
The center straight transporter is \(R_c=e^{i\ell a_\mu(y)}\). The source average is
  \[
  M_\ell(U)(c)
     =\exp\{\ell^{-d}\sum_{r}\log(U_xR_c^{-1})\}R_c.
  \]
On the small branch, \(\sum_r r_\nu=0\) gives
  \[
                 M_\ell(U)(y,y+\ell e_\mu)
                        =e^{i\ell a_\mu(y)}.
  \tag{2.4}
  \]
These are exact local analytic identities. Formally they hold coefficientwise at zero curvature for arbitrary \(y\), whether or not one common global logarithm ball contains the affine field.

Iteration gives the composite ordinary map, not a replacement by a different direct-\(K\) map:
  \[
  M_\ell^k(U)(y,y+K e_\mu)=e^{iK a_\mu(y)},
       \qquad K=\ell^k.
  \tag{2.5}
  \]
After writing \(y=Kn\), the coarse linear matrix is \(K^2B\). To prescribe a coarse affine curvature \(F\), use the fine affine curvature \(F/K^2\). This is the correct angle normalization.

## 3. The actual direct-\(K\) contour gauge causes no new force

Let \(u(x)=P_K(U;y,x)\) in the block centered at \(y\). Then \(u(y)=I\). Exact endpoint covariance gives \(P_K(U^u;y,x)=I\), and composite ordinary covariance gives \(M_\ell^k(U^u)=M_\ell^k(U)\).

The rooted field is still Wilson stationary by gauge invariance. Its coefficients in a formal curvature parameter have polynomial growth in the block center: at each fixed order, (2.2) supplies polynomial dependence on the center and fixed finite dependence on the within-block displacement. No claim that this gauge is globally small is needed for these local formal identities.

Thus there is an explicit rooted affine candidate satisfying, coefficientwise, the actual composite constraint, direct contour gauge and unconstrained Wilson equation. Its constrained multiplier is identically zero. Identifying this candidate with the polynomial jets of the constructed minimum section is the additional step addressed next.

## 4. Polynomial-jet extension and uniqueness

Here is the exact functional-analytic statement needed; its use does not evaluate an infinite action on an affine field.

Let a stationary equation in fixed current-cell coordinates be
  \[
        \mathcal A z+\mathcal B w+\mathcal N(w,z)=0,
        \qquad \mathcal N=O((w,z)^2).
  \tag{4.1}
  \]
Assume:

1. \(\mathcal A^{-1}\) and \(\mathcal A\) have exponentially summable row and column kernels, and their two-sided inverse identities hold.
2. Every Taylor coefficient of \(\mathcal N\) through the required finite order has an exponentially summable rooted mixed-input kernel; output and input fibers are finite-dimensional at this fixed endpoint.
3. The analytic solution on bounded small fields is the actual rooted stationary branch, with its actual coordinate constraint and gauge.

For any polynomial-growth input sequence \(v_i\), the convolution \(\mathcal A^{-1}v\) converges absolutely, with polynomial growth of the same degree. Indeed
  \[
  (1+|j|)^m\le(1+|i|)^m(1+d(i,j))^m,
  \]
and exponential summability absorbs the last factor. Two convolutions can be interchanged absolutely with this weight. Hence the inverse identities remain valid on polynomial-growth sequences. In particular \(\mathcal A z=0\) has no nonzero polynomial-growth solution.

The same argument applies to a fixed multilinear coefficient: each input polynomial factor is bounded by a polynomial in the output coordinate times a polynomial in the lengths of the joining tree. The rooted exponential kernel absorbs the latter. Therefore all finite-order substitutions are well defined and retain polynomial growth.

Put \(w(t)=t w_1\), where \(w_1\) is affine. Expanding (4.1) order by order gives
  \[
  \mathcal A z_n=h_n(w_1,z_1,\ldots,z_{n-1}).
  \tag{4.2}
  \]
The preceding argument makes \(h_n\) meaningful and gives a unique polynomial-growth solution \(z_n=\mathcal A^{-1}h_n\). It is exactly the extension of the analytic branch's \(n\)-th Taylor coefficient, since the same differentiated equation defines that coefficient on bounded inputs. Thus any explicit polynomial-growth formal solution must have those same jets.

The fixed-endpoint stationary/support and Gaussian modules provide these hypotheses for the identity-background retained chart: the flat retained precision is invertible with exponential kernels, the affine pivot chart is finite-range, and the action's mixed Taylor kernels are exponentially localized. Constants may depend on the fixed endpoint. Only orders one and two are needed for a determinant Hessian, requiring the corresponding finite action/constraint jet bounds. No bound uniform as \(K\to\infty\) follows from this lemma.

Applied first to the bare Wilson action and the explicit candidate in Sections 1–3, the lemma identifies the actual minimum section's polynomial jets with that candidate. The formal multiplier vanishes through the same order. For an effective \(S_M\), this conclusion follows by the same one-shot bare-action construction at depth \(MK\), plus the already established composition/minimum identity and its polynomial-jet extension; it must not be inferred just by replacing \(S_M\) with the bare Wilson action in its current-coordinate Hessian.

The last effective-action identification is consequently a precise interface to check when using this simplification in a varying-old-depth determinant. The bare-action case is the direct application of (4.1)–(4.2).

## 5. Extracting a Maxwell moment without assigning a total to an affine field

Let \(K_{\mu\mu}(r)\) be the total translation-invariant quadratic kernel in one fixed real color direction, with symmetry and zero row sum, and with summable second moments. For finitely supported scalar component fields,
  \[
  E_2(A)=-\frac14\sum_{x,r}
        K_{\mu\mu}(r)[A_\mu(x+r)-A_\mu(x)]^2.
  \tag{5.1}
  \]
This follows by expanding the square, using the zero row sum and reanchoring the symmetric kernel. Taking formal \(A_\mu(x)=t x_\nu\), \(\mu\ne\nu\), assigns the quadratic *density coefficient*
  \[
       -\frac{t^2}{4}\sum_r r_\nu^2K_{\mu\mu}(r).
  \tag{5.2}
  \]
This is the Maxwell moment, in the chosen normalization. It does not define the divergent total \(E_2(A)\). A single off-diagonal affine component fits Sections 1–2, so an antisymmetric gauge is not necessary. For a simple gauge group, color invariance then reduces the quadratic color tensor to its fixed invariant pairing.

The kernel in (5.1) must be the total kernel with the established Ward and translation identities. Arbitrary individual anchored densities can differ by discrete divergences that do not vanish on unbounded affine inputs. One cannot evaluate a convenient local coefficient at the affine field and call it the quotient-invariant Maxwell coefficient. A constant-curvature determinant calculation must be matched to (5.2), or to an equivalent explicitly reanchored trace expression.

The formal vanishing of the multiplier on this candidate removes \(\lambda\cdot f''\) in the corresponding first two curvature jets of the actual operator. It does not by itself estimate the other vector/ghost/coarse factors, identify their trace density with a reference convention, or compute a sign.

## 6. Boundaries of the result

* On a fixed periodic torus, nonzero constant Cartan flux obeys quantization/transition-function conditions. It is not a continuous small periodic family through zero in the ordinary globally trivial link chart. Replacing it by an affine field with a seam changes the local equations near that seam.
* The infinite affine connection is unbounded. The argument uses polynomial extensions of localized derivatives, not the bounded-field analytic map at a nonzero affine input.
* Exact Wilson stationarity alone would not prove minimizer identification. The fixed-endpoint linearized inverse and orderwise uniqueness supply the needed jet argument.
* Constant non-Abelian magnetic backgrounds can have unconstrained stability issues. None of those is resolved by local stationarity. The present argument uses the constrained fixed-endpoint flat inverse for formal jets.
* Uniform endpoint finite-part estimates, full-site ghost/mass comparison, and the actual normalized determinant coefficient remain separate analytic work. No drift sign or ultraviolet trajectory is concluded here.
