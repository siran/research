# Relational Formulation of Electromagnetism from a Scalar Energy Field
**Sir Jean† & Anes Palma**
†Corresponding author: sir.jean@example.org

---

## Abstract
Building on our result that electric and magnetic fields arise as **orthogonal double-curl circulations of a single scalar energy field** $U$ ([Palma & Rodríguez 2025, DOI 10.13140/RG.2.2.17548.01929]), we show that the same scalar construction is fully **relational**: every observable depends only on coincidences of field values, not on absolute spatial points.
Given an oriented four-manifold $(\mathcal{M},g)$ with light-based metric, the field strength

$$
F \;=\; d\bigl(\star\,dU\bigr)
$$

satisfies $dF=0$, and minimal coupling to a conserved current 3-form $J$ yields the inhomogeneous equation $d\!\star F=-J$.
We detail existence and uniqueness of $U$, relate the scalar gauge to the usual vector potential, give examples, sketch numerical schemes, and discuss conceptual advantages of abandoning absolute space.
(Recall that the “Cartesian 3-space” we *see* is a cortical reconstruction, not a given external stage [^vision].)

---

## 1 Motivation
Experimental data are *relational*: instruments compare configurations but never label *where* in space the event occurs.
General relativity encodes this for gravity; classical electromagnetism appears to retain an absolute vector potential $A_\mu(\mathbf{x},t)$.
Our earlier work introduced a **scalar energy field** $U$ and showed that electric/magnetic vectors emerge via a double curl:

$$
\mathbf{E}= \nabla\times\nabla\times(\hat z\,U),\qquad
\mathbf{B}= \nabla\times\nabla\times(\hat\theta\,U).
$$

The present paper embeds that 3-D result into full four-dimensional form language, proving that **Maxwell’s theory is entirely relational** once formulated through $U$.

---

## 2 Geometric preliminaries
Let $(\mathcal{M},g)$ be an oriented, time-oriented $C^{\infty}$ four-manifold with signature $(-{+}{+}{+})$.
Notation

| symbol | meaning |
|-------|---------|
| $\Omega^{p}(\mathcal{M})$ | smooth $p$-forms |
| $d:\Omega^{p}\!\to\!\Omega^{p+1}$ | exterior derivative |
| $\star:\Omega^{p}\!\to\!\Omega^{4-p}$ | Hodge dual (depends on $g$) |
| $\delta=\!\star d\star$ | codifferential |

Units $c=\varepsilon_{0}=\mu_{0}=1$; hence the metric is *light-based* in the metrological sense [^light].
Define the operator

$$
\mathcal{R}=d\,\star d:\;\Omega^{0} \longrightarrow \Omega^{2}.
$$

On spatial hypersurfaces $\Sigma_t$ with induced metric it reduces to the familiar curl–curl.

---

## 3 Scalar-energy construction

### 3.1 Wave-equation assumption
Following [1] we posit a scalar energy field obeying

$$
\partial_{t}^{2}U \;=\; c^{2}(\rho)\,\nabla^{2}U, \tag{1}
$$

where the local propagation speed $c$ may depend on energy density $\rho\propto U^{2}$.

### 3.2 Field strength and Maxwell system
Define

$$
F \;=\; d\bigl(\star\,dU\bigr) \;\in\; \Omega^{2}(\mathcal{M}). \tag{2}
$$

*Homogeneous equations* follow immediately:

$$
dF=0, \tag{3}
$$

equivalent to $\nabla\!\cdot\!\mathbf{B}=0$ and Faraday’s law.

*Inhomogeneous equations* arise by coupling $U$ to a conserved 3-form current $J$:

$$
S[U]=\int_{\mathcal{M}}\!\Bigl[\tfrac12\,F\wedge\!\star F + U\,J\Bigr]. \tag{4}
$$

Varying $U$ gives

$$
d\!\star F = -\,J. \tag{5}
$$

Gauge shift $U\!\mapsto\!U+\text{const}$ leaves $F$ and $S$ unchanged.

### 3.3 Recovery of the 3-D double curls
On a constant-time slice (with Euclidean 3-metric) Eq. (2) decomposes into the previously published orthogonal circulations [1].

---

## 4 Existence and uniqueness of $U$

*Local theorem* (contractible patch $\mathcal{D}\subset\mathcal{M}$):
solving the elliptic equation

$$
\triangle U = -\,\star J \tag{6}
$$

with boundary data on $\partial\mathcal{D}$ yields a unique $U$ up to an additive constant.

*Global obstruction*: when $H^{3}(\mathcal{M})\neq0$, only the co-exact part of $J$ is sourced by $U$; harmonic flux sectors remain, just as in the usual vector-potential picture.
Thus the scalar and vector formulations are equivalent whenever $H^{3}=0$ (e.g. Minkowski, FRW).

*Proof sketch* is supplied in **Appendix A**.

---

## 5 Relation to the vector potential
Any 1-form $A$ with $F=dA$ admits a Hodge decomposition

$$
A = d\chi + \delta\beta + h,
$$

($h$ harmonic).  Choosing the **scalar gauge**

$$
A = \star\,dU \tag{7}
$$

eliminates $d\chi$ and $h$, leaving $F=dA$ automatically.
Hence Eq. (2) is Maxwell theory expressed in gauge (7).  Observables remain gauge-independent.

---

## 6 Relational ontology
Physical quantities are integrals of $F$ or $\star F$ over chains:

$$
\Phi_{B}(S)=\int_{S}\!F,\qquad
\Delta\varphi(\gamma)=\int_{\gamma}\!\star F.
$$

These depend only on the *images* of $S$ and $\gamma$, i.e. on relations between regions, not on point labels.
This perspective dovetails with frameworks where **distance and dimension emerge from causal correlations** :contentReference[oaicite:5]{index=5}, :contentReference[oaicite:6]{index=6}.

---

## 7 Examples

### 7.1 Plane wave
Let $k^{\mu}$ be null, $k\!\cdot\!k=0$, and set

$$
U = U_{0}\sin(k\!\cdot\!x).
$$

Then $F_{\mu\nu} = k_{[\mu}k^{\alpha}\epsilon_{\nu]\alpha\beta\gamma}x^{\beta}k^{\gamma}U_{0}\cos(k\!\cdot\!x)$ satisfies Eqs. (3)–(5) with $J=0$ and recovers the standard plane-wave solution.

### 7.2 Static point charge
In flat space use

$$
J = q\,\delta^{3}(\mathbf{x})\,dt\wedge dx\wedge dy\wedge dz.
$$

Solving (6) gives $U(r)=q/(4\pi r)$ and, via (2),

$$
\mathbf{E} = \frac{q}{4\pi r^{2}}\hat{\mathbf{r}},\qquad \mathbf{B}=0,
$$

i.e. Coulomb’s law.

### 7.3 Cosmological FRW background
With metric $ds^{2}=-dt^{2}+a^{2}(t)d\mathbf{x}^{2}$, Eq. (2) yields comoving electric/magnetic fields diluted by $a^{2}(t)$ exactly as in the standard Maxwell theory.

---

## 8 Numerical implementation
Equation (6) is Poisson-type; standard finite-element or multigrid solvers apply on arbitrary meshes.
In explicit time-stepping one solves **one scalar elliptic problem per step**; divergence constraints are automatic.
This reduces memory and communication overhead versus $\mathbf{E}$–$\mathbf{B}$ field updates in particle-in-cell codes.

---

## 9 Discussion and outlook
*Conceptual*: both gravity and electromagnetism admit formulations free of absolute spatial structure.
*Computational*: the single-scalar approach may simplify constraint handling and gauge fixing.
*Quantum*: $U$ offers a single gauge-invariant degree of freedom, potentially streamlining path integrals.
*Future*: incorporate media by $U$-dependent constitutive laws, analyse topological sectors on $H^{3}\!\neq\!0$ manifolds, and seek experimental signatures of energy-dependent propagation speed $c(\rho)$.

---

## 10 Conclusions
Electromagnetism can be written as the **double rotor of a scalar energy field** on any oriented four-manifold.
The resulting theory is locally Maxwell yet **purely relational**; the familiar 3-space is not a necessary backdrop but an emergent perceptual model [^vision].
This view promises both conceptual clarity and practical benefits.

---

## Acknowledgments
We thank colleagues X and Y for pre-submission comments.

---

## References
[1] A. Palma & A. M. Rodríguez, *Electric and Magnetic Fields as Orthogonal Circulations of a Scalar Energy Field*, Aug 2025, DOI 10.13140/RG.2.2.17548.01929.
[2] J. C. Maxwell, *A Dynamical Theory of the Electromagnetic Field* (1865).
[3] J. A. Wheeler, *Geometrodynamics* (Academic, 1962).
[4] E. Witten, *Topological Quantum Field Theory*, Commun. Math. Phys. **117**, 353 (1988).
[5] M. Nakahara, *Geometry, Topology and Physics*, 2nd ed. (IOP, 2003).
[6] A. M. Rodríguez, *A Cause-Effect Model for Emergent Time and Distance* (2023) :contentReference[oaicite:7]{index=7}.
[7] ——, *Dimension and Space as Emergent Properties of Distance* (2025) :contentReference[oaicite:8]{index=8}.

---

## Appendix A Proof of local existence / uniqueness
Let $\mathcal{D}$ be a contractible open subset of $\mathcal{M}$ with smooth boundary.
Eq. (6) can be written $\delta dU = -\,\star J$.
Because $\delta d$ is an elliptic, self-adjoint operator on functions, the Lax–Milgram theorem ensures a weak solution for any $L^{2}$ source and Dirichlet (or Neumann) data.
Standard elliptic regularity upgrades weak to smooth solutions.
If $U_{1},U_{2}$ solve (6) with identical boundary data then $\triangle(U_{1}-U_{2})=0$ and $U_{1}-U_{2}$ is harmonic; contractibility implies constant, proving uniqueness up to an additive constant. ∎

---

[^vision]: Neuroscience shows that the 3-D scene we *see* is *reconstructed* by the visual cortex from retinal patterns; “external space” is therefore a brain-generated model, not a direct datum.
[^light]: Our metric is operationally defined by light-signal intervals: null paths coincide with causal influence lines, reflecting practical metrology since Einstein.
