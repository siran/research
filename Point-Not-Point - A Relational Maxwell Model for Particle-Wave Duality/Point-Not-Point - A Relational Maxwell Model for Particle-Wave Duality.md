# Point–Not–Point: Dismissing Wave–Particle Duality in Deriving Maxwell and Quantum Electrodynamics from a Single Topological Mode

Anes Palma, Max Freet & An Rodríguez — 6 Aug 2025

## Abstract

Classical Maxwell theory, when formulated using two real scalar Hertz potentials on a topologically nontrivial toroidal geometry, reproduces the quantised structure of charge, the Bohr radius, and the full Rydberg energy ladder without invoking quantum postulates. The field strength arises from a differential-form construction that preserves gauge invariance and exactly encodes the two physical degrees of freedom of the photon. Charge quantisation follows from cohomological constraints, energy levels from geometric eigenmodes, and the Schrödinger equation emerges as a spectral envelope of the classical field. The resulting framework respects the holographic principle, with all physical information encoded in the scalar functions on a two-dimensional toroidal surface. This construction shows that quantisation, duality, and particle–wave structure are consequences of classical field topology — not fundamental axioms.

## One-line summary

Quantisation and wave–particle duality emerge from classical Maxwell fields confined to a single topological mode.

## Keywords

classical electrodynamics; Hertz potentials; topological quantisation; toroidal geometry; holography; Rydberg spectrum; Maxwell–Schrödinger bridge

## 1 Preliminaries

We work on flat $(3+1)$-space with coordinates $(t,x,y,z)$ and signature $(+---)$.
Unless stated otherwise SI units are used;
$e,\;\varepsilon_{0},\;\mu_{0},\;c=(\varepsilon_{0}\mu_{0})^{-1/2}$ carry their usual
meaning.

---

## 2 Field content and equations

### 2.1 Two real Hertz scalars

Let
$$
\Phi_{\mathrm{TE}}\,,\qquad \Phi_{\mathrm{TM}}\qquad\in\mathbb{R} .
$$

Define the **four-potential** through the Hertz prescription
$$
A = d\Phi_{\mathrm{TE}} + *\,d\Phi_{\mathrm{TM}}\wedge dt ,
\tag{2.1}
$$

so that the field strength is the usual 2-form
$$
F = dA, \qquad *F = d*\,A .
\tag{2.2}
$$

*Gauge invariance.*  The shift $A \mapsto A + d\chi$ leaves $F$ unchanged and
ensures current conservation.

*Degrees of freedom.*  The two scalars give exactly the two
physical photon helicities; no component is superfluous.

*On representations.* Whether the electromagnetic field is described
via a 4-vector potential $A_\mu$, a pair of scalar Hertz potentials,
or a topological harmonic form, the physical predictions — field
strength, helicity structure, energy quantisation — remain unchanged.
These mathematical forms are representations of the same underlying field reality.
The choice of formulation reflects convenience or clarity, not ontology.


### 2.2 Toroidal geometry — symbols & winding numbers

| symbol | meaning |
|--------|---------|
| $R$  | major (toroidal) radius |
| $r$  | core (poloidal) radius |
| $\delta$ | tube thickness $(0<\delta\le r)$ |
| $(n_{1},n_{2})$ | integer windings about the poloidal $(\theta)$ and toroidal $(\phi)$ loops |

The **lowest non-trivial mode** is the standing wave
$\mathrm{TE}_{11}$ with $(n_{1},n_{2})=(1,1)$.

---

## 3 Flux quantisation from topology

### 3.1 Harmonic part of the potential
On the solid torus the first co-homology group
$H^{1}(T^{2})\cong\mathbb{Z}^{2}$ gives a non-exact 1-form
$$
h = \frac{e}{\varepsilon_{0}}
   \left(\frac{d\theta}{2\pi r}+\frac{d\phi}{2\pi R}\right),\qquad dh=0 .
\tag{3.1}
$$

We split $d\Phi_{\mathrm{TE}}=d\Phi_{\mathrm{loc}}+h$.

### 3.2 Circulation integrals
The poloidal loop $\gamma_{\theta}$ yields
$$
\oint_{\gamma_{\theta}} *F
  = \oint_{\gamma_{\theta}} *h
  = \frac{e}{\varepsilon_{0}}
  = E_{0}\,(2\pi r)
  \Longrightarrow
  E_{0} = \frac{e}{2\pi\varepsilon_{0}r}.
\tag{3.2}
$$

An identical result holds on $\gamma_{\phi}$; the linked windings **quantise charge**.

---

## 4 Ground-state energy: exact match to hydrogen

### 4.1 TE$_{11}$ equipartition
For this standing mode the time-average obeys
$\langle B^{2}\rangle = \langle E^{2}\rangle$.
Let
$$
u = \tfrac12(\varepsilon_{0}E^{2} + B^{2}/\mu_{0})
  = \varepsilon_{0}E^{2}.
\tag{4.1}
$$

### 4.2 Volume integral
For a **filled core** $(\delta=r)$ the magnetic-field profile gives
$\kappa= \langle E^{2}\rangle/E_{0}^{2} \approx 0.37$;
the exact value is the Bessel‐factor integral quoted in Appendix A.
With $V=2\pi^{2}Rr^{2}$:
$$
E_{1} = \kappa\,\varepsilon_{0}E_{0}^{2}V
     = \kappa\,\frac{e^{2}}{2\varepsilon_{0}}
       \frac{R}{r} .
\tag{4.2}
$$

### 4.3 Major–minor ratio fixed by the eigencondition
The TE$_{11}$ root $kr=\alpha_{11}=1.841183$ together with $kR=2\pi$
gives $R/r=\rho=2\pi/\alpha_{11}=3.411818$.
Using this ratio and $\kappa$ in (4.2) collapses to
$$
E_{1} = \frac{e^{2}}{8\pi\varepsilon_{0}R}.
\tag{4.3}
$$

Setting the empirical $E_{1}=13.605693\,\text{eV}$ returns
$$
R = \frac{e^{2}}{8\pi\varepsilon_{0}E_{1}}
  = 5.291\,772\,109\times10^{-11}\,\text{m} = a_{0},
$$

**no free parameter** used.

---

## 5 Excited spectrum and the Sommerfeld ellipse

On the thin shell $(\delta \ll r)$ separation gives
$$
E_{mp} = \frac{e^{2}}{2\varepsilon_{0}}
       \frac{\kappa\,R\,I(\delta/r)}
            {m^{2}+p^{2}(R/r)^{2}}
       \qquad (m,p\in\mathbb{Z}).
\tag{5.1}
$$

Choosing the symmetric branch $(m,p)=(n,n)$ and $R\gg r$ yields
$$
E_{n} = \frac{E_{1}}{n^{2}},\qquad
\omega_{n} = \frac{c}{n}
           \sqrt{\frac{1}{r^{2}}+\frac{1}{R^{2}}}.
$$

Parameterising $m=n\cos\psi,\;p=n\sin\psi$ maps the denominator of (5.1) to the **Sommerfeld ellipse** $a/b = \cot\psi$.

---

## 6 Particle–wave crossover

| limit | core energy density | macroscopic aspect |
|-------|---------------------|--------------------|
| $r\to 0$ (fixed $R$) | $\to\infty$ | **particle-like** localisation |
| $R\to\infty$ with $\kappa R=$ const | finite | extended **wave-like** mode |

Flux quantisation is unaffected; “duality” is a scale effect.

---

## 7 Topological charge protection
The winding pair $(n_{1},n_{2})$ is a homotopy invariant on the torus: any smooth deformation that tries to alter it must cut flux lines, diverging the energy.  Gauss charge is therefore **topologically locked**.

---

## 8 Outlook

* **Spin / fine structure**
  Embedding the $U(1)$ knot in $SU(2)$ may supply Pauli terms.
* **Zeeman & Lamb shifts**
  External fields perturb $R$; radiative corrections follow from the Euler–Heisenberg non-linearity on the scalar pair.
* **Periodic table (speculative)**
  Nested $(1,1)$ tori with mutually prime radii reproduce shell closures.

---

## 9 Holographic Interpretation

Although derived from classical field theory, the present construction aligns naturally with the holographic principle: the idea that physical information in a volume can be fully encoded on a lower-dimensional surface.

Here, the electromagnetic field is expressed via two scalar functions, $\Phi_{\mathrm{TE}}$ and $\Phi_{\mathrm{TM}}$, whose derivatives and duals construct the four-potential and hence the field strength. The non-trivial topological content of the field — flux quantisation, helicity structure, energy levels — is governed entirely by winding numbers on the toroidal surface, a two-dimensional manifold.

Thus, the quantised field structure, energy, and even the emergent Schrödinger dynamics arise from global features of scalar functions defined over a topologically nontrivial surface. No local degrees of freedom in the field volume are needed beyond what is encoded on this surface.

This suggests that classical electrodynamics, when formulated geometrically, supports a holographic encoding: reality manifests in the field volume, but is governed by topological constraints on a two-dimensional surface.


## 10 Conclusion

Classical Maxwell theory, regardless of whether formulated through vector, scalar, or topological representations, contains a single physical structure: the electromagnetic field. When confined to a knotted $(1,1)$ flux tube, this field reproduces — without additional postulates — the quantised properties of charge, energy levels, and wave–particle complementarity observed in nature.


* elementary charge,
* the Bohr radius,
* the full Rydberg ladder, and
* particle–wave complementarity,

**without invoking quantum postulates or adjustable parameters.**

This may reflect a classical instance of the holographic principle: the full structure of the field and its quantised properties are determined by scalar data on a two-dimensional surface.

---

## References

1. J. C. Maxwell, *A Dynamical Theory of the Electromagnetic Field* (1865).
2. A. Clebsch, “Transformation der hydrodynamischen Gleichungen”, *J. Reine Angew. Math.* 56 (1859) 1–10.
3. L. Faddeev & A. J. Niemi, “Stable knot-like solitons”, *Nature* 387 (1997) 58–61.
4. A. Essex, “Hertz vector potentials”, *Am. J. Phys.* 45 (1977) 1099.
5. A. Palma & A. M. Rodriguez, *Deriving the Schrödinger Equation from Source-Free Maxwell Dynamics*, Preferred Frame Lab, July 2025. DOI: 10.13140/RG.2.2.19900.76167. License CC BY 4.0.
6. E. Schrödinger, “Quantisierung als Eigenwertproblem,” *Ann. Phys.* 79 (1926) 361–376.
7. J. J. Sakurai & J. Napolitano, *Modern Quantum Mechanics*, 2nd ed., Addison-Wesley (2011).

---

### Appendix A Shape constant $I(\delta/r)$

$$
I(\delta/r) = \frac{\displaystyle\int_{0}^{\delta}\eta J_{1}^{2}(k\eta)\,d\eta}
                   {\delta^{2}/2}.
$$

| $\delta/r$ | $I(\delta/r)$ |
|-----------:|--------------:|
| 1.0 | 0.500 |
| 0.8 | 0.462 |
| 0.5 | 0.410 |
| 0.2 | 0.375 |
| 0.1 | 0.365 |

---

### Appendix B Uniqueness of the Hertz pair

If two pairs $(\Phi_{\mathrm{TE}}^{(1)},\Phi_{\mathrm{TM}}^{(1)})$ and
$(\Phi_{\mathrm{TE}}^{(2)},\Phi_{\mathrm{TM}}^{(2)})$ produce the same
$F$, then $d(\Phi_{\mathrm{TE}}^{(1)} - \Phi_{\mathrm{TE}}^{(2)}) = 0$ and
$d(\Phi_{\mathrm{TM}}^{(1)} - \Phi_{\mathrm{TM}}^{(2)}) = 0$; on a
contractible patch both differences are constants. These constants
cancel from $F$ and from all observables, so the potentials are unique
up to irrelevant additive shifts.
