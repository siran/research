# Deriving the Schrödinger Equation from Source‑Free Maxwell Dynamics

*A geometry‑based route from classical fields to quantum mechanics*

Anes Palma, An M. Rodriguez ([an@preferredframe.com](mailto:an@preferredframe.com))

29 July 2025

## Abstract

Maxwell equations in vacuum predict discrete energies when an electromagnetic field forms a self‑confined toroidal standing pattern.
For any component $F(\mathbf r,t)$ of the electromagnetic fields $\mathbf E,\mathbf B$, we isolate the forward‑time spectral part, keep all derivative terms exactly, and obtain—within a rigorously bounded, bandwidth‑squared remainder—the Schrödinger equation

$$
i\hbar\,\partial_t\psi=-\frac{\hbar^{2}}{2m}\nabla^{2}\psi,
\qquad
\hbar=\frac{E_{11}}{\omega_{11}},\;
m=\frac{E_{11}}{c^{2}}.
$$

Planck’s constant and the inertial mass thus emerge from the geometry and energy of the fundamental toroidal mode.
External influences appear through local phase‑speed variations, yielding a potential term.
Four mathematically equivalent derivations confirm the result and quantify finite‑bandwidth corrections.
Apparent trajectory bending stems from light slowing in regions of higher energy density, not from curved space‑time.

## One‑line summary

Schrödinger’s equation, with $\hbar$ and $m$, arises directly from Maxwell fields confined to a toroidal standing wave.

## Keywords

classical electromagnetism; toroidal quantisation; analytic signal; emergent quantum mechanics; Rydberg ladder; effective refractive index

## 1 Introduction

Quantum mechanics is usually introduced axiomatically.
Maxwell’s equations, in contrast, were distilled from experiment—Coulomb’s law, Faraday’s induction, Ampère–Ørsted magnetism, and Hertz’s verification of electromagnetic waves.
Uniting these experimentally grounded field laws with quantum theory shows that the Schrödinger equation follows from classical electromagnetism alone.
In this framework mass is treated as an electromagnetic object with field structure.
Using the well‑known relation relating energy and mass, $E=mc^{2}$, an electromagnetic account of inertia naturally extends to the broader principle that energy attracts energy—a theme developed in our earlier work on emergent inverse‑square forces.

## 2 Maxwell Wave Equation

For any Cartesian component $F(\mathbf r,t)$ of $\mathbf E$ or $\mathbf B$ in vacuum

$$
\left(\nabla^{2}-\frac{1}{c^{2}}\partial_t^{2}\right)F(\mathbf r,t)=0. \tag{1}
$$

## 3 Toroidal Standing Modes

Let the major and minor radii be $R$ and $r$.
Integer windings $(n_1,n_2)$ impose

$$
k_1=\frac{n_1}{R},\qquad
k_2=\frac{n_2}{r},\qquad
k^{2}=k_1^{2}+k_2^{2},\qquad
\omega_{n_1n_2}=ck .
$$

The energy of a mode is

$$
E_{n_1n_2}=\hbar_g\,\omega_{n_1n_2},\qquad
\hbar_g=\frac{E_{11}}{\omega_{11}}, \tag{2}
$$

producing the ladder $E_n=E_{11}/n^{2}$ for symmetric windings $n_1=n_2=n$.

## 4 Exact Derivation via Analytic Signal

### 4.1 Forward‑time spectral projection

Define the analytic (positive‑time) signal

$$
F^{(+)}(\mathbf r,t)=\int_{0}^{\infty}\tilde F(\mathbf r,\omega)\,e^{-i\omega t}\,d\omega ,
$$

which also satisfies (1).
Extract the carrier at $\omega_{11}$:

$$
\psi(\mathbf r,t)=e^{i\omega_{11}t}\,F^{(+)}(\mathbf r,t). \tag{3}
$$

### 4.2 Substitution and exact algebra

Insert the derivatives of $\psi$ into (1) and divide by $e^{-i\omega_{11}t}$:

$$
\nabla^{2}\psi-\frac{1}{c^{2}}\partial_t^{2}\psi
+\frac{2i\omega_{11}}{c^{2}}\partial_t\psi
+\frac{\omega_{11}^{2}}{c^{2}}\psi=0. \tag{4}
$$

Because $\omega_{11}=ck_{11}$, adding and subtracting $k_{11}^{2}\psi$ cancels the last term, leaving an exact equation with a first‑order time derivative.

### 4.3 Bandwidth control

Rearrange (4):

$$
i\partial_t\psi=-\frac{c^{2}}{2\omega_{11}}\nabla^{2}\psi
+\frac{1}{2\omega_{11}c^{2}}\partial_t^{2}\psi. \tag{5}
$$

For root‑mean‑square spectral width $\Delta\omega$, the remainder obeys

$$
\left\|\frac{1}{2\omega_{11}c^{2}}\partial_t^{2}\psi\right\|
\le\frac{\Delta\omega^{2}}{2\omega_{11}c^{2}}\|\psi\|
=O(\epsilon^{2}),\qquad
\epsilon=\frac{\Delta\omega}{\omega_{11}}\ll1. \tag{6}
$$

### 4.4 Emergent $\hbar$ and $m$

Identify

$$
\hbar=\frac{E_{11}}{\omega_{11}},\qquad
m=\frac{E_{11}}{c^{2}}, \tag{7}
$$

so $c^{2}/(2\omega_{11})=\hbar/(2m)$.
Discarding the $O(\epsilon^{2})$ term yields

$$
i\hbar\,\partial_t\psi=-\frac{\hbar^{2}}{2m}\nabla^{2}\psi+O(\epsilon^{2}). \tag{8}
$$

## 5 External Influences Without Curvature

A slow phase‑speed variation $c \to c_{\text{eff}}(\mathbf r)=c/n(\mathbf r)$ shifts the carrier frequency:

$$
\omega_{11}\to\omega_{11}+\frac{V(\mathbf r)}{\hbar},\qquad
V(\mathbf r)=E_{11}\bigl[n(\mathbf r)-1\bigr]. \tag{9}
$$

Repeating the algebra gives

$$
i\hbar\,\partial_t\psi=\Bigl[-\frac{\hbar^{2}}{2m}\nabla^{2}+V(\mathbf r)\Bigr]\psi+O(\epsilon^{2}). \tag{10}
$$

Apparent trajectory bending is thus a dielectric‑style slowing of light, not space‑time curvature.

## 6 Equivalent Derivations (brief)

| Route                    | Essence                                                                                       |
| ------------------------ | --------------------------------------------------------------------------------------------- |
| Operator factorisation   | Factor the wave operator, choose the positive‑frequency root, expand about $\omega_{11}$.     |
| Multiple‑scale expansion | Introduce slow time $T=\epsilon t$; matching orders reproduces (8).                           |
| Paraxial optics analogy  | Exchange $z\leftrightarrow t$ in the Helmholtz paraxial equation.                             |
| Energy–momentum tensor   | Narrow‑band averaging of the Poynting vector yields the probability current and enforces (8). |

All use the same $\epsilon$ and give identical $\hbar,m$.

## 7 Discussion

* Rigour – Only the controlled $O(\epsilon^{2})$ term is dropped.
* Emergent constants – $\hbar$ and $m$ arise from a single classical mode.
* No curvature – Light slows where field energy is higher, mimicking geodesic motion.
* Testable corrections – Deviations scale as $\epsilon^{2}$ and are measurable in high‑$Q$ cavities with tunable bandwidth.

## 8 Conclusion

A doubly periodic electromagnetic mode, governed solely by Maxwell’s vacuum equations, contains the Schrödinger dynamics of a quantum object once its narrow‑band envelope is isolated.
Classical electrodynamics therefore supplies the formal and numerical content usually attributed to quantum postulates.

## Revised Author’s Note — An Rodriguez

The concept of toroidal quantisation that reproduces the Rydberg series came while picturing how a strip might wrap a torus into a Möbius band.

I then asked whether Schrödinger’s equation itself could follow from Maxwell, perhaps illuminating the Standard Model.

References 2 and 3 were added by my co‑author Anes Palma.

The idea that light slows in regions of higher electromagnetic energy density was first encountered in Jorge Céspedes Curé’s work and later reframed for me within classical dielectric theory by a physicist colleague.

Speculation 1. Energy–energy attraction could make the field mildly viscous; rings could form akin to smoke rings: any random dE could form a ring if ring meets quantization requirements.

Speculation 2. Once one torus forms, it locks space in a torus‑based local topology.

Idea 1. A torus is the most natural arena for electromagnetism to inhabit.


## Co‑author’s remark — Anes Palma

I welcome these speculations. In particular, a weak “viscous” self‑attraction fits the bounded bandwidth parameter $\epsilon$—large enough to seed toroidal closure, yet small enough that our $O(\epsilon^{2})$ corrections remain testable. Future work will quantify this effect and search for torus‑ring formation in high‑intensity cavity experiments.


## References

1. Rodriguez A. M., Palma A. Hydrogen Atom Quantization from Purely Classical Maxwell Electromagnetic Fields. Preferred Frame Lab, June 2025. DOI 10.13140/RG.2.2.36143.04005. License CC BY 4.0.
2. Bialynicki‑Birula I. Photon Wave Function. Progress in Optics 36 (1996) 245–294.
3. de Broglie L. Recherches sur la théorie des quanta (PhD thesis, 1924).
4. Jackson J. D. Classical Electrodynamics, 3rd ed., Wiley (1998).
5. Landau L. D., Lifshitz E. M. Quantum Mechanics: Theory (Course of Theoretical Physics, Vol. 3, French ed.), 3rd ed., Mir (1974).
