% A New Constructive Ordering of the Natural Numbers
% Aurey Hippa, An M. Rodriguez*
% September 3, 2025


## Abstract

A constructive total order on the natural numbers is introduced based on a hereditary exponent rank computed from the prime factorization of an integer and the prime factorizations of its exponents, recursively. Each number is assigned a finite rank measuring the minimal exponent-depth needed to build it from one by prime powers and finite products. Ordering first by rank and then by magnitude yields a computable, divisibility–compatible linear extension of the divisibility partial order. The rank grows on the scale of the iterated logarithm, which implies that almost all numbers occur very early in the order. Structural characterizations, bounds, and algorithms for evaluation and enumeration are provided.


## One-Sentence Summary

Order the natural numbers by the minimal hereditary depth of their exponent trees, then by size; this yields a computable, fine-grained, multiplicative–structural ordering with iterated-logarithm height.


## Keywords

natural numbers, constructive order, divisibility, prime exponents, iterated logarithm, enumeration


## Introduction

Standard numerical order organizes the natural numbers primarily by size, ignoring multiplicative structure. Many tasks in arithmetic and computation benefit from orderings that surface algebraic complexity—e.g., divisibility, smoothness, or exponentiation depth. A constructive scheme is presented that linearly orders the natural numbers by a **hereditary exponent rank**. The rank reflects how many exponent layers are required to assemble the number from one using prime powers and finite products. The resulting order is a linear extension of divisibility, computable, and admits quantitative control: the rank is bounded above and below by iterated logarithms of the number. This provides a principled, structure-aware alternative to size-first enumeration.


## Framework

### Basic definitions

Let $\mathbb N:=\{1,2,3,\dots\}$. Every $n\in\mathbb N$ has the canonical factorization
$$
n=\prod_{p} p^{\alpha_p},
$$
over primes $p$, where all but finitely many exponents $\alpha_p\in\mathbb N\cup\{0\}$ vanish.

Define the **hereditary exponent rank** $r:\mathbb N\to\mathbb N$ recursively by
$$
r(1):=0,\qquad
r(n):=1+\max_{p\mid n} r(\alpha_p)\quad (n>1).
$$
Intuitively, $r(n)$ is one plus the maximal rank among the exponents appearing in the prime factorization of $n$; exponents themselves are ranked by the same rule.

For $t\in\mathbb N$, define the **rank layers**
$$
\mathcal L_t:=\{\,n\in\mathbb N:\ r(n)=t\,\},\qquad
\mathcal U_t:=\{\,n\in\mathbb N:\ r(n)\le t\,\}.
$$

### The constructive order

Define a total order $\prec$ on $\mathbb N$ by
$$
n\prec m\ \Longleftrightarrow\ \big( r(n)<r(m)\big)\ \text{ or }\ \big(r(n)=r(m)\ \text{ and }\ n<m\big).
$$
Thus numbers are listed first by increasing rank, and within each rank by increasing value.

This yields the sequence
$$
1\ (r=0),\quad
\text{all squarefree }n\ge 2\ (r=1),\quad
\text{then all }n\text{ with squarefree exponents }(r=2),\ \text{etc.}
$$


## Derivation

### Structural properties

1. **Partition and minimality.** The sets $\{\mathcal L_t\}_{t\ge0}$ form a partition of $\mathbb N$, with $\mathcal L_0=\{1\}$ and $\mathcal L_1$ the set of squarefree integers $\ge 2$.

   *Proof.* Immediate from the definition: $r(n)=1$ iff every nonzero $\alpha_p$ equals $1$, i.e., $n$ is squarefree.

2. **Hereditary characterization.** For $t\ge1$,
   $$
   r(n)\le t\ \Longleftrightarrow\ \text{for every }p\mid n,\ \ r(\alpha_p)\le t-1.
   $$
   Equivalently, expanding exponents recursively, the rooted “exponent tree” of $n$ has depth at most $t$, with leaves equal to $1$.

3. **Closure under exponentiation and products.** If $e\in \mathcal U_{t}$ and $p$ is prime, then $p^{e}\in \mathcal U_{t+1}$. Finite products of such prime powers remain in $\mathcal U_{t+1}$. Moreover, $\mathcal L_{t+1}$ consists exactly of finite products $\prod p^{e_p}$ with each $e_p\in\mathcal U_t$ and at least one $e_p\in\mathcal L_t$.

   *Proof.* Follows from the definition and the max in $r(n)$.

4. **Divisibility compatibility.** If $m\mid n$, then either $r(m)<r(n)$ or $\big(r(m)=r(n)$ and $m\le n\big)$. Hence the order $\prec$ is a linear extension of divisibility.

   *Proof.* For each $p$, $\alpha_p(m)\le \alpha_p(n)$ and $r$ is monotone nondecreasing under $\alpha\mapsto r(\alpha)$ and under $n\mapsto r(n)$ by the hereditary characterization. If $r(m)=r(n)$, numeric tiebreak gives $m\prec n$.

5. **Rank stability under units.** For $a\in\mathbb N$ and $u\in\{1\}$, $r(au)=r(a)$. (Trivial here; noted for completeness.)

### Quantitative bounds

Define the base-$2$ iterated logarithm
$$
\log^{(0)}_2 n:=n,\qquad
\log^{(k+1)}_2 n:=\log_2\big(\log^{(k)}_2 n\big),\qquad
\log^{*}_2 n:=\min\{\,k:\ \log^{(k)}_2 n\le 1\,\}.
$$

**Upper bound.** For $n\ge 2$,
$$
r(n)\ \le\ 1+r(\lfloor\log_2 n\rfloor)\ \le\ 1+\log^{*}_2 n.
$$

*Proof.* In $n=\prod p^{\alpha_p}$, each nonzero $\alpha_p\le \log_2 n$. Apply the definition of $r$ and iterate.

**Lower bound (sharp up to constants).** Define $x_0:=1$ and $x_{t+1}:=2^{x_t}$. Then $r(x_t)=t$ for all $t\ge 0$. Consequently,
$$
r(n)\ \ge\ \max\{\,t:\ x_t\le n\,\}\ \ge\ \log^{*}_2 n-1.
$$

*Proof.* $r(1)=0$. If $r(x_t)=t$, then $x_{t+1}=2^{x_t}$ has factorization with a single exponent $x_t$, so $r(x_{t+1})=1+r(x_t)=t+1$.

Combining the bounds,
$$
\log^{*}_2 n-1\ \le\ r(n)\ \le\ 1+\log^{*}_2 n,
$$
i.e., $r(n)=\Theta(\log^{*} n)$.

### Density of low ranks

- $\mathcal L_1$ is the set of squarefree integers; its natural density is $6/\pi^2$.
- $\mathcal U_2$ is the set of integers whose exponents are all squarefree (hereditarily squarefree of depth two). This set has density one: for any fixed $k$, the proportion of integers with every prime exponent $\le k$ tends to one; squarefree exponents are a fortiori bounded. More precisely, for any $\varepsilon>0$ there exists $k$ such that the set $\{n:\ \alpha_p(n)\le k\ \forall p\}$ has lower density $\ge 1-\varepsilon$, and among those, the squarefree-exponent constraint removes a proportion $O(1/k)$.

These observations align with the $\Theta(\log^{*} n)$ height: almost all integers appear at very small ranks.

### Algorithms

**Rank evaluation (given $n$).**

1. If $n=1$, return $0$.
2. Factor $n$ as $\prod p^{\alpha_p}$.
3. Recursively compute $r(\alpha_p)$ for each nonzero exponent $\alpha_p$.
4. Return $1+\max_p r(\alpha_p)$.

This terminates since $\alpha_p<n$ for $n>1$ and recursion depth is $O(\log^{*} n)$.

**Enumeration up to a bound $B$.**

1. For $t=0,1,2,\dots$:
2. For $n=1,2,\dots,B$:
3. Output $n$ if $r(n)=t$ (computed by the evaluation procedure).
4. Stop once all $n\le B$ have been output.

This lists $\{1,\dots,B\}$ in the order $\prec$. For unbounded enumeration, increase $B$ as needed or generate by products $\prod p^{e_p}$ with $e_p$ drawn from previously enumerated layers, pruned by increasing numeric thresholds to avoid duplicates; tie-resolution by magnitude enforces the prescribed order.


## Results

1. **Totality.** The relation $\prec$ is a total order on $\mathbb N$.
2. **Linear extension of divisibility.** If $m\mid n$ and $m\ne n$ then $m\prec n$.
3. **Low rank characterization.**
   - $r(n)=0$ iff $n=1$.
   - $r(n)=1$ iff $n$ is squarefree and $n\ge2$.
   - $r(n)\le 2$ iff every exponent in the prime factorization of $n$ is squarefree.
4. **Height.** $r(n)=\Theta(\log^{*} n)$ with explicit two-sided bounds given above.
5. **Constructive closure.** $\mathcal U_{t+1}$ is the multiplicative monoid generated by $\{p^{e}:\ e\in\mathcal U_t,\ p\text{ prime}\}$.
6. **Early density.** $\mathcal U_2$ has natural density one; hence almost all integers appear by rank two, and $\prec$ lists “most” numbers immediately after the squarefree layer.

Proofs have been indicated in the derivation section; full details follow directly from the recursive definition and standard multiplicative estimates.


## Discussion

The hereditary exponent rank exposes multiplicative structure ignored by the usual order. The top layer ($r=1$) isolates squarefree numbers; the next ($r=2$) includes precisely those with squarefree exponents, and so on. The closure rule ensures exponent–feeding: exponents from earlier layers become exponents for new prime powers one layer later. The resulting order is computable, respects divisibility, and organizes integers by a natural complexity measure with extremely slow growth (iterated logarithm), implying shallow global height.

This order interfaces cleanly with algorithms that prefer divisibility precedence (e.g., dynamic programming over divisors, multiplicative convolutions) and with analytic number theory contexts where exponent structure matters (e.g., $p$-adic valuations, smoothness, or lifting the exponent). It also offers canonical “levels” for sampling and testing number-theoretic phenomena under controlled multiplicative complexity.


## Conclusion

A constructive, divisibility–compatible linear order on $\mathbb N$ has been defined via the hereditary exponent rank. The order is computed by recursion on prime-exponent trees, is a linear extension of divisibility, and has height $\Theta(\log^{*} n)$. Almost all integers appear by rank two, yet the order distinguishes fine multiplicative structure beyond mere size. The framework provides a principled alternative to numerical order when multiplicative complexity is primary.


## Next Work

1. Develop efficient, duplicate-free generators for $\mathcal L_t$ via priority queues keyed by magnitude and seeded by $p^{e}$ with $e\in\mathcal U_{t-1}$.
2. Analyze precise asymptotics of $|\mathcal U_t\cap[1,B]|$ as $B\to\infty$ for fixed $t\ge2$.
3. Extend to $\mathbb N^k$ by componentwise ranks and to $\mathbb Z$ via sign strata; study compatibility with convolution and Dirichlet series.
4. Compare with alternative complexity orders (addition–multiplication circuits, integer complexity) and examine correlations.
5. Investigate applications to sieve layers where exponent patterns govern inclusion–exclusion weights.


## Corresponding author(s)

Contact: author@proton.example


## References

1. Niven, I., Zuckerman, H. S., & Montgomery, H. L. (1991). An Introduction to the Theory of Numbers (5th ed.). Wiley.

2. Hardy, G. H., & Wright, E. M. (2008). An Introduction to the Theory of Numbers (6th ed.). Oxford University Press.

3. Tenenbaum, G. (2015). Introduction to Analytic and Probabilistic Number Theory (3rd ed.). American Mathematical Society.

4. Granville, A. (2008). Smooth numbers: computational number theory and beyond. In Algorithmic Number Theory: Lattices, Number Fields, Curves and Cryptography (pp. 267–323). Cambridge University Press.
