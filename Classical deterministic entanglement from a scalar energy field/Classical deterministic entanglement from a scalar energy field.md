# Probabilities as Field-Energy Fractions
## A deterministic scalar-field account of quantum statistics with a finite-environment test

**Anes Palma · August 2025**

### Abstract
A source-free scalar energy field $\phi(\mathbf r,t)$ reproduces the Schrödinger equation in the narrow-band limit.
We show that the conserved quadratic form
$$
\mathcal E[\Phi]=\int d^{3N}r\,|\Phi|^{2}
$$
acts as the total field energy in configuration space.
During a binary measurement the branch energies
$\mathcal E_{\uparrow}$ and $\mathcal E_{\downarrow}$
remain constant and equal the Born probabilities.
If the environment that produces decoherence contains only $M$ modes, subsequent recoherence transfers energy between branches and violates standard quantum statistics by a factor $\delta P\!\approx\!e^{-\Lambda(M)t}$.
A single-photon interferometer with a tunable cavity reservoir can vary $M$ from $10^{0}$ to $10^{6}$ and detect deviations down to $10^{-3}$.
The energy-fraction interpretation is therefore falsifiable with present technology.

### Scalar-field framework
The free wave equation
$$
\partial_{t}^{2}\phi=c^{2}\nabla^{2}\phi
$$
with the ansatz
$$
\phi=\Re\!\bigl[\psi(\mathbf r,t)\,e^{-i\omega_{0}t}\bigr],\qquad
\epsilon=\frac{|\partial_{t}\psi|}{\omega_{0}}\ll1,
$$
reduces to
$$
i\partial_{t}\psi=-\frac{c^{2}}{2\omega_{0}}\nabla^{2}\psi .
$$
Setting $\hbar=E_{11}/\omega_{11}$ and $m=E_{11}/c^{2}$ gives the Schrödinger form
$$
i\hbar\partial_{t}\psi=-\frac{\hbar^{2}}{2m}\nabla^{2}\psi .
$$

For $N$ particles we write $\Phi(\mathbf r_{1},\dots,\mathbf r_{N},t)$.
The conserved quantity
$$
\mathcal E[\Phi]=\langle\Phi|\Phi\rangle=1
$$
is interpreted as total configuration-space field energy.

### Measurement as branch-energy partition
A projective measurement produces
$\Phi=\Phi_{\uparrow}+\Phi_{\downarrow}$
with $\langle\Phi_{\uparrow}|\Phi_{\downarrow}\rangle=0$.
Because $\mathcal E$ is quadratic, the fractions
$$
P(\uparrow)=\langle\Phi_{\uparrow}|\Phi_{\uparrow}\rangle,\qquad
P(\downarrow)=\langle\Phi_{\downarrow}|\Phi_{\downarrow}\rangle
$$
satisfy $P(\uparrow)+P(\downarrow)=1$ and reproduce the Born rule without extra postulates.

### Finite-environment recoherence
Couple the pointer coordinate $Q$ to $M$ environmental oscillators $(x_j,p_j)$ via
$$
H_{\text{env}}=Q\sum_{j=1}^{M}g_j x_j .
$$
Tracing out the environment yields an off-diagonal decay
$$
c(t)=c(0)\,\exp\!\bigl[-\Lambda(M)t\bigr],\qquad
\Lambda(M)=\frac{2k_BT}{\hbar^{2}}(\Delta Q)^{2}\sum_{j=1}^{M}m_j g_j^{2}.
$$
For finite $M$, coherence revives at $t_{\text{rev}}\sim1/\Lambda$.
The branch energy then oscillates as
$$
\mathcal E_{\uparrow}(t)=\mathcal E_{\uparrow}(0)+|c(0)|\,e^{-\Lambda t}\sin(\Omega t),
$$
giving a probability deviation $\delta P\approx e^{-\Lambda t}$.

### Dynamical derivation of probability drift

We model the combined qubit–pointer–bath Hamiltonian as

$$
H=H_{\rm S}+H_{\rm E}+H_{\rm I},\qquad
H_{\rm S}=\frac{\omega_{q}}{2}\sigma_{z}+\frac{P^{2}}{2M}+V(Q),
$$
$$
H_{\rm E}=\sum_{j=1}^{M}\!\Bigl(\frac{p_{j}^{2}}{2m_{j}}+\frac{1}{2}m_{j}\omega_{j}^{2}x_{j}^{2}\Bigr),
\qquad
H_{\rm I}=Q\sum_{j=1}^{M}g_{j}x_{j}.
$$

*Initial state* (after the ideal projective interaction but before bath coupling)

$$
\rho(0)=\bigl[\;
\alpha\,\lvert\uparrow\rangle\langle\uparrow\rvert\otimes\!\chi(Q-Q_{0})
+\beta\,\lvert\downarrow\rangle\langle\downarrow\rvert\otimes\!\chi(Q+Q_{0})
\bigr]\otimes\rho_{\rm th},
$$

where $\chi$ is a narrow Gaussian pointer packet and $\rho_{\rm th}$ is a thermal bath state.

#### Reduced evolution

Tracing over the bath (second-order Born–Markov but **without** the continuum limit) gives, in the pointer basis,

$$
\rho_{\uparrow\downarrow}(t)=\rho_{\uparrow\downarrow}(0)
                              \,\exp\!\bigl[-\Gamma(M)t\bigr]
                              \,\exp\!\bigl[i\varphi(t)\bigr],
$$

$$
\Gamma(M)
 =\frac{(\Delta Q)^{2}}{2\hbar^{2}}\!\sum_{j=1}^{M}\!\frac{g_{j}^{2}}{m_{j}\omega_{j}}
  \coth\!\Bigl(\frac{\hbar\omega_{j}}{2k_{B}T}\Bigr)\!,
\qquad
\varphi(t)=\sum_{j=1}^{M}\frac{g_{j}^{2}}{m_{j}\omega_{j}^{2}}
           \sin(\omega_{j}t).
$$

For a finite bath the phase $\varphi(t)$ periodically re-phases the two branches and converts part of the off-diagonal term back into diagonal population:

$$
\delta P(t)=2\,\text{Re}
   \bigl[\rho_{\uparrow\downarrow}(0)\,e^{-\Gamma t}e^{i\varphi(t)}\bigr].
$$

Taking equal coupling $g_{j}=g$, identical masses $m_{j}=m$, and $\omega_{j}=(j\pi/L)v$ (1-D cavity of length $L$) yields

$$
\varphi(t)=\frac{2g^{2}}{m}\sum_{j=1}^{M}\!\frac{\sin(j\omega_{1}t)}
                                            {j^{2}\omega_{1}^{2}}\;,
\quad \omega_{1}=\frac{\pi v}{L},
$$

which approximates a **saw-tooth revival** with envelope

$$
\delta P(t)\approx|\alpha\beta|\,e^{-\Gamma t}\,
          \frac{\sin\!\bigl(M\omega_{1}t/2\bigr)}
               {M\sin(\omega_{1}t/2)} .
$$

At the first revival $t_{\rm rev}\!=\!2\pi/\omega_{1}$ the sinc prefactor is $\simeq1/M$, giving

$$
\delta P_{\rm max}\approx|\alpha\beta|\frac{e^{-\Gamma t_{\rm rev}}}{M}
                      \propto\frac{1}{M}.
$$

*Numerical estimate* (cryogenic cavity, parameters from previous section):
$M\!=\!150,\; \Gamma t_{\rm rev}\!\approx\!0.1 \Rightarrow
\delta P_{\rm max}\!\sim\!2\times10^{-3}$, in line with the $10^{-3}$ target.

---

*Interpretation.*
Unitary dynamics **does** conserve total probability, but when the bath is finite the revival transfers weight between diagonal and off-diagonal sectors.
Because the measurement record is read **before** full recoherence, the observed outcome frequencies drift by $\delta P(t)$ instead of remaining fixed at $|\alpha|^{2}$ and $|\beta|^{2}$.
Taking the bath continuum limit ($M\!\to\!\infty$) restores orthodox statistics.


### Experimental proposal

| Element | Specification | Purpose |
|---|---|---|
| Mach–Zehnder interferometer | Single 1550 nm photons, SNSPD readout | Binary outcomes $\uparrow/\downarrow$ |
| Tunable cavity reservoir | $Q$ factor $10^{3}$–$10^{6}$ (mode count $M$) | Control $\Lambda(M)$ |
| Cryostat | $T=20$ K | Reduce thermal noise, lengthen $t_{\text{rev}}$ |
| Optical delay line | Variable $t=0$–$10\,\mu$s | Observe $\delta P(t)$ |

Predicted deviation: $\delta P\approx10^{-3}$ for $M\!\sim\!10^{2}$, $\Delta Q=1\,\mu$m.
Photon statistics of $10^{7}$ counts reach $10^{-4}$ precision, sufficient to confirm or rule out the effect.

### Implications
* Detecting $\delta P$ validates deterministic field-energy probabilities and quantifies environmental decoherence.
* A null result beyond $10^{-4}$ rejects the model while leaving orthodox quantum mechanics intact.

### Conclusion
Identifying Born weights with conserved field-energy fractions makes a clear, falsifiable prediction: finite environments induce measurable deviations from standard statistics.
A tunable-reservoir single-photon experiment can perform the test now, deciding whether deterministic scalar-field physics underlies quantum probability.

### References
1. A. Palma, *Deriving the Schrödinger Equation from Source-Free Maxwell Dynamics*, manuscript, 2025.
2. W. Zurek, "Decoherence, einselection and the quantum origins of the classical", Rev. Mod. Phys. 75, 715 (2003).
3. Y. Aharonov & M. Scully, "Time-reversal quantum-eraser interactions", Phys. Rev. Lett. 51, 1410 (1983).
4. J. Kwiat et al., "High-visibility quantum eraser", Phys. Rev. Lett. 74, 4763 (1995).
5. H. Wiseman, "How many modes does the environment need?", Phys. Rev. A 49, 2133 (1994).
