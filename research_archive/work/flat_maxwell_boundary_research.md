# A boundary-adapted compact Maxwell lift for incident-bond Dirichlet data

16 October 2026. Separate extension of `flat_maxwell_lift_research.md`, pending independent audit. The whole-lattice and periodic note is unchanged. This establishes an explicit linear construction for a particular complete-block Dirichlet convention; no nonlinear source identification or general boundary convention is asserted.

## 1. Exact domain and constraint convention

Let `S` be any finite collection of coarse lattice sites, or any subset of a periodic coarse lattice. The coarse spacing is one. Fix odd `M=2h+1>=3` and fine spacing `eta=1/M`. The fine site region is the union of full centered blocks

\[
 \Lambda=B_M(S)=\bigcup_{j\in S}
      \{j+\eta r:r\in\{-h,\ldots,h\}^d\}.
                                                               \tag{1.1}
\]

Retain each positively oriented coarse bond `(j,j+e_mu)` having **at least one endpoint** in `S`. Retain each fine bond having at least one endpoint in `Lambda`. All other field coordinates are zero. Thus fine crossing bonds are variables, not frozen bonds. A coarse datum `B` is extended by zero to every coarse bond with both endpoints outside `S`.

The constraint is the **full** normalized straight-string average applied to the zero-extended fine field:

\[
 (Q_MA)_\mu(j)
 =M^{-d-1}\sum_{r\in\{-h,\ldots,h\}^d}
           \sum_{t=0}^{M-1}
             A_\mu(j+\eta r+\eta t e_\mu).           \tag{1.2}
\]

In particular boundary strings are not truncated and renormalized. They read zero on excluded fine bonds. The construction below gives `Q_M A=B` on **all** coarse bonds, so it also obeys any formulation that imposes only the retained coarse rows and treats the other data as zero.

Use the physical volume norm and curl of the preceding note:

\[
 \|A\|_\eta^2=\eta^d\sum_{x,\mu}|A_\mu(x)|^2,
\]
\[
 (d_\eta A)_{\mu\nu}(x)
 =\eta^{-1}[A_\nu(x+\eta e_\mu)-A_\nu(x)
            -A_\mu(x+\eta e_\nu)+A_\mu(x)],\quad\mu<\nu.
                                                               \tag{1.3}
\]

The energy is the full curl norm of the zero-extended fine field. Every nonzero curl plaquette contains a nonzero incident bond and therefore at least one vertex of `Lambda`; hence this equals the sum over all plaquettes incident to `Lambda`. Restricting the plaquette sum further can only decrease this energy.

**Proposed boundary theorem.** For `d>=2`, there is a real linear right inverse `E_M^S` whose output is supported on the retained fine bonds and obeys

\[
 Q_ME_M^SB=B,
 \qquad \|E_M^SB\|_\eta^2\le2^{d+2}\|B\|_1^2,
\]
\[
 \boxed{\quad
 \|d_\eta E_M^SB\|_\eta^2
 \le2^{d+7}(d-1)\|B\|_1^2.
 \quad}                                               \tag{1.4}
\]

The constants do not depend on `M`, the region, its number of boundary components, or the torus volume. For `M=1`, use the identity on retained bonds and the elementary lattice curl bound. In four dimensions the displayed boundary energy constant is `6144`.

## 2. Recalled interior profiles

Use the transverse tent from the whole-lattice construction:

\[
 \phi_M(r)={M\over h+1}\left(1-{|r|\over h+1}\right)
 \quad(|r|\le h),\qquad \phi_M(r)=0\quad(|r|>h).
\]

It satisfies

\[
 {1\over M}\sum_r\phi_M(r)=1,
 \quad {1\over M}\sum_r\phi_M(r)^2\le2,
 \quad {1\over M}\sum_r|M[\phi_M(r+1)-\phi_M(r)]|^2\le16.
                                                               \tag{2.1}
\]

For a coarse bond with both endpoints in `S`, use the interior longitudinal profile `psi_M` from that note. It is supported on `s=0,...,M-1`, is even about `h`, has normalized sum one, has zero separate first moments about `h`, and has normalized squared norm at most four.

The new issue is a coarse bond with exactly one endpoint in `S`. Its interior profile would use fine bonds internal to the exterior endpoint block. We replace only that longitudinal profile.

## 3. Explicit outgoing and incoming profiles

Set

\[
 a_M={2M^2\over(h+1)(h+2)}\le8.                       \tag{3.1}
\]

For an **outgoing** bond, whose initial coarse site is inside and final site outside, define

\[
 \psi_M^{\rm out}(s)=
 \begin{cases}
 a_M\left(1-{3(h-s)\over M}\right),&0\le s\le h,\\
 0,&\text{otherwise}.
 \end{cases}                                         \tag{3.2}
\]

For an **incoming** positive-oriented bond, whose initial site is outside and final site inside, define

\[
 \psi_M^{\rm in}(s)=
 \begin{cases}
 a_M\left(1-{3(s-h)\over M}\right),&h\le s\le M-1,\\
 0,&\text{otherwise}.
 \end{cases}                                         \tag{3.3}
\]

These profiles are reflections about `s=h`. The value at the interface bond `s=h` is included in both formulas; it is a retained crossing bond in either case. It is included only once in the profile selected for a given coarse bond.

### 3.1 Moment proof

It suffices to use `r=0,...,h` and the sequence

\[
 p(r)=a_M(1-3r/M).
\]

The elementary sums are

\[
 \sum_{r=0}^h r={h(h+1)\over2},\qquad
 \sum_{r=0}^h r^2={h(h+1)M\over6}.
\]

Consequently

\[
 {1\over M}\sum_{r=0}^h p(r)
 ={a_M(h+1)(h+2)\over2M^2}=1,
\]
\[
 {1\over M}\sum_{r=0}^h{r\over M}p(r)=0.             \tag{3.4}
\]

Multiplying `p=a_M(1-3r/M)` by `p` and using these two moments gives the exact norm identity

\[
 {1\over M}\sum_{r=0}^h p(r)^2=a_M\le8.              \tag{3.5}
\]

There is no derivative estimate for these longitudinal profiles and none is needed by the curl. They can change sign; the cancellation of a neighboring average requires that possibility.

At `M=3`, `a_M=3`. Both one-sided profiles put value three on the central interface bond and zero at the other available site, in agreement with the interior profile. At `M=5`, `a_M=25/6`; expressed in the distance `r` from the interface, the values are `25/6, 5/3, -5/6`. Their sum is five and their first moment is zero.

## 4. Exact coarse averages of the one-sided profiles

For a source coarse bond starting at longitudinal coordinate zero, the one-dimensional average is

\[
 (K_Mp)(z)={1\over M^2}\sum_{s\in\mathbb Z}k_M(s-Mz)p(s),
 \qquad k_M(s)=(M-|s-h|)_+.
\]

On the interval `0<=s<M`, write `w=s-h`. Only coarse rows `z=-1,0,1` can contribute, with weights

\[
 (-w)_+,\qquad M-|w|,\qquad(w)_+,
\]

respectively.

For `psi_out`, `w<=0`. The row `z=1` is identically zero. Row `z=-1` is the first moment `h-s` and vanishes by (3.4). Row zero equals the normalized zeroth moment minus this first moment, so it is one. For `psi_in`, the same reasoning is reflected: row `z=-1` vanishes identically and row `z=1` vanishes by the moment condition. Again row zero is one. All further rows are zero by support.

Thus each of the three available longitudinal profiles, interior, outgoing and incoming, has the same exact coarse averaging identity

\[
 K_M\psi^{\rm type}=\delta_0.                       \tag{4.1}
\]

No approximate boundary equation or normalization correction remains.

## 5. Source bases, support and boundary orientation

For a coarse positive `mu`-bond starting at `j`, choose its profile according to its endpoints:

| Initial site `j` | Final site `j+e_mu` | Profile |
|---|---|---|
| in `S` | in `S` | `psi_M` |
| in `S` | outside `S` | `psi_out` |
| outside `S` | in `S` | `psi_in` |
| outside `S` | outside `S` | no source, because `B_mu(j)=0` |

Define

\[
 \Psi^S_{\mu,j}(x)
 =\psi^{\rm type}_M(Mx_\mu-Mj_\mu)
           \prod_{\nu\ne\mu}\phi_M(Mx_\nu-Mj_\nu),
\]
\[
 (E_M^SB)_\mu(x)=\sum_jB_\mu(j)\Psi^S_{\mu,j}(x).     \tag{5.1}
\]

For an outgoing edge, the nonzero fine bond bases have normal coordinate `s=0,...,h`. Those with `s<h` have both endpoints in the initial block; `s=h` is precisely the interface-crossing bond, whose initial endpoint is in that block. Thus every used fine bond is retained.

For an incoming edge, the bases have `s=h,...,M-1`. At `s=h`, the final endpoint `h+1` is the first site in the final centered block. At `s>h`, both endpoints are in the final block. Every used fine bond is again retained. The transverse support is the common centered transverse block of the two coarse endpoints, so there is no leakage through a transverse exterior block.

For an interior edge, both endpoint blocks are allowed and the full interior basis is allowed. This proves support preservation even for a nonconvex union of blocks or a region with holes. Complete blocks and incident crossing bonds are both used essentially in this proof.

The transverse block averages are delta functions in their coarse transverse labels, while the longitudinal average is (4.1). Therefore every basis maps to exactly its source coarse bond, including all exterior rows. This proves `Q_M E_M^S B=B` on the zero-extended coarse space.

## 6. Uniform energy and basis-overlap count

For a fixed component `mu`, every selected source basis remains inside the same longitudinal tile `0<=s<M` and the same transverse centered tiles as before. Different coarse source labels therefore have disjoint fine bond-base supports, even though their profile types can differ. The squared norm product is at most

\[
 8\,2^{d-1}=2^{d+2}.
\]

This gives the norm bound in (1.4).

For `nu!=mu`, the derivative acts only on a transverse tent; the longitudinal profile is a fixed function for that source label, independent of the fine transverse coordinate. There is no differentiation of a position-dependent choice of profile type. Differentiate each linear basis term before summing. Its squared derivative norm is at most

\[
 8\cdot16\cdot2^{d-2}=2^{d+5}.                      \tag{6.1}
\]

At a given derivative bond base, two neighboring transverse tiles can contribute, and no others. The normal-coordinate tile and every other transverse tile are fixed uniquely. Thus the overlap multiplicity remains at most two, including where one source uses an interior profile and the other a one-sided profile. Cauchy--Schwarz gives

\[
 \|D_{\eta,\nu}(E_M^SB)_\mu\|_\eta^2
 \le2^{d+6}\sum_j|B_\mu(j)|^2.                     \tag{6.2}
\]

Finally,

\[
 \|d_\eta E_M^SB\|_\eta^2
 \le2\sum_\mu\sum_{\nu\ne\mu}
                       \|D_{\eta,\nu}(E_M^SB)_\mu\|_\eta^2
 \le2^{d+7}(d-1)\|B\|_1^2.                         \tag{6.3}
\]

This also bounds any Dirichlet action obtained by keeping only a subset of these plaquette terms. The fine extension is exactly zero on excluded bonds, so no separate extension energy has been omitted.

On a periodic lattice, the same computation holds after counting geometric lattice cells and any coincident local contributions with multiplicity. The three coarse row contributions in Section 4 add to the same delta function after periodic identification. A very short torus does not require dropping a row or a boundary term.

## 7. What the boundary result does and does not supply

For the specified incident-bond convention it gives the uniform upper bound

\[
 \inf\{\|d_\eta A\|_\eta^2:
       A\text{ supported on incident fine bonds},\ Q_MA=B\}
 \le2^{d+7}(d-1)\|B\|_1^2.                         \tag{7.1}
\]

It is a purely linear, real statement. It may be inserted into the finite-level implicit-function/variational comparison of the whole-lattice note only after checking that the actual nonlinear constraint and minimizer use this boundary convention and this flat derivative, or a proved energy-preserving gauge correction of it.

The construction does not cover blocks truncated by the boundary, a different normalization of truncated averaging rows, or a convention freezing the crossing fine bonds. It does not itself identify a multilevel rooted nonlinear constraint on a retained history with (1.2). It also supplies no uniform complex analytic radius, no free-current response bound, and no preservation statement for the original sharp cutoff coordinates.

Unlike the original compact lift, this extension does not need an exterior-block collar for incident coarse source bonds. That improvement is confined to the exact complete-block geometry and the explicit one-sided moment profiles proved above, pending independent audit before promotion.
