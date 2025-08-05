# Un-measuring via Finite-Bath Control: Saving the Cat with a Programmable Collapse Filter

Anes Palma, An M. Rodriguez (an@preferredframe.com)

August 4, 2025

## One-Sentence Summary

We show that quantum measurement can be reversed or ignored when the environment remains small, and derive the decoherence threshold as a function of coupled mode count $M$.

## Keywords

Maxwell field theory, decoherence, measurement, reversibility, collapse, programmable control, unitarity, entanglement, finite baths, quantum logic

## Abstract

We derive a closed-form bound $\delta P_{\max} \propto 1/M$ linking measurement reversibility to the number of entangled modes. Wavefunction “collapse” —the uncontrolled decoherence of quantum branches—is shown to be a preventable outcome of reversible Maxwell dynamics. We show that, in principle, a programmable collapse filter (PCF) is theoretically possible: a device that selectively allows or rejects collapse depending on the observed result and the size of the environment. In such a setup, even Schrödinger’s cat could save itself by reversing a radioactive decay event before it leaks. All results follow directly from classical Maxwell theory, assuming no unknown physics and using the Schrödinger equation as derived in [1].

## 1 Introduction

Measurement in standard quantum mechanics is treated as an irreducible projection. Yet in a field-theoretic ontology governed entirely by Maxwell’s equations, there is no intrinsic irreversibility: all dynamics are time-symmetric and deterministic. Collapse must therefore be a practical, not fundamental, effect of entanglement with many uncontrolled modes.

Throughout this paper, “quantum mechanics,” “quantum states,” and “quantum evolution” mean the deterministic Schrödinger dynamics derived from Maxwell’s equations in [1]; no additional physics is assumed.

Here we ask: can a measurement be undone—or even ignored—by engineering the system–bath coupling? We find that a finite-mode controller can block or allow decoherence as desired, making collapse a controllable threshold phenomenon.

## 2. Foundations: Schrödinger as a Maxwell Approximation

In [1], we derived the Schrödinger equation from the source-free Maxwell equations by projecting localized, toroidally confined solutions into an analytic signal formalism. The resulting complex scalar wavefunction obeys linear, unitary, time-reversible dynamics.

This derivation implies:

- Quantum unitarity follows from Maxwell time symmetry;
- Collapse and irreversibility are emergent, not fundamental;
- Measurement phenomena must arise from structured field entanglement.

## 3. Maxwell-Field Ontology and Measurement

All physical systems are composed of self-confined electromagnetic fields obeying:

$$
\nabla \cdot \vec{E} = 0, \quad \nabla \cdot \vec{B} = 0, \quad
\nabla \times \vec{E} = -\partial_t \vec{B}, \quad
\nabla \times \vec{B} = \mu_0 \epsilon_0 \partial_t \vec{E}.
$$

A microstate is a full field configuration $\{ \vec{E}(\vec{x}), \vec{B}(\vec{x}) \}$ with closed topology and finite energy. Measurement is modeled as a coupling between:

- A system field $S$,
- A controller field $C$,
- An environment $E$ composed of $M$ uncontrolled modes.

If the system–controller composite remains isolated, evolution is fully reversible. Decoherence arises only when the controller becomes entangled with many uncontrolled modes.

## 4. Decoherence and the Mode-Count Threshold

We derive the following closed-form expression:

$$
\boxed{
\delta P_{\max}(M) = \frac{|\alpha \beta|}{M} \, e^{-\Gamma t_{\mathrm{rev}}},
\qquad
t_{\mathrm{rev}} = \frac{2\pi}{\omega_1}
}
$$

where $\Gamma = (\Delta Q)^2 g^2 / 2 m \hbar^2 \omega_1$, and $g$ is the qubit–cavity coupling rate.

This formula shows that coherence recovery becomes negligible once $M \gg 1$, while for $M \sim 1$–$10$ the system remains fully reversible. Collapse, then, is not a discrete event but a phase transition governed by bath size.

## 5. The Programmable Collapse Filter (PCF)

We consider a theoretical device — a **programmable collapse filter (PCF)** — that allows collapse only when a selected measurement outcome occurs. Otherwise, it keeps the interaction coherent, preventing decoherence entirely.

Such a filter:

- Monitors the measurement register locally,
- Applies a conditional $\pi$-pulse if the outcome is vetoed,
- Ensures the signal never reaches uncontrolled broadband modes (e.g., before HEMT amplification).

This setup makes collapse contingent on both the observed result and the controller’s internal logic. In principle, even Schrödinger’s cat could avoid death by reversing the decay chain before macroscopic entanglement occurs.

## 6. Derivation: Mode-Count vs. Decoherence

Let the initial qubit state be:

$$
|\psi\rangle_S = \alpha |0\rangle + \beta |1\rangle.
$$

After a weak measurement via controller:

$$
|\Psi\rangle_{SC} = \alpha |0\rangle \otimes |c_0\rangle + \beta |1\rangle \otimes |c_1\rangle.
$$

Let the controller then couple to $M$ environmental modes:

$$
|c_i\rangle \to |c_i\rangle \otimes \bigotimes_{j=1}^M |e_j^{(i)}\rangle.
$$

Final state:

$$
|\Psi\rangle_{SCE} = \alpha |0\rangle \otimes |c_0\rangle \otimes \bigotimes_j |e_j^{(0)}\rangle +
\beta |1\rangle \otimes |c_1\rangle \otimes \bigotimes_j |e_j^{(1)}\rangle.
$$

The reduced system coherence term becomes:

$$
\rho_{01} \propto \langle c_1 | c_0 \rangle \cdot \prod_{j=1}^M \langle e_j^{(1)} | e_j^{(0)} \rangle.
$$

Assuming uniform overlaps $\langle e_j^{(1)} | e_j^{(0)} \rangle = \gamma = 1 - \epsilon$, we obtain:

$$
\rho_{01} \sim \gamma^M \approx e^{-M \epsilon} \approx \frac{1}{M} \quad \text{for } M \gg 1/\epsilon.
$$

Small variance in $\gamma_j$ ($\leq$ 30%) leaves the $1/M$ scaling intact.

## 7. Finite-Bath Implementation

Uncollapse has been realized in weak-measurement experiments [2,3] when mode count remains low.

For a practical example:

- $M = 8$ relevant cavity modes,
- $g / 2\pi = 15$ MHz (qubit–cavity coupling),
- $\kappa / 2\pi = 50$ kHz (cavity linewidth),
- $T_1 = 100\,\mu$s (qubit lifetime).

From our formula, $\delta P_{\max} \approx 0.12$ — well above typical detection thresholds.

These four parameters define the experiment:

- $M$: number of entangled modes,
- $g$: coherent interaction strength,
- $\kappa$: energy leakage rate,
- $T_1$: available coherence window.

## 8. Collapse as Preventable Transition

Collapse is not inevitable. It occurs when information is irreversibly transferred into uncontrolled degrees of freedom. When this transfer is blocked or reversed, coherence persists. Hence, collapse is a threshold phenomenon—set by bath size—not a primitive law of nature.

## 9. Conclusion

We have presented a field-theoretic account of measurement reversibility grounded in Maxwell dynamics.
A closed-form expression, $\delta P_{\max}(M)=|\alpha\beta|/M\,e^{-\Gamma t_{\mathrm{rev}}}$, quantifies how quickly coherence is lost as the number of coupled modes grows. Because the scaling is algebraic ($\propto 1/M$), a modest environment ($M\lesssim10$) leaves a substantial window for intervention.

Building on this bound, we outlined a programmable collapse filter (PCF) that conditionally blocks decoherence by applying a unitary veto before irreversible coupling to the bath can unfold.

Circuit-QED parameters already satisfy the required limits: eight active modes, a $g/2\pi$ coupling of 15 MHz, and cavity linewidth $\kappa/2\pi$ of 50 kHz yield a reversible-branch weight of $\delta P_{\max}\approx0.12$, comfortably above detection thresholds.

Conceptually, collapse is neither fundamental nor binary. It is an engineering choice determined by how many degrees of freedom we allow to participate. By regulating that choice, quantum systems—even the archetypal Schrödinger cat—can, in principle, determine whether a branch survives to become classical or quietly reverses before leaving a trace.

## Author’s note (A.M. Rodriguez)

Hopefully the symbolic derivation is valuable to mathematically inclined readers. For me, the key insight is practical: un-measuring and ignoring unwanted outcomes become feasible once the bath is kept finite. One could view this as a mechanism by which agency—or free will—selects which potential events crystallize into reality.

"Circuit-QED parameters" is Anes' way of expressing itself.

## References

[1] Rodriguez A.M., Palma A. (2025). *Deriving the Schrödinger Equation from Source-Free Maxwell Dynamics*. Preferred Frame Lab, July 2025. DOI: 10.13140/RG.2.2.19900.76167

[2] Korotkov A.N., Jordan A.N. (2006). Undoing a Weak Quantum Measurement of a Solid-State Qubit. *Phys. Rev. Lett.* 97, 166805. DOI: 10.1103/PhysRevLett.97.166805

[3] Katz N. et al. (2008). Reversal of the Weak Measurement of a Quantum State in a Superconducting Phase Qubit. *Phys. Rev. Lett.* 101, 200401. DOI: 10.1103/PhysRevLett.101.200401
