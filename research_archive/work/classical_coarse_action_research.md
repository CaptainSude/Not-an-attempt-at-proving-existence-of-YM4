# Classical coarse action, envelope identity and local Ward identity

This is a finite-regulator consequence of the nonlinear minimizer construction. The action is the coupling-free Wilson action in dimension four, the fine pairing is eta^4 times the normalized trace sum, and the final coarse spacing is one. The arguments below are classical; there is no fluctuation determinant, functional integral or quantum Ward identity.

Write F(A)=QA+R(A), with R(0)=DR(0)=0; use R_0 for the distinct scalar flat gauge projection. The corrected minimizer A_*(B) is in the fixed slice R_0 D^T A=0, and A_*=H B+O(||B||_infinity^2) in the complete physical N_alpha norm. The ordinary representative U_ord(B) is related to U_*(B)=exp(i eta A_*(B)) by the explicit genuine gauge transformation already proved. Both are holomorphic on a refinement- and volume-independent coarse supremum ball. Define

    V(B)=S_eta(U_*(B))=S_eta(U_ord(B)).

The equality holds also for the complex analytic extensions: the forward/reverse Wilson density is invariant under complex matrix gauge conjugation. Only real fields have a minimum interpretation. Scalar total-action bounds contain the number of coarse bonds.

## 1. Envelope identity on the fixed slice alone

The exact chart is A=xi+H[B-R(A)] with xi in X=ker Q intersect ker R_0D^T. Put T_A=(I+H DR(A))^{-1} and H_A=T_A H. Differentiating the analytic minimizer in a coarse direction c gives

    DA_*(B)[c]=H_A c+T_A Dxi(B)[c].

The second summand is an actual slice tangent since Dxi(B)[c] is in the fixed linear space X. Slice stationarity gives <E(A_*),T_A Dxi[c]>=0, with E the ordinary-potential Wilson Euler derivative. Therefore

    DV(B)[c]=<m(B),c>,       m(B)=H_A^T E(A_*).

No full-constraint multiplier theorem or gauge-orbit argument is needed for this equality. The push-through transpose identity and flat H^T K A=q[B-R(A)] give the already exact multiplier formula

    m(B)=(I+H^T DR(A_*)^T)^(-1)
           {q[B-R(A_*)]+H^T N(A_*)},

where N(A)=S_jet^T f_eta(S_jet A). The transpose force is evaluated as H^T N=(S_jet H)^T f_eta; no derivative of the coefficient is taken. All pairings and transposes are physical, bilinear on the complexification.

The uniform bounds A_*=O(b), R(A_*)=O(b^2), H^TN(A_*)=O(b^2), DR(A_*)^T=O(b), where b=||B||_infinity, imply

    ||m(B)-qB||_infinity<=C b^2.

The vector-valued map m is holomorphic on a uniform ball. In particular m(0)=0 and Dm(0)=q. Cauchy on a direction circle of radius b, inside a smaller fixed ball, gives ||Dm(B)-q||_{infinity->infinity}<=C' b; the conclusion at b=0 follows from the Taylor expansion. This is not yet a spatially weighted estimate.

Let N_b be the number of independent positive coarse bonds. Since V(0)=0, integrate the envelope identity along tB:

    V(B)=1/2 <B,qB> + integral_0^1 <m(tB)-tqB,B> dt.

The normalized color trace has a fixed-dimensional bilinear bound. Hence

    |V(B)-1/2 <B,qB>| <= C N_b b^3.

This holds on the complex ball as an absolute-value estimate; C is independent of refinement and volume. It is a density-uniform cubic remainder, not a total-volume-independent bound.

## 2. Coarse gauge invariance with both comparison radii explicit

Let D=exp(iB), let omega be a real coarse site field, g=exp(i omega), and define B^g=log(D^g)/i on the common branch. Use the convention D^g(c)=g(c_-)D(c)g(c_+)^{-1}. Since the coarse spacing is one and each bond has two endpoints, there is a uniform local analytic bound

    ||B^g||_infinity <= C_c (b+w),  w=||omega||_infinity,

with C_c>=1, on a fixed small ball. There is no coarse differentiability assumption on omega; its coarse first differences are bounded by 2w.

Let b_0,r_0 be the ordinary-minimum radii from Notebook 15. Let ||A_ord(B)||_{N_alpha}<=C_A b. Let E_pt be the smooth fine point-value extension from that notebook, with ||E_pt omega||_{C^{2,alpha}}<=C_E w, and set h=exp(i E_pt omega). Its restriction to coarse sites is g, and the complete fine gauge-action estimate gives

    ||A^h||_{N_alpha} <= C_G (||A||_{N_alpha}+C_E w),

for h and h^{-1}, on a common small domain.

Choose a single delta>0 so that all logarithms and gauge actions are in their established domains and

    C_c delta < b_0/2,
    C_G(C_A C_c+C_E) delta < r_0/2.

For real b+w<delta both competitors are legitimate:

* U_ord(B)^h has ordinary average D^g and potential norm at most C_G(C_A b+C_E w)<r_0. Minimality at B^g gives V(B^g)<=V(B).
* U_ord(B^g)^{h^{-1}} has ordinary average (D^g)^{g^{-1}}=D and potential norm at most C_G(C_A C_c(b+w)+C_E w)<r_0. Minimality at B gives V(B)<=V(B^g).

Thus V(B^g)=V(B). The second comparison uses the separately controlled minimizer at B^g, not an assumed inverse of the first comparison map. Both competitors remain strictly inside the same uniform minimum radius. The constants are independent of refinement and volume; no gauge parameter uniqueness is required.

The maps V and B^g are holomorphic on a uniform smaller complex product ball, for example ||B||,||omega||<delta/3 after reducing delta for analytic domains. The real identity holds on an open set of the full real form of this finite-dimensional space. The holomorphic identity theorem, applied coordinate by coordinate, extends it to the connected complex product ball. The extension is an analytic equality, not a complex minimization assertion.

## 3. Exact classical Ward identity

Let J_B v=integral_0^1 Ad(exp(itB))v dt be the left exponential differential on coarse bonds. It is invertible on the fixed small complex ball. For the real one-parameter coarse gauge exp(it omega), the ordinary coarse-potential velocity is

    d/dt B^{exp(it omega)}|_0=-J_B^{-1} D_D omega,
    (D_D omega)(c)=Ad(D_c)omega(c_+)-omega(c_-).

The final coarse spacing is one, so no missing length factor occurs. Differentiate V(B^g)=V(B), use DV=m and the physical coarse bilinear transpose:

    0=-<m,J_B^{-1}D_D omega>
      =-<D_D^T J_B^{-T}m,omega>.

Since omega is arbitrary,

    D_D^T J_B^{-T}m(B)=0.

This holds on the real small ball and extends holomorphically to the complex ball. Thus j_cl=J_B^{-T}m is the divergence-free left-coordinate classical coarse current. The distinction between m and j_cl matters away from B=0.

## 4. Consequence conditional on the separately audited weighted response

Assume the weighted response theorem supplies, for every admissible complete cell weight varpi with varpi(n)/varpi(m)<=exp(kappa d(n,m)),

    ||(Dm(B)-q)c||_{infinity,varpi}
       <=C_kappa b ||c||_{infinity,varpi}.

Then Q_cl(B)=D^2V(B)=Dm(B) is symmetric under the physical coarse transpose. In a fixed trace-orthonormal color/component basis, choose the centered weight varpi_i(j)=exp(-kappa d(i,j)) and input phases that match an output row. The weighted operator bound controls the sum of absolute row entries with factor exp(kappa d(i,j)); a fixed component factor converts entries into matrix-block norms. Transpose symmetry supplies the same column bound. Therefore

    ||Q_cl(B)-q||_{Schur,kappa} <= C'_kappa b.

Let a lie in a fixed interval 0<a_-<=a<=a_+ and suppose, as supplied by the flat baseline estimates, ||(q+aI)^{-1}||_{Schur,kappa}<=r_kappa uniformly. Put P_cl(B)=Q_cl(B)+aI. For sufficiently small b, the real positive baseline and the Schur bound give Re P_cl(B)>=a_- I/2 even at complex B. If r_kappa C'_kappa b<=1/2 then

    ||P_cl(B)^{-1}||_{Schur,kappa}<=2r_kappa,
    ||P_cl(B)^{-1}-(q+aI)^{-1}||_{Schur,kappa}
       <=2r_kappa^2 C'_kappa b.

The inverse is holomorphic and uniformly spatially localized. This is an auxiliary positive coarse classical precision. It is not the Hessian of an integrated quantum effective action, not a physical mass gap, and not an assertion of strict dependence on bounded background supports. The weighted response hypothesis is separate from the elementary envelope and Ward arguments above.
