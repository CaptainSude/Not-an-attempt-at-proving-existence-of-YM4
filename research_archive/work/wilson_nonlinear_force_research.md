# A uniform ordinary-coordinate Wilson nonlinear force

16 October 2026. Research proof for independent audit. This note concerns the explicitly normalized coupling-free Wilson action in the ordinary physical coordinate U=exp(i eta A), with a globally defined small connection. It is not a new identification of every source action prefactor or fluctuation chart. The local nonlinear force estimate is independent of the constrained Green operator used later to solve stationarity.

## 1. Action, physical jet and exact density

Let 0<eta<=1, dimension d fixed, and use compatible periodic lattices with physical measure eta^d. The full-lattice identities hold for finite-support variations of bounded fields. Matrices belong to the complexification of the Hermitian traceless Lie algebra. Write tau=Tr/N_c and use the bilinear physical pairing; transposes below are its fixed bilinear transposes, not conjugates of a variable complex background.

For a positive plaquette p=(x;mu,nu), mu<nu, define the physical jet

    (J_eta A)_p=(a,b,c,e)
       =(A_mu(x), A_nu(x),
         nabla_(eta,mu) A_nu(x), nabla_(eta,nu) A_mu(x)).     (1.1)

The positive fine difference is nabla_(eta,rho)f(x)=(f(x+eta e_rho)-f(x))/eta. The plaquette holonomy of U=exp(i eta A) is exactly

    P_eta(a,b,c,e)
      =exp(i eta a) exp(i eta b+i eta^2 c)
         exp(-i eta a-i eta^2 e) exp(-i eta b).              (1.2)

Thus there is no estimate or Taylor approximation in the replacement of shifted link potentials by the physical jet.

Define the normalized analytic Wilson action by

    S_eta(A)=eta^(d-4) sum_p [1-(1/2)tau(P_p+P_p^(-1))].   (1.3)

It equals the usual real Wilson expression on Hermitian A. Its eta normalization and factor 1/2 are explicit. The algebraic identity

    P+P^(-1)-2I=(P-I)^2 P^(-1)                             (1.4)

is exact for every invertible matrix P.

## 2. Joint removability and the exact quadratic part

**Lemma 2.1.** The matrix-valued function

    F_eta(z)=(P_eta(z)-I)/eta^2,

initially for eta!=0, extends jointly holomorphically to eta=0 and all finite jet coordinates z=(a,b,c,e). The density

    L_eta(z)=-(1/2)tau(F_eta(z)^2 P_eta(z)^(-1))             (2.1)

is likewise jointly holomorphic. On every fixed bounded complex jet ball all its jet derivatives are bounded uniformly for eta in [0,1]. Its quadratic Taylor term at z=0 is exactly

    L_2(z)=(1/2)tau((c-e)^2),                              (2.2)

for every eta, including eta=0.

**Proof.** Products of the four matrix exponentials are entire in eta and the finitely many complex coordinates of z. For every z, P_0(z)=I and partial_eta P_eta(z)|eta=0=i(a+b-a-b)=0. Taylor's formula therefore gives the jointly analytic extension

    F_eta(z)=integral_0^1 (1-s) partial_eta^2 P_(s eta)(z) ds.   (2.3)

Here partial_eta^2 means the second derivative of P in its scalar argument, evaluated at s eta. Formula (2.3) is valid for complex eta as well. Equivalently, divide the joint convergent power series by eta^2. The inverse P_eta^(-1) is the reverse product of inverse exponentials, and is entire too. This proves the assertion for (2.1).

Choose, for example, |eta|<=2 and ||z||<=2r_0 in any fixed coordinate norm. Every exponential and its needed eta derivatives are bounded on this compact polydisc. Equation (2.3) bounds F uniformly there. Cauchy's formula on the jet coordinates then bounds every fixed-order jet derivative of L uniformly on ||z||<=r_0, with constants depending on the chosen radius and order, but not on eta in [0,1]. One can write bounds C n! R^(-n) after passing to an equivalent finite-dimensional polydisc norm. No lattice dimension or volume appears.

At z=0, P_eta=I and F_eta=0. Differentiation in the jet direction z gives

    D_z P_eta(0)[z]=i eta^2(c-e),
    D_z F_eta(0)[z]=i(c-e).                                (2.4)

Thus the quadratic part of (2.1) is -tau((i(c-e))^2)/2, giving (2.2). As a check, the value at eta=0 is

    F_0(z)=i(c-e)-[a,b].                                   (2.5)

The commutator is quadratic in the jet variables and does not alter (2.2). The proof does not assume that noncommuting exponentials combine into the exponential of their sum.

By (1.4) and Lemma 2.1 the action is exactly

    S_eta(A)=eta^d sum_p L_eta((J_eta A)_p).                 (2.6)

The apparent inverse fourth power of eta has completely canceled before any force derivative is taken.

## 3. The force factorization

Put R_eta=L_eta-L_2. It is analytic and its constant, linear and quadratic Taylor coefficients vanish. Let f_eta(z) be its gradient in the four jet slots, using the fixed bilinear trace pairing:

    D R_eta(z)[w]=sum_{l in {a,b,c,e}} tau(f_eta,l(z) w_l). (3.1)

Projection onto the fixed traceless Lie space is included in this definition. It has a fixed finite-dimensional norm and introduces no eta dependence. On a smaller fixed complex jet ball, Lemma 2.1 gives constants C independent of eta such that

    f_eta(0)=0,       D f_eta(0)=0,
    ||f_eta(z)|| <= C ||z||^2,
    ||D f_eta(z)|| <= C ||z||,
    ||D^2 f_eta(z)||+||D^3 f_eta(z)|| <= C.                 (3.2)

For example the first two inequalities follow by integrating D^2 f along the segment from 0 to z. Higher fixed-order derivatives have the same uniform analyticity bounds.

Define the ordinary-coordinate Euler force E_eta(A) by

    D S_eta(A)[H]=<E_eta(A),H>_eta.

Let d be the ordinary fine curl, so that (dA)_p=c-e, and K=d^T d. Taking the variation of (2.6) gives the exact identity

    E_eta(A)=K A+J_eta^T F_eta^nl(A),
    F_eta^nl(A)_p=f_eta((J_eta A)_p).                       (3.3)

The notation F_eta^nl is distinct from the matrix F_eta=(P-I)/eta^2 in §2. Equivalently one may write the nonlinear map as mathcal F_eta(A)=f_eta(J_eta A).

For complete oriented component formulas, if q_p=(q_p^a,q_p^b,q_p^c,q_p^e),

    (J_eta^T q)_lambda(x)
      =sum_{nu>lambda} [q_(lambda,nu)^a(x)
                         +nabla_(eta,nu)^T q_(lambda,nu)^e(x)]
       +sum_{mu<lambda} [q_(mu,lambda)^b(x)
                         +nabla_(eta,mu)^T q_(mu,lambda)^c(x)],   (3.4)

where nabla_(eta,rho)^T q(x)=(q(x-eta e_rho)-q(x))/eta. Equation (3.4) is the physical transpose, since every slot uses the same eta^d measure. In particular the nonlinear force is a sum of bounded nonlinear jet coefficients and divergences of such coefficients. It is not asserted to be bounded pointwise independently of eta before applying a Green operator. The divergence stays outside the nonlinear coefficient map.

At the quadratic level the c and e coefficients are c-e and e-c, respectively; (3.4) therefore reproduces K=d^T d with coefficient one. This independently checks the normalization and signs in (3.3).

## 4. Complete-field physical Hölder norms

Fix 0<alpha<1. For a complete field f on the fine lattice, compare values of the same component at translated sites. On the full lattice one convenient equivalent global norm is

    ||f||_(C^alpha)=||f||_infinity
                    +sup_(0<|x-y|<=R) |f(x)-f(y)|/|x-y|^alpha,   (4.1)

where R>1 is fixed in physical units. For periodic fields use periodic distance, or lifted neighboring charts; all constants below are uniform. Changing the fixed R only changes constants, because larger differences are bounded by twice the supremum.

Define

    N(A)=||A||_infinity+max_rho||nabla_(eta,rho) A||_infinity,
    N_alpha(A)=N(A)+max_rho[nabla_(eta,rho) A]_alpha.        (4.2)

These are the homogeneous source-shaped first-difference norms; no Laplacian or second-difference supremum is included. Maxima and finite sums of components are equivalent with fixed constants.

**Lemma 4.1 (jet norm).** There is C_J, independent of eta and volume, such that

    ||J_eta A||_infinity <= C_J N(A),
    ||J_eta A||_(C^alpha) <= C_J N_alpha(A).                 (4.3)

**Proof.** The c and e jet entries already are first differences and their Hölder seminorms are in (4.2). For a and b, telescope A(x)-A(y) along an axis-aligned lattice path of length at most sqrt(d)|x-y|. For distances <=R,

    |A(x)-A(y)|/|x-y|^alpha
       <=sqrt(d) R^(1-alpha) max_rho||nabla_(eta,rho)A||_infinity.

The estimate is valid even for nearest-neighbor separation eta: the factor is eta^(1-alpha), never eta^(-alpha). Periodic paths use the shortest lifted coordinate displacements. The argument proves (4.3) and shows explicitly why no inverse mesh factor or second derivative is needed.

For weighted localization, let C_n be unit physical cells and C_n^+ fixed enlarged cubic collars. Use complete fields throughout. Define ||f||_(C^alpha,w) as the supremum over n of w(n) times the local supremum and Hölder norm on C_n^+, and define N_(alpha,w) similarly from A and its complete first differences. Let

    w(n)/w(m)<=exp(kappa dist(n,m)).                        (4.4)

Neighboring collar conventions have uniformly comparable weights. The telescoping path between two points in a cubic collar can be taken in that collar, with a fixed enlargement if needed. Consequently the weighted versions of (4.3) hold:

    ||J_eta H||_(C^alpha,w)<=C_J,kappa N_(alpha,w)(H),
    ||J_eta H||_(infinity,w)<=C_J,kappa N_w(H).              (4.5)

All comparisons use physical distances. No field is multiplied by a sharp cell indicator, and no derivative is taken of the weight. The jet itself reads entries at the plaquette base point and first differences of the complete field; (3.4) is used only after these complete coefficients are formed.

## 5. Hölder algebra and quantitative nonlinear bounds

For fixed matrix-valued complete fields, the product difference identity gives

    [uv]_alpha <= ||u||_infinity [v]_alpha
                        +[u]_alpha ||v||_infinity.        (5.1)

The same inequality on each collar gives weighted product estimates with the weight assigned to either factor. In particular an unweighted C^alpha coefficient acts boundedly on weighted C^alpha fields, with a fixed norm constant. This is also true for fixed multilinear maps of the jet values.

**Theorem 5.1 (uniform nonlinear coefficient).** Choose r>0 sufficiently small, independently of eta and volume. If N_alpha(A),N_alpha(B)<=r, then mathcal F_eta(A)=f_eta(J_eta A) is holomorphic and obeys

    ||mathcal F_eta(A)||_(C^alpha,w)
          <= C N(A) N_(alpha,w)(A),                        (5.2)

    ||mathcal F_eta(A)-mathcal F_eta(B)||_(C^alpha,w)
          <= C (N_alpha(A)+N_alpha(B))
                                      N_(alpha,w)(A-B),   (5.3)

whenever the weighted quantities on the right are finite. In particular the unweighted coefficient is quadratic and locally Lipschitz with constant Cr. For a weighted direction H,

    ||D mathcal F_eta(A)[H]||_(C^alpha,w)
       <= C [N(A) N_(alpha,w)(H)+N_alpha(A)N_w(H)]
       <= C N_alpha(A)N_(alpha,w)(H).                      (5.4)

The same estimates hold uniformly on compatible tori.

**Proof.** Write z=J_eta A. By (3.2), the supremum of f_eta(z) is bounded by C||z||_infinity^2. Along the segment between z(x) and z(y), the derivative of f is bounded by C||z||_infinity. Therefore

    |f(z(x))-f(z(y))|
           <=C||z||_infinity |z(x)-z(y)|.

Multiplying the local norms by w(n) and using (4.3)–(4.5) proves (5.2). Notice that the coefficient N(A) in this bound does not require a Hölder seminorm.

For (5.4), the exact derivative is

    D mathcal F_eta(A)[H](x)=D f_eta(z(x))(J_eta H)(x).

The coefficient D f_eta(z) has supremum at most C||z||_infinity and Hölder seminorm at most C[z]_alpha, because D^2 f_eta is uniformly bounded. The product estimate (5.1), with the weighted norm on J_eta H, proves (5.4). Integrate this estimate along A_s=B+s(A-B), whose N_alpha norm is at most N_alpha(A)+N_alpha(B), to obtain (5.3). This proof keeps the weight on the direction and does not require weighted bounds on the base fields A,B separately.

A more precise tame difference estimate, useful if the sup and Hölder radii differ, is

    ||mathcal F_eta(A)-mathcal F_eta(B)||_(C^alpha,w)
       <=C [(N(A)+N(B))N_(alpha,w)(A-B)
            +(N_alpha(A)+N_alpha(B))N_w(A-B)].             (5.5)

The pointwise mean-value formula and the same product estimate prove it. Constants in these inequalities depend on alpha, the fixed physical collar, d, the group and the fixed analytic radius, but not on eta.

Second and higher directional derivatives also have uniform tame estimates. For example, from D^2 f_eta and D^3 f_eta,

    ||D^2 mathcal F_eta(A)[H,K]||_(C^alpha,w)
       <=C(1+N_alpha(A)) N_alpha(H) N_(alpha,w)(K),         (5.6)

with the weighted direction exchangeable by symmetry. Thus one may localize a direction while the base field and other directions remain merely bounded in the unweighted N_alpha norm.

## 6. Holomorphy, higher derivatives and the energy form

The local function f_eta has a convergent finite-dimensional Taylor series, starting at degree two, with coefficient bounds uniform in eta. The C^alpha product inequality and the bounded linear map J_eta:N_alpha->C^alpha make the substituted series converge absolutely on a fixed sufficiently small complex N_alpha ball. This proves Banach-space holomorphy of mathcal F_eta and is an alternative direct proof of its uniformity. Its derivatives are exactly the pointwise derivatives used in §5.

On a smaller ball, all higher derivatives have Cauchy bounds. For instance a uniform operator bound on a ball with margin delta gives, for unweighted directions,

    ||D^n mathcal F_eta(A)[H_1,...,H_n]||_(C^alpha)
       <=C n! (e/delta)^n product_m N_alpha(H_m).           (6.1)

This follows using polydisc radii delta/(n N_alpha(H_m)) and n^n<=e^n n!. For one weighted direction, differentiate the local Taylor series and use the weighted product inequality; the resulting constants have the same factorial/Cauchy character, with that direction's N_(alpha,w) norm replacing its unweighted norm. When weights are not bounded below, holomorphic weighted statements are understood on the intersection of the unweighted small ball with the weighted direction space; no implication from a weighted norm to the unweighted smallness condition is assumed.

There is a useful energy consequence requiring only small N(A), without Hölder smallness. From (3.3),

    D E_eta(A)[H]
        =K H+J_eta^T Df_eta(J_eta A) J_eta H.               (6.2)

Hence, for physical L2 fields H,K,

    |D^2 S_eta(A)[H,K]-<dH,dK>_eta|
       <=C N(A) ||J_eta H||_(2,eta)||J_eta K||_(2,eta).     (6.3)

The coefficient Df_eta(J_eta A) is pointwise in the plaquette jet, has bounded row norm O(N(A)), is symmetric for the fixed bilinear transpose, and has fixed fine range. Thus it is a small energy-form perturbation. Equation (6.3) is for the ordinary global exponential coordinate and should not be identified with a different background-relative simultaneous chart without its coordinate conversion.

## 7. Interface with a constrained minimizer

The exact force (3.3) and (5.3) are the needed nonlinear input for a fixed-gauge contraction. One must separately establish an equal-exponent Green estimate of the form

    ||C J_eta^T q||_(N_alpha)<=B_alpha ||q||_(C^alpha),     (7.1)

and its weighted version for the specific constrained inverse C, as well as the coarse compression/transposed-extension estimates used by the stationarity equations. The older right-divergence theorem with input exponent gamma>output exponent beta cannot be substituted for (7.1) at gamma=beta. The subsequently proved equal-exponent massive heat split supplies the appropriate baseline mechanism, but its adaptation to the selected constrained inverse must remain explicit.

Given (7.1), the map A->C J_eta^T mathcal F_eta(A) is quadratic and locally Lipschitz on N_alpha with constant C B_alpha r, and similarly for a single weighted direction. No derivative of mathcal F_eta(A), no second fine derivative of A, and no inverse power of eta is needed in that contraction estimate. Its complex analyticity follows by composition.

The result does not identify a nonflat source minimizer, prove the separate constrained Green bound, or fix a source action convention not explicitly matched to (1.3). It proves the required local ordinary-coordinate Wilson force module, including its physical Hölder and weighted estimates, uniformly over refinement and compatible volume.
