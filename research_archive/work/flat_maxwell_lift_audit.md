# Independent audit of the compact flat Maxwell lift

16 October 2026. This note independently checks the compact tensor lift circulated by root for `flat_maxwell_lift_research.md`. The formulas and all stated constants pass. The key requirements are M odd and at least three for the displayed longitudinal formula, the physical spacing eta=1/M, the normalized straight-string operator, and the full periodic or whole-lattice setting. The trivial M=1 case can be treated separately by R=I.

## 1. Longitudinal moments and exact cancellation

Write M=2h+1 with h>=1, s in {0,...,M-1}, and u_s=(s-h)/M. With E denoting the average over these M indices,

    m_1=E|u|=(M^2-1)/(4M^2),
    m_2=E|u|^2=(M^2-1)/(12M^2),
    v=m_2-m_1^2=(M^2-1)(M^2+3)/(48M^4)>0.

Therefore

    alpha=m_2/v=4M^2/(M^2+3)<4,
    beta=-m_1/v=-3alpha,
    psi(s)=alpha+beta|u_s|

satisfies E psi=1, E(|u|psi)=0, and E psi^2=alpha. These are exact equalities, not asymptotic moment conditions.

For the normalized straight-string operator, its one-dimensional longitudinal coefficient at a fine site s of the central coarse-bond cell is

    N_s/M^2,   N_s=M-|s-h|.

Consequently the central lift has averaging coefficient

    M^(-2) sum_s [M-|s-h|]psi(s)
      =E psi-E(|u|psi)=1.

The two neighboring coarse-bond coefficients are, respectively,

    M^(-2) sum_{s>h}(s-h)psi(s),
    M^(-2) sum_{s<h}(h-s)psi(s).

Symmetry of psi makes each equal to one half of E(|u|psi), hence zero. There are no farther neighbors. These identities prove the needed exact longitudinal interpolation, despite the sign changes of psi near its ends.

## 2. Transverse moments and derivative budget

Define

    phi(r)=M(h+1-|r|)/(h+1)^2 for -h<=r<=h,
    phi(r)=0 otherwise.

The triangular sum gives E phi=1. Since phi>=0 and max phi=M/(h+1)<2, one has E phi^2<=2. The discrete derivative D_eta phi(r)=M[phi(r+1)-phi(r)] has exactly 2(h+1) nonzero differences, each of magnitude M^2/(h+1)^2. Thus

    eta sum_r |D_eta phi(r)|^2
      =2M^3/(h+1)^3 <=16.

The derivative sum includes both exterior jumps to zero; omitting them would be incorrect. They are included in the displayed constant.

## 3. Tensor reconstruction and its L2 norm

For each orientation mu and coarse bond with initial point y, the profile is psi in coordinate mu, supported on the fine initial-site indices 0,...,M-1 relative to y, and phi in every transverse coordinate, supported on -h,...,h. The fine vector field is the sum of these profiles times B_mu(y).

For a fixed orientation, the non-derivative profile supports partition the fine initial sites: longitudinal intervals and transverse centered blocks each contain exactly M indices. Thus their squared norm has no overlap factor. In the physical volume norm,

    ||R B||_eta^2
      = (E psi^2)(E phi^2)^(d-1) ||B||_1^2
      <= 4*2^(d-1)||B||_1^2
      = 2^(d+1)||B||_1^2.

The exact equality uses the translation-invariant profiles and the corresponding fine/coarse volume weights. The tensor averaging factors separate. Every transverse factor averages to one and the longitudinal coefficients are those of Section 1, proving Q_M^st R=I exactly.

## 4. Transverse derivatives and curl energy

For nu!=mu, differentiating the mu-oriented profile in direction nu differentiates exactly one transverse phi factor. At each fine initial site, at most two differentiated profiles contribute, including the interface between neighboring cells. Pointwise Cauchy--Schwarz therefore costs at most two.

Integrating and summing the profiles gives

    ||D_eta,nu (R B)_mu||_eta^2
      <= 2*(E psi^2)*(E phi^2)^(d-2)
             *(eta sum |D_eta phi|^2)*||B_mu||_1^2
      <= 2^(d+5)||B_mu||_1^2.

For d>=2, sum the two terms in each plaquette curl with |X-Y|^2<=2|X|^2+2|Y|^2. Each component has d-1 transverse directions, so

    ||d_eta R B||_eta^2
      <= 2^(d+6)(d-1)||B||_1^2.

The potentially large longitudinal derivative of psi does not occur in the Maxwell curl of its own vector component. No bound on the full gradient or divergence is being inferred from this curl estimate.

## 5. Periodic multiplicities and support

The formulas remain valid on the exact torus by periodizing the profiles. Non-derivative supports still form one complete tiling of the fine initial-site indices for each orientation. A transverse derivative has overlap at most two; if those two images represent the same coarse cell on a very small torus, the same pointwise factor-two estimate remains valid. Summing a fundamental domain with profile images is exactly the unfolded sum used above. The neighboring interpolation weights are separately zero, so identifying those neighbors periodically does not spoil Q_M^st R=I.

Each coarse-bond profile is supported inside the union of the two endpoint Lattice blocks at scale M. The included fine bond endpoints also lie in that union. This proves compact support but not arbitrary Dirichlet support preservation. If both endpoint blocks of every active coarse bond lie in an allowed union of full blocks, the lift stays there. For an active coarse bond crossing the boundary of that union, part of the profile generally lies in the exterior endpoint block. Freezing all exterior or crossing bonds can therefore invalidate the lift. A boundary application needs a separate support convention and constraint check.

## 6. Variational upper bound for an actual effective Hessian

For a purely quadratic Maxwell minimization with constraint Q A=B, Q R=I immediately gives

    inf_{Q A=B} ||d_eta A||_eta^2
       <= ||d_eta R B||_eta^2
       <= 2^(d+6)(d-1)||B||_1^2.

Transferring this inequality to the Hessian of a nonlinear effective action requires actual minimization, not merely a selected right-inverse branch. It also requires a nonlinear feasible curve tangent to each proposed lift.

Those curves follow locally at each fixed finite volume and scale from analytic averaging and the linear right inverse. Write the averaging constraint in logarithmic coordinates as Phi(a), with Phi(0)=0 and D Phi(0)=Q. For any A with QA=B, solve

    Phi(tA+R c(t))=tB.

The derivative in c at zero is QR=I, so the implicit function theorem gives c(t)=O(t^2). The resulting fine field satisfies the exact nonlinear constraint and has tangent A. The Wilson action is stationary at the trivial configuration, so the O(t^2) correction does not change its quadratic action coefficient. Comparing the actual constrained minimum with this competitor, and dividing by t^2/2, proves the Hessian upper bound whenever that effective Hessian exists with the stated averaging convention.

A uniform radius for the implicit-function construction is not needed for this flat quadratic comparison. It is not supplied by it either: the argument establishes neither a common complex-background domain nor analytic norm bounds for the nonlinear response.

For the rooted contour constraint, the gradient adjustment established in `flat_maxwell_gap_research.md` Section 4.2 converts a straight-feasible lift into a rooted-feasible lift without changing curl energy. That adjustment can enlarge support and its potential norm is not bounded here. Therefore the energy upper bound transfers under the proved operator identification, but the original compact-support assertion does not automatically transfer to the adjusted rooted lift.

## 7. Audit conclusion

The proposed compact right inverse and its three constants, 2^(d+1), 2^(d+5), and 2^(d+6)(d-1), are correct under the stated normalized straight-string convention. Periodic multiplicities are harmless. The substantive scope limits are the M=1 separate case, Dirichlet support, the distinction between straight and rooted constraints, and the minimization/feasible-curve requirement for the actual nonlinear effective Hessian. None of these invalidates the whole-lattice or periodic flat quadratic theorem.

The complete saved `flat_maxwell_lift_research.md`, Sections 1--9, was subsequently read against this independent derivation. Its tensor construction, longitudinal cancellation, derivative overlap count, periodic extension, Fourier cross-check and finite-level variational argument agree with the calculations above. In four dimensions the stated energy constant is 3072. No substantive mathematical correction was found. For maximal regularity precision, its minimizer assumption should be read as C^2 on a neighborhood of the trivial datum (an analytic branch suffices), rather than mere differentiability at that one point. Mere differentiability supplies only the quadratic Peano coefficient without by itself supplying a classical Hessian.
