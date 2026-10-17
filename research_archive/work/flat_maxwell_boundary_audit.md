# Independent audit of the boundary-adapted compact Maxwell lift

16 October 2026. Audited the complete `flat_maxwell_boundary_research.md`, Sections 1--7, against its formulas and the deposited Dirichlet definitions. **The stated linear boundary theorem is ready for promotion. No mathematical correction is required.** Its energy constant is 6144 in four dimensions. Identification with a particular nonlinear retained-history minimizer, or a boundary covariance theorem, remains a separate task.

## 1. Exact one-sided moments

Let M=2h+1>=3 and

    a=2M^2/[(h+1)(h+2)],   p(r)=a(1-3r/M),  0<=r<=h.

The identities

    sum r=h(h+1)/2,   sum r^2=h(h+1)M/6

give

    M^(-1) sum p(r)=a(h+1)(h+2)/(2M^2)=1,
    sum r p(r)=0.

Multiplying p(r)=a(1-3r/M) by p(r), summing, and applying these two identities gives

    M^(-1) sum p(r)^2=a.

Since M=2h+1, a<=8 follows directly from

    2(2h+1)^2<=8(h+1)(h+2).

The outgoing profile is p(h-s), supported on 0<=s<=h; the incoming profile is p(s-h), supported on h<=s<M. Their normalized sums are one and their nontrivial signed first moment about h is zero. The other signed first moment is zero by support. Their normalized squared norms are a<=8. These facts hold exactly for every odd M>=3; no large-M estimate is used. The supplied M=3 and M=5 examples are correct.

## 2. Exact all-row averaging identity

The longitudinal row kernel is

    k_M(s)=(M-|s-h|)_+.

For a source profile supported in 0<=s<M, only rows z=-1,0,1 can read it. On that support, their counting weights k_M(s-Mz) are respectively

    (h-s)_+,   M-|s-h|,   (s-h)_+.

For the outgoing profile, the last weight vanishes by support and the first sums to zero by its first moment. Its central coefficient is

    M^(-2) sum_s [M-(h-s)] psi_out(s)
       =M^(-1) sum_s psi_out(s)=1.

The incoming calculation exchanges the two neighboring rows. Thus both profiles have K_M psi=delta_0, exactly as the interior profile does. Tensoring with the transverse tents gives a delta function in every transverse coarse label. Each basis therefore maps to its designated positive-oriented coarse bond and to zero on every other row.

The claimed all-row equation is stronger than necessary but consistent: extending the coarse datum by zero causes no extra compatibility condition. This is not merely a property of the constructed lift. For any field supported on fine bonds incident to a union of complete centered blocks, a coarse row whose two endpoint blocks are outside the region is automatically zero. Every fine bond in its strings has both endpoints in the union of those two exterior blocks. Consequently the full zero-extended equation and the equation imposed only on incident coarse rows are equivalent.

## 3. Incident-bond support, including orientation

Use integer fine coordinates relative to the source coarse bond. The initial block occupies longitudinal sites [-h,h], while its final block occupies [h+1,3h+1]. A fine bond based at s has endpoints s and s+1.

* For an outgoing source, 0<=s<h places both endpoints in the initial block. At s=h the initial endpoint is in that block and the final endpoint is in the exterior final block. This is an allowed incident crossing bond.
* For an incoming source, s=h is the same crossing bond, now retained because its final endpoint belongs to the inside final block. For h<s<M, both endpoints belong to the final block.
* For an interior source, 0<=s<M places both endpoints in the union of its two retained endpoint blocks.

Every transverse coordinate stays in the common centered transverse block. Therefore no transverse exterior block is used. This proves the support statement for arbitrary unions of full blocks, including nonconvex regions, isolated blocks and holes. The interface value is used once for the chosen source profile; the formulas do not double-count it.

If a plaquette has nonzero curl of the zero extension, it contains a nonzero fine bond. Such a bond has an endpoint in the region, so the plaquette has a vertex there. Hence the full curl norm equals the sum over incident plaquettes; no hidden extension energy is omitted. Further restricting the nonnegative plaquette sum lowers the energy.

## 4. Mixed-profile overlap and constants

For a fixed vector component mu, all longitudinal profiles, whatever their type, are supported inside the same longitudinal tile 0<=s<M relative to their coarse source. All transverse factors are supported inside the centered tiles. These tiles partition the fine bond-base indices. Different source labels consequently have disjoint undifferentiated supports.

Using the independently audited tent bounds gives

    ||Psi_mu,j||_eta^2 <= 8*2^(d-1)=2^(d+2),

and hence the stated lift norm bound.

For a transverse derivative in direction nu!=mu, differentiate the individual basis terms in the linear sum. The profile type is fixed for each source label: it is not a variable of differentiation. The derivative acts solely on the nu tent. A single basis has squared derivative norm at most

    8*16*2^(d-2)=2^(d+5).

At a given fine derivative base, the undifferentiated normal tile and every other transverse tile are unique. In the differentiated direction, a forward difference can read at most two adjacent tent tiles. Thus at most two summands contribute, even when these sources use different profile types. The pointwise inequality |u+v|^2<=2(|u|^2+|v|^2) gives

    ||D_eta,nu(E_M^S B)_mu||_eta^2
       <=2^(d+6) sum_j |B_mu(j)|^2.

Only transverse derivatives of each component occur in its curl. Therefore

    ||d_eta E_M^S B||_eta^2
       <=2 sum_mu sum_(nu!=mu) ||D_eta,nu(E_M^S B)_mu||_eta^2
       <=2^(d+7)(d-1)||B||_1^2.

No uncontrolled longitudinal derivative of the one-sided profile enters. A full-gradient bound is neither proved nor needed. For M=1 the identity lift preserves the incident-bond space and the elementary curl bound 8(d-1)||B||^2 is below the displayed constant.

## 5. Small periodic volumes

Periodize the source basis by summing its images in the covering lattice. In each coordinate the undifferentiated source tiles still partition the fine sites, with one relevant tile image at each fine bond base. A transverse forward difference reads at most two images. If these images represent the same coarse label on a one-cell periodic direction, the same two-term estimate remains valid; summing the unfolded squared contributions counts precisely their multiplicities.

The averaging identity is the periodization of the infinite-lattice delta identity. Neighboring rows can coincide on a short torus, but their coefficients were separately zero before identification. Summing them therefore leaves the same delta function. A periodic direction with one coarse site has no incoming/outgoing source distinction along that direction: both endpoints have the same membership in S. This is consistent with the interior or absent profile rule. No lower bound on the torus side lengths is needed for this linear theorem, provided the lattice incidence sums retain multiplicities.

## 6. Match to the deposited Dirichlet convention

The inspected source is `work/Yang--Mills-LLM-experiment/theorem_0_complete_account_raw_II.tex`.

* Lines 9032--9039 define Lambda-bonds as bonds with at least one endpoint in Lambda, and extend the bond field and site parameters by zero elsewhere.
* Lines 9042--9075 define the global covariant differences, Q^flat and Q_1=Q^flat+D_1 a, rather than a boundary-truncated renormalized average.
* The positivity proposition around lines 9717--9810 repeats the incident-bond convention. Its hypothesis (tilde H1), beginning at line 9743, requires Lambda=B(Lambda'), a union of complete L-blocks. Around lines 9779--9791 it specifies the Q_1 constraint and fields zero off Lambda.
* The distinction between Q_1 and the contour-rooted Q^flat is explicit around lines 9266--9286. At the trivial background, the previously checked identity Q^flat=Q_st-D_1 aT implies Q_1=Q_st.

Thus the **flat one-step Q_1 Dirichlet field space and its rows match the linear boundary theorem with M=L**. The automatic vanishing of exterior rows proved in Section 2 supplies the precise equivalence between a global zero-extended constraint and constraints on incident coarse bonds. This conclusion uses the deposited definitions and an elementary support fact; it does not rely on a pressure estimate or on the source's asserted covariance theorem.

The corrected straight-average source in raw I around lines 24355--24375 also reduces to Q_st at the flat background. Its full-block composition may therefore use the same theorem with M=L^k if the actual boundary region consists of the corresponding complete M-blocks and the actual constrained space has that composition. The retained-history multilevel problem has not been identified with this special case merely by checking one-step support. Its original contour-rooted average and nonlinear minimizing branch remain distinct source interfaces.

For the flat one-step rooted operator, a compactly supported gauge adjustment can be separately constructed using its coarse-center covariance and site gauges supported in the complete-block region. Such an adjustment requires its own explicit operator calculation before transferring any claimed potential-norm bound. The boundary theorem audited here asserts only the straight-average right inverse, so no such extra argument is silently used.

## 7. Promotion status and exact remaining scope

The incident-bond linear theorem, including all-row equality and constants independent of region, scale and periodic volume, is proved and ready for promotion. The source's flat one-step complete-block geometry is compatible with it. It removes the exterior-block collar needed by the original symmetric compact lift in this particular incident-bond setting.

An application to an effective boundary Hessian still needs the actual nonlinear constraint, a C^2 minimizing branch near the trivial datum and feasible competitors in that branch's field space, as in the audited finite-level implicit-function argument. A boundary covariance conclusion additionally needs the appropriate coercive lower bound and operator identification; an energy upper bound alone supplies neither covariance existence nor decay. No claim about a complex analytic radius, independent-current variation, preserved sharp cutoff coordinates, truncated blocks or frozen crossing bonds follows from this note.
