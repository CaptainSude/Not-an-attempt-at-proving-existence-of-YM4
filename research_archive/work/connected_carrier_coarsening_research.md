# Connected carriers under block projection

Research candidate, 17 October 2026. This geometric estimate addresses a
specific future induction issue. Notebook18 produces an anchored
exponential support-cardinality norm with exponent a_* at most 1/2,
whereas its sufficient interaction input uses exponent at least 4.
An unchanged-cell estimate does not close that norm loop. Coarsening
connected carriers can improve the available exponent, subject to
explicit constants; the lemma below is not a quantum induction.

Let the fine cell graph be Z^d or a compatible rectangular torus, with
each period a multiple of odd L>=5. Partition into L-cubes and let pi
map fine cells to their coarse blocks. Let H be a nonempty finite
connected set of fine cells. Set

    r=(L-1)/2,  s=floor((r-1)/2),  k=s+1.

Then

    |pi(H)| <= 2^d max(1, |H|/k).                          (1)

Here all distances on tori are periodic distances. Identified edges or
blocks only decrease the counts.

Proof. Choose a maximal subset {x_1,...,x_J} of H separated by at least
r in the sup graph distance. Maximality covers H by sup balls of
radius r-1. Such a ball has side length 2r-1<L and intersects at most
two L-blocks in each coordinate, hence at most 2^d coarse blocks.
Therefore |pi(H)|<=2^d J.

If J=1 the assertion follows immediately. If J>=2, the graph-distance
balls B_1(x_j,s) are disjoint: separation in sup distance implies
separation at least r in graph distance, and 2s<r. For each center
choose a path in H to any other center. Before leaving B_1(x_j,s),
the path has at least s+1 distinct vertices. Thus each disjoint ball
contains at least k vertices of H, and Jk<=|H|. This proves (1).
Connectedness is used exactly in this path argument. Without it,
one fine cell per coarse block contradicts any gain proportional
to L.

In particular, for target exponent A>=0 and input exponent a>0,
if

    A 2^d/k <= a-delta,  0<delta<a,

then

    exp(A |pi(H)|) <= exp(A 2^d) exp((a-delta)|H|).         (2)

For an anchored family E_H with connected H and

    sup_x sum_(H contains x) exp(a|H|)||E_H|| <= epsilon,

define the unmodified projection family

    E'_K = sum_(H : pi(H)=K) E_H.

This grouping changes the carrier, not the variables on which the
function depends, so it is not yet a background-substitution theorem.
With that distinction, its carrier norm satisfies

    sup_B sum_(K contains B) exp(A|K|)||E'_K||
        <= L^d exp(A 2^d) epsilon.                       (3)

Indeed K contains B only if H meets B. Bound that condition by the
sum over the L^d fine cells of B, use (2), and apply the fine anchored
norm. The reserved exp(delta|H|) may pay later local costs. Equation
(3) is bounded, not contractive; its constant grows with L.

The counterexample to an automatic contraction is already a singleton
vacuum activity E_{ {x} }=c: its coarse block sum is L^d c. Even after
normalizing away vacuum terms, marginal directions require their own
analysis. This is why an RG induction cannot be inferred from (3).

## Spatial exponents and localization blocks

A separate useful bound applies to arbitrary terminal sets Y, not
necessarily connected, when regrouping into blocks of side J. Let
tau be graph Steiner length and ell the terminal metric spanning-tree
length. For coordinate block projection pi_J,

    d_block(pi_J x,pi_J y) <= d_unit(x,y)/J + d.

Apply this to the edges of a terminal spanning tree and use
ell_unit(Y)<=2 tau_unit(Y). It follows that

    tau_block(pi_J Y)
       <= 2 tau_unit(Y)/J + d(|Y|-1).                    (4)

Thus any desired fixed coarse exponent sigma can be obtained from
a smaller original spatial exponent mu when 2 sigma/J<=mu,
provided a cardinality reserve at least d sigma is available:

    exp(sigma tau_block(pi_JY)+A|pi_JY|)
       <= exp(mu tau_unit(Y)+(A+d sigma)|Y|).             (5)

The anchor multiplicity and block matrix norms change by fixed powers
of J. This is applicable to Notebook21's classical support families,
which have arbitrary fixed cardinality reserve on a smaller domain.
It cannot be applied to a quantum family possessing only a fixed
small cardinality exponent unless that exponent pays the displayed
cost. In particular (4) does not by itself solve the quantum
re-insertion problem.

## What remains to combine these facts

1. Derive the actual stationary-background substitution, including
   the connecting supports introduced by its nonlocal response.
2. Track whether its spatial and cardinality losses fit the spare
   delta in (2), with a common analytic domain.
3. Prove the running-coupling and relevant/marginal extraction bounds.
4. Include the large-field pieces and the sourced observable norms.

The estimates above are geometric inputs and a precise warning
against identifying a bounded one-step map with an iterative proof.
