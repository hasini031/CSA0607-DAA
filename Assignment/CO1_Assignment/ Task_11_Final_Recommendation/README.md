# Task 11 – Final Algorithm Recommendation

## 1. Aim
To recommend the most appropriate searching algorithm for a large student database based on theoretical complexity, experimental results, memory usage, and update requirements.

## 2. Evaluation Criteria

The algorithms are evaluated using:

- Worst-case and expected search time.
- Auxiliary space requirements.
- Preprocessing costs.
- Correctness of search results.
- Performance as dataset size increases.
- Suitability for frequent searches and database updates.

## 3. Comparison

### Linear Search
Advantages:
- Simple implementation.
- No preprocessing.
- Works with unsorted records.

Limitation:
- Worst-case time is Θ(n), making it inefficient for frequent searches over one million records.

### Recursive Binary Search
Advantages:
- Worst-case search time is Θ(log n).
- Requires relatively few comparisons.

Limitations:
- Records must be sorted.
- Sorting and maintaining sorted data introduce additional costs.
- Recursive calls require stack space.

### Hash Table Search
Advantages:
- Expected Θ(1) lookup.
- Does not require sorted records.
- Suitable for frequent exact-match searches.

Limitations:
- Requires Θ(n) additional space.
- Construction and updates must be managed.
- Worst-case lookup can be Θ(n) under extreme collisions.

## 4. Recommendation

A hash-based index is a strong candidate when the system primarily searches for exact registration-number matches, registration numbers are unique, and sufficient memory is available.

If ordered traversal and range queries are important, a sorted index or database B-tree index may be more appropriate.

Linear Search can be retained as a baseline or used for small datasets.

## 5. Evidence Required

The final recommendation must be supported by:
- Mathematical complexity analysis.
- Actual execution timings from Task 9.
- The theory-versus-experiment comparison from Task 10.
- Correctness test results.
- Consideration of memory and update requirements.

## 6. Conclusion
The recommended algorithm should balance search speed, memory consumption, preprocessing, and update behavior. The final choice must be justified using the actual experimental results rather than theoretical complexity alone.
