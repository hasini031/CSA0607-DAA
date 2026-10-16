# Task 1 – Algorithm Design

## 1. Title

Design and Comparison of Searching Algorithms for a Large-Scale Student Record System

## 2. Aim

To design three different searching algorithms to find student registration numbers in a university database and study their working principles, preprocessing requirements, advantages, limitations, and expected efficiency.

## 3. Problem Statement

A university maintains a database containing a large number of student records. Each record contains a unique student registration number and other student details. The system must locate a student's record efficiently when a registration number is provided.

As the database grows to one million records or more, selecting an appropriate searching algorithm becomes important. The selected algorithm should provide correct results, minimize search time, and support the expected workload.

This task considers three approaches: Linear Search, Recursive Binary Search, and Hash Table Search.

## 4. Objectives

- Design three different searching algorithms.
- Explain the working principle of each algorithm.
- Write pseudocode for each approach.
- Identify preprocessing requirements.
- Understand the expected time and space complexity.
- Establish a basis for mathematical analysis and experimental comparison in subsequent tasks.

## 5. Algorithm 1 – Linear Search

### 5.1 Design Strategy

Linear Search uses an iterative sequential-search approach.

### 5.2 Working Principle

The algorithm starts from the first student record and compares its registration number with the target registration number. If they match, the corresponding record is returned. Otherwise, the algorithm moves to the next record and continues until the target is found or all records have been examined.

### 5.3 Pseudocode

    LINEAR_SEARCH(records, target)
        FOR i = 0 TO length(records) - 1
            IF records[i].registration_number = target
                RETURN records[i]
        RETURN NOT_FOUND

### 5.4 Preprocessing Requirement

No preprocessing or sorting is required. The algorithm can search both sorted and unsorted records.

### 5.5 Complexity

- Best-case time: O(1)
- Average-case time: O(n)
- Worst-case time: O(n)
- Auxiliary space: O(1), excluding the returned record and input storage.

Here, n represents the number of student records.

### 5.6 Advantages

- Simple to understand and implement.
- Works with unsorted records.
- Requires no additional index or preprocessing.

### 5.7 Limitations

- May examine every record before finding the target.
- Becomes inefficient for large databases with frequent searches.

## 6. Algorithm 2 – Recursive Binary Search

### 6.1 Design Strategy

Recursive Binary Search uses the divide-and-conquer approach.

### 6.2 Working Principle

The algorithm compares the target registration number with the middle element of a sorted list. If they match, the record is returned. If the target is smaller, the algorithm recursively searches the left half. Otherwise, it searches the right half.

At every recursive step, approximately half of the remaining records are eliminated.

### 6.3 Pseudocode

    BINARY_SEARCH(records, low, high, target)
        IF low > high
            RETURN NOT_FOUND

        mid = floor((low + high) / 2)

        IF records[mid].registration_number = target
            RETURN records[mid]

        ELSE IF target < records[mid].registration_number
            RETURN BINARY_SEARCH(records, low, mid - 1, target)

        ELSE
            RETURN BINARY_SEARCH(records, mid + 1, high, target)

### 6.4 Preprocessing Requirement

The records must be sorted in ascending order by registration number before searching. If the records are initially unsorted, an efficient comparison-based sorting algorithm generally requires O(n log n) time.

### 6.5 Complexity

- Best-case time: O(1)
- Average-case time: O(log n)
- Worst-case time: O(log n)
- Auxiliary space: O(log n) for the recursive call stack in the worst case.

### 6.6 Advantages

- Efficient for large, sorted datasets.
- Reduces the search range by approximately half at each step.
- Requires relatively few comparisons for large inputs.

### 6.7 Limitations

- Requires sorted records.
- Initial sorting can be expensive if the data is not already sorted.
- Recursive calls require additional stack space.

## 7. Algorithm 3 – Hash Table Search

### 7.1 Design Strategy

Hash Table Search uses hashing to provide direct access to student records.

### 7.2 Working Principle

A hash table stores registration numbers as keys and the corresponding student records as values. A hash function determines where each key should be stored. When a registration number is searched, the hash table uses the key to retrieve the associated record.

The expected lookup time is constant under suitable hashing assumptions and a controlled load factor.

### 7.3 Pseudocode

    BUILD_HASH_TABLE(records)
        CREATE an empty hash_table

        FOR each record IN records
            hash_table[record.registration_number] = record

        RETURN hash_table

    HASH_SEARCH(hash_table, target)
        IF target exists in hash_table
            RETURN hash_table[target]

        RETURN NOT_FOUND

### 7.4 Preprocessing Requirement

The hash table must be constructed from the student records. Building the table takes expected O(n) time and requires O(n) additional space.

### 7.5 Complexity

- Expected lookup time: O(1)
- Worst-case lookup time: O(n) under extreme collisions.
- Expected construction time: O(n)
- Auxiliary space: O(n) for the hash table.

### 7.6 Advantages

- Provides expected constant-time exact-match lookup.
- Suitable for frequent searches.
- Does not require registration numbers to be stored in sorted order.

### 7.7 Limitations

- Requires additional memory.
- Hash collisions can reduce performance.
- Does not naturally maintain records in sorted order.
- Duplicate registration numbers must be handled explicitly to avoid unintentionally overwriting records.

## 8. Comparative Overview

| Feature | Linear Search | Recursive Binary Search | Hash Table Search |
|---|---|---|---|
| Design strategy | Iterative | Divide and conquer | Hash-based lookup |
| Sorted data required | No | Yes | No |
| Preprocessing | None | Sorting if needed | Build hash table |
| Expected search time | O(n) | O(log n) | O(1) |
| Worst-case search time | O(n) | O(log n) | O(n) |
| Auxiliary space | O(1) | O(log n) | O(n) |
| Best use case | Small or unsorted datasets | Sorted records | Frequent exact-match lookups |

## 9. Initial Design Assessment

Linear Search is appropriate when the dataset is small or unsorted and searches are infrequent. Recursive Binary Search is suitable when records are maintained in sorted order and fast searching is required. Hash Table Search is a strong candidate when frequent exact-match searches are performed and sufficient memory is available.

The final choice must also consider preprocessing costs, daily record updates, memory requirements, and experimental results.

## 10. Conclusion

Three distinct searching algorithms have been designed for the student record system. Their working principles, pseudocode, preprocessing requirements, advantages, limitations, and initial complexity estimates have been documented.

This design provides the foundation for the remaining tasks, which will mathematically analyze the algorithms, examine their best-, average-, and worst-case behavior, implement them in Python, measure their performance, and recommend a suitable approach for the university database.
