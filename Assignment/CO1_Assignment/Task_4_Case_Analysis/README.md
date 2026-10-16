# Task 4 – Best, Average, and Worst-Case Analysis

## 1. Aim
To analyze the behavior of the three searching algorithms under best-, average-, and worst-case input conditions.

## 2. Linear Search

**Best case:** The target is the first record. Only one comparison is required. Complexity: Θ(1).

**Average case:** For a successful search where every position is equally likely, the expected number of comparisons is (n + 1) / 2. Complexity: Θ(n).

**Worst case:** The target is the last record or is absent. All n records are checked. Complexity: Θ(n).

## 3. Recursive Binary Search

**Best case:** The target is exactly at the middle of the sorted list. Complexity: Θ(1).

**Average case:** The search repeatedly halves the remaining range. Complexity: Θ(log n).

**Worst case:** The target is found after the maximum number of halvings or is absent. Complexity: Θ(log n).

The records must be sorted before searching.

## 4. Hash Table Search

**Best case:** The target is retrieved directly with no collision handling. Complexity: Θ(1).

**Average case:** With a suitable hash function and controlled load factor, lookup takes expected Θ(1) time.

**Worst case:** Many keys collide, requiring examination of a large number of entries. Complexity: Θ(n).

## 5. Comparison Table

| Algorithm | Best case | Average/expected case | Worst case |
|---|---|---|---|
| Linear Search | Θ(1) | Θ(n) | Θ(n) |
| Recursive Binary Search | Θ(1) | Θ(log n) | Θ(log n) |
| Hash Table Search | Θ(1) | Expected Θ(1) | Θ(n) |

## 6. Conclusion
Linear Search is sensitive to the target's position. Binary Search performs consistently well on sorted records. Hash Table Search provides fast expected lookup but may degrade when collisions are severe. These differences must be considered when selecting an algorithm for a large student database.
