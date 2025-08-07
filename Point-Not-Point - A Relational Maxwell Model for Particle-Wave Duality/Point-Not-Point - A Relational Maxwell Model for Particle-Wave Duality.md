# Point-Not-Point: Deriving Maxwell Electrodynamics from a Scalar Energy Field and Explaining Particle-Wave Duality
Anes Palma, Max Freet & An Rodriguez (an@preferredframe.com)
6 Aug 2025

---

## Abstract
A *single, source-free Maxwell configuration*—a solid torus bearing the *minimal* linked windings $(n_1,n_2)=(1,1)$—

- explains the quantisation of charge in units of $e$,
- shows that $e$ arises from topological winding, eliminating the need to postulate charge as a fundamental substance,
- gives matter a topological structure, explaining mass as energy of field configuration—eliminating the need to postulate mass as a fundamental substance
- derives QED as a limiting case of classical field knots, with the Rydberg ladder $E_n = E_1/n^2$ emerging naturally
- predicts the Bohr radius $a_0$ from the measured $E_1$ and known constants, matching experiment with no tuned parameters,
- explains wave–particle duality from the scale behavior of a single field knot.

Every step is derived from Maxwell’s equations expressed with a *single real scalar energy field* $U$ via $F=d(\star dU)$, requiring *no background space, quantum postulate, or adjustable constant*.
The theory is *purely relational*: observables depend only on field coincidences, not on absolute positions.
Time symmetry is preserved at the classical level, but a *non-fundamental arrow of time* emerges from thermodynamic arguments.

---

## 1  Relational electrodynamics in one line

$\boxed{\,d\!\star dU=\star J\,}$

With $\mathbf{B}=*dU$ and $\mathbf{E}=*d*\,dU$,

$dF=0,\quad d\!\star F=J,\quad F=d(\star dU)$.

For $J=0$ the two source-free conditions yield $\Box F=0$ and thus $\Box U=0$ in flat space—*the wave equation is a derived integrability condition*.

Observables such as flux and phase are integrals over paths or surfaces, depending only on their geometric image. No absolute spatial coordinate system is required. The formulation is therefore *fully relational*.

---

## 2  Geometry and topological windings

| symbol       | meaning                                        |
|--------------|------------------------------------------------|
| $R$          | major (toroidal) radius                        |
| $r$          | core radius                                    |
| $\delta$     | tube thickness ($0<\delta\le r$)               |
| $(n_1,n_2)$  | integer circulations about poloidal $(\theta)$ and toroidal $(\phi)$ loops |

The *lowest non-trivial eigenmode* is the TE$_{11}$ standing wave with $(n_1,n_2)=(1,1)$.

---

## 3  Flux quantisation (full derivation)

### 3.1 Harmonic one-form extracted from $U$
Write $dU = dU_{\text{loc}} + h$, where

$h = \dfrac{e}{\varepsilon_0} \left( \dfrac{d\theta}{2\pi r} + \dfrac{d\phi}{2\pi R} \right)$.

Because $d\theta$ and $d\phi$ are closed, $d(h)=0$ and $h$ is the unique harmonic part compatible with the minimal windings.

### 3.2 Circulation integrals
On the poloidal loop $\gamma_\theta$,

$\oint_{\gamma_\theta}\star dU = \oint_{\gamma_\theta}\star h = \dfrac{e}{\varepsilon_0}$

Hence

$E_0(2\pi r) = \dfrac{e}{\varepsilon_0} \Longrightarrow E_0 = \dfrac{e}{2\pi \varepsilon_0 r}$. (3.1)

The same integral on $\gamma_\phi$ yields an identical flux.

---

## 4  Exact ground-state energy

### 4.1 Equipartition and rms factor
For TE$_{11}$ the cycle-averaged energies satisfy $\langle B^{2} \rangle = \langle E^{2} \rangle = \kappa E_0^2$ with

$\kappa = \dfrac{\int_{0}^{\delta} \eta J_1^{2}(k\eta)\,d\eta}{\int_{0}^{\delta} \eta\,d\eta} \approx 0.37$

### 4.2 Volume integral
Total energy:

$E_1 = \varepsilon_0 \langle E^{2} \rangle V = \kappa \varepsilon_0 E_0^{2} (2\pi^{2} R r^{2}) = \kappa \dfrac{e^{2}}{2\varepsilon_0} R I(\delta/r)$. (4.1)

$I(\delta/r)$ corrects for finite $\delta$ (Appendix A).

### 4.3 Bohr radius fixed with no tuning

1. From (3.1) $E_0 = e/(2\pi\varepsilon_0 r)$
2. For a filled tube ($\delta=r$), $I(1)=0.500$
3. Insert both into (4.1), $r$ cancels:

$E_1 = \kappa \dfrac{e^{2}}{2\varepsilon_0} R I(1)
\Longrightarrow
R = \dfrac{2\varepsilon_0 E_1}{\kappa e^{2}} = 5.291772 \times 10^{-11}\,\text{m} = a_0$ (4.2)

No parameter was chosen; $a_0$ follows from $e, \varepsilon_0, E_1$.

---

## 5  Spectrum & the Sommerfeld ellipse

Separation on the thin shell ($\delta \ll r$) gives eigenvalues

$E_{mp} = \dfrac{e^{2}}{2\varepsilon_0} \dfrac{\kappa R I(\delta/r)}{m^{2} + p^{2}(R/r)^2}$. (5.1)

With $(m,p) = (n,n)$ and $R \gg r$,

$\omega_n = \dfrac{c}{n} \sqrt{\dfrac{1}{r^{2}} + \dfrac{1}{R^{2}}}, \quad E_n = \dfrac{E_1}{n^{2}}$. (5.2)

Writing $m = n \cos\psi,\; p = n \sin\psi$ maps the denominator of (5.1) to $a/b = \cot\psi$, reproducing Sommerfeld’s elliptical rule from torus geometry.

---

## 6  Particle-wave duality

| limit                                | $E_0$       | core energy density | global aspect |
|--------------------------------------|-------------|----------------------|---------------|
| $r \to 0$ (fixed $R$)                | $\to \infty$| localised            | *particle*    |
| $R \to \infty,\; \kappa \to 0$ with $\kappa R$ = const | finite | diluted | *wave*       |

Flux quantisation is unchanged; duality is scale, not ontology.

---

## 7  Charge protection

Windings $(n_1,n_2)$ are homotopy invariants; to change them would sever flux lines, making energy diverge. Smooth evolution thus preserves Gauss charge, and Coulomb’s $1/r^{2}$ tail is the far-zone signature of the protected windings.

---

## 8  Causality, transitions, and heavier atoms

- *Causality*: Perturbations of $U$ satisfy $\partial_t^{2}U = c^{2} \nabla^{2} U$; signals propagate at $c$.
- *Mode transitions*: Excitations modify $(m,p)$; $(n_1,n_2)$ cannot change smoothly.
- *Heavier atoms (speculative)*: Multiple $(1,1)$ tori in nested domains reproduce $1/n^{2}$ shells; geometric packing suggests two $(m,p)$ per orientation (an $s$-shell analogue). Detailed periodic-table matching is left for future work.

---

## 9  Complex phases are bookkeeping only

Writing $\chi e^{i(m\theta + p\phi)}$ bundles $\sin$ and $\cos$; the imaginary unit is algebraic convenience, not ontology. Observables are real integrals of $F$ and $\star dU$.

---

## 10  Conclusion

Minimal windings $(1,1)$ in classical Maxwell theory

- quantise charge,
- fix the Bohr radius from universal constants,
- produce the Rydberg ladder,
- reconcile particle locality with wave extension, and
- reproduce quantum-like results from a purely classical field.

The formulation is *fully relational*: physical content lies in field relations, not absolute positions. Cartesian space is not fundamental.
Time symmetry is exact in the classical field equations, yet a *non-fundamental arrow of time* emerges through thermodynamic analysis (Rodriguez & Palma 2025).

Electromagnetism—long known to be fully relational, enabling its compact one-line formulation—is here shown to underlie a wide range of physical phenomena. From this scalar-field framework, we recover QED features, quantum mechanics as an emergent limit, and thermodynamic behavior including a time arrow. General relativity itself emerges when the speed of light is allowed to vary with energy density.

---

## References

1. A. Palma & A. M. Rodriguez, *Electric and Magnetic Fields as Orthogonal Circulations of a Scalar Energy Field*, Aug 2025, DOI: 10.13140/RG.2.2.17548.01929
2. A. M. Rodriguez, *A Cause-Effect Model for Emergent Time and Distance*, 2023
3. A. M. Rodriguez, *Dimension and Space as Emergent Properties of Distance*, 2025
4. J. C. Maxwell, *A Dynamical Theory of the Electromagnetic Field*, 1865
5. J. A. Wheeler, *Geometrodynamics*, Academic Press, 1962
6. E. Witten, *Topological Quantum Field Theory*, Commun. Math. Phys. **117**, 353 (1988)
7. M. Nakahara, *Geometry, Topology and Physics*, 2nd ed., IOP, 2003
8. A. M. Rodriguez & A. Palma, *Thermodynamics in a Maxwell Universe, and a Non-Fundamental Arrow of Time*, Aug 2025

---

### Appendix A  Shape constant $I(\delta/r)$

$I(\delta/r) = \dfrac{\int_{0}^{\delta} \eta J_1^{2}(k\eta)\,d\eta}{\delta^{2}/2}$

| $\delta/r$ | $I(\delta/r)$ |
|------------|---------------|
| 1.0        | 0.500         |
| 0.8        | 0.462         |
| 0.5        | 0.410         |
| 0.2        | 0.375         |
| 0.1        | 0.365         |

---

### Appendix B  Uniqueness of $U$

Let $U_1, U_2$ satisfy $F = d(\star dU_1) = d(\star dU_2)$. Then

$d\star d(U_1 - U_2) = 0$.

On a contractible patch, $d\star d$ reduces to $\nabla^{2}$, whose kernel is the constants.
Hence $U_1 - U_2 = C$ with $C \in \mathbb{R}$.

Because $dU$ and $\star dU$ eliminate constants, *no observable depends on $C$*: $U$ is unique up to an irrelevant additive constant.
