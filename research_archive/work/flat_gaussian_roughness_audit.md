# Independent audit of the flat constrained Gaussian roughness calculation

16 October 2026. Audited the complete `work/flat_gaussian_roughness_research.md` and root's shorter `work/gaussian_smooth_ball_obstruction_fragment.tex`. Result: pass, no mathematical correction requested. The covariance is the identified homogeneous flat constrained covariance, not an asserted interacting fluctuation law.

## 1. Physical Gaussian normalization

With physical one-form pairing eta^d times the coordinate sum and density exp[-<Z,KZ>_eta/2] on X, the covariance as an operator under that pairing is C. The covariance matrix of the actual bond values is eta^(-d) times the coordinate matrix of C. One sees this either by testing the covariance identity against coordinate delta functions or by writing the physical orthonormal coordinate vector as eta^(-d/2) delta_e.

The trace identity `E||LZ||^2_(2,eta)=Tr(L C L^T)` consequently has no additional factor. Physical volume supplies that cancellation. A quadratic coupling exp[-S/g^2] scales the field to gZ, rather than changing the physical spacing convention. Per-color calculations use a real basis orthonormal for the normalized trace, so there is no missing color or factor-two normalization.

## 2. Constraint dimension, including zero modes

Q is surjective by QH=I, giving dim ker Q=d(n_f-n_c). The scalar projection R has complementary range ran(G'Q0^T) of dimension n_c because Q0 is onto and G' is invertible, including the scalar constant mode through its positive block penalty. Thus rank R=n_f-n_c.

The longer note correctly proves L(ker Q0)=ran R: orthogonality follows from L G'=I-Q0^T a' Q0 G', and the restriction of L is injective because a nonzero periodic constant has nonzero block mean. Equal dimensions then give equality. The shorter proof's explicit right inverse agrees: T=G'R obeys Q0T=0 and RLT=R, so DT maps ran R into ker Q and has RD^T DT=I there. Therefore RD^T restricted to ker Q is onto, with no hidden dependent constraints.

Rank subtraction gives dim X=(d-1)(n_f-n_c). The proof handles small compatible periodic volumes with incidence multiplicities. At M=1 the fluctuation space is zero, as it should be; the nontrivial probability bound is stated only for M>=3.

## 3. Exact curl variance and the smooth-ball probability

The variational covariance C=J_X K_X^(-1)J_X^T gives `Tr(KC)=dim X` by cyclicity. The physical curl covariance is eta^(-d)dCd^T. Dividing its trace by the number binom(d,2)n_f of positive plaquette coordinates gives `(2/d)(M^d-1)` per real color. In dimension four the exact average is therefore `(M^4-1)/2`, independent of the coarse periodic volume.

At least one deterministic real curl coordinate has variance at least that average. M>=3 provides a fixed lower bound c eta^(-2) on its standard deviation. The event N_alpha(A0+gZ)<=r implies that its selected curl lies in an interval of length at most C r/g. A one-dimensional Gaussian density is everywhere bounded by its maximum 1/(sqrt(2 pi) sigma), regardless of the interval center. Hence the probability is at most min(1,C r eta^2/g), uniformly for every deterministic A0. No independence, concentration estimate, or typicality claim about several coordinates is required.

The conclusion as g_eta/eta^2 tends to infinity follows directly for fixed r. It does not address much faster vanishing couplings, prove any running coupling law, or estimate a non-Gaussian measure. The shorter fragment states these limits accurately.

## 4. Potential variance lower and upper bounds

The bound K<=4d M^2 I gives the inverse-compression trace lower bound `Tr C>=dim X/(4dM^2)`. After the physical covariance conversion the averaged potential variance is Tr C/(d n_c), yielding exactly `(3/64)(M^2-M^(-2))` in d=4.

For the pointwise upper bound the order C<=Gamma<=G0 is valid because C=Gamma-DZD^T and Z is nonnegative at the real flat background; Gamma<=G0 is its covariance subtraction. The cited canceled full inverse formulas were checked against `flat_full_inverse_research.md`, equations (2.4), (2.5), (4.1), (4.2), and (7.2). F_00 is uniformly bounded, its high compression is bounded by the diagonal P_r inverse, and the positive rank correction has E_a bounded away from zero.

On the real central coarse cube and centered odd-M aliases, all fine arguments lie within the principal fine Brillouin interval. For a nonzero integer coordinate r_mu, `|z_mu+2pi r_mu|>=pi|r_mu|`; the elementary sine bound therefore proves P_r>=4|r|^2. The beta envelope in the note agrees with the canceled formula. The normalized scalar and bond averages have the stated product decay, so the absolute beta alias sum is uniformly bounded. The logarithmic shell bound used is conservative and sufficient.

Positivity of F controls central/high cross terms by twice the two diagonal quadratic forms. A fine-point evaluation vector has unit-modulus alias entries in its selected orientation, giving a bound C+2 sum_(r!=0) P_r^(-1). The latter is O(M^2) in d=4. The physical Fourier inverse contributes M^(-d), canceled precisely by eta^(-d) in the covariance conversion. Averaging over the coarse Bloch grid adds no volume factor. Thus the claimed pointwise upper variance C M^2 is correctly normalized, including the canceled zero coarse fiber.

The result is an averaged lower bound plus a pointwise upper bound, not a uniform pointwise lower bound. The note preserves that distinction.

## 5. First differences and rescaling

The inequality ||dA||_2^2<=2||nabla A||_2^2 gives the stated first-difference trace lower bound. The established uniform first-derivative sandwich of G0, combined with C<=G0, gives a uniform physical Hilbert operator bound for nabla C nabla^T. Its trace is bounded by the output dimension d^2 n_f, and each coordinate diagonal is bounded by the operator norm. Multiplication by eta^(-d) then proves the averaged order M^4 and the pointwise upper bound C eta^(-4).

Consequently eta Z and eta^2 nabla Z have uniformly bounded component variances, with nonzero averaged scales. The microscopic Hölder term is indeed bounded by the rescaled gradient supremum because distinct sampled positions are separated by at least eta, up to the fixed orientation convention. Fixed microscopic blocks therefore have a fixed-dimensional Gaussian control. A physical cell contains M^4 sites and is not such a block.

The stated union bound `2N exp(-c t^2)` requires only the pointwise variance upper bound, not independence. It gives the advertised upper scale O(sqrt(log M)) for a physical-cell maximum, without claiming a matching lower bound or a polymer tail estimate.

## 6. Interface meaning

The calculation correctly identifies why a uniform smooth classical chart is not itself a domain containing typical flat quadratic fluctuations at fixed or sufficiently slowly decreasing coupling. It is not an obstruction to Yang--Mills theory. The distinction between smooth backgrounds, microscopic fluctuations, global maxima, and non-Gaussian integration is maintained in both versions. The short qg- fragment needs only the exact rank and trace calculation; the longer note's additional alias and first-difference bounds also pass this audit.
