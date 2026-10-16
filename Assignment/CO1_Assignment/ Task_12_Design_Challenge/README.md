# Task 12 – Design Challenge: Large-Scale Student Database

## 1. Aim
To design a searching solution for a student database containing one million records, supporting 50,000 search requests per hour, with new records added once per day.

## 2. System Requirements

- Existing database size: 1,000,000 student records.
- Search workload: 50,000 requests per hour.
- Record updates: New records are added once per day.
- Main requirement: Fast, correct registration-number lookups.

The average search rate is:

50,000 / 3,600 ≈ 13.89 searches per second.

Actual peak traffic may be higher than this average.

## 3. Evaluation of Searching Algorithms

### Linear Search
Worst-case search time is Θ(n). With one million records, a search may require examining all one million entries. This is not the preferred approach for the stated frequent-search workload.

### Recursive Binary Search
Worst-case search time is Θ(log n). It is efficient when records are sorted, but the system must maintain sorted data and account for sorting or update costs.

### Hash Table Search
Expected lookup time is Θ(1), with Θ(n) memory for the index. It is a strong candidate for exact-match searches when hashing is suitable and memory is available.

## 4. Proposed Design

1. Maintain the student records in a reliable source-of-truth database.
2. Create an index using registration numbers as keys.
3. Validate that each registration number is unique.
4. Build or update the index when daily records are added.
5. If new records must become searchable immediately, update the index incrementally rather than waiting for a daily rebuild.
6. Verify that lookups return the correct student records.
7. Monitor response time, memory consumption, collision behavior, and failed searches.

## 5. Capacity Considerations

The average request rate of approximately 13.89 searches per second is a useful starting point for capacity planning. However, actual performance must be tested using the target hardware, realistic concurrency, database overhead, and peak traffic patterns.

The hourly request count alone does not guarantee that the system will meet a particular response-time requirement.

## 6. Trade-Off Analysis

| Criterion | Linear Search | Binary Search | Hash Table |
|---|---|---|---|
| Search time | Θ(n) worst case | Θ(log n) | Expected Θ(1) |
| Extra space | Θ(1) | Θ(log n) stack | Θ(n) |
| Sorted data required | No | Yes | No |
| Update considerations | Simple append | Sorted order may need maintenance | Index must be updated |
| Suitability for exact-match workload | Low at scale | Good | High, subject to constraints |

## 7. Final Recommendation

Use a hash-based index or an appropriate database index for exact registration-number lookups, subject to memory availability, uniqueness constraints, and measured performance. If the system also needs ordered reports or range queries, a database B-tree index may be a better overall solution.

Validate the design with realistic tests at one million records and the required search workload. Include actual measurements and explain any limitations.

## 8. Conclusion

The design challenge demonstrates that algorithm selection depends on more than asymptotic time complexity. Search frequency, daily updates, memory usage, correctness, peak traffic, and database requirements must all be considered before deploying the solution.
