from __future__ import annotations

import argparse
from collections import defaultdict
from math import gcd, isqrt


def power_cost(n: int) -> int:
    """Least generator ceiling needed to realize n as a^b with b >= 1."""
    best = n
    max_b = n.bit_length() + 1
    for b in range(2, max_b + 1):
        lo = 2
        hi = n
        while lo <= hi:
            mid = (lo + hi) // 2
            value = mid**b
            if value == n:
                best = min(best, max(mid, b))
                break
            if value < n:
                lo = mid + 1
            else:
                hi = mid - 1
    return best


def tau_up_to(limit: int) -> list[int]:
    """Compute tau(n) for 1 <= n <= limit."""
    tau = [0] * (limit + 1)
    tau[1] = 1
    for n in range(2, limit + 1):
        best = power_cost(n)
        for a in range(2, isqrt(n) + 1):
            if n % a != 0:
                continue
            b = n // a
            if gcd(a, b) != 1:
                continue
            best = min(best, max(tau[a], tau[b]))
        tau[n] = best
    return tau


def era_sets(tau: list[int]) -> dict[int, list[int]]:
    eras: dict[int, list[int]] = defaultdict(list)
    for n in range(1, len(tau)):
        eras[tau[n]].append(n)
    return dict(sorted(eras.items()))


def cumulative_sorted(tau: list[int], max_era: int) -> list[int]:
    return sorted(n for n in range(1, len(tau)) if tau[n] <= max_era)


def is_prime(n: int) -> bool:
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    k = 3
    while k * k <= n:
        if n % k == 0:
            return False
        k += 2
    return True


def prime_frontier_histogram(values: list[int], bin_size: int) -> list[tuple[int, int]]:
    bins: dict[int, int] = defaultdict(int)
    for n in values:
        if is_prime(n):
            bins[(n - 1) // bin_size] += 1
    return sorted((k * bin_size + 1, count) for k, count in bins.items())


def main() -> None:
    parser = argparse.ArgumentParser(description="Compute causal eras for integers.")
    parser.add_argument("--limit", type=int, default=200, help="largest integer to compute")
    parser.add_argument("--max-era", type=int, default=None, help="largest era to print cumulatively")
    parser.add_argument("--bin-size", type=int, default=10, help="prime histogram bin size")
    args = parser.parse_args()

    tau = tau_up_to(args.limit)
    eras = era_sets(tau)

    print("Era sets")
    for era, values in eras.items():
        print(f"era {era}: {values}")

    if args.max_era is not None:
        values = cumulative_sorted(tau, args.max_era)
        print()
        print(f"Cumulative sorted values through era {args.max_era}:")
        print(values)
        print()
        print(f"Prime histogram (bin size {args.bin_size}) through era {args.max_era}:")
        for start, count in prime_frontier_histogram(values, args.bin_size):
            print(f"[{start:>4}, {start + args.bin_size - 1:>4}]  {count}")


if __name__ == "__main__":
    main()
