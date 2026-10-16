
# Task 8 – Implementation and Testing

## 1. Aim
To implement Linear Search, Recursive Binary Search, and Hash Table Search in Python and verify their correctness using student registration numbers.

## 2. Tools Used
- Programming language: Python
- Execution environment: Google Colab
- Version control: GitHub

## 3. Implementation Description

### Linear Search
Examines registration numbers sequentially and returns the matching index or NOT_FOUND.

### Recursive Binary Search
Compares the target with the middle element and recursively searches the appropriate half. The input must be sorted.

### Hash Table Search
Builds a dictionary mapping registration numbers to records and retrieves the target using a key lookup.

## 4. Source Code Location

Save the Python implementation in:

Task_8_Implementation_Testing/Source_Code/search_benchmark.py

## 5. Test Cases

| Test | Input condition | Expected result |
|---|---|---|
| 1 | Target is the first record | Target found |
| 2 | Target is in the middle | Target found |
| 3 | Target is the last record | Target found |
| 4 | Target is absent | NOT_FOUND |
| 5 | Empty list | NOT_FOUND |

## 6. Testing Procedure

1. Open Google Colab and create a new notebook.
2. Copy the Python implementation into a code cell.
3. Run the code.
4. Check whether each algorithm returns the correct result.
5. Record execution times and operation counts.
6. Capture screenshots of the source code and actual output.
7. Save the screenshots in the corresponding Report folders.

## 7. Correctness Criteria
All algorithms must return the correct record when the target exists. When the target is absent, they must report NOT_FOUND. Binary Search must only be used on sorted data.

## 8. Complexity

- Linear Search: O(n) worst-case time, O(1) auxiliary space.
- Recursive Binary Search: O(log n) worst-case time, O(log n) recursion-stack space.
- Hash Table Search: expected O(1) lookup time, O(n) additional space.

## 9. Conclusion
The implementation will verify the algorithms' correctness and provide execution measurements for later experimental analysis. Actual code and output screenshots must be generated from a successful execution in Google Colab.
