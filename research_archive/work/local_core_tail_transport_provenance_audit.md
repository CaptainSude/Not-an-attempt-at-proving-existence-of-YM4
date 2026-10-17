# Independent audit: local-core/small-tail analytic transport

17 October 2026. Auditor: provenance. Source read in full: `work/local_core_tail_transport_research.md`. This audit concerns the displayed abstract estimate and its fixed-parameter consistency argument, not an actual quantum iteration.

## Verdict

The mathematical proof passes. One scope clarification was sent to the author and has now been incorporated: the total functional and absolute convergence in (2.2) are literal in finite compatible volume. On the infinite lattice the hypotheses imply an anchored local activity expansion, not absolute convergence of the global sum over all carriers. For example, equal nonzero constant singleton activities satisfy (1.1) and give an infinite total sum. This does not affect the stated anchored norm estimate or any finite-volume application.

## Checks

1. **Cauchy about the local core.** The componentwise margin `||f_H^0|| <= b-m` permits the product Cauchy bound `||c_(H,nu)|| <= e_H m^(-|nu|)` uniformly in the target field. If desired use radii below `m` and pass to the limit. The coefficients are holomorphic on the target domain and read only `K0(H)`. There is no scalar-coordinate expansion of the core and therefore no hidden `D|H|` cost from its full amplitude.

2. **Tail expansion and multiplicities.** Expanding each scalar tail occurrence separately gives exactly the multiindex sum `(1-t)^(-D|H|)`. Repeated support choices already carry the powers' multiplicities; no further factorial is needed. The supremum over roots and scalar components in (1.6) is sufficient for this estimate. The stronger complete-fiber maximum-inside-support norm is an admissible source for it, not an implicit interchange of maximum and sum.

3. **Carrier geometry and rerooting.** Each tail tree attaches at a root in the connected core. Thus `|K| <= |K0|+T` and `d(z,pi(H)) <= h0+T` for every final anchor. The extra `exp(delta h0)` is necessary and present. Combining the cardinal/spatial weight with the tail-tree budget gives precisely `c1 beta+alpha_D(t) <= a0` and `beta+delta <= kappa`. Summing old anchors through `pi` gives the stated fiber factor `F S_delta`, including anchors on added trees or in the core halo.

4. **Constant terms.** The full estimate includes the zero Taylor term. The separate vacuum statement is correct under `f_H^0(0)=0` and zero tails at zero. Coefficientwise subtraction of values at zero costs at most two, and the warning against treating a function of a remaining fluctuation variable as a vacuum constant is appropriate.

5. **Core/tail decomposition.** Restricting old support labels to `X subset B_ell(i)` gives a core whose actual component amplitude is bounded by the original absolute family norm `S(r)`. A label outside that ball has rooted Steiner length greater than `ell`, so spending `kappa_0-kappa_t` proves the exponential tail factor in (4.3). This uses the supported-family constant `C_A`, not only the smaller pointwise full-field constant `C_0`.

6. **Auxiliary grouping.** For `ell <= J-1`, each projected neighborhood lies in the coordinatewise one-neighbor halo, hence graph distance at most `d` from the projected roots and cardinal factor at most `3^d`. The projected root set is explicitly assumed connected. Grouping the tail coefficient families costs at most `J^d`; the actual componentwise core amplitude does not acquire that loss. The rooted projection inequality and reserve `A >= d kappa` correctly pay the new exponential weight.

7. **Dimension versus tail decay.** With `D(J) <= D_* J^d R^d`, the bound in (5.5) follows directly. At fixed `R`, taking `ell = c log J + O(1)` with `c > 2d/(kappa_0-kappa_t)` makes the tail Taylor cost tend to zero, while `ell/J` tends to zero. The required old cardinal reserve is fixed before `J`, so there is no circular growth of that reserve in this argument.

8. **Scope.** The numerical sample only demonstrates a positive output weight with room for the tail. It does not claim that the old `L` weight test survives unchanged, that the physical one-step supported constant obeys `C_A(L)<L/2`, that a macrostep integral exists for `R=L^s`, or that activity amplitudes contract. Those are correctly separated as model-specific inputs.

## Conclusion

With the finite/infinite-volume wording clarification incorporated, the abstract local-core transport estimate is ready for use as a conditional lemma. Its main gain is genuine: only the supported tail pays the dimension-sensitive Taylor factor. The local core still requires an actual common-domain amplitude margin and a controlled carrier halo.
