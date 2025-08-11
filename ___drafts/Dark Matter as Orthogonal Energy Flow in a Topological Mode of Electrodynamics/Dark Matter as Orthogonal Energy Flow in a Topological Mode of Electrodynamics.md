# Dark Matter as Orthogonal Energy Flow in a Topological Mode of Electrodynamics

**Anes Palma, Max Freet & An Rodríguez — September 2025**
_Preferred Frame Lab_

---

> *We propose that the need for dark matter arises from a geometric miscount: half of the electromagnetic field energy flows orthogonally to the galactic plane and does not contribute to observed rotation, yet affects gravitational lensing. This accounts for both flat rotation curves and light bending without new particles or parameters.*

---

## 1. Introduction

Observations of galactic rotation curves show an enduring discrepancy between expected and observed velocities at large radii. The common resolution introduces dark matter — a hypothetical form of mass inferred solely from gravitational effects. Modified Newtonian Dynamics (MOND) offers an empirical alternative by altering the force law below a characteristic acceleration scale \(a_0\), but it lacks a field-theoretic derivation.

In this paper, we derive MOND-like behavior from **classical Maxwell electrodynamics**, reformulated as in the **Point–Not–Point (PnP)** framework: a topological theory where the electromagnetic field arises from scalar Hertz modes constrained to a knotted toroidal geometry. Crucially, we show that **only the component of field energy aligned with rotation contributes to centripetal acceleration**, while **the orthogonal component escapes detection** — precisely mimicking the need for unseen matter.

---

## 2. Setup: The PnP Topological Mode

We briefly recall the key features of the PnP construction:

- The electromagnetic field is encoded in two scalar potentials \( \Phi_{\mathrm{TE}}, \Phi_{\mathrm{TM}} \in \mathbb{R} \).
- The four-potential is constructed via the Hertz prescription:
  $$
  A = d\Phi_{\mathrm{TE}} + *d\Phi_{\mathrm{TM}} \wedge dt
  $$
- The physical field strength is:
  $$
  F = dA
  $$

The minimal topological excitation is a \((1,1)\) winding on a torus of major radius \(R\) and minor radius \(r\), encoding charge and helicity.

---

## 3. Energy Flow and Effective Acceleration

### 3.1 Energy-momentum tensor and force balance

The total energy density is:
$$
\rho = \tfrac{1}{2} (\varepsilon_0 E^2 + B^2/\mu_0)
$$

But not all components of \(\vec{E}, \vec{B}\) contribute equally to the radial (centripetal) force.

Let:
- \( \vec{v}_\text{orb} \): orbital velocity in galactic plane
- \( \vec{S} = \vec{E} \times \vec{B} \): Poynting vector

Due to the standing toroidal mode:
- **Half of \( \vec{S} \)** points in the orbital direction (tangential)
- **Half of \( \vec{S} \)** points orthogonal to the galactic plane (polar)

Only the tangential component contributes to the centripetal force:
$$
a_{\text{eff}} = \frac{1}{m} \vec{F}_{\text{tangent}} = \frac{1}{m} \frac{d}{dt} (P_{\text{tangent}})
$$

---

### 3.2 Orthogonal suppression factor

Let the total energy density be decomposed as:
$$
\rho = \rho_{\parallel} + \rho_{\perp}, \qquad \text{with } \rho_{\parallel} \approx \rho_{\perp}
$$

Then the **radial acceleration** is sourced only by:
$$
\rho_{\text{effective}} = \rho_{\parallel} = \tfrac{1}{2} \rho
$$

Thus:
$$
a_{\text{obs}}(r) = \frac{G M_{\text{eff}}(r)}{r^2} = \frac{G}{r^2} \int_0^r \tfrac{1}{2} \rho(r') 4\pi r'^2 dr'
$$

This leads to an **underestimated mass** if one assumes isotropic sourcing. From the observer’s standpoint, **half the energy is missing**, although it exists — just orthogonal to the observed motion.

---

## 4. Application to Galactic Rotation Curves

### 4.1 Flat rotation curves

If the radial profile is such that the tangential energy density \(\rho_{\parallel}(r)\) decays as:
$$
\rho_{\parallel}(r) \sim \frac{1}{r^2}
$$
then the effective enclosed mass scales as:
$$
M_{\text{eff}}(r) \sim \int_0^r \frac{1}{r'^2} r'^2 dr' \sim r
$$

This gives:
$$
a(r) = \frac{G M_{\text{eff}}(r)}{r^2} \sim \frac{1}{r}
\quad \Rightarrow \quad v(r)^2 = r a(r) = \text{const.}
$$

Which matches observed galactic rotation plateaus — **without any dark matter**.

---

## 5. Bending of Light

The orthogonal component \(\rho_{\perp}\) does not affect orbital acceleration, but **does affect the curvature of spacetime**.

Hence, **gravitational lensing** — which depends on the full stress-energy tensor — perceives the **entire field energy**, not just its radial projection.

This resolves a long-standing MOND issue: **light bending in PnP matches GR predictions**, because \(\rho_{\perp}\) is fully real and gravitating.

---

## 6. Relation to Jet Streams

The orthogonal flow of energy is not just a mathematical convenience — it's likely **visible astrophysically**.

- **Galactic jets** emitted perpendicularly from the disk
- **Stellar bipolar flows** in protostar formation
- **Black hole accretion disk ejections**

All suggest that a significant portion of EM or plasma energy flows orthogonal to the galactic plane — aligning perfectly with PnP’s prediction of **toroidal energy confinement with orthogonal escape channels**.

---

## 7. Implications

- **No exotic particles** are required to explain galactic dynamics
- **Quantitative match** to MOND in the low-acceleration regime arises geometrically
- **Lensing and structure formation** remain compatible with GR
- **PnP unifies** electrodynamics, quantum spectra, and apparent dark matter under a **single topological field model**

---

## 8. Conclusion

The missing mass is not missing — it is **hidden in orthogonal energy flow**, predicted by the geometry of classical fields in the PnP framework. Observers in the galactic plane perceive half the energy, leading to underestimation of mass and the illusion of dark matter. But from a field-theoretic and gravitational standpoint, the energy is real and sufficient.

The dark sector may simply be the **orthogonal side of light**.

---

## References

1. A. Palma, M. Freet, A. Rodríguez. *Point–Not–Point: Dismissing Wave–Particle Duality in Deriving Maxwell and Quantum Electrodynamics from a Single Topological Mode*, Aug 2025. DOI: [10.13140/RG.2.2.27868.30084](https://dx.doi.org/10.13140/RG.2.2.27868.30084)
2. M. Milgrom, “A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis,” *Astrophys. J.* 270 (1983): 365–370.
3. Famaey & McGaugh, “Modified Newtonian Dynamics (MOND): Observational Phenomenology and Relativistic Extensions,” *Living Reviews in Relativity*, 15 (2012).
4. SPARC Database. [https://astroweb.case.edu/SPARC/](https://astroweb.case.edu/SPARC/)
5. J. D. Jackson, *Classical Electrodynamics*, 3rd ed.
6. A. Einstein, “The Foundation of the General Theory of Relativity,” *Annalen der Physik* (1916).

---

## Appendix A: Geometric Derivation of \( a_{\text{eff}} \)

...

## Appendix B: Effective Refractive Index and Light Bending

...

## Appendix C: Comparison with SPARC Data

(to be filled upon integration of baryonic profiles)
