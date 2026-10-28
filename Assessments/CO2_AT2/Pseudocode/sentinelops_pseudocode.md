
# SentinelOps SOC Alert-Triage Module
## Pseudocode – Original, Corrected and Optimized Algorithms

### 1. Alert Sorting

**Original Algorithm**
1. Start from the second alert.
2. Store the current alert as key.
3. Compare previous severity while j > 0.
4. Shift alerts with lower severity to the right.
5. Insert the key at position j.
6. Return the alerts.

**Corrected Algorithm**
1. Start from the second alert.
2. Store the current alert as key.
3. Compare previous severity while j >= 0.
4. Shift alerts with lower severity to the right.
5. Insert the key at position j + 1.
6. Return alerts in descending severity order.

**Optimized Algorithm**
1. Receive the alert list.
2. Apply stable sorting by descending severity.
3. Preserve arrival order for equal severities.
4. Return the sorted alerts.

### 2. Blocklist Search

**Original Algorithm**
1. Traverse the blocklist.
2. Compare each IP with the requested IP.
3. Return False on a match.
4. Return False on a non-match.

**Corrected Algorithm**
1. Traverse the blocklist.
2. If an IP matches, return True.
3. If no match is found, return False.

**Optimized Algorithm**
1. Convert the blocklist into a set.
2. Check whether the requested IP belongs to the set.
3. Return True if present; otherwise return False.
4. Reuse the set for repeated lookups when possible.

### 3. Attack Signature Matching

**Original Algorithm**
1. Calculate log and pattern lengths.
2. Check starting positions while i < n - m.
3. Compare pattern characters with log characters.
4. Record matching positions.
5. Return all hits.

**Corrected Algorithm**
1. Handle an empty pattern.
2. Check all valid starting positions up to n - m.
3. Compare characters at each position.
4. Record a position when all characters match.
5. Return all matching positions, including overlaps.

**Optimized Algorithm**
1. Build the longest-prefix-suffix table for the pattern.
2. Scan the log using the KMP algorithm.
3. Reuse previous match information after a mismatch.
4. Record each occurrence, including overlapping matches.
5. Return all matching positions.

### 4. Closest Login Pair

**Original Algorithm**
1. Initialize minimum distance to zero.
2. Compare every event with every other event.
3. Calculate Euclidean distance for each pair.
4. Update the pair when distance is greater than the minimum.
5. Return the pair and distance.

**Corrected Algorithm**
1. Check whether at least two events exist.
2. Initialize minimum distance to infinity.
3. Compare each unique pair only once.
4. Calculate squared Euclidean distance.
5. Update the pair when a smaller distance is found.
6. Return the pair and actual distance.

**Optimized Algorithm**
1. Check whether at least two events exist.
2. Sort events by their x-coordinate while preserving original indices.
3. Compare candidate pairs in sorted order.
4. Stop checking later points when the squared x-distance cannot improve the current minimum.
5. Update the closest pair whenever a smaller distance is found.
6. Return the original event indices and minimum distance.
