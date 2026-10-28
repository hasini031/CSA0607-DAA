
"""
SentinelOps SOC Alert-Triage Module
CSA0607 - Design and Analysis of Algorithms
CO2 Assessment: Debugging and Optimization

This file contains:
1. Original faulty implementations from the assessment.
2. Corrected implementations.
3. Optimized implementations.
"""

import math


# ============================================================
# SECTION 1: ORIGINAL FAULTY CODE
# ============================================================

def original_sort_alerts(alerts):
    for i in range(1, len(alerts)):
        key = alerts[i]
        j = i - 1
        while j > 0 and alerts[j][1] < key[1]:
            alerts[j + 1] = alerts[j]
            j -= 1
        alerts[j] = key
    return alerts


def original_is_blocked(blocklist, ip):
    for i in range(len(blocklist)):
        if blocklist[i] == ip:
            return False
        else:
            return False


def original_find_signature(log, pattern):
    n, m = len(log), len(pattern)
    hits = []
    for i in range(n - m):
        for j in range(m):
            if log[i + j] != pattern[j]:
                break
        if j == m - 1:
            hits.append(i)
    return hits


def original_closest_logins(events):
    min_dist = 0
    pair = None

    for i in range(len(events)):
        for j in range(len(events)):
            d = math.sqrt(
                (events[i][0] - events[j][0]) ** 2
                + (events[i][1] - events[j][1]) ** 2
            )
            if d > min_dist:
                min_dist = d
                pair = (i, j)

    return pair, min_dist


# ============================================================
# SECTION 2: CORRECTED CODE
# ============================================================

def corrected_sort_alerts(alerts):
    """Sort by descending severity, preserving arrival order on ties."""
    alerts = list(alerts)

    for i in range(1, len(alerts)):
        key = alerts[i]
        j = i - 1

        while j >= 0 and alerts[j][1] < key[1]:
            alerts[j + 1] = alerts[j]
            j -= 1

        alerts[j + 1] = key

    return alerts


def corrected_is_blocked(blocklist, ip):
    """Return True if the IP address is present in the blocklist."""
    for blocked_ip in blocklist:
        if blocked_ip == ip:
            return True
    return False


def corrected_find_signature(log, pattern):
    """Find every occurrence, including overlapping matches."""
    if pattern == "":
        return list(range(len(log) + 1))

    n, m = len(log), len(pattern)
    hits = []

    for i in range(n - m + 1):
        j = 0

        while j < m and log[i + j] == pattern[j]:
            j += 1

        if j == m:
            hits.append(i)

    return hits


def corrected_closest_logins(events):
    """Find the closest pair using brute-force pair comparison."""
    n = len(events)

    if n < 2:
        return None, math.inf

    best_squared = math.inf
    pair = None

    for i in range(n):
        for j in range(i + 1, n):
            dx = events[i][0] - events[j][0]
            dy = events[i][1] - events[j][1]
            squared = dx * dx + dy * dy

            if squared < best_squared:
                best_squared = squared
                pair = (i, j)

    return pair, math.sqrt(best_squared)


# ============================================================
# SECTION 3: OPTIMIZED CODE
# ============================================================

def optimized_sort_alerts(alerts):
    """Use Python's stable sorting implementation."""
    return sorted(alerts, key=lambda alert: -alert[1])


def optimized_is_blocked(blocklist, ip):
    """Use a set for efficient repeated blocklist lookups."""
    return ip in set(blocklist)


def optimized_find_signature(log, pattern):
    """Use KMP string matching to avoid redundant comparisons."""
    if pattern == "":
        return list(range(len(log) + 1))

    n, m = len(log), len(pattern)

    if m > n:
        return []

    # Build the longest proper prefix/suffix table.
    lps = [0] * m
    length = 0
    i = 1

    while i < m:
        if pattern[i] == pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        elif length > 0:
            length = lps[length - 1]
        else:
            lps[i] = 0
            i += 1

    # Search the log using KMP.
    hits = []
    i = 0
    j = 0

    while i < n:
        if log[i] == pattern[j]:
            i += 1
            j += 1

            if j == m:
                hits.append(i - j)
                j = lps[j - 1]
        elif j > 0:
            j = lps[j - 1]
        else:
            i += 1

    return hits


def optimized_closest_logins(events):
    """
    Sort locations by x-coordinate and prune pairs that cannot
    improve the best distance found so far.

    Returns original event indices and the minimum distance.
    """
    n = len(events)

    if n < 2:
        return None, math.inf

    points = sorted(
        (x, y, index) for index, (x, y) in enumerate(events)
    )

    best_squared = math.inf
    pair = None

    for i in range(n - 1):
        x1, y1, original_i = points[i]

        for j in range(i + 1, n):
            x2, y2, original_j = points[j]

            dx = x2 - x1

            # Later points have equal or larger x-coordinates.
            if dx * dx >= best_squared:
                break

            dy = y2 - y1
            squared = dx * dx + dy * dy

            if squared < best_squared:
                best_squared = squared
                pair = (original_i, original_j)

    return pair, math.sqrt(best_squared)


# ============================================================
# SECTION 4: ASSESSMENT SAMPLE DATA
# ============================================================

if __name__ == "__main__":
    alerts = [
        ("A1", 3), ("A2", 9), ("A3", 5),
        ("A4", 9), ("A5", 1)
    ]

    blocklist = [
        "10.0.0.5", "10.0.0.9", "172.16.4.2"
    ]

    queries = [
        "10.0.0.9", "10.0.0.5", "8.8.8.8"
    ]

    log = "FAILFAIXFAIL"
    pattern = "FAIL"

    events = [
        (2, 3), (12, 30), (40, 50),
        (5, 1), (12, 10), (3, 4)
    ]

    print("SENTINELOPS - CORRECTED AND OPTIMIZED RESULTS")

    print("\nCorrected alert sorting:")
    print(corrected_sort_alerts(alerts))

    print("\nOptimized alert sorting:")
    print(optimized_sort_alerts(alerts))

    print("\nBlocklist search:")
    for ip in queries:
        print(ip, "->", optimized_is_blocked(blocklist, ip))

    print("\nCorrected signature search:")
    print(corrected_find_signature(log, pattern))

    print("\nOptimized signature search:")
    print(optimized_find_signature(log, pattern))

    print("\nCorrected closest login pair:")
    print(corrected_closest_logins(events))

    print("\nOptimized closest login pair:")
    print(optimized_closest_logins(events))
