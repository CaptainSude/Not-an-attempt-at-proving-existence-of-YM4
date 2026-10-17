# The sharp cutoff after pivot elimination

17 October 2026. Focused source audit; pinned repository and output files
were not edited. The issue is the exact integration window, not merely the
existence or regularity of the pivot chart.

## 1. Finding and verification level

The premise that the original CMP109 cutoff necessarily contains independent
indicators on **all** relative-field bonds is not supported by the checked
source passages. The published CMP116 integration proof explicitly uses
retained, pivot-removed bond sets in its cutoff decomposition. CMP109's
sentence immediately after (2.9) also treats pivot bounds as consequences
of the preceding restrictions. This points to an original retained-bond
cutoff, rather than a later replacement of a moving all-bond window by a
rectangular one.

There is one precise verification limit: the accessible primary PDF text
extraction drops the product subscript in CMP109 (2.9). I have not visually
read that subscript and do not present an inferred transcription as a
verified image reading. The CMP116 retained-bond definition and its use
in the cutoff expansion are readable in the primary extraction. The
algebra below proves the fixed-window conclusion for exactly that
retained-bond convention.

## 2. Primary locations and the deposited account

Original papers:

- [CMP109, Part I, DOI 10.1007/BF01215223](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf).
- [CMP116, Part II, DOI 10.1007/BF01239022](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf).

**CMP109:** (2.9), journal p.266, defines the cutoff. The continuation on
p.267 says that these restrictions also control the eliminated pivot
variables, with a changed constant. The same page gives the support of
\(h\), the constraint-linearizing change, and its quadratic remainder.
Pivot elimination and the resulting integral are on p.268, (2.12)–(2.13).

**CMP116:** on p.12, immediately before (2.3), the set of tested bonds in
\(Y_0\) explicitly excludes \(b_0(c)\). Formula (2.3) expands the cutoff
into retained-bond bad sets. Equations (2.5)–(2.6) condition and whiten the
Gaussian; (2.14), p.15, keeps the cutoff as a function of the real retained
field while the Gaussian operators are deformed. The analyticity discussion
on pp.14–15 uses this representation. I did not identify, in these steps,
a theorem replacing an additional moving pivot indicator by a fixed one.

In the pinned deposit, Raw II:73888–73890 describes the cutoff as a product
over bonds but does **not** reproduce the index set and does not explicitly
say “all bonds.” Raw II:73891–73910 records the change and pivot elimination.
The recovered relative field is displayed at Raw II:73963–73967. Raw I:4333–4344
explicitly defines pivot-removed bond sets in its integration setup. The
unindexed wording in Raw II should therefore not be promoted into a new
all-bond definition without a further statement.

Access record: the original article text was read through the public
primary-PDF URLs above. The existing local PDF placeholders are empty;
a normal retrieval did not produce PDF bytes. The screenshot calls
returned no page image. The normal Project Euclid page requested an
additional security check, at which point that route was stopped;
Springer's normal PDF endpoint was unavailable through the tool. No gate
was bypassed. These limits matter only for the unrendered CMP109 subscript.

## 3. Exact retained-window calculation

Let \(I\) be the retained bonds and \(P=\{b_0(c)\}\) the pivots.
Write \(C_V\) for the source extension map, not the covariance. It satisfies

\[
 (C_V z)|_I=z,\qquad (h_V w)|_I=0.
\]

At fixed positive real coupling \(g\), the recovered relative field is

\[
 \Psi_V(gz)=g C_Vz-h_V\widetilde D_V(g C_Vz),
 \qquad \widetilde D_V(0)=D\widetilde D_V(0)=0.
 \tag{3.1}
\]

Consequently, exactly and without a small-error estimate,

\[
 \Psi_V(gz)|_I=gz.
 \tag{3.2}
\]

If the source cutoff is

\[
 \chi^{I}_\varepsilon(B')
 =\prod_{b\in I}\mathbf1_{\{\|B'(b)\|<\varepsilon\}},
\]

then its pullback is the fixed rectangular window

\[
 \chi^{I}_\varepsilon(\Psi_V(gz))
 =\prod_{b\in I}\mathbf1_{\{\|z(b)\|<\varepsilon/g\}}.
 \tag{3.3}
\]

Neither the background dependence of \(C_V,h_V,\widetilde D_V\) nor its
complex analytic continuation moves this real integration window. The
unchanged retained coordinates are the reason. The norm indicator itself
is not analytically continued.

Replacing the retained threshold \(\varepsilon/g\) by a prescribed
logarithmic threshold \(R(g)\) still gives a fixed real window. It changes
the integral and requires the appropriate cutoff-budget transfer; it is
not an equality of two choices of threshold. On this window, the analytic
chart and every inherited term must be defined for the **recovered whole
field**, including its pivot components.

## 4. What a genuinely all-bond cutoff would do

For comparison, a separately prescribed cutoff on all relative bonds has
the exact pullback

\[
 \chi^{I\cup P}_\varepsilon(\Psi_V(gz))
 =\prod_{b\in I}\mathbf1_{\{\|z(b)\|<\varepsilon/g\}}
  \prod_{p\in P}\mathbf1_{
   \{\|g(C_Vz)(p)-(h_V\widetilde D_V(gC_Vz))(p)\|<\varepsilon\}}.
 \tag{4.1}
\]

The second product is generally a background-dependent nonlinear real
window. It cannot be omitted from a claimed exact identity. It is not a
bounded holomorphic interaction multiplier merely because its argument is
holomorphic.

This is already visible in a one-variable example. Let the retained
coordinate be a standard Gaussian \(z\), and let a pivot equal \(az\).
The integral with both unit cutoffs is

\[
 Z(a)=\mathbb P\{|z|<\min(1,|a|^{-1})\}.
\]

For positive real \(a\), this function has a derivative jump at \(a=1\).
Thus small analytic changes in a pivot map do not by themselves give
analyticity of an all-bond sharply truncated integral. This example is a
warning about an altered window, not a counterexample to the retained
source construction.

## 5. A useful redundancy criterion, with its exact scope

Suppose the actual chart has uniform bounds on its analytic neighborhood,

\[
 \|C_V\|_{\infty\to\infty}\le K,
 \qquad
 \|h_V\widetilde D_V(x)\|_\infty\le K_2\|x\|_\infty^2.
\]

For \(\|z\|_\infty<R\), formula (3.1) then gives

\[
 \|\Psi_V(gz)\|_\infty
 \le gKR+K_2g^2K^2R^2.
 \tag{5.1}
\]

Hence an **additional** pivot cutoff with a strictly larger threshold than
the right side is redundant on that retained window. This can verify
containment in a larger analytic chart. It does not prove redundancy of a
pivot cutoff having the same threshold \(gR\). Even a linear constraint
\(p=-z_1-z_2\) shows why the latter implication fails.

For fixed \(K,K_2\) and \(R(g)=c(\log g^{-2})^p\), the right side of (5.1)
tends to zero. A fixed positive analytic radius can therefore contain the
whole recovered field after lowering the coupling ceiling. The required
source uniformity of \(K,K_2\) and of all restricted reconstructions remains
an explicit hypothesis.

## 6. Consequence for the current Gaussian modules

For the retained-bond integral used by the readable CMP116 cutoff
decomposition, the moving-pivot-window objection is removed by (3.2)–(3.3).
No contour deformation or localized replacement error is needed for that
particular coordinate fact. The original conditioning/whitening step is a
Gaussian operation, not evidence for a general moving-indicator theorem.

The exact physical-background reduced precision still has to match the
source chart and gauge, and its complex neighborhood and local coefficient
norms still have to be verified. In retained-history or modified-window
versions, every extra field, contour, pivot, and regional characteristic
function must be tracked separately. The original retained-coordinate
identity does not dispose of such extra conditions.

The narrow remaining source-reading task is a direct image verification
of the CMP109 (2.9) product subscript. The present conclusion rests on the
explicit retained-bond setup of CMP116 plus the exact source coordinate
algebra; it should be cited at that verification level.
