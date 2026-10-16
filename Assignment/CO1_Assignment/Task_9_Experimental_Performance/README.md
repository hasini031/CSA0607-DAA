# Task 9 – Experimental Performance Analysis

## 1. Aim
To measure the execution time of the three searching algorithms for different dataset sizes and evaluate their practical performance.

## 2. Experimental Environment
- Language: Python
- Platform: Google Colab
- Dataset: Synthetic student registration numbers
- Timer: Python time.perf_counter()

## 3. Dataset Sizes

The experiment will use the following input sizes:

- 1,000 records
- 10,000 records
- 100,000 records
- 1,000,000 records

## 4. Experimental Method

1. Generate unique registration numbers for each dataset.
2. Use the same dataset for all three algorithms.
3. Select the final record as the search target for a worst-case Linear Search test.
4. Measure Linear Search execution time.
5. Measure Recursive Binary Search execution time on sorted records.
6. Measure hash-table construction time separately.
7. Measure the time for an individual hash-table lookup.
8. Verify that all three approaches return the correct result.
9. Record the measured values in a performance table.

## 5. Performance Table

Fill this table using the actual output from Google Colab.

| Records | Linear Search (s) | Binary Search (s) | Hash Construction (s) | Hash Lookup (s) |
|---|---|---|---|---|
| 1,000 | To measure | To measure | To measure | To measure |
| 10,000 | To measure | To measure | To measure | To measure |
| 100,000 | To measure | To measure | To measure | To measure |
| 1,000,000 | To measure | To measure | To measure | To measure |

## 6. Expected Trends

- Linear Search should take longer as the dataset grows when the target is at the end.
- Binary Search should scale slowly because it repeatedly halves the search range.
- Hash-table construction time should increase with dataset size.
- Hash-table lookup should generally remain approximately constant under suitable conditions.

## 7. Graphical Representation
Create a graph comparing measured search times against dataset size. A logarithmic scale can help display the different growth rates. Report hash-table construction time separately from lookup time.

## 8. Important Observation
Execution time depends on the hardware, Python implementation, memory, and system load. Actual measurements must be obtained from Google Colab rather than copied from theoretical estimates.

## 9. Conclusion
Experimental measurements help demonstrate the practical differences between the searching algorithms. The results will support the final recommendation in Task 11.
