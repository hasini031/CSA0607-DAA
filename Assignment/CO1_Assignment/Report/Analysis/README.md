# Complexity Analysis

## 1. Linear Search
- Best-case time: Θ(1)
- Average-case time: Θ(n)
- Worst-case time: Θ(n)
- Auxiliary space: Θ(1)

Linear Search checks records sequentially. In the worst case, all n records are examined.

## 2. Recursive Binary Search
- Best-case time: Θ(1)
- Average-case time: Θ(log n)
- Worst-case time: Θ(log n)
- Auxiliary space: Θ(log n)

Binary Search requires sorted records and reduces the search range by approximately half in each recursive call.

Recurrence:

T(n) = T(n/2) + c

T(1) = d

Expanding the recurrence gives T(n) = d + c log₂(n), so the time complexity is Θ(log n).

## 3. Hash Table Search
- Expected lookup time: Θ(1)
- Worst-case lookup time: Θ(n)
- Expected construction time: Θ(n)
- Additional space: Θ(n)

Expected constant-time lookup assumes a suitable hash function and controlled load factor. Severe collisions can increase lookup time.

## 4. Case Analysis
Linear Search is fastest when the target is first and slowest when it is last or absent. Binary Search is fastest when the target is at the midpoint and has logarithmic worst-case time. Hash Table Search generally provides expected constant-time lookup.

## 5. Experimental Analysis
Insert your measured execution times and explain how the observed results compare with the theoretical complexities.

Do not claim experimental results until the code has been executed and the results verified.
