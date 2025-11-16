% Dimension and Space as Emergent Properties of Distance in a Cause-Effect Model
of the Emergence of Time
% Anonymous, An M. Rodriguez
% November 16, 2025


## One-Sentence Summary

Dimension and space emerge from causal distances inside a single stable Node,
via approximate metric embeddings.


## Abstract

We extend a previously introduced framework where time and distance arise from
internal causal relations within a stable Node. Time follows from a partial
ordering of subnode interactions, while distance is the minimal causal-chain
length between subnodes. Here we show that dimension and space similarly emerge
when these causal distances embed into manifold-like structures. We formalize
effective dimensionality through approximate metric embeddings. This clarifies
how conventional spatial dimensions may arise from deeper relational dynamics.


## Keywords

emergent spacetime, causal sets, relational physics, dimension, embeddings,
metric structure


## Introduction

Standard physics treats a $D$-dimensional spacetime as pre-existing structure.
Discrete or relational programs instead propose spacetime as emergent,
constructed from deeper causal or combinatorial elements @bombelli @dowker
@surya @t_konopka.

In @NodePaper, a single stable Node $N$ was introduced, containing subnodes
interacting by internal causal links. A partial order $\succ$ encodes causality:

$$ n_i \succ n_j $$

interpreted as "subnode $n_i$ can trigger a change in $n_j$".
Time emerges from this partial order.
Distance emerges as the minimal length of causal chains between subnodes.

Here we formalize how dimension can also emerge from this structure. When causal distances admit approximate embeddings into $\mathbb{R}^D$ with low distortion, the system exhibits effective dimensionality. This aligns with ideas of manifold-like limits in discrete spacetime models.


## Recap of the Node Framework

### Structure of the Node

- Stable Node: a single entity $N$ with fixed total property (e.g., energy).
- Subnodes: a set $\{n_i\}_{i \in I}$ of internal components.
- Causality: a partial order $\succ$ where $n_i \succ n_j$ means causal
  influence.


### Distance from Minimal Chains

For subnodes $n_i, n_j$, a causal chain of length $k$ is:

$$
n_i \succ n_{a_1} \succ \dots \succ n_{a_{k-1}} \succ n_j
$$

Distance $d(n_i,n_j)$ is the minimal $k$ for which such a chain exists.
If none exists, the distance may be infinite or undefined.


### Time as Partial Order

The relation $n_i \prec n_j$ expresses temporal precedence.
Recurrent cycles allow local "clock" definitions: the count of causal steps
gives a measure of duration. Details appear in @NodePaper.


## Formalizing Emergent Dimension

### Metric-Like Properties

The distance function $d$ behaves like a graph distance.
It may not be symmetric, but when finite it provides a metric-like structure.

**Proposition (Pseudo-Metric)**
If the causal relation is acyclic and well-defined, $d$ induces a pseudo-metric
on pairs with finite causal connection.


### Approximate Embeddings and Effective Dimension

At large scales, if causal distances embed faithfully into $\mathbb{R}^D$, the perceived geometry is $D$-dimensional.

**Definition (Effective Dimensionality)**
Let $\mathbf{N}$ be the set of subnodes with distance $d$.
A finite subset $S \subset \mathbf{N}$ embeds in $\mathbb{R}^D$ with fidelity $\epsilon \ge 0$ if there exists:

$$
\Phi : S \to \mathbb{R}^D
$$

such that for all $n_{i_p}, n_{i_q} \in S$:

$$
\bigl|\|\Phi(n_{i_p}) - \Phi(n_{i_q})\| - d(n_{i_p}, n_{i_q})\bigr| \le \epsilon
$$

If arbitrarily large subsets embed with arbitrarily small $\epsilon$, the system
is effectively $D$-dimensional.


### Connections to Manifold-Like Behavior

Discrete causal structures often approximate manifolds at large scales.
Our definition captures this without assuming smoothness.
If embeddings exist with small distortion for $D=3$ or $4$, the system is
effectively 3D or 4D.


## Implications and Discussion

### Space vs Distance

Space is not fundamental. We instead have:

- Distance: minimal causal-chain length.
- Embedding: a representation of distances in $\mathbb{R}^D$.

Space appears when dense regions of the causal graph admit low-distortion
embeddings.


### Origin of Dimensionality

Quantum-gravity scenarios often show scale-dependent dimension @carlip.
In the Node framework:

- Dimension may vary with scale.
- Small-scale behavior may be fractal-like.
- Large-scale behavior may approximate an integer dimension.

Dimension is emergent rather than assumed.


### Beyond Geometry: Matter and Fields

Additional physical properties (mass, charge, fields) might also emerge if
incorporated into the causal structure.
Future work may define embeddings preserving additional attributes, leading to
emergent gauge fields or matter excitations.


## Conclusions

Dimension arises rather than being postulated.
Effective dimensionality follows from approximate embeddings of causal distances into $\mathbb{R}^D$.
Thus time, distance, space, and dimension emerge from deeper causal relations
within a stable Node.

Observers impose geometry because large causal regions admit faithful metric
embeddings.


## About Author(s)

* Anonymous
* An M. Rodriguez, anmichel.rodriguez@gmail.com


## References

Anonymous, An M. Rodriguez. *A Cause-Effect Model for Emergent Time and
Distance*. ResearchGate. DOI: https://doi.org/10.13140/RG.2.2.35753.30569

Bombelli, L., Lee, J., Meyer, D., Sorkin, R. *Space-Time as a Causal Set.* Phys.
Rev. Lett. 59, 521 (1987).

Dowker, F. *Causal Sets and the Deep Structure of Spacetime.* In *100 Years of
Relativity* (2005).

Surya, S. *The Causal Set Approach to Quantum Gravity.* Living Reviews in
Relativity 22, 5 (2019).

Konopka, T., Markopoulou, F., Smolin, L. *Quantum Graphity.*
arXiv:hep-th/0611197 (2006).

Carlip, S. *Dimensional Reduction in Quantum Gravity.* Int. J. Mod. Phys. D 23,
1430023 (2014).
