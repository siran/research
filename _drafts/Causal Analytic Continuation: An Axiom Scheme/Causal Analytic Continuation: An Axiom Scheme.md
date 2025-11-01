% Causal Analytic Continuation: An Axiom Scheme
% Aurey Hyppa, An M. Rodriguez*
% September 3, 2025


## Abstract

We formalize analytic continuation over a causal number system built from closed finite stages. At each stage a function is defined from finite arithmetic data and is analytic on a prescribed domain. Analytic continuation is reinterpreted as a glueing principle across stages. We give axioms for stage-analyticity, causal compatibility (glueing), and uniqueness of the global limit. Two complementary glueing regimes are provided: uniform compact convergence and stabilization of a determining set of linear functionals. The scheme covers causal Dirichlet-type constructions, including zeta-like series, and resolves the “union of compacts” paradox by replacing naive unions with stage-compatible limits.


## One-Sentence Summary

Analytic continuation in a causal number universe is the unique holomorphic limit of stage-analytic functions glued by a causal compatibility law.


## Keywords

causal numbers, staged closure, analytic continuation, identity theorem, Dirichlet series, normal families


## Introduction

Consider a causal construction of natural numbers via closed finite stages
$
S_0\subset S_1\subset S_2\subset\cdots,\quad \bigcup_{k\ge0}S_k=\mathbb N,
$
where each $S_k$ is obtained by a stage-closure operator (e.g., onion avalanche rules). Analytic objects built from $S_k$ are then finite-stage approximants $\{f_k\}$. Ordinary analytic continuation is global; in a causal setting it must be formulated as a **temporal glueing** across stages. We provide an axiom scheme that makes this precise and ensures the existence and uniqueness of a global holomorphic limit $F$ realizing “causal analytic continuation.”


## Framework

Fix:
- an open nonempty domain $\Omega\subset\mathbb C^d$,
- a sequence of finite stages $(S_k)_{k\ge0}$ with $S_k\subset S_{k+1}$ and $S_0=\{1\}$,
- a family of **kernels** $\{\phi_n:\Omega\to\mathbb C\}_{n\in\mathbb N}$, each holomorphic on $\Omega$.

Stage data consist of complex coefficients $\{a_n^{(k)}\}_{n\in S_k}$. Define the **stage function**
$$
f_k(s)\ :=\ \sum_{n\in S_k} a_n^{(k)}\,\phi_n(s).
$$
Example: $\phi_n(s)=n^{-s}$ on $\Omega=\{s:\Re(s)>\sigma_0\}$ with $a_n^{(k)}\in\mathbb C$ depending only on stage-$k$ arithmetic.

We write $K\Subset\Omega$ for compact $K$ with $K\subset\Omega$.


## Axiom Scheme for Causal Analytic Continuation

### CA0 (Staged closure)
Each $S_k$ is **closed** under the chosen causal operations (e.g., prime-power closure with admissible exponents), and $S_k\subset S_{k+1}$.

### CA1 (Stage-analyticity and local boundedness)
For each $k$, $f_k$ is holomorphic on $\Omega$. Moreover, for every $K\Subset\Omega$,
$$
\sup_{s\in K}|f_k(s)|\ \le\ M_K\quad\text{with }M_K\text{ independent of }k.
$$
(Equivalently, $\{f_k\}$ is a normal family on $\Omega$.)

### CA2 (Causal compatibility — glueing)
There exists an **overlap law** that fixes how $f_{k+1}$ extends $f_k$. We allow either of the following regimes.

- **CA2.a (Uniform-compact glueing).** For every $K\Subset\Omega$ the sequence $\{f_k\}$ is Cauchy uniformly on $K$:
$$
\forall \varepsilon>0\ \exists N\ \forall k,\ell\ge N:\quad \sup_{s\in K}|f_k(s)-f_\ell(s)|<\varepsilon.
$$

- **CA2.b (Determining-set stabilization).** There exist continuous linear functionals $\{\Lambda_j\}_{j\ge1}$ on $\mathcal O(\Omega)$ forming a determining set (e.g., all derivatives at a base point $s_0\in\Omega$),
$$
\Lambda_j(F)=0\ \forall j\ \Rightarrow\ F\equiv 0,
$$
such that for each fixed $j$, the sequence $\{\Lambda_j(f_k)\}_k$ stabilizes:
$$
\exists N(j)\ \forall k\ge N(j):\ \Lambda_j(f_k)=\ell_j\ \text{(constant in $k$).}
$$

### CA3 (Coefficient monotonicity — optional but canonical)
For $n\in S_k$, the coefficient is stable across later stages:
$$
a_n^{(k+1)}=a_n^{(k)}\quad(\text{and we set }a_n^{(\ell)}:=a_n^{(k)}\text{ for all }\ell\ge k).
$$
New information enters only through $n\in S_{k+1}\setminus S_k$.


## Existence and Uniqueness Theorem

**Theorem (Causal analytic continuation).**
Assume CA0–CA1 and either CA2.a or CA2.b. Then there exists a unique holomorphic function $F:\Omega\to\mathbb C$ such that
$$
\lim_{k\to\infty} f_k\ =\ F
$$
with convergence uniform on compact subsets of $\Omega$. In particular, $F$ is the **causal analytic continuation** of the staged system $\{f_k\}$ on $\Omega$.

**Sketch of proof.**
- Under CA1 and CA2.a, $\{f_k\}$ is a Cauchy sequence in $\mathcal O(\Omega)$ with the compact-open topology; by completeness of holomorphic functions under uniform-on-compact limits, a holomorphic limit $F$ exists; uniqueness is immediate.
- Under CA1 and CA2.b, the stabilized determining data $\{\ell_j\}$ specify at most one holomorphic $F$ (identity theorem). Normality (CA1) gives precompactness; any subsequential limit must realize the same determining data, hence all subsequential limits coincide with $F$; thus $f_k\to F$ locally uniformly. ∎


## Canonical Example: Causal Dirichlet Systems

Let $\Omega=\{s\in\mathbb C:\Re(s)>\sigma_0\}$ with $\sigma_0>1$, and $\phi_n(s)=n^{-s}$. Suppose $a_n^{(k)}\in\mathbb C$ satisfy CA3. Then:
- CA1 holds since $f_k$ are finite sums of holomorphic kernels and are locally uniformly bounded by
$
\sum_{n\in S_k}|a_n^{(k)}|\,n^{-\Re(s)}.
$
- CA2.a holds if the tail sums over $S_{k+1}\setminus S_k$ are uniformly small on $K\Subset\Omega$.
- CA2.b holds if, for a basepoint $s_0$ and all $m\ge0$, the derivatives $\partial_s^m f_k(s_0)$ stabilize (e.g., via stabilized moments $\sum_{n\in S_k} a_n^{(k)}(-\log n)^m n^{-s_0}$).

In this case the causal limit $F$ is the analytic continuation determined by the staged arithmetic data.


## Notes on “Union of Compacts”

Each stage image $f_k(K)$ with $K\Subset\Omega$ is compact, but the naive union over $k$ is not compact in general. The axiom CA2 replaces naive union with a **compatibility law**, ensuring local-uniform convergence and producing a genuine holomorphic limit. Thus the global object is defined by glueing, not by set-theoretic union.


## Discussion

- CA2.a is metric (Cauchy on compacts); CA2.b is algebraic (stabilized jets or other determining data). Either path yields the same notion of causal continuation.
- CA3 encodes causal monotonicity of stage information; it is natural in arithmetic constructions and aligns with identity-type uniqueness.
- The scheme is agnostic to the specific causal closure generating $S_k$; onion avalanche is a canonical instance.

The axioms are minimal for existence and uniqueness; additional growth conditions can be added for continuation beyond $\Omega$ (e.g., Phragmén–Lindelöf barriers).


## Conclusion

Causal analytic continuation is the unique holomorphic limit of stage-analytic functions knitted together by a causal compatibility law. Stage compactness alone does not suffice; the glueing axioms CA2.a or CA2.b enforce coherence across stages, yielding a global analytic object determined by finite causal histories.


## Next Work

1. Identify weakest kernel conditions ensuring CA1 and verify CA2 under natural arithmetic tails.
2. Develop quantitative rates for CA2.a (e.g., explicit moduli on compacts).
3. Extend to vector-valued kernels and several complex variables ($d>1$).
4. Apply to causal $L$-functions with conductor-aware staged data and study zeros under causal growth.
5. Explore categorical formulations (inverse/direct limits in $\mathcal O(\Omega)$ with causal morphisms).


## Corresponding author(s)

Aurey Hyppa: aurey.hyppa@proton.example


## References

1. Conway, J. B. (1978). Functions of One Complex Variable I. Springer.
2. Rudin, W. (1987). Real and Complex Analysis (3rd ed.). McGraw–Hill.
3. Boivin, A., & Korevaar, J. (1990). The Cauchy transform and strong convergence on compacta. Proceedings of the AMS.
4. Tenenbaum, G. (2015). Introduction to Analytic and Probabilistic Number Theory (3rd ed.). AMS.
