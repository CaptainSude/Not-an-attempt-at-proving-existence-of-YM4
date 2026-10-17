# CMP116 interaction bridge: what can be imported, and into which theorem

17 October 2026. Focused source-interface note. The original PDF was read through its extracted text; some displayed coefficients are lost in OCR. Such coefficients are located below rather than silently reconstructed. The repository and outputs were not modified.

## 1. The appropriate original result

The relevant result is **Lemma 2, pp.10–11, equations (1.41)–(1.43)** of [Bałaban, CMP116 (1988)](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-4penm4k7hc.pdf), followed by **Lemma 3, p.20, (2.38), and the logarithmic estimate (2.41), p.21**. Lemma 2 covers the full exponent, including the inherited-action difference, rather than just the Wilson cubic remainder. Its fluctuation radius is the physical-field condition `g|B|<epsilon1`; its localized functions read the background, independent current and fluctuation in their localization domain. Lemma 3 supplies the specialized integration of these overlapping terms. This is already an integration theorem; no second abstract integration theorem is inherently needed.

The complete domain is (1.34), p.9:

    U^c_(k+1)(Y,(1+beta)alpha0,(1+beta)alpha1,alpha0)
              × {B : |B| < epsilon1/g on Y}.

The first factor is the orbit domain defined in [CMP109](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf), pp.262–263, (1.10)–(1.16). In particular it includes the condition involving reconstructed backgrounds on subregions, not merely a global sup-norm ball. The analytic operator/minimizer deformations used in CMP116 pp.3–6 are also inputs to the localization argument. The original published result can be cited in its own setting; importing a modified carrier or domain still requires a separate containment/matching statement.

## 2. Exact algebraic format and deposited transcription

To avoid confusing the refinement `M=L^k` in our flat notebooks with Bałaban's fixed localization-block size, denote the latter here by `M_loc`. The source's localized exponent has the format

    P^(k)(g,U,J,B) + inherited difference = sum_(Y in D_k) V_Y,
    V_Y = (1/2)<B,Q_Y(U,J,B)B> + V''_Y(U,J,B).

The numbered source displays controlling these two terms are respectively (1.43) and (1.36). The latter is transcribed at Raw I:30590–30597 as

    |V''_Y| <= E0 epsilon1 C1 M_loc^q exp(C2 kappa1)
                        exp[-(1-2delta) kappa d_k(Y)].

Raw II:3190–3208 records the same format, including the field-dependent quadratic kernel. Its citation to `(1.43)` of CMP109 at that location is a reference typo: the source format is CMP116 (1.43), as confirmed by CMP116 Lemma 2 and by Raw II:11178–11188. The kernel's dependence on the physical fluctuation vanishes at zero; the bounded remainder need only vanish to first order. The exact small-field exponent, including Haar, the constraint Jacobian and exponential gauge terms, is displayed at Raw II:73910–73945.

The domain weight `d_k(Y)` is a normalized minimum tree length meeting all `M_loc` cubes of Y; it is not merely the diameter. Its definition is at CMP109 §1 and transcribed at Raw I:62752–62760. The source uses geometric sums (1.26)–(1.28), rather than an unspecified count of arbitrary fine-bond subsets.

The original output estimate is located at CMP116 (2.41): it retains exponential decay in `d_(k+1)(X)` and a prefactor proportional to epsilon1, with constants fixed before the coupling ceiling. The deposited statement of the original-sized small-field step is Raw I:4135–4189. Its subsequent altered-radius clause is a stronger transfer statement and should be checked as such.

## 3. What happens at a logarithmic cutoff

The numerical inclusion is elementary. Fix the source constants first, and take

    R(g)=c(log g^-2)^p,       p>1/2.

Then `gR(g)<epsilon1/2` for all sufficiently small g. Thus every real cutoff point lies strictly inside the original physical-field analytic radius. One must apply this statement to the actual independent fluctuation variable used by the source, including the exact constraint chart; it is not a license to replace that variable by a gauge-equivalent one.

Here is the independent analytic estimate that makes the transfer useful. Suppose the localized quadratic kernel and bounded remainder have the same localization coefficients as in the original lemma, and are holomorphic on a fixed physical field ball `|z|<epsilon1`. Suppose their relevant zero-field values vanish. Radial Schwarz/Cauchy estimates on the smaller ball give, schematically,

    ||Q_Y(gB)|| <= a_Y gR,
    |V''_Y(gB)| <= a'_Y gR,

after fixed inverse powers of epsilon1 have been incorporated into `a_Y,a'_Y`. On the real cutoff,

    |V_Y(B)| <= (1/2) a_Y gR sum_(b in Y)|B_b|^2 + a'_Y gR.

Hence a cutoff sup bound is `O(g R^3)` times a localized coefficient and a polynomial support-count factor. The support polynomial can be absorbed into a reserved fraction of exponential tree decay. This does not require the auxiliary radius `P(g)=C(log g^-2)^p1` to contain R(g); it uses the original fixed physical-field radius instead. Raw II:11178–11195 already makes this distinction, obtaining `g(T^C)^3` for the cubic/quadratic-kernel pieces and `gT^C` for merely vanishing pieces.

Changing the real cutoff from epsilon1/g to R(g) is nevertheless a change of the integral. At the level of the original proof, the required additional verification is that its bad-bond gain still dominates all entropy costs: replace the old threshold by R(g) in (2.22), (2.26), (2.31), while retaining `gR(g)<epsilon1`. The Gaussian gain is of order exp(-c R(g)^2), so the numerical domination holds once all geometric constants are fixed. This checks the scale of the required bound; exact preservation of the localized representations and analytic operator neighborhoods is a source-matching obligation, not a consequence of the numerical limit alone.

## 4. The source theorem versus the present oi theorem

The published integration proof is tailored to its own localized quadratic kernels and Gaussian conditioning. It is therefore a natural direct route once its hypotheses are matched. A mechanical application of our current overlapping-interaction theorem requires a stronger numerical verification than just citing Lemma 2.

The oi input norm is

    epsilon_oi = sup_i sum_(Y contains i)
             v_Y K_G^|Y| exp[4|Y|+kappa_oi ell(Y)],
    v_Y = sup_cutoff |exp(V_Y)-1|.

Its `|Y|` counts the cells of the Gaussian expansion. If these are fixed current-unit cells, a localization region with N source cubes contains O(M_loc^4 N) such cells. If one instead makes a source cube into one Gaussian cell, its coordinate dimension is O(M_loc^4), so log K_G itself incurs that cost. These are equivalent obstacles for the displayed norm.

To see the quantitative requirement, assume the coefficient estimate supplied by the source has

    v_Y <= epsilon(g) P(N) exp[-rho d_k(Y)]

with P polynomial. For fixed-dimensional lattice geometry there is a constant c such that `N<=c(1+d_k(Y))`; covering an Euler traversal of a minimum tree by fixed-size balls proves it. Also `ell(Y)<=c' M_loc(1+d_k(Y))` in unit-cell distances. A sufficient conversion into the oi norm therefore needs spare decay at least

    rho > c M_loc^4 (4+log K_G)
                      + c' kappa_oi M_loc + geometric entropy.

The actual factors can be optimized, but a factor proportional to the number of tested fine coordinates cannot be dropped. The original parameter hierarchy takes M_loc large after the required localization exponents; it does not assert this displayed stronger inequality. Making g smaller decreases epsilon(g), but cannot cure a negative exponential support exponent for arbitrarily large Y. Thus **the published coefficient bound is not automatically the current oi norm**.

This is a limitation of that sufficient norm, not a failure of the original integration result. The source's complex comparison uses a controllably small quadratic/determinant error; its cost is O(alpha5) times the volume, and it chooses `(L M_loc)^4 alpha5` small. See CMP116 (2.16)–(2.25) and the parameter discussion immediately preceding Lemma 3. Its specialized organization avoids paying a fixed large Gaussian absolute-density factor per coordinate.

There is a possible repair to oi if an independent route is wanted. Keep the relative perturbation parameter epsilon free in the tested-marginal Gaussian estimate rather than fixing it to 1/4. Its density factor is

    [(1+s)/(1-s)]^(r/2),       s=epsilon/(1-epsilon),

so for epsilon small its logarithm is O(epsilon r). Take source localization cubes as the Gaussian cells, so the fixed support weight exp(4|Y|) counts N cubes rather than M_loc^4 N unit cells. Use similarly small covariance Cauchy radii around each real forest-deformed covariance. Choosing epsilon of order M_loc^-4 then makes the dimension cost harmless; derivative constants grow by a fixed inverse power of epsilon, which a later smaller coupling may absorb. A complete revised forest proof and a relative-background hypothesis would still be needed. This is a viable refinement, not an already proved application of oi as printed.

## 5. Strict background support and the first remaining hypothesis

The original localized V_Y are functions on a gauge/current orbit domain restricted to Y. This is useful strict source dependence in the original variables. Our Gaussian strict-support theorem instead asks for a specified product background domain and a small support-valued expansion of the actual reduced precision. Neither weighted response locality of the classical minimizer nor the mere existence of a localized V_Y supplies that precision expansion. Composition with a globally defined stationary background can also reintroduce dependence outside Y unless its response is localized explicitly.

For the **original homogeneous source step**, the next efficient bridge is therefore to state the original CMP116 integration theorem with its exact field domain and verify that the object we integrate is that object. The checklist is concrete:

1. The background/current pair and every restricted reconstruction used by (1.34) belong to the original CMP109 domain; or a specific smaller domain is proved to map into it using the cited original results.
2. The operator/minimizer walk deformations used in the proof are the source deformations, with their original analytic bounds. Our flat weighted kernels alone do not identify those deformations.
3. The fluctuation coordinate, pivot map, measure, fixed cutoff and exponent are those of CMP109 (2.12)–(2.13), with all normalization factors retained.
4. If the cutoff or hereditary carrier is modified, the exact corresponding proof transfer is checked. The interior radius is not replaced by CMP119's boundary-specific (3.43).

The original literature may be invoked for its original assertions; there is no need to reprove each cited operator lemma. The first unresolved bridge in the present self-contained modules is their identification with this full local orbit-domain/walk input, beyond the now-proved flat homogeneous covariance and classical smooth branch. The general retained-history problem is broader still. No absence claim about published results is made here.
