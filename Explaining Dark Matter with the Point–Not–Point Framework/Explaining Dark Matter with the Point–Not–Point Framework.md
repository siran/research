# Explaining Dark Matter with the Point–Not–Point Framework
An M. Rodríguez, Anes Palma, Max Freet
Preferred Frame Lab — August 2025

---

## Abstract

The concept of dark matter was introduced in the Newtonian paradigm to explain observed flat galactic rotation curves. MOND attempts to modify Newtonian gravity empirically; particle models introduce new unseen substances. In the Point–Not–Point (PNP) framework, no extra matter or arbitrary law changes are needed. We consider a baryonic bulge with the observed luminous–matter profile. Its PNP scalar field $U_b$ generates, outside the bulge, a spherically symmetric energy–flow halo consisting of two orthogonal components: a (weak) radial energy flux and a dominant tangential (circulating) energy flow. The halo is thus an emergent flow configuration of the same field, not an added substance. From Maxwell’s equations in scalar form $F = d(\star dU)$, we compute the stress–energy tensor explicitly and show that the tangential pressure profile induced by the bulge reproduces flat rotation curves without dark matter.

---

## 1  Introduction

The Newtonian framework predicts that the orbital velocity of a star in a galaxy should decrease with radius, $v(r) \propto r^{-1/2}$, if only luminous matter is present. Observations instead show $v(r) \approx \text{const}$ at large $r$. The standard fix introduces invisible "dark matter" halos; MOND adjusts the force law empirically.

We use the Point–Not–Point (PNP) framework as formulated in [1] to describe the electromagnetic field and its energy flows, and apply it to the dynamics around galactic bulges.

---

## 2  Bulge-driven halo: two orthogonal energy flows

Let the baryonic bulge have the measured mass–light profile and define its stationary PNP field $U_b$ via

$$
F_b = d(\star dU_b),\qquad dF_b=0,\quad d\!\star F_b=0.
$$

Outside the bulge radius $R_b$, the same field supports a spherically symmetric energy–flow halo:

- **Radial component:** angle–averaged Poynting flux $\langle S_r\rangle>0$ (weak).
- **Tangential component:** dominant circulating energy (orthogonal to $\hat r$).

Write the time–averaged fields

$$
\mathbf B=*\,dU_b,\qquad \mathbf E=*\,d*\,dU_b,
$$

and the energy density

$$
u(r)=\frac{\varepsilon_0}{2}\big(E^2+c^2B^2\big),\qquad
E^2=E_r^2+E_\perp^2,\; B^2=B_r^2+B_\perp^2.
$$

The flow decomposition is

$$
\mathbf S=\frac{1}{\mu_0}\,\mathbf E\times\mathbf B
= S_r(r)\,\hat r + \mathbf S_\perp(r),\qquad
\langle S_r\rangle=\frac{K}{4\pi r^2}.
$$

No extra degrees of freedom are added: the halo is a configuration of $U_b$ constrained by stationarity and momentum conservation.

---

## 3  Stress from radial/tangential flows

The time–averaged Maxwell stress is

$$
T_{ij}=\varepsilon_0\!\left(E_iE_j+c^2B_iB_j-\frac{\delta_{ij}}{2}(E^2+c^2B^2)\right).
$$

Define the radial tension and tangential pressure pieces:

$$
\sigma_r:=\frac{\varepsilon_0}{2}(E_r^2+c^2B_r^2),\qquad
u_\perp:=\frac{\varepsilon_0}{2}(E_\perp^2+c^2B_\perp^2).
$$

Spherical symmetry (of the flow ensemble) implies a diagonal stress with

$$
T_{rr}=\sigma_r-u_\perp,\qquad
T_{\theta\theta}=T_{\phi\phi}=\tfrac12(\sigma_r-u_\perp)\,r^2.
$$

In a bulge–driven halo, tangential energy dominates: $\sigma_r\ll u_\perp$, hence

$$
T_{rr}\approx -\,u_\perp\ (<0).
$$

---

## 4  Momentum conservation in the halo

Stationarity and spherical symmetry imply $\nabla\!\cdot T = 0$, whose radial component is

$$
\frac{dT_{rr}}{dr}+\frac{2}{r}(T_{rr}-T_{\theta\theta}/r^2)=0.
$$

With $T_{\theta\theta}=T_{\phi\phi}$ and $T_{rr}=\sigma_r-u_\perp$ this reduces, for $\sigma_r\ll u_\perp$, to

$$
\frac{du_\perp}{dr}+\frac{2u_\perp}{r}=0
\quad\Rightarrow\quad
u_\perp(r)=\frac{C}{r^2}
$$

if the tangential energy transport speed is constant. However, in PNP the effective transport speed is not constant; it depends on $u$ via the index $n(u)$. This changes the scaling.

---

## 5  Energy–flux continuity set by the bulge

Stationarity gives $\nabla\!\cdot\mathbf S=0$, hence

$$
\frac{d}{dr}\!\big(r^2\langle S_r\rangle\big)=0
\quad\Rightarrow\quad
\langle S_r\rangle=\frac{K}{4\pi r^2}.
$$

The constant flux $K$ is not free: it is fixed by the interior solution $U_b$ (the measured bulge) through matching across $r=R_b$:

$$
K=4\pi R_b^2\,\langle S_r(R_b^+)\rangle
=4\pi R_b^2\,\langle S_r(R_b^-)\rangle,
$$

where the inner value is computed from $U_b$ (bulge luminosity/field outflow). Thus the halo transport is set by the bulge.

---

## 6  Constitutive law from PNP

Write $\langle S_r\rangle=v_g(r)\,u(r)$, where $v_g$ is the effective transport speed of energy across a spherical shell, determined by local field structure of $U_b$ (dielectric–style slowing in PNP):

$$
v_g(u)=\frac{c}{n(u)}.
$$

Flux continuity gives the algebraic self–consistency

$$
u(r)\,r^2=K\,n(u(r)).
$$

This links the bulge–set flux $K$ and the halo profile $u(r)$ via the PNP constitutive law $n(u)$.

---

## 6.1  Example: $n(u)$ from the $O(\epsilon^2)$ Maxwell $\to$ Schrödinger term

In the PNP derivation of the Schrödinger equation, the $O(\epsilon^2)$ term modifies the dispersion relation as

$$
\omega(k,u)\approx c k\left(1+\frac{\alpha}{u}\right),
$$

for weak dispersion, with $\alpha$ a constant depending on the mode structure. The group index is then

$$
n(u)=\frac{c}{v_g}\approx 1+\frac{\alpha}{u}.
$$

Substituting into $u r^2 = K\,n(u)$ gives

$$
u(r)\,r^2 = K\left(1+\frac{\alpha}{u(r)}\right)
\quad\Rightarrow\quad
u^2(r)\,r^2 - K\,u(r) - \alpha K=0.
$$

Solving:

$$
u(r) = \frac{K + \sqrt{K^2 + 4\alpha K r^2}}{2\,r^2}.
$$

For $r\gg \sqrt{4\alpha/K}$:

$$
u(r) \approx \frac{\sqrt{\alpha K}}{r}.
$$

Thus the tangential stress scales as $1/r$, giving a constant orbital velocity.

---

## 7  Rotation curves

Given $T_{rr}\approx -\,u_\perp$ and $u_\perp\propto u$ for the isotropic tangential flow ensemble generated by $U_b$, the radial acceleration of a compact test star (another $U$–knot aggregate) at radius $r$ is

$$
a_r(r) \;=\; \frac{4\pi a^2}{E_\star/c^2}\,T_{rr}(r)
\;\propto\;-\,u(r).
$$

Hence the shape of $a_r$ is the shape of $u(r)$, which for the above $n(u)$ tends to $1/r$ at large $r$:

$$
a_r(r)\propto -\frac{1}{r},\qquad v^2(r)=r|a_r(r)|=\text{const}.
$$

Flat rotation curves emerge as an energy–flow effect of the bulge–generated PNP field.

---

## 8  Discussion

This derivation uses only:

1. The PNP scalar formulation of electromagnetism as in [1].
2. The observed baryonic bulge profile.
3. Maxwell stress and momentum conservation.
4. The $O(\epsilon^2)$ dispersion correction from the PNP $\to$ Schrödinger link.

No dark matter substance is introduced; no force laws are modified by hand. The halo is an emergent flow of the same scalar field that encodes all electromagnetic structure in PNP. The resulting large–radius acceleration profile matches the observed flat rotation curves.

---

## Addendum — What is $\alpha$ and is the approximation necessary?

We give two closures for $n(u)$ and derive $u(r)$ in each case.

**Closure 1 (weak dispersion)**: from the $O(\epsilon^2)$ envelope term and local ergodicity $\epsilon^2\propto 1/u$,

$$
n(u)=1+\frac{\alpha}{u},\quad \alpha=\gamma_2\,\chi.
$$

Inserting into flux continuity yields

$$
u(r)=\frac{\mathcal K+\sqrt{\mathcal K^2+4\mathcal K\alpha\,r^2}}{2\,r^2}
\ \xrightarrow[r\to\infty]{}\ \frac{\sqrt{\mathcal K\alpha}}{r}.
$$

This gives $T_{rr}\sim -1/r$, hence flat curves.

**Closure 2 (transport-limited)**: with $\epsilon\propto 1/(u r^2)$,

$$
n(u)=1+\beta\,\frac{\mathcal K}{u\,r^2}\quad\Rightarrow\quad u\propto r^{-2},
$$

recovering the Newtonian decline, not flat curves.

Flat curves require Closure 1 or any law with $n(u)$ increasing fast enough as $u$ decreases.

---

## Short, non-technical ResearchGate description

**Explaining Dark Matter with the Point–Not–Point Framework.**
We model a galaxy’s luminous bulge in the Point–Not–Point (PNP) framework and show that it naturally generates a halo of electromagnetic energy flow with two components: a weak radial flux and a dominant tangential circulation. Using only Maxwell’s equations (in the PNP form) plus conservation of momentum and energy flux, we derive the halo’s stress profile and the resulting orbital speeds. A simple link between local energy density and transport speed—motivated by our Maxwell $\to$ Schrödinger analysis—produces a $1/r$ tangential stress and thus constant rotation velocities at large radii. The observed “dark matter” effect emerges from energy flow, without new particles or ad-hoc force laws.

---

## References

1. Palma, A., Rodríguez, A. M. & Freet, M., *Point–Not–Point: Deriving Maxwell Electrodynamics from a Scalar Energy Field and Explaining Particle–Wave Duality*, Aug 2025.
2. Milgrom, M., *A modification of the Newtonian dynamics as a possible alternative to the hidden mass hypothesis*, ApJ 270, 365–370 (1983).
3. Binney, J., Tremaine, S., *Galactic Dynamics*, 2nd ed., Princeton Univ. Press, 2008.
