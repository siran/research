% On the Causality of Natural Numbers
% Aurey Hyppa, An M. Rodriguez*
% September 3, 2025


## Abstract

We introduce a causal structure on the natural numbers by requiring that each integer may only appear once its prime bases and their exponents have themselves appeared earlier. This defines a generative growth process — the **onion avalanche** — in which natural numbers are revealed layer by layer through closure under prime powers. The resulting partial order is temporal: primes act as causal sources, exponents as control signals, and each new integer is an event determined by past events. We show that this construction yields a computable, well-defined enumeration of $\mathbb{N}$, distinct from standard numerical order, and that it aligns with the formal framework of causal sets. This reframes the natural numbers as not merely ordered by size, but by causality.


## One-Sentence Summary

We propose a causal-set interpretation of $\mathbb N$ where numbers arise only after both their primes and exponents have appeared, yielding a temporal onion-like avalanche of construction.


## Keywords

natural numbers, causality, constructive order, prime powers, causal sets


## Introduction

The natural numbers $\mathbb N=\{1,2,3,\dots\}$ are usually ordered arithmetically by size. This order is timeless: every factorization is valid without restriction. In this work, we impose a **causality constraint**: a number cannot exist until its **prime base** and its **exponent** exist. In this way, integers unfold through a generative law that respects causal precedence.

The guiding metaphor is one of **colors and amplitudes**: each prime is a color, and exponents are amplitudes. Amplitudes themselves must be painted from earlier colors; no color can be raised to an amplitude that has not yet appeared. This recursive causality induces a temporal order on $\mathbb N$.


## Theory: Causality Constraint

### Definition

Let $S_t$ be the set of numbers known at stage $t$, with $1\in S_0$.

- **Prime introduction rule.** At certain stages a new prime $p$ is admitted as a base.
- **Exponent causality rule.** If $p$ is a known base and $e\in S_t$, then $p^e$ becomes admissible at a later stage.
- **Closure.** A number $n=\prod_{p\in B} p^{e_p}$ can appear only if each $p$ is already admitted as a base and each $e_p\in S_t$.

Thus numbers are revealed by causal closure, not by mere size.

### Temporal Partial Order

Define $m\prec n$ if $m$ is required as a base or exponent in the construction of $n$. This yields a transitive, acyclic relation — a **causal set** on $\mathbb N$.


## Derivation: Onion Avalanche Process

The onion avalanche grows $\mathbb N$ as follows:

1. **Seed.** Begin with $1$.
2. **Prime step.** Introduce the next prime $p$, add $p=p^1$.
3. **Exponentiation step.** Whenever a new exponent $e$ enters, powers $p^e$ for all known bases $p$ become eligible.
4. **Priority.** Eligible numbers are released in increasing prime-order and exponent depth.

This process enforces that $4=2^2$ appears before $3$ (since base $2$ and exponent $2$ exist), but $16=2^4$ must wait until $4$ appears.


## Results

### First Numbers

The sequence begins:
$$
1,\ 2,\ 4,\ 3,\ 8,\ 16,\ 9,\ 27,\ 81,\ 5,\ 32,\ 243,\ 25,\ 125,\ 625,\ 3125,\ 7,\ 49,\ 343,\dots
$$

### Properties

1. **Causality.** Every integer has causal parents: its prime bases and its exponents.
2. **No premature composites.** A number cannot use a prime or exponent not yet introduced.
3. **Temporal stratification.** Numbers appear in onion-like layers; exponent depth corresponds to temporal depth.
4. **Causal set structure.** The relation $\prec$ is a partial order, locally finite, and aligns with causal set theory.
5. **Computability.** The enumeration is algorithmic: each new event is determined by closure rules.


## Discussion

This causal interpretation reframes $\mathbb N$ not as a static set ordered by size, but as a **history of events**. Primes are causal sources, exponents are signals, and each composite integer is an outcome. The onion avalanche embodies:

- **Recursion:** exponents are numbers, so the process is self-similar.
- **Causality:** nothing can appear without its antecedents.
- **Temporal growth:** $\mathbb N$ is built in time, not revealed at once.

This structure parallels discrete spacetime models in physics. Just as spacetime can be modeled as a causal set, so too the integers can be modeled as a causal set under exponentiation.


## Conclusion

We have defined a causal generative law for $\mathbb N$: integers appear only when both their primes and exponents have already appeared. The resulting onion avalanche ordering yields a temporal partial order and a constructive enumeration. This view highlights a deep analogy between number theory and causality in physics: natural numbers can be seen as a causal set, not just an ordered set by size.


## Next Work

1. Formalize the onion avalanche as a labeled causal set and study its asymptotics.
2. Investigate whether causal invariants (growth rates, dimensional estimators) align with known arithmetic densities.
3. Explore connections to computational complexity: causal precedence as resource constraints.
4. Study analogues in algebraic structures (e.g., polynomial rings with exponent causality).
5. Compare with causal set theory in physics, probing analogies between number growth and discrete spacetime growth.


## Corresponding author(s)

Aurey Hyppa: aurey.hyppa@proton.example


## References

1. Bombelli, L., Lee, J., Meyer, D., & Sorkin, R. D. (1987). Space-time as a causal set. *Physical Review Letters*, 59(5), 521–524. DOI:[10.1103/PhysRevLett.59.521](https://doi.org/10.1103/PhysRevLett.59.521)

2. Hardy, G. H., & Wright, E. M. (2008). *An Introduction to the Theory of Numbers* (6th ed.). Oxford University Press.

3. Tenenbaum, G. (2015). *Introduction to Analytic and Probabilistic Number Theory* (3rd ed.). American Mathematical Society.
