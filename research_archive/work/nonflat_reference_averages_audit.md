# Independent audit of ordinary reference averages

16 October 2026. Audited `nonflat_reference_averages_research.md` in full against its stated inputs and the pinned deposited passages. No mathematical correction found. This is an internal audit, not external certification or a new original-paper verification.

## Source and gauge identities

Checked Raw I:24313--24325 and I:47082--47086: at reference one the corrected map is exactly `C(V)=a_-^{-1} M(V) a_+`. Checked gauge convention and ordinary covariance at I:43018--43026; the complex covariance citation is I:82901--82904. Therefore `M^t(U)=C_t^{g_t}` implies precisely `g_{t+1}=(g_t restricted) a(C_t)`, with that multiplication order. No assumption that the rooted flat average contracts the bounded-field norm enters.

The contour and source-product passages I:23913--23920, I:25147--25155, I:47046--47048 and I:17800--17810 support the two linear averaging definitions used in Sections 5 and 6. The source bond Q is the corrected one-step linearization, whereas the ordinary reference evolves by M; the note preserves this distinction. The independently checked coordinate-conversion note makes that distinction explicit at the derivative level.

## Amplitude and complex domains

The conservative constant `K_Gamma=8 m_Gamma` safely bounds the contour logarithm under the displayed half-unit-ball condition. Ordered products and inverse products satisfy the stated exponential bounds without unitarity. The exact geometric sum `(h_t-eta)/(L-1)` supplies the missing h_t factor in the cumulative gauge. The value `K_V=2+2K_Gamma/(L-1)` accounts for both endpoint gauges and the corrected middle bond. The logarithm bound `||B_t||<=3K_V a` follows from `||log(1+E)||<=2||E||` and `e^s-1<=3s/2` on the stated interval.

The construction is not circular: C_t is already defined by the corrected theorem; its endpoint gauge defines g_t; the resulting V_t is inside the ordinary one-step analytic domain before invoking M(V_t). A fixed further reduction of a suffices at all depths. The dependence radius is a geometric sum of physical one-step radii.

## First differences and curvature

The one-step corrected map is covariant under the **coarse** translation Lh, which is all the proof needs. Translating an input by Lh costs L fine differences, so division by Lh introduces no factor L. Integrating the local derivative along the straight segment between a field and its translate gives exactly the product in (4.2). The interpolation stays in the same complex bounded-field ball.

For the ordinary physical C1 bound, shifting a scale-s endpoint mean by h_t, t>s, preserves that block pattern. Its derivative in the physical potential is O(h_s), so its difference is O(h_s h_t b). The ordered-product difference for g_t sums these terms to O(h_t^2 b), rather than merely O(h_t a). Combining this with the corrected bond difference O(h_t^2 b), then taking the logarithm in a convex half-unit matrix ball and dividing by h_t^2, proves (4.8). All factors and scales check. The t=0 case is handled separately by the initial bound.

The plaquette argument separates opposite-edge variations O(h_t^2 b_t) from a constant-field commutator O(h_t^2 a^2). Gauge conjugation then proves the ordinary curvature bound. The small-amplitude counterexample correctly explains why an initial first-difference hypothesis is necessary for a refinement-uniform curvature statement.

## Actual source Q, scalar Q' and physical normalization

The physical absolute Schur norm has the correct column factor `(H/h)^d`, is submultiplicative across scales, and dominates physical L2. At flatness both its row and physical-adjoint row sums are exactly one. Finite one-step complex analyticity and incidence therefore give an O(||X||) coefficient perturbation with no hidden h-dependent constant. Inserting `X=h_t B_t` and multiplying the actual source factors gives the geometric exponential in (5.3), including the same estimate for physical adjoints.

The scalar contour bound uses only finitely many level-p bonds per leg and the summable ordinary connection amplitudes. Each input vertex belongs to one block, so its physical adjoint coefficient has the stated normalization. The scalar estimate also follows by multiplying one-step covariant scalar averages. This scalar operator is appropriately distinguished from the bond average and from CMP98's differently named main term Q_0.

Finally, each final cell block is bounded by the global physical L2 norm, and only a fixed number of cells occur in a row or column. Thus the weighted cell-Schur conversion loses a fixed range factor, not the number of fine sites. Periodic multiplicities and coarse translation wrapping are harmless for the stated compatible tori.

## Verdict and scope

The full candidate passes: ordinary connection amplitudes, ordinary physical C1 and curvature under the stated initial regularity, and the actual bond/scalar source-average perturbation bounds all follow with constants independent of refinement and volume. It remains restricted to globally trivialized homogeneous small-potential fields and the deposited source conventions. No moving-gauge inverse, nonflat Hessian, source carrier theorem or interacting continuum limit follows merely from this audit.
