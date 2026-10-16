# Task 5 – Asymptotic Analysis

## 1. Aim
To describe the growth rates of the searching algorithms using Big-O, Big-Omega, and Big-Theta notation.

## 2. Big-O Notation – O(g(n))
Big-O describes an asymptotic upper bound on an algorithm's growth.

Examples:
- Linear Search worst-case time: O(n).
- Recursive Binary Search worst-case time: O(log n).
- Hash Table Search worst-case time: O(n).

## 3. Big-Omega Notation – Ω(g(n))
Big-Omega describes an asymptotic lower bound.

Examples:
- Linear Search best-case time: Ω(1).
- Recursive Binary Search best-case time: Ω(1).
- Hash Table Search can perform a lookup in constant time: Ω(1).

## 4. Big-Theta Notation – Θ(g(n))
Big-Theta describes a tight asymptotic bound when upper and lower bounds have the same order of growth.

Examples:
- Linear Search worst-case time: Θ(n).
- Recursive Binary Search worst-case time: Θ(log n).
- Hash Table Search expected lookup time: Θ(1), under suitable hashing assumptions.

## 5. Growth-Rate Comparison

For sufficiently large n, the common growth order is:

Θ(1) < Θ(log n) < Θ(n) < Θ(n log n)

Constant and logarithmic growth rates increase much more slowly than linear growth.

## 6. Space Complexity

- Linear Search: O(1) auxiliary space.
- Recursive Binary Search: O(log n) recursion-stack space.
- Hash Table Search: O(n) additional space for the index.

## 7. Conclusion
Asymptotic notation helps compare algorithms independently of a particular computer's speed. Binary Search is efficient for sorted records, and Hash Table Search has expected constant-time lookup. The actual choice must also consider memory, preprocessing, updates, and measured performance.
