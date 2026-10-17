# Geometry and local chart of the composite ordinary macrostep

17 October 2026. Research proof. The nonlinear incidence, flat pivot coefficient, analytic local elimination and independent contour-gauge identities below are proved from the actual ordinary averaging formula. They are uniform in volume and in an unrelated prior refinement M once the finite primitive ratio ell and depth s are fixed. They do not give bounds uniform as R=ell^s tends to infinity. No output file or compilation is involved.

This constructs a new composite constraint. It does not identify that constraint with a direct-R ordinary average, nor identify one macro integral with s separately truncated/gauge-fixed primitive integrals. Gaussian coercivity and exact integral normalization are separate modules being checked independently.

## 1. Source formula and conventions

Fix odd ell>=3, s>=1 and R=ell^s. Use positive oriented unit current bonds, with inverse group elements on reversed bonds. Work on the infinite lattice locally or compatible finite periodic quotients with distinct lifted interfaces; the source periods 2 ell^n, n>=s, are sufficient. Translate one common macro center to zero. Every intermediate lattice is then a translate identified with ell^t Z^d, and its centered blocks are nested. This removes the harmless half-integer shift of the source notation.

For a block center y, the source contour family consists of the coordinate-order shortest paths from y to x: one traverses each nonzero coordinate displacement in a prescribed permutation, and averages over those permutations. Every edge stays inside the centered block. Let M_G be the local analytic group mean, and write

    P_ell(V;y,x)=M_G({V(Gamma):Gamma in G_ell(y,x)}).         (1.1)

For c=(y,y+ell e_mu), x'=x+ell e_mu, and the straight center transporter R_c(V), the ordinary map is

    U_x(V)=P_ell(V;y,x) V([x,x']) P_ell(V;y+ell e_mu,x')^-1,
    M_ell(V)(c)
       =exp{ell^-d sum_(x in B_ell(y)) log[U_x(V)R_c(V)^-1]} R_c(V).
                                                               (1.2)

All logarithms use their common small branch. The present theorem concerns that local analytic map. It makes no assertion about the deposit's measurable extension outside the small-field domain.

Primary definition: Bałaban, *Commun. Math. Phys.* 109 (1987), pp.252--254, (0.3),(0.5)--(0.12), accessible original article at [the public PDF](https://scispace.com/pdf/renormalization-group-approach-to-lattice-gauge-field-3ygai0vxt1.pdf). Its stated contour and group-mean properties are the only source inputs used here; the macro proof is derived below. Deposited references at pinned commit e392ef45013a581664bab76b90867170b30fe10e: Raw I786--850 defines the iterated ordinary map and nested blocks; I46952--46986 records the left-relative coordinates, angle normalization and primitive pivot right inverse. The workspace's exact one-step transcription is `physical_current_pivot_precision_research.md`, Section2.

The proof uses the actual chosen source mean through its axioms: local analyticity, endpoint covariance and arithmetic differential. The original article gives the following implicit equation as one admissible realization in (0.10), while explicitly allowing any mean satisfying (0.5)--(0.9). It is not a claim that this equation uniquely specifies every allowed source mean. For this realization, near common identity P is the unique small solution of

    sum_j log(U_j P^-1)=0.                                  (1.3)

At identity its derivative in the P logarithm is minus the number of inputs times identity. The analytic implicit-function theorem gives local uniqueness and analyticity. Linearizing (1.3) shows that the differential is the arithmetic mean. If U'_j=g U_j h^-1 and P'=gPh^-1, their defining logarithms are conjugated by g. Uniqueness gives the exact local endpoint identity

    M_G({g U_j h^-1})=g M_G({U_j}) h^-1.                    (1.4)

For any other selected admissible mean, (1.4) is its stated endpoint-covariance axiom and its arithmetic differential is (0.8); no substitution of means is required. Thus the contour and ordinary maps obey

    P_ell(V^u;y,x)=u(y)P_ell(V;y,x)u(x)^-1,
    M_ell(V^u)=M_ell(V)^(u restricted to new centers),       (1.5)

whenever both sides lie in the common analytic domains. The real group identities extend to their common complex neighborhoods. They also follow directly from (1.2),(1.4) and logarithm conjugacy.

## 2. One primitive interface pivot has only one nonlinear consumer

For c=(y,y+ell e_mu), let

    p_ell(c)=[y+(ell-1)e_mu/2, y+(ell+1)e_mu/2].             (2.1)

No internal root contour contains this edge: it crosses between two different primitive blocks. If a positive parallel string for a coarse bond c' contains p_ell(c), its direction must be mu, its transverse block center must equal y's transverse center, and its pair of longitudinal blocks must be the two separated by this interface. Therefore c'=c. The same is true of a reference center string. On a torus use the specified local lifts: the opposite interface of two periodic neighboring blocks is a distinct edge and is not traversed by this positive string.

It follows from the actual products and means in (1.2), before any derivative is taken, that changing only V(p_ell(c)) changes at most the output M_ell(V)(c). Every other output is independent of that group coordinate. This holds simultaneously for any selection of these primitive middle-interface pivots.

At V=1, write B([x,x']) for the oriented sum of a Lie field B along the straight string, and let t_y(B;x) be the arithmetic contour mean of its root-to-x sums. The angle differential of (1.2) is

    C_ell B(c)
       =ell^-d sum_(x in B_ell(y))
          [t_y(B;x)+B([x,x+ell e_mu])-t_(y+ell e_mu)(B;x+ell e_mu)].
                                                               (2.2)

The reference-string derivative cancels: it appears with a minus sign inside every logarithm and once with a plus sign outside the exponential. Neither root term reads the pivot. Exactly ell of the starting sites have the pivot's transverse coordinates, and each of their ell-long strings contains it once with positive orientation. Hence the whole pivot column is

    C_ell (b supported at p_ell(c))
           =ell^(1-d) b at c, and zero at every other output. (2.3)

The coefficient is identity in the color fiber times ell^(1-d). This is an angle derivative; no physical length factor has been suppressed.

## 3. Exact incidence through the whole composition

Define the composite group map

    M_R^comp=M_ell o ... o M_ell,          s factors.          (3.1)

The primitive maps act on their respective successive lattices. For a final positive macro bond c=(y,y+R e_mu), choose the original unit pivot

    p_R(c)=[y+(R-1)e_mu/2, y+(R+1)e_mu/2].                 (3.2)

Put h_t=ell^t and define the intermediate bond

    b_t(c)=[y+(R-h_t)e_mu/2, y+(R+h_t)e_mu/2],
                 0<=t<=s.                                 (3.3)

Its endpoints lie in the level-t lattice because R/h_t is odd. We have b_0(c)=p_R(c), b_s(c)=c, and b_t(c) is exactly the primitive middle-interface pivot of b_(t+1)(c) at spacing h_t.

**Nonlinear incidence theorem.** Varying the input group coordinate at p_R(c), with all other input coordinates held fixed, changes at level t at most the single bond b_t(c). Therefore M_R^comp(V)(c') is independent of p_R(c) for every c' different from c. In particular every final constraint contains its own selected pivot and no other selected pivot.

Proof is induction in t. The assertion is tautological at t=0. If only b_t(c) can change, Section2 at spacing h_t says only b_(t+1)(c) can change at the next average. The argument uses functional dependence, so it applies to arbitrary allowed nonlinear variations and not just to the differential at identity. Different macro bonds give distinct b_t(c), including on compatible source tori when opposite interfaces are retained as distinct local lifts. The simultaneous support statement follows from the same primitive incidence.

**Two-block locality.** Every output M_R^comp(V)(c) reads only unit bonds in the two endpoint R-blocks and their internal connecting corridor. More precisely, every read edge has both endpoints in their union, using the local lift for c.

To see this, a level-t output bond reads level-(t-1) bonds in its two endpoint ell-blocks by (1.2). The smaller descendants centered at all sites of one such block tile precisely the centered unit block of side ell^t at that endpoint. Repeating this observation down to unit scale proves the claim. It is a bound on the full nonlinear dependency set, not merely on derivative support. The path-lift convention matters on short periodic quotients; set containment in the periodic union alone would not distinguish its two interfaces, whereas the incidence induction above does.

Let C_R be the angle differential of M_R^comp at identity. The chain rule and (2.3), applied along (3.3), give

    (C_R)_(c,p_R(c'))=R^(1-d) delta_(c,c') I_color.           (3.4)

There is no sum over intermediate outputs: the previous pivot column has only one nonzero row at every stage. This proves the proposed coefficient, including its power of R.

Iterating (1.5) also gives exact gauge covariance

    M_R^comp(V^u)=M_R^comp(V)^(u restricted to R centers).    (3.5)

With the unit forward gradient (D phi)(x,mu)=phi(x+e_mu)-phi(x), differentiation at identity yields

    C_R D phi(c)=phi(c_+)-phi(c_-).                          (3.6)

The right side is the endpoint difference, or R times the physical coarse gradient. This distinction is needed if C_R is converted from angle to physical-potential coordinates.

## 4. Actual analytic elimination for this composite constraint

Fix a small background V=e^{ia} and introduce the left-relative coarse Lie map

    F_(R,V)(B;c)
       =(1/i)log[M_R^comp(e^{iB}V)(c) M_R^comp(V)(c)^-1],
    A_(R,V)=D_B F_(R,V)(0).                                 (4.1)

For each fixed ell,s this is analytic on a positive product ball in a and B. One can obtain a ball directly by finite composition near identity; only finitely many local dependency types occur. Its radius can depend on R. It is independent of volume and of the prior classical refinement M, which does not enter the current group map.

Define the pivot matrix

    pi_c(V)=R^(d-1) (A_(R,V))_(c,p_R(c)).                    (4.2)

By (3.4), pi_c(1)=I, and by two-block locality it depends only on the same two-R-block background neighborhood. After a common fixed-R shrink,

    ||pi_c(V)-I||<=1/2,
    ||pi_c(V)^-1||<=2.                                      (4.3)

The actual right inverse h_(R,V) inserts only at the corresponding pivot:

    (h_(R,V) w)(p_R(c))=R^(d-1) pi_c(V)^-1 w(c),
    (h_(R,V) w)(b)=0 on nonpivots,
    A_(R,V) h_(R,V)=I.                                     (4.4)

Thus its maximum row norm is at most 2R^(d-1) in the chosen color operator norm. If Q_(R,V)=A_(R,V)/R is the physical coarse-potential derivative, its kernel convention Q B=sum_b R^-d Q(c,b)B(b) has pivot coefficient Q(c,p)=pi_c(V). This recovers exactly the source-style factor R^(d-1) in (4.4), without asserting any equality to a direct-R source average.

Let E_free insert retained nonpivot values and zero at pivots. Put

    K_(R,V)=E_free-h_(R,V)A_(R,V)E_free.                    (4.5)

Then A K=0, restriction of Kz to every retained coordinate is z, and every eliminated pivot row is finite range in the same two blocks.

Write F(B)=A B+C(B), with C(0)=DC(0)=0. Define the local implicit correction by

    dtilde_V(B)=C_V(B-h_(R,V) dtilde_V(B)).                 (4.6)

For a given output c, the right side depends on dtilde(c) alone: every other component inserts at a different pivot, which the full nonlinear c equation does not read. The derivative in dtilde of the implicit equation at B=dtilde=0 is identity. A finite-dimensional analytic implicit-function theorem, uniformly over the finitely many oriented cell types, therefore gives a unique small solution. Equivalently, choose a local ball with ||DC h||<=1/2 and use contraction in this one color fiber. The right side reads only the local B,a neighborhood; iteration cannot spread its dependence to other equations.

The exact retained chart is

    Phi_(R,V)(z)=K_(R,V)z-h_(R,V)dtilde_V(K_(R,V)z),
    F_(R,V)(Phi_(R,V)(z))=0,
    Phi_(R,V)(z)(b)=z(b) on every nonpivot.                 (4.7)

It is the unique small solution of the actual composite constraint for its prescribed nonpivot values. Its derivatives satisfy

    D Phi_(R,V)(0)=K_(R,V),
    D² Phi_(R,V)(0)[u,v]
       =-h_(R,V) D²F_(R,V)(0)[K_(R,V)u,K_(R,V)v].          (4.8)

The affine version solving F_(R,V)(B)=w is equally local:

    B=K_(R,V)z+h_(R,V)w-h_(R,V)C_V(B).                   (4.9)

For fixed R it has a uniform positive small product domain in a,z,w. Restriction to the retained coordinates is still exactly z. Finite local dimension, Cauchy estimates on smaller polydiscs and bounded neighborhood incidence give finite weighted row/column bounds for the first derivatives and contracted second derivatives. These constants can depend on R but are independent of volume and prior refinement M. No uniform-in-R chart estimate is claimed.

With a coupling g inserted, the actual relative field is Phi_(R,V)(g z). In particular it equals g z on retained bonds. The coupling cannot be moved outside the nonlinear chart. A retained-link window is therefore preserved in its actual variables. Any additional pivot or contour indicator remains at its exact nonlinear pulled-back argument; this geometry does not remove such factors.

## 5. An independent direct-R internal contour gauge

Use the same source prescription (1.1) for root-to-site coordinate-order shortest contours inside a centered R-block, and denote the resulting local mean by

    P_R(V;y,x)=M_G({V(Gamma):Gamma in G_R(y,x)}).             (5.1)

This is a separately chosen gauge variable; it is not used to redefine M_R^comp. It is analytic near identity, satisfies P_R(V;y,y)=I, and by (1.4) has exact endpoint covariance

    P_R(V^u;y,x)=u(y)P_R(V;y,x)u(x)^-1.                    (5.2)

Each such contour remains inside one R-block. Every selected p_R(c) crosses an R-block interface. Therefore P_R reads no selected pivot, at every allowed background, before taking any derivative.

Define its relative linearization

    T_(R,V)B(y,x)
       =D_B[(1/i)log(P_R(e^{iB}V;y,x)P_R(V;y,x)^-1)]_(B=0).
                                                               (5.3)

Since h_(R,V) is supported only on pivots,

    T_(R,V)h_(R,V)=0,
    T_(R,V)K_(R,V)=T_(R,V)E_free.                          (5.4)

There is the stronger exact nonlinear identity

    P_R(e^{i Phi_(R,V)(z)}V;y,x)
       =P_R(e^{i E_free z}V;y,x).                         (5.5)

Thus the contour penalty only sees the unchanged retained variables, although its coefficients still depend on the background.

For the normalized trace tau, define

    G_R(V)=sum_y sum_(x in B_R(y),x!=y)
                 [1-(1/2)tau(P_R(V;y,x)+P_R(V;y,x)^-1)].   (5.6)

It is nonnegative on real unitary fields, and vanishes when all P_R=I. At such a background its first relative derivative is zero and its pulled-back quadratic form is

    D_z² G_R(e^{i Phi_(R,V)(z)}V)|_0
          =K_(R,V)^T T_(R,V)^T T_(R,V) K_(R,V),           (5.7)

with the stated counting/trace pairing. The nonlinear second derivative of the chart contributes nothing: it is pivot-supported and G_R is pivot-independent. Formula (5.5) holds without the assumption P_R=I.

At flat background, gauge covariance gives the useful second exact-sequence identity

    T_(R,1)D phi(y,x)=phi(x)-phi(y).                       (5.8)

Together with (3.6), this supplies the gradient-kernel relations needed in a separate finite-patch coercivity argument.

## 6. Clearing the contour gauge while preserving the composite constraint

For V in a common small domain, define the rooted site gauge

    u_V(y)=I at every R-center,
    u_V(x)=P_R(V;y,x) for x in its R-block.                 (6.1)

Equation (5.2) gives P_R(V^(u_V);y,x)=I exactly, and (3.5) gives

    M_R^comp(V^(u_V))=M_R^comp(V).                        (6.2)

Both statements hold first on the real common domain and then as local analytic identities. This proves the geometric gauge-clearing operation. It does not by itself show that V is a classical constrained minimum or identify a Gaussian centered branch; those need the independent action comparison and positive reduced Hessian.

For a fixed R, the gauge is analytic and ||log u_V/i||<=C_R||log V/i||. A useful elementary refinement follows from the actual contour lengths. There are at most d! contour orderings and each path has length at most d(R-1)/2. Products of links e^{ia_b} obey ||product-I||<=exp(length*||a||)-1 in a fixed submultiplicative norm. The local mean has a fixed Lipschitz bound near equal identity inputs, depending on d and the group but not on R, because its number of inputs is bounded by d!. Hence, when R||a|| is small,

    ||log u_V/i|| <= C R ||a||.                            (6.3)

For the supported pre-gauge representative a_p=O(w/R), this gives a rooted gauge of size O(w), with the constants of that amplitude statement independent of R at fixed primitive base. It does not put the rooted representative in an O(w/R) angle ball: endpoint gauge differences can still produce angles of order w. Nor does (6.3) make the chart radii of Section4 uniform in R. Common-domain restrictions remain explicit.

## 7. Established outputs and remaining interfaces

Proved in this note for the actual composite M_ell^s:

* exact nonlinear one-selected-pivot incidence and two-R-block dependence;
* flat angle pivot coefficient R^(1-d) I and the gradient identity (3.6);
* local analytic right inverse, affine/nonlinear elimination and retained-coordinate identity;
* an independently chosen direct-R internal averaged-contour gauge with endpoint covariance, T_R h_R=0 and exact pivot independence;
* gauge clearing that preserves the composite constraint, and the flat root-gradient identity (5.8).

Still separate, not inferred here:

* uniform-in-old-M retained Gaussian coercivity/decay for C_R and T_R, and its small-background Hessian comparison;
* the exact gauge insertion, delta/Haar/pivot normalization and a definition of every cutoff in the new macro integral;
* the classical minimum comparison identifying a particular cleared V_p as the physical centered branch, with common chart domains;
* equality of any enlarged-domain inherited insertion or integral with the actual macrostep analytic germ;
* stable analytic-domain and activity-amplitude recursion, running coupling, large fields and observables.

The local elimination is genuine progress beyond the earlier construction proposal. It does not justify importing the direct-R source integral or treating this one composite integration as s already-controlled quantum integrations.
