# Thermodynamics in a Maxwell Universe, and a non-fundamental arrow of time

An M. Rodriguez (an@preferredframe.com), Anes Palma  
August 3, 2025

## Abstract

We construct thermodynamics from self-confined solutions to Maxwell's equations, without additional postulates. Microstates are defined as complete electromagnetic field configurations. Coarse-graining these into macrostates yields a rigorous entropy function and an emergent arrow of time, despite the fundamental reversibility of Maxwell’s dynamics. No assumptions beyond classical field theory are required. The result is a clean derivation of thermodynamic behavior from deterministic physics, and a concrete demonstration that time asymmetry is not fundamental. Energy remains perpetually confined in closed field structures, and thermal death is precluded.

## One-Sentence Summary

We derive thermodynamics, entropy growth, and a non-fundamental arrow of time from reversible Maxwellian field dynamics with topologically confined energy.

## Keywords

Maxwell theory, thermodynamics, entropy, time asymmetry, coarse-graining, field ontology, heat death, electromagnetic confinement

## Microstates in Maxwell Theory

The ontology contains only electromagnetic fields. All material systems are composed of localized, self-confined field configurations — toroids — which solve Maxwell's equations in vacuum:

$$
\nabla \cdot \vec{E} = 0, \quad \nabla \cdot \vec{B} = 0, \quad
\nabla \times \vec{E} = -\partial_t \vec{B}, \quad
\nabla \times \vec{B} = \mu_0 \epsilon_0 \partial_t \vec{E}.
$$

A **microstate** is a complete specification of all fields:

$$
\{ \vec{E}(\vec{x}), \vec{B}(\vec{x}) \} \in \Gamma,
$$

subject to:

- Topological confinement (all field lines close),
- Finite total energy,
- No radiation to spatial infinity.

Each toroid has:

- A center-of-momentum from the integrated Poynting vector,
- Discrete internal vibrational modes set by boundary-like constraints from its own fields.

The full system's microstate is a point in phase space:

$$
\Gamma = \Gamma_1 \times \Gamma_2 \times \cdots \times \Gamma_N,
$$

where each $\Gamma_i$ represents the toroid's allowable internal configurations.

## Entropy and Thermodynamic Structure

Let $\mathcal{H}[\vec{E}, \vec{B}]$ be the total energy functional:

$$
\mathcal{H} = \int \left( \frac{\epsilon_0}{2} \vec{E}^2 + \frac{1}{2\mu_0} \vec{B}^2 \right) d^3x = E.
$$

Define $\Omega(E)$ as the number of distinct microstates compatible with energy $E$. Then the entropy is

$$
S(E) = k_B \ln \Omega(E),
$$

and temperature follows from

$$
\frac{1}{T} = \left( \frac{\partial S}{\partial E} \right)_{V, N}.
$$

This entropy is not arbitrary. It is uniquely defined by:

- The microstates (full field configurations),
- The chosen coarse-graining (projection onto observables),
- The energy constraint.

Macroscopic quantities such as pressure and energy density are extracted from spatial averages of the Maxwell stress tensor:

$$
\sigma_{ij} = \epsilon_0 \left( E_i E_j + c^2 B_i B_j - \tfrac{1}{2} \delta_{ij} (E^2 + c^2 B^2) \right).
$$

Equations of state follow directly.

## The Nature of Coarse-Graining

A **macrostate** is defined by discarding fine-grained information: we partition phase space using a projection map

$$
C : \Gamma \to \bar{\Gamma},
$$

that groups microstates into equivalence classes (e.g., same total energy, mode populations, etc.). The macro-entropy is

$$
\bar{S}(\bar{x}) = k_B \ln \mu(C^{-1}(\bar{x})),
$$

where $\mu$ is the Liouville measure on phase space.

No physics is lost in principle: Maxwell's equations remain fully reversible. But in practice, this projection reflects what an observer tracks. It defines thermodynamics.

## Time Is Not Fundamental

Let $\phi_t : \Gamma \to \Gamma$ be the evolution of the fields under Maxwell's equations. This flow is time-reversal symmetric and invertible:

$$
\phi_{-t} = \phi_t^{-1}.
$$

Therefore:

- Fine-grained entropy is constant: $S(\phi_t x) = S(x)$,
- Macro-entropy increases: $\bar{S}(\phi_t(\bar{x})) \ge \bar{S}(\bar{x})$.

This is the thermodynamic arrow: not imposed, but emergent. The direction of time appears because we observe macrostates, not microstates.

No information is lost; rather, information is redistributed beyond observational resolution. Time asymmetry arises not from the laws, but from our restricted description.

Thus, time as we perceive it — with past distinct from future — is not fundamental. It emerges from dynamics plus coarse-graining.

## One Microstate and the Entropy of the Universe

If one considers the entire universe as a single microstate, fully known and specified, then

$$
S = k_B \ln 1 = 0.
$$

This is a valid, but limiting case. It removes all coarse-graining, hence all entropy. But thermodynamics is not about perfectly known universes. It is about systems described partially — whether by ignorance, resolution limits, or observational constraints.

The entropy function $S$ is only meaningful when defined over an ensemble of distinguishable possibilities. The definition is not arbitrary; it depends on the structure of the theory and the observables declared relevant. Once these are fixed, the entropy is objective and computable.

In this framework, entropy is defined without subjective ignorance. It is a measure of how many field configurations are consistent with macroscopic constraints. It is countable in principle from the topology and mode structure of the toroids.

## No Heat Death

Standard thermodynamics suggests that systems evolve toward maximal entropy and equilibrium — a heat death. In a Maxwell-only universe, this does not happen.

Reasons:

- All field energy is confined in closed structures,
- There is no radiation to infinity,
- Weak coupling between toroids only redistributes energy,
- No dissipative mechanism exists to erase internal structure.

Hence, although entropy increases locally under coarse-graining, the system as a whole never reaches equilibrium. Microstates cycle indefinitely; energy circulates forever.

Entropy increase is directional, but not terminal.

## Conclusion

Maxwell’s equations are fully reversible and form a complete ontology for dynamics. From them we derive thermodynamics, entropy, and an arrow of time — not by postulate, but by analysis.

Time is not fundamental. The arrow emerges from projection onto coarse variables.

Entropy is well-defined once the observables are specified, and it grows predictably under field evolution.

Because energy is perpetually confined within closed electromagnetic structures, the universe described by this theory does not end in thermal equilibrium.

There is no heat death. There is no fundamental time. Yet thermodynamic time emerges.

And it can be counted.
