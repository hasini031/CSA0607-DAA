
"""
Performance benchmark for the SentinelOps CO2 assessment.
Run using: python benchmark.py
"""

import random
import time
import math

from sentinelops_module import (
    original_sort_alerts,
    optimized_sort_alerts,
    original_closest_logins,
    optimized_closest_logins,
)


def make_events(n, seed=42):
    """Generate reproducible random login locations."""
    rng = random.Random(seed)
    return [
        (rng.uniform(0, 10000), rng.uniform(0, 10000))
        for _ in range(n)
    ]


def measure_time(function, *args):
    """Return elapsed execution time in seconds."""
    start = time.perf_counter()
    function(*args)
    return time.perf_counter() - start


def count_brute_force_pairs(n):
    """Count pair evaluations in the original nested loops."""
    return n * n


def count_optimized_pairs(events):
    """
    Count candidate pairs inspected by the optimized algorithm.
    This mirrors its pair loop and x-distance pruning.
    """
    points = sorted(
        (x, y) for x, y in events
    )

    best_squared = math.inf
    count = 0

    for i in range(len(points) - 1):
        x1, y1 = points[i]

        for j in range(i + 1, len(points)):
            x2, y2 = points[j]
            dx = x2 - x1

            if dx * dx >= best_squared:
                break

            count += 1
            dy = y2 - y1
            squared = dx * dx + dy * dy

            if squared < best_squared:
                best_squared = squared

    return count


def main():
    print("CLOSEST-PAIR PERFORMANCE")
    print("-" * 75)
    print(
        f"{'Events':>8} {'Brute pairs':>14} "
        f"{'Optimized pairs':>18} {'Optimized time (s)':>20}"
    )

    for n in (1000, 4000, 8000):
        events = make_events(n)

        optimized_time = measure_time(
            optimized_closest_logins, events
        )

        brute_pairs = count_brute_force_pairs(n)
        optimized_pairs = count_optimized_pairs(events)

        print(
            f"{n:8d} {brute_pairs:14,d} "
            f"{optimized_pairs:18,d} {optimized_time:20.6f}"
        )

    print("\nINSERTION SORT COMPARISON")
    print("-" * 60)

    rng = random.Random(42)
    n = 2000

    random_alerts = [
        (f"A{i}", rng.randint(1, 10))
        for i in range(n)
    ]

    nearly_sorted = optimized_sort_alerts(random_alerts)

    # Reverse the nearly sorted order to create a different input.
    # This is not guaranteed to be random.
    reverse_alerts = list(reversed(nearly_sorted))

    for label, data in (
        ("Nearly sorted", nearly_sorted),
        ("Reversed order", reverse_alerts),
    ):
        insertion_time = measure_time(original_sort_alerts, data.copy())
        optimized_time = measure_time(optimized_sort_alerts, data)

        print(
            f"{label:16} | Original insertion sort: "
            f"{insertion_time:.6f}s | Built-in sort: "
            f"{optimized_time:.6f}s"
        )


if __name__ == "__main__":
    main()
