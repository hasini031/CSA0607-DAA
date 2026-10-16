# Task 3 – Mathematical Complexity Analysis

## 1. Aim
To derive mathematical functions for the number of operations performed by the three searching algorithms.

Let n be the number of student records.

## 2. Linear Search

In the best case, the target is the first record:

C_best(n) = 1

In the worst case, the target is last or absent:

C_worst(n) = n

If a successful target is equally likely to occur at any position:

C_avg(n) = (1 + 2 + ... + n) / n

Using the arithmetic-series formula:

C_avg(n) = [n(n + 1) / 2] / n

C_avg(n) = (n + 1) / 2

Therefore, best-case time is Θ(1), while average- and worst-case time are Θ(n).

## 3. Recursive Binary Search

Each recursive call performs constant work and searches at most half the remaining records.

Recurrence:

T(n) = T(n/2) + c

where c is constant work per call.

After k halvings, the remaining size is:

n / 2^k = 1

Therefore:

2^k = n

k = log₂(n)

The number of comparisons grows logarithmically. Thus, best case is Θ(1) and average- and worst-case time are Θ(log n).

If initially unsorted records must be sorted using comparison sorting, preprocessing generally costs Θ(n log n). A subsequent binary search costs Θ(log n).

## 4. Hash Table Search

Expected hash-table construction time:

T_build(n) = Θ(n)

Expected lookup time with suitable hashing:

T_lookup(n) = Θ(1)

Worst-case lookup under extreme collisions:

T_worst(n) = Θ(n)

The hash table requires Θ(n) additional space.

## 5. Complexity Summary

| Algorithm | Best case | Average/expected case | Worst case |
|---|---|---|---|
| Linear Search | Θ(1) | Θ(n) | Θ(n) |
| Recursive Binary Search | Θ(1) | Θ(log n) | Θ(log n) |
| Hash Table Search | Θ(1) | Expected Θ(1) | Θ(n) |

## 6. Conclusion
Mathematical analysis shows that Binary Search scales logarithmically when records are sorted. Hash Table Search provides expected constant-time lookup but uses additional memory. Linear Search is simple but its running time increases linearly with the dataset size.
