# Exact local gauge covariance of the homogeneous chart integral

Research candidate, 17 October 2026. This is a possible input to the
relevant/marginal extraction step, not that extraction itself. It uses
only the physical branch and exact retained-coordinate integral of
Notebooks19--21. Independent audit is required before promotion.

Fix a compact connected semisimple matrix gauge group, with color
coordinates orthonormal for an invariant positive trace form. Let V_*(W)
be the homogeneous physical stationary current configuration, with
ordinary next average W and every internal averaged contour P equal
to identity. Work on smaller overlapping small-potential domains so
all configurations and their gauge transforms below remain in the
proved domains. We make no extension to arbitrary group configurations.

## 1. The exact block lift of a next-coarse gauge

For a next-coarse site gauge u(y), define its current block lift

    u^up(x)=u(y) for x in the L-block centered at y.

The current transformation convention is

    V^v(b)=v(b_-) V(b) v(b_+)^-1.

Contour equivariance and the fact that an internal contour remains
inside its block give

    P_(V^(u^up))(y,x)=u(y) P_V(y,x) u(y)^-1,
    M_L(V^(u^up))=M_L(V)^u.                              (1)

The previously proved local gauge invariance of S_M applies to this
current site gauge when it and the transformed configurations lie
in common smaller domains. Its fine extension need only be smooth
on the original fine mesh relative to the current unit scale; the
fixed L-block jump does not introduce an M-dependent derivative.

The transformed V_*(W)^(u^up) is feasible at W^u, has P=1, and is a
critical point of the classical action plus absolute gauge penalty.
One may see criticality by transporting the original constrained
stationarity through the gauge diffeomorphism; gauge invariance of
S_M and conjugacy invariance of the penalty preserve it. The common
strict convexity/uniqueness theorem of Notebook19 then gives

    V_*(W^u)=V_*(W)^(u^up).                              (2)

This argument needs the common-radius conditions, including a chart
containing both candidates. It does not infer P=1 from stationarity.
For real small u all identities are ordinary group identities;
holomorphic identities extend to a sufficiently small complex
parameter domain where the same maps are defined.

## 2. Equivariance of the nonlinear pivot chart

Let R_u act on all relative current Lie algebra bond fields by

    (R_u B)(b)=Ad_(u^up(b_-)) B(b),

and let D_u be its restriction to retained coordinates. If
V'=V^(u^up), the relative constraint satisfies

    F_(V')(R_u B)(c)=Ad_(u(c_-)) F_V(B)(c).              (3)

Indeed the two ordinary averages transform with the same endpoint
gauges, so their left-relative product transforms by conjugation
at the initial coarse endpoint. The logarithm has that conjugacy
property on its common chart.

The nonlinear chart Phi has F_V(Phi_V(z))=0 and retained
coordinates exactly z. Thus R_u Phi_V(z) solves the V' constraint
with retained coordinates D_u z. Uniqueness of the small pivot
solution gives the exact identity

    Phi_(V')(D_u z)=R_u Phi_V(z).                        (4)

It is stronger than equality only of tangent spaces.
For real u, D_u is orthogonal in each retained color block and
det D_u=1 because the adjoint representation of a connected compact
group has determinant one. Each retained bond-color norm and hence
the full retained rectangle is preserved. The whole chart is carried
into the corresponding chart at V'.

## 3. Every factor in the normalized integral

Let

    T_V(z)=S_M(log(exp(i Phi_V(z))V)/i)
                         +G(exp(i Phi_V(z))V).

In the common domains, equations (1),(4) and action gauge invariance
give T_(V')(D_u z)=T_V(z). Consequently

    A_M(V')=D_u A_M(V) D_u^T                            (5)

for real u. The normalized real Gaussian transforms accordingly,
and its determinant is unchanged.

The Haar pullback density satisfies j(Ad_u X)=j(X), directly by
conjugation invariance of Haar measure and det Ad_u=1. For the
straightening factor, differentiate (3) in the pivot of c:

    A_(V',c,p)=Ad_(u(c_-)) A_(V,c,p)
                            Ad_(u^up(p_-))^-1.          (6)

The determinant of each adjoint matrix equals one, so the pivot
delta factor D(V)=product_c det A_(V,c,p)^-1 is unchanged. The same
identity holds for the nonlinear pivot derivative DF at the
transformed field, so the normalized straightening determinant
ratio is unchanged as well.

Constants, linear terms and quadratic terms in the action Taylor
expansion transform separately under the fixed linear map D_u.
Therefore the remainder used in the centered product-domain
extension, together with the normalized Haar and straightening
factors, gives an invariant normalized integral:

    Z_(M,g)(V')=Z_(M,g)(V).                              (7)

The real retained change of variables D_u has unit determinant
and preserves the sharp rectangle exactly. No complex sharp
indicator or deformation of that rectangle is used.

The Gaussian determinant correction

    Q_M(V)=-(1/2)log det(A_M(V) A_(M,0)^-1)

is invariant as well: det A_(M,0) is the same scalar denominator,
and det A_M(V')=det A_M(V). The reference matrix itself need not
be invariant under the local gauge. D(V)/D(1) has the same property.
For the logarithms, choose their common analytic branches;
equalities follow first from positive real integrals and continuous
real gauge paths, then from holomorphic uniqueness.

It follows that the generated total correction

    E_eff(W)=log[D(V_*(W))/D(1)]
                 +Q_M(V_*(W))+log Z_(M,g)(V_*(W))        (8)

obeys E_eff(W^u)=E_eff(W) on the common small domain. If a strictly
local expansion in W has been separately established by stationary
support transport, this is gauge invariance of its sum. It does
not assert gauge invariance of each arbitrary support coefficient.
The explicit field-independent factors and the classical stationary
action have been kept separate.

## 4. An inherited gauge-invariant correction

The same argument applies if the integrand is multiplied by
exp E(U), provided E is a gauge-invariant holomorphic current-field
functional on the needed common domain and its composition/integration
is actually convergent and holomorphic there. This gives equality
of the integrals. Equality of their logarithms additionally requires
nonvanishing on the common connected domain and a compatible
analytic logarithm branch, continued from the identity gauge;
a verified cluster expansion is one way to provide those properties.
Convergence of a complex integral alone does not exclude zeros.
Gauge invariance of E is a hypothesis in this extension, not an
automatic property of an arbitrary polymer family. The exact chart
symmetry then survives that integration. Norm closure and the
running-coupling estimates remain separate.

## 5. The quadratic Ward identity

Write W=exp(iw) and let F(w) be the total correction (8), or any
holomorphic coarse functional with the same local gauge invariance.
Global constant gauges act by adjoint conjugation on each w bond.
For a semisimple group there is no invariant nonzero Lie algebra
covector. Hence

    D F(0)=0.                                           (9)

For a small site gauge exp(it lambda), the infinitesimal potential
variation at w=0 is the signed coarse gradient D_1 lambda.
Differentiate the gauge identity first in t and then in an arbitrary
potential direction v. Using (9) removes the derivative of the
nonlinear gauge generator, giving

    D^2 F(0)[v,D_1 lambda]=0.                            (10)

Thus the actual total quadratic correction is transverse. This
identity is exact on each admissible finite periodic regulator.
It does not apply coefficientwise to an arbitrary polymer
decomposition. It also does not determine the coefficient of the
gauge-invariant F^2 term or its RG flow.

If one additionally has translation-invariant kernels converging
with a uniform exponential summability bound to an infinite-lattice
kernel, its Fourier multiplier K(p) is analytic near p=0 and
K(p)d(p)=0. Taking p=t e_mu implies K(t e_mu)e_mu=0 for nonzero t,
so continuity gives K(0)e_mu=0 for every mu and hence K(0)=0.
This excludes a nonzero momentum-independent quadratic mass
coefficient in that limit. Those limit hypotheses are explicit;
finite discrete momenta alone do not justify evaluating a Ward
identity at arbitrary continuous momentum.

No rotational/reflection classification, unique marginal coefficient,
one-loop beta function, stable analytic-domain induction, or mass-gap
claim is made here. The result supplies a symmetry identity that
such an extraction must respect.
