% On the Causality of Natural Numbers
% Aurey Hyppa, An M. Rodriguez*
% September 3, 2025


## Abstract

We define a canonical era function on the natural numbers by withholding each
integer until it can be generated from already admitted integer labels. Powers
are taken as primitive generation events, and multiplicative recombination is
allowed only across coprime blocks. This yields a recursive map
$\tau:\mathbb N\to\mathbb Z_{\ge 1}$, where $\tau(n)$ is the least era in
which $n$ can appear. The resulting structure is a well-founded dependency
order, distinct from the usual order by size. Primes are forced to appear at
their own eras, while composites may appear earlier than their numerical value
when their generators are already present. We give the formal definition,
derive basic properties, and compute the first era sets.


## One-Sentence Summary

Natural numbers can be ordered by the earliest era in which they can be
generated from admitted integer labels using powers and coprime recombination.


## Keywords

natural numbers, causality, constructive order, prime powers, generations,
dependency order


## Introduction

The natural numbers $\mathbb N=\{1,2,3,\dots\}$ are usually ordered by size.
That order is static: every factorization is valid at once. Here we instead
introduce a generational order. Integers are withheld until the integer labels
needed to generate them have appeared.

The intended examples are:

- era $1$: $1^1$
- era $2$: $2, 2^2$
- era $3$: $3, 3^2, 2^3, 3^3$
- era $4$: $2^4, 3^4, 4^2, 4^3, 4^4$

The key point is that powers are primitive generation events. An integer such
as $64$ need not wait for the representation $2^6$; it can already appear in
era $4$ as $4^3$. More generally, once a number has appeared, it may later act
as a base when its own label-era arrives.

To pass from examples to mathematics, we define a canonical era function
$\tau(n)$.


## Theory: Era Function

### Power cost

For $n\ge 1$, define the power cost

$$
\kappa(n)
=
\min\{\max(a,b): n=a^b,\ a,b\in\mathbb N,\ b\ge 1\}.
$$

The trivial representation $n=n^1$ is always allowed, so $\kappa(n)\le n$.

Examples:

$$
\kappa(4)=2,
\qquad
\kappa(8)=3,
\qquad
\kappa(16)=4,
\qquad
\kappa(64)=4,
$$

since

$$
4=2^2,\quad 8=2^3,\quad 16=2^4=4^2,\quad 64=2^6=4^3=8^2.
$$

### Era function

Define $\tau:\mathbb N\to\mathbb Z_{\ge 1}$ recursively by

$$
\tau(1)=1,
$$

and for $n>1$,

$$
\tau(n)
=
\min\left(
\kappa(n),
\min_{\substack{ab=n\\1<a<n\\\gcd(a,b)=1}}
\max(\tau(a),\tau(b))
\right).
$$

If no nontrivial coprime factorization exists, the inner minimum is omitted.

This definition says:

1. An integer can appear directly as a power event, with cost $\kappa(n)$.
2. It can also appear by recombining previously generated coprime blocks.
3. Its era is the earliest moment either route becomes available.

The coprime condition prevents repeated splitting of a single prime channel.
For example, $16$ is not treated as $2\cdot 2\cdot 2\cdot 2$ at era $2$.
Instead it appears through the power channel $2^4$ or $4^2$, both of which
place it in era $4$.


## Basic Properties

### Well-definedness

The recursion is well-founded. In every coprime factorization $n=ab$ with
$1<a<n$, both $a$ and $b$ are smaller than $n$. So $\tau(n)$ is computed from
previously known values of $\tau$ together with the explicit finite quantity
$\kappa(n)$.

### Primes

If $p$ is prime, then it has no nontrivial coprime factorization. Hence

$$
\tau(p)=\kappa(p)=p.
$$

So primes are forced to appear at their own eras.

### Prime-power channels

If

$$
n=\prod_{i=1}^r p_i^{e_i}
$$

is the prime factorization of $n$, then the coprime factorization rule implies
that different prime channels recombine by taking the maximum of their
individual eras. In practice,

$$
\tau(n)=\max_i \tau(p_i^{e_i}),
$$

where each prime-power era $\tau(p^e)$ is determined by the power-cost rule.

So the era of a general integer is the latest era among its prime-power
channels.


## Results

### First eras

The first era sets are:

$$
E_k=\{n\in\mathbb N:\tau(n)=k\}.
$$

For the first few eras:

$$
E_1=\{1\},
$$

$$
E_2=\{2,4\},
$$

$$
E_3=\{3,6,8,9,12,18,24,27,36,54,72,108,216\},
$$

$$
E_4=\{16,48,64,81,144,162,192,256,324,432,576,648,768,1296,1728,\dots\}.
$$

The important phenomenon is already visible:

- primes are sparse frontier events,
- prime powers can appear much earlier than their numerical value,
- large integers may belong to low eras if their generators are simple.

### Interpretation

The natural order by size and the causal order by era are fundamentally
different. For example,

$$
\tau(64)=4
\qquad\text{while}\qquad
64\gg 4.
$$

So $\tau$ measures generative accessibility, not magnitude.


## Discussion

This definition isolates the part of the original idea that is mathematically
salvageable: not a privileged display sequence, but a canonical era grading.

Any list of integers that respects increasing $\tau$ is secondary. The primary
object is the function $\tau$ itself and the induced stratification

$$
\mathbb N = \bigsqcup_{k\ge 1} E_k.
$$

This makes the causal claim precise:

- primes are forced frontier events,
- powers are primitive generation steps,
- composites appear when their prime-power channels can be recombined.

The next natural question is whether familiar arithmetic observables can be
recovered from this grading. In particular, if one sorts the generated integers
back into the usual order on $\mathbb N$, the frontier behavior of the primes
can be studied as a histogram on the era process rather than as an independent
random irregularity.


## Conclusion

We have defined a canonical era function on $\mathbb N$ by withholding integers
until they can be generated from admitted integer labels through powers and
coprime recombination. This yields a well-founded dependency order distinct
from the ordinary order by size. The resulting structure is computable and
gives a concrete notion of generational appearance for the integers.


## Next Work

1. Compute the era sets $E_k$ at larger cutoffs and study their asymptotic
   growth.
2. Sort the cumulative generated set back into the ordinary order and compare
   its prime frontier with $\pi(x)$.
3. Investigate whether the era grading explains the jaggedness of prime
   counting as a deterministic generational effect.
4. Compare this era process with other dependency orders on factorization data.


## Corresponding author(s)

Aurey Hyppa: aurey.hyppa@proton.example


## References

1. Hardy, G. H., & Wright, E. M. (2008). *An Introduction to the Theory of
   Numbers* (6th ed.). Oxford University Press.
2. Tenenbaum, G. (2015). *Introduction to Analytic and Probabilistic Number
   Theory* (3rd ed.). American Mathematical Society.
