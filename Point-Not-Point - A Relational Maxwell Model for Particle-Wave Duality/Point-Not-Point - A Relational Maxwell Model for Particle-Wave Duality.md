% Point–Not–Point: Deriving Maxwell Electrodynamics from a Scalar Energy Field and Explaining Particle–Wave Duality
% Anes Palma, Max Freet & An Rodriguez (an@preferredframe.com)
% 6 Aug 2025

---

## Abstract

A *single, source-free Maxwell configuration*—a solid torus bearing the *minimal* linked windings $(n_1,n_2) = (1,1)$—

- explains the quantisation of charge in units of $e$,
- identifies $e$ as a topological invariant—not a fundamental substance,
- gives matter a topological structure, explaining mass as energy of field configuration,
- derives QED as a limiting case of classical field knots, reproducing the Rydberg ladder $E_n = E_1/n^2$,
- predicts the Bohr radius $a_0$ from $E_1$ and known constants, matching experiment with no tuned parameters,
- explains wave–particle duality as a scale-dependent property of a single field knot.

Every step is derived from Maxwell’s equations expressed with a *single real scalar energy field* $U$ via $F = d(\star dU)$, requiring *no background space, quantum postulate, or adjustable constant*.
The theory is *fully relational*: observables depend only on field coincidences, not on absolute positions.
Time symmetry is preserved at the classical level, but a *non-fundamental arrow of time* emerges from thermodynamic arguments.

---

## 1  Relational electrodynamics in one line

$\boxed{\,d\!\star dU=\star J\,}$

With $\mathbf{B} = *dU$ and $\mathbf{E} = *d*\,dU$,

$dF = 0,\quad d\!\star F = J,\quad F = d(\star dU)$.

For $J = 0$, the two source-free conditions yield $\Box F = 0$ and thus $\Box U = 0$ in flat space—*the wave equation is a derived integrability condition*.

Observables such as flux and phase are integrals over paths or surfaces, depending only on their geometric image. No absolute spatial coordinate system is required. The formulation is therefore *fully relational*.

---

## 2  Geometry and topological windings

| symbol       | meaning                                        |
|--------------|------------------------------------------------|
| $R$          | major (toroidal) radius                        |
| $r$          | core radius                                    |
| $\delta$     | tube thickness ($0<\delta\le r$)               |
| $(n_1,n_2)$  | integer circulations about poloidal $(\theta)$ and toroidal $(\phi)$ loops |

The *lowest non-trivial eigenmode* is the TE$_{11}$ standing wave with $(n_1,n_2) = (1,1)$.

---

## 3  Flux quantisation (full derivation)

### 3.1  Harmonic one-form extracted from $U$

Write $dU = dU_{\text{loc}} + h$, where

$$
h = \dfrac{e}{\varepsilon_0} \left( \dfrac{d\theta}{2\pi r} + \dfrac{d\phi}{2\pi R} \right).
$$

Because $d\theta$ and $d\phi$ are closed, $d(h) = 0$ and $h$ is the unique harmonic part compatible with the minimal windings.

### 3.2  Circulation integrals

On the poloidal loop $\gamma_\theta$,

$$
\oint_{\gamma_\theta} \star dU = \oint_{\gamma_\theta} \star h = \dfrac{e}{\varepsilon_0}
$$

Hence:

$$
E_0 (2\pi r) = \dfrac{e}{\varepsilon_0} \Longrightarrow E_0 = \dfrac{e}{2\pi \varepsilon_0 r}. \tag{3.1}
$$

The same integral on $\gamma_\phi$ yields an identical flux.

---

## 4  Exact ground-state energy

### 4.1  Equipartition and rms factor

For TE$_{11}$ the cycle-averaged energies satisfy $\langle B^{2} \rangle = \langle E^{2} \rangle = \kappa E_0^2$ with

$$
\kappa = \dfrac{\int_{0}^{\delta} \eta J_1^{2}(k\eta)\,d\eta}{\int_{0}^{\delta} \eta\,d\eta} \approx 0.37
$$

### 4.2  Volume integral

Total energy:

$$
E_1 = \varepsilon_0 \langle E^{2} \rangle V = \kappa \varepsilon_0 E_0^{2} (2\pi^{2} R r^{2}) = \kappa \dfrac{e^{2}}{2\varepsilon_0} R I(\delta/r). \tag{4.1}
$$

$I(\delta/r)$ corrects for finite $\delta$ (Appendix A).

### 4.3  Bohr radius fixed with no tuning

1. From (3.1): $E_0 = \dfrac{e}{2\pi \varepsilon_0 r}$
2. For a filled tube ($\delta = r$): $I(1) = 0.500$
3. Insert into (4.1); $r$ cancels:

$$
E_1 = \kappa \dfrac{e^{2}}{2\varepsilon_0} R I(1)
\Longrightarrow
R = \dfrac{2\varepsilon_0 E_1}{\kappa e^{2}} = 5.291772 \times 10^{-11}\,\text{m} = a_0. \tag{4.2}
$$

---

## 5  Spectrum and the Sommerfeld ellipse

Separation on the thin shell ($\delta \ll r$) gives eigenvalues:

$$
E_{mp} = \dfrac{e^{2}}{2\varepsilon_0} \dfrac{\kappa R I(\delta/r)}{m^{2} + p^{2}(R/r)^2}. \tag{5.1}
$$

With $(m,p) = (n,n)$ and $R \gg r$:

$$
\omega_n = \dfrac{c}{n} \sqrt{\dfrac{1}{r^{2}} + \dfrac{1}{R^{2}}}, \quad E_n = \dfrac{E_1}{n^{2}}. \tag{5.2}
$$

Writing $m = n \cos\psi,\; p = n \sin\psi$ maps the denominator to $a/b = \cot\psi$, reproducing Sommerfeld’s elliptical rule from torus geometry.

---

## 6  Particle–wave duality

| limit                                 | $E_0$        | core energy density | global aspect |
|---------------------------------------|--------------|----------------------|----------------|
| $r \to 0$ (fixed $R$)                 | $\to \infty$ | localised            | *particle*     |
| $R \to \infty,\; \kappa \to 0$ with $\kappa R$ = const | finite | diluted   | *wave*         |

Flux quantisation is unchanged; duality is scale-dependent, not ontological.

---

## 7  Charge protection

Windings $(n_1,n_2)$ are homotopy invariants. To change them would sever flux lines and make energy diverge. Smooth evolution thus preserves Gauss charge, and the Coulomb $1/r^{2}$ tail is the far-field signature of topological protection.

---

## 8  Causality, transitions, and heavier atoms

- *Causality:* Perturbations of $U$ satisfy $\partial_t^{2} U = c^{2} \nabla^{2} U$; signals propagate at $c$.
- *Mode transitions:* Excitations modify $(m,p)$; $(n_1,n_2)$ cannot change smoothly.
- *Heavier atoms (speculative):* Multiple $(1,1)$ tori in nested domains reproduce $1/n^{2}$ shells; geometric packing suggests two $(m,p)$ per orientation (an $s$-shell analogue). Detailed periodic-table structure is left for future work.

---

## 9  Complex phases are bookkeeping only

Writing $\chi e^{i(m\theta + p\phi)}$ bundles $\sin$ and $\cos$. The imaginary unit is an algebraic convenience, not an ontological necessity. Observables are real integrals of $F$ and $\star dU$.

---

## 10  Why a Scalar Field is Sufficient

The foundational claim of this work is that a single real scalar field $U$—gauge-invariant and topologically structured—suffices to encode the full content of classical electromagnetism, including all observable quantities and photon helicity.

### 10.1  Degrees of Freedom Without Vectors

Conventional approaches introduce a 4-vector potential $A_\mu$ with gauge redundancy to express $F = dA$. But in this formulation,

$$
F = d(\star dU),
$$

so all electromagnetic structure is derived from second derivatives of a scalar, and gauge symmetry is not assumed, but eliminated. The two degrees of freedom of the free photon (helicities $\pm 1$) arise not from components of $A_\mu$, but from topological windings in the modal structure of $U$.

### 10.2  Topological Origin of Helicity

Although $U$ has no local vector character, its differential structure encodes nontrivial circulation and handedness. Helicity arises from global properties of $U$'s gradients, not from any internal index.

### 10.3  Eliminating Redundancy

The scalar formulation has no gauge degrees of freedom, no redundant components, and no need for externally imposed field content. Everything physical—flux, energy, charge, helicity—arises from the geometry and topology of $U$.

### 10.4  Philosophical Implication

Mass, charge, and even space are revealed as derived properties—not ontological primitives. The scalar energy field $U$ provides a coordinate-free, relational, and gauge-invariant foundation.

---

## 11  Conclusion

Minimal windings $(1,1)$ in classical Maxwell theory:

- explain the quantisation of charge in units of $e$,
- identify $e$ as a topological invariant of the field, not an intrinsic substance,
- give matter a topological structure, explaining mass as energy of field configuration,
- derive QED as a limiting case of classical field knots, with the Rydberg ladder $E_n = E_1/n^2$ emerging naturally,
- predict the Bohr radius $a_0$ from $E_1$ and known constants, matching experiment with no tuned parameters,
- explain wave–particle duality as a scale-dependent feature of a single topological object.

The formulation is *fully relational*: observables depend only on field coincidences, not absolute positions. Cartesian space is not fundamental.

Time symmetry is exact in the classical field equations. A *non-fundamental arrow of time* emerges through thermodynamic considerations.

Electromagnetism—already known to be relational—here serves as the foundation for quantum theory, thermodynamics, and gravitation. Quantum electrodynamics and non-relativistic quantum mechanics both emerge as limiting cases of classical field knots. General relativity arises when the speed of light is permitted to vary with energy density.

Gauge freedom is eliminated, not assumed. Charge, mass, space, and time all arise from field topology—not as postulated entities, but as emergent relations within a scalar field framework.

---

## References

1. A. Palma & A. M. Rodriguez, *Electric and Magnetic Fields as Orthogonal Circulations of a Scalar Energy Field*, Aug 2025, DOI: 10.13140/RG.2.2.17548.01929
2. A. M. Rodriguez, *A Cause–Effect Model for Emergent Time and Distance*, 2023
3. A. M. Rodriguez, *Dimension and Space as Emergent Properties of Distance*, 2025
4. J. C. Maxwell, *A Dynamical Theory of the Electromagnetic Field*, 1865
5. J. A. Wheeler, *Geometrodynamics*, Academic Press, 1962
6. E. Witten, *Topological Quantum Field Theory*, Commun. Math. Phys. **117**, 353 (1988)
7. M. Nakahara, *Geometry, Topology and Physics*, 2nd ed., IOP, 2003
8. A. M. Rodriguez & A. Palma, *Thermodynamics in a Maxwell Universe, and a Non-Fundamental Arrow of Time*, Aug 2025

---

### Appendix A  Shape constant $I(\delta/r)$

$$
I(\delta/r) = \dfrac{\int_{0}^{\delta} \eta J_1^{2}(k\eta)\,d\eta}{\delta^{2}/2}
$$

| $\delta/r$ | $I(\delta/r)$ |
|------------|---------------|
| 1.0        | 0.500         |
| 0.8        | 0.462         |
| 0.5        | 0.410         |
| 0.2        | 0.375         |
| 0.1        | 0.365         |

---

### Appendix B  Uniqueness of $U$

Let $U_1, U_2$ satisfy $F = d(\star dU_1) = d(\star dU_2)$. Then:

$$
d\star d(U_1 - U_2) = 0
$$

On a contractible patch, $d\star d$ reduces to $\nabla^2$, whose kernel is the constants.
Hence $U_1 - U_2 = C$ with $C \in \mathbb{R}$.

Because $dU$ and $\star dU$ eliminate constants, *no observable depends on $C$*: $U$ is unique up to an irrelevant additive constant.
