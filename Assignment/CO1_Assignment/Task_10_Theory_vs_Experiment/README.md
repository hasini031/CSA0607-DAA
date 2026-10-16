# Task 10 – Theoretical Versus Experimental Comparison

## 1. Aim
To compare the theoretical time complexities of the three searching algorithms with their measured execution times.

## 2. Theoretical Analysis

### Linear Search
Worst-case time complexity is Θ(n). When the target is last or absent, every record must be checked.

### Recursive Binary Search
Worst-case time complexity is Θ(log n). Each recursive call reduces the search range by approximately half.

### Hash Table Search
Expected lookup time is Θ(1) with suitable hashing assumptions. Building the hash table takes expected Θ(n) time and Θ(n) additional space.

## 3. Comparison Table

| Algorithm | Theoretical complexity | Expected experimental trend |
|---|---|---|
| Linear Search | Θ(n) worst case | Time increases with dataset size |
| Recursive Binary Search | Θ(log n) worst case | Time increases slowly |
| Hash Table Search | Expected Θ(1) lookup | Lookup time stays approximately flat |

## 4. Factors Affecting Experimental Results

- Computer processing speed.
- Python interpreter overhead.
- Memory allocation and availability.
- Dataset size and target position.
- Hash-table construction cost.
- System load and measurement overhead.

## 5. Analysis Procedure

1. Collect the actual execution times from Task 9.
2. Compare the measured trends with the theoretical growth rates.
3. Check that Binary Search receives sorted data.
4. Separate hash-table construction time from lookup time.
5. Explain any differences between theoretical expectations and measured results.
6. Include the comparison table and graph in the final report.

## 6. Expected Findings

Linear Search should show approximately linear growth in the worst case. Binary Search should scale more slowly. Hash-table lookup should generally remain fast, although building and maintaining the table requires additional time and memory.

Small datasets may show irregular timings because timer overhead and implementation details can be significant.

## 7. Conclusion
Theoretical analysis explains how an algorithm scales as input size increases, while experimental measurements show its actual performance in a particular environment. Both are necessary for selecting a suitable searching algorithm.
