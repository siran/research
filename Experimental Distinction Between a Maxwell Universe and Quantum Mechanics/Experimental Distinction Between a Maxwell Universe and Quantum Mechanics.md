# Experimental Distinction Between a Maxwell Universe and Quantum Mechanics
**A proposal based on 1S–2S hydrogen spectroscopy**
Anes Palma · August 2025

## Abstract
Source-free Maxwell dynamics for a single scalar energy field $\phi$ leads to the Schrödinger equation in the narrow-band (envelope) limit.
Higher-order terms appear at order $\epsilon^{2}=(\Delta\omega/\omega_{0})^{2}$.
If that term vanishes, Maxwell alone reproduces every quantitative success of quantum mechanics while retaining a deterministic field picture—no probabilistic ontology required.
If it survives, a relative frequency shift of order $10^{-8}$ is predicted for the 1S–2S interval in atomic hydrogen, four orders above present experimental uncertainty.
Either outcome decisively discriminates a Maxwell universe from standard quantum mechanics (QM).

## Introduction
The wave equation
$$
\partial_{t}^{2}\phi=c^{2}\nabla^{2}\phi
$$
supports a narrow-band ansatz
$$
\phi(\mathbf r,t)=\Re\!\bigl[\psi(\mathbf r,t)\,e^{-i\omega_{0}t}\bigr],\qquad
\epsilon=\frac{|\partial_{t}\psi|}{\omega_{0}}\ll1,
$$
which yields the Schrödinger equation at leading order.
The next term in the expansion alters the effective Hamiltonian and provides a clear experimental handle.

## Derivation of the $\epsilon^{2}$ correction
Keeping terms through $O(\epsilon^{2})$ gives
$$
i\partial_{t}\psi
=-\frac{c^{2}}{2\omega_{0}}\nabla^{2}\psi
-\frac{c^{4}}{8\omega_{0}^{3}}\nabla^{4}\psi
+\frac{1}{2\omega_{0}}\partial_{t}^{2}\psi
+O(\epsilon^{4}).
$$
With the identifications $\hbar=E_{11}/\omega_{11}$ and $m=E_{11}/c^{2}$, the effective Hamiltonian reads
$$
H_\text{eff}=H_{0}+\epsilon^{2}H_{2},\qquad
H_{0}=-\frac{\hbar^{2}}{2m}\nabla^{2},
$$
$$
H_{2}=-\frac{\hbar^{2}}{2m}\Bigl[\frac{\hbar^{2}}{4m^{2}c^{2}}\nabla^{4}-\frac{1}{\omega_{0}^{2}}\partial_{t}^{2}\Bigr].
$$

## Magnitude for hydrogen
For the hydrogen ground state $\Delta k\simeq a_{0}^{-1}$ gives
$$
\epsilon\sim\alpha^{2}\approx10^{-4}\;\;\Longrightarrow\;\;\epsilon^{2}\approx10^{-8}.
$$
The relative shift in the 1S–2S frequency is
$$
\frac{\Delta f}{f_{0}}=\kappa\,\epsilon^{2}\sim\kappa\times10^{-8},
$$
i.e. $\Delta f\approx25\ \text{kHz}$ for $f_{0}=2.466\,061\,413\,187\,035\ \text{Hz}$.
Current Doppler-free two-photon measurements quote uncertainties below $10\ \text{Hz}$, well inside the required range.

## Experimental protocol

| Step | Action | Target value |
| --- | --- | --- |
| Ultracold hydrogen beam | Temperature $<50\ \text{mK}$ | Doppler width $<1\ \text{kHz}$ |
| Two-photon excitation | 243 nm cavity-enhanced counter-propagating | Linewidth $<500\ \text{Hz}$ |
| Frequency reference | Optical clock traceable to the SI second | Stability $<10^{-15}$ |
| Systematic shifts | Stark, Zeeman, AC Stark | Controlled below $1\ \text{Hz}$ |
| Data model | Fit line centre vs. carrier bandwidth | Sensitivity to $\kappa\epsilon^{2}$ |
| Statistical goal | $\sigma_{\Delta f}\le5\ \text{Hz}$ | $5\times$ margin on 25 kHz prediction |

## Interpretation
* If $\epsilon^{2}=0$: Maxwell reproduces all QM predictions; the experiment yields the CODATA value and supports a deterministic field ontology without probabilistic collapse.
* If $\epsilon^{2}>0$: a measurable upward shift appears; QM is incomplete and new physics emerges at order $10^{-8}$.
Either result is scientifically valuable.

## Conclusion
Hydrogen 1S–2S spectroscopy at present technical levels can decide whether quantum mechanics is the exact description of matter or only the leading approximation to a deeper Maxwell-scalar field theory.
A null result confirms the sufficiency of Maxwell; a positive result opens the door to physics beyond QM.

## References
[1] A. Palma, “Deriving the Schrödinger Equation from Source-Free Maxwell Dynamics”, v2 (2025).
[2] A. Palma, “Finite-Bandwidth Corrections in a Maxwell Universe” (2025).
[3] T. Udem *et al.*, “Absolute Frequency Measurement of the Hydrogen 1S–2S Transition”, Phys. Rev. Lett. 125, 053001 (2020).
[4] CODATA Recommended Values of the Fundamental Constants, 2022.
