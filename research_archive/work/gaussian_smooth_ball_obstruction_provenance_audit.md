# Independent audit of the qg- Gaussian smooth-ball obstruction

Audited `gaussian_smooth_ball_obstruction_fragment.tex` against the broader independent derivation in `flat_gaussian_roughness_research.md`. Verdict: pass, no correction required.

The rank argument using T=G'R is valid: Q_0T=0 and R L T=R make DT an explicit right inverse of RD^T from ker Q onto ran R. Since Q is onto and rank R=n_f-n_c, dim X=3(n_f-n_c) follows exactly per real color. The positive restricted variational covariance then gives Tr(d C d^T)=dim X by cyclicity.

The physical covariance conversion is essential and correctly included. The value-coordinate covariance matrix is eta^{-4} times the coordinate matrix of the physical covariance operator; the same factor applies to d C d^T. Dividing its diagonal trace by the 6 n_f plaquettes gives exactly (M^4-1)/2. This is not a pointwise equality at every within-cell plaquette, and the fragment correctly uses only existence of one component with variance at least the average.

The selected marginal remains a one-dimensional centered Gaussian regardless of correlations among all other coordinates. A deterministic background merely translates the interval imposed by the smooth-ball event. Its interval length is O(r/g), while the standard deviation is at least c eta^{-2}; the maximum-density bound therefore gives min(1,C r eta^2/g), uniformly in that interval's center. No independence, concentration theorem, or typical maximum estimate is needed.

The coupling condition g_eta/eta^2 -> infinity is explicit and correct. The conclusion is about this Gaussian reference and a fixed physical smooth ball, not arbitrary coupling sequences or an interacting law. The final distinction between component/averaged variances, a growing supremum and polymer activity estimates is accurate. The statement is fully consistent with the broader potential and first-difference variance calculations in the independent research note.
