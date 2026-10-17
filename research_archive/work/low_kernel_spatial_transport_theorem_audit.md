# Audit and repair of low-kernel spatial transport

17 October 2026. Independent audit of the root research note, followed by the explicitly authorized repair of its quadratic algebra. No output edits or compilation.

## Substantive correction

The original identity

    K_2(a,a)/2 = -1/4 sum_(x,r)
          (a(x+r)-a(x))^T K_2(r)(a(x+r)-a(x))

does not follow from Hessian reciprocity K_2(r)^T=K_2(-r). A skew matrix J with K(1)=J and K(-1)=-J has a nonzero antisymmetric cross-field translation form, while every displayed same-increment quadratic expression is zero. The error cannot be excused by midpoint parity: converting a midpoint kernel to tail coordinates can produce skew/odd components.

That identity has been removed from the active proof. Section 1 now assumes the actual Ward consequence: all quadratic momentum jets through degree three vanish. Section 3 uses ordered Laurent divided differences, which are valid for the tail-coordinate matrix kernel without any pointwise matrix symmetry.

## Checked replacement

For a Laurent monomial z^r, the ordered divided difference B_j produces |r_j| monomials, all at exponent length at most |r|_1. Consequently the combined absolute row norm, summing j before the row supremum, loses at most 1/[e(sigma-sigma')] between weighted Wiener exponents. Its local Taylor series reduces vanishing order by one. Two applications to K_2 therefore leave H_(rho,tau) with a second-order zero at z=1.

Setting Htilde_(rho,tau)=-z_rho H_(rho,tau) yields exactly

    K_2(z)=sum_(rho,tau)
        (z_rho^-1-1) Htilde_(rho,tau)(z) (z_tau-1),
    Htilde_(rho,tau)(1)=0.

At successive exponents sigma,3sigma/4,sigma/2 the combined bound is
16 exp(sigma/2)/(e^2 sigma^2) times the original norm. The shift and sign are correct because (z^-1-1)(-z)=z-1.

Integration by parts gives a product of D_rho a(x) and
D_tau a(x+r)-D_tau a(x). The zero-sum kernel justifies the latter subtraction. This is an exact total quadratic identity. Near displacements give b^2 h^(4+alpha)|r|^alpha; far displacements give b^2 h^4. No second derivative of the field is invoked.

## Other algebra and norm checks

The cubic zeroth/first-moment subtraction leaves precisely the six terms listed in the note. With physical C1alpha coefficient norms their leading order is h^(4+alpha); the two-gradient cubic term has h^5. The quartic frozen-product subtraction and telescoping give h^5 times one displacement. Their componentwise moment hypotheses are supplied by the stronger Ward vanishing orders.

The use of coherent complete-field coefficients is essential and is explicit in the hypotheses. On a fixed collar, derivatives, differences and Hölder quotients are controlled inside the support sum. Thus near-displacement Taylor estimates concern coefficient families, rather than only their scalar sum.

The carrier construction keeps the output anchor and joins endpoint roots and each field-factor support tree. The projection bound, together with
exp(a0 |H|)1_(z in H) <= exp(a0) exp(-dist(z,j(x))) exp((a0+1)T),
is valid because H is connected, contains j(x), and has at most 1+T vertices. The conditions 2(a0+1)/J<=kappa and A>=4(a0+1) pay every attached tree and cardinality factor. The finitely many endpoint/neighbor roots cost only a fixed constant.

The exact anchor count is (JL)^4 current sites per final J-cell, followed by S_1. Internal direction/color counts are fixed; there is no further count of all output coordinates. Far endpoint-root trees cost exp(C m/(JL)), which is absorbed once L is chosen after sigma and J. Using sigma_*=sigma/2 for all three kernels leaves the exponentially small bound stated in the patched note.

All absolute estimates are linear in the kernels and establish normal convergence of the regrouped holomorphic coefficients. Compactly supported final input implies each nonzero carrier meets that support, so the total vacuum-normalized sum converges.

## Result and scope

After the quadratic repair the full argument passes this audit. It proves the claimed C(J) epsilon L^-alpha connected-norm estimate under the stated coherent infinite-family or explicitly periodized-family hypotheses and exact lifted moments. It does not supply those moments for arbitrary finite torus kernels, compare sequential quantum windows, or prove an invariant quantum activity class.
