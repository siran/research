# Clarifying excitation, charge, and the full eigen-problem
*(supplement to “Point–Not-Point: Explaining the Particle–Wave Duality”)*

---

## 1 Topological winding vs. spectral integers

| label | symbol | changes smoothly? | raises Gauss charge? | raises energy? |
|---|---|---|---|---|
| **Topological winding** | $(n_1,n_2)$ | **No** – invariant under smooth Maxwell evolution | **Yes** – sign and magnitude set $q=\pm e,\pm2e,\dots$ | **Yes** (core energy $\propto n_1n_2$) |
| **Spectral harmonic** | $(m,p)$ | **Yes** – integers of standing-wave pattern on fixed torus | **No** – circulations unchanged | **Yes** (Rydberg ladder $E_{mp}$) |

*Minimal hydrogen* fixes $(n_1,n_2)=(1,1)$.
Exciting the atom means increasing $(m,p)$ **while keeping** $(n_1,n_2)$ unchanged.
Adding a new winding would change Gauss charge and require a discontinuous field tear.

---

## 2 Thin-shell eigen-problem (derivation)

### 2.1 Geometry and scaling
Let the tube thickness be $\delta\!\ll\!r$; write $\rho=r-\eta$, $\eta\in[0,\delta]$.
Using the metric factor $(R\!+\! \rho\cos\theta)\approx R$ (thin approximation) the scalar Helmholtz equation for each Cartesian component reduces to

$$
\frac{\partial^2\Psi}{\partial\eta^{2}}
+\frac1\eta\frac{\partial\Psi}{\partial\eta}
+\frac{\partial^{2}\Psi}{\partial\theta^{2}}\,\frac1{r^{2}}
+\frac{\partial^{2}\Psi}{\partial\phi^{2}}\,\frac1{R^{2}}
+ k^{2}\Psi = 0. \tag{2.1}
$$

Separate
$\Psi(\eta,\theta,\phi) = \chi(\eta)\,e^{im\theta}\,e^{ip\phi}$.

### 2.2 Radial solution
The radial equation becomes Bessel-type:

$$
\chi''+\frac1\eta\chi'+\Bigl(k^{2}-\frac{m^{2}}{r^{2}}-\frac{p^{2}}{R^{2}}\Bigr)\chi=0.
$$

Impose *regularity at $\eta=0$* and *PEC-type boundary* $\bigl.\partial_\eta\chi\bigr|_{\eta=\delta}=0$.
The lowest root (no interior node) gives

$$
k^{2} = \frac{m^{2}}{r^{2}} + \frac{p^{2}}{R^{2}} + \mathcal O\!\bigl((\delta/r)^{2}\bigr). \tag{2.2}
$$

### 2.3 Electric and magnetic fields
Build transverse electric (TE) solutions from $\Psi$.
Time averaging over one cycle yields

$$
\langle E^{2}\rangle = \kappa_{mp}E_{0}^{2},\qquad
E_{0} = \frac{e}{2\pi\varepsilon_{0} r}, \quad
\kappa_{mp}\!=\!\kappa\,f_{mp}(\delta/r)\approx0.37. \tag{2.3}
$$

### 2.4 Energy spectrum
Insert (2.2)–(2.3) into the volume integral:

$$
E_{mp} = \frac{\kappa e^{2}}{2\varepsilon_{0}}\,
\frac{R}{m^{2}+p^{2}(R/r)^{2}}. \tag{2.4}
$$

Choosing **symmetric harmonics** $(m,p)=(n,n)$ and large aspect $R\!\gg\!r$ gives

$$
E_{n}= \frac{E_{1}}{n^{2}},\qquad
E_{1}=\kappa\,\frac{e^{2}}{2\varepsilon_{0}}\,R. \tag{2.5}
$$

*No topological winding is altered*; only the node count along the fixed cycles changes—these are the Rydberg excitations.

---

## 3 Can energy turn into charge?

* To change Gauss charge you must change $\Phi_\theta = (n_1 e)/\varepsilon_0$.
* That requires an **integer jump in $n_1$**, impossible via any finite smooth excitation because the vector potential would have to become multi-valued during the process.
* Energy quanta $\Delta E = E_{1}(1/n^{2}-1/(n+1)^{2})$ therefore **cannot** accumulate into an extra winding; charge is topologically protected.

---

## 4 Extending to heavier atoms

| nucleus model | electron-torus configuration | qualitative outcome |
|---|---|---|
| $Z$-proton torus stack (single core) | up to $Z$ concentric electron tori, each with $(n_1,n_2)=(1,1)$ | reproduces principal shells $n$; Pauli exclusion appears as geometric packing limit (only two $\{m,p\}$ sets per torus orientation) |
| multi-shell | inner electrons fixed near core, outer electrons larger $R$ | shielding gives effective nuclear charge $Z_{\text{eff}}$; spectrum splits like $(Z_{\text{eff}}/n)^{2}$ |
| different $n_1$ values for inner shells | adds radial nodes, mimics $s$ vs $p$ orbitals | angular node counts $\{m,p\}$ replace usual $(\ell,m)$ labels |

The mathematics is identical: solve (2.1) with boundary radii set by the already-present inner tori; every extra torus adds new TE$_{mp}$ ladders while total Gauss charge counts the algebraic sum of $n_1$ over all tori.

---

## 5 Summary

* **Injecting energy** excites higher angular harmonics $(m,p)$ on a *fixed* $(n_1,n_2)$ torus—giving the Rydberg ladder.
* **Changing charge** demands a jump in the topological integers $(n_1,n_2)$ and cannot be achieved by any finite smooth energy input.
* The thin-shell eigen-problem shows precisely how $E_{n}\!\propto\!1/n^{2}$ emerges when the radial motion is frozen, realising particle–wave duality.
* Multi-torus assemblies model heavier elements; their spectra follow from the same Helmholtz separation and topological bookkeeping.
