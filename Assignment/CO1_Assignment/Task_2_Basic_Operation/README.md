# Task 2 – Identification of Basic Operations

## 1. Aim
To identify the basic operation performed by each searching algorithm and understand how the number of these operations changes with input size.

## 2. Definition of Basic Operation
A basic operation is the fundamental operation that contributes most directly to an algorithm's running time. For searching algorithms, it is generally a comparison or lookup used to determine whether the target registration number is present.

Let n represent the number of student records and let the target be the registration number to search for.

## 3. Linear Search

**Basic operation:** Comparison between the current registration number and the target.

**Location:** Inside the loop that examines each record.

**Operation count:**
- Best case: 1 comparison.
- Worst case: n comparisons.
- Average successful search, assuming every position is equally likely: (n + 1) / 2 comparisons.

**Explanation:** Linear Search checks records sequentially. The number of comparisons depends on the position of the target.

## 4. Recursive Binary Search

**Basic operation:** Comparison of the target registration number with the middle element.

**Location:** At each recursive call.

**Operation count:** The search range is approximately halved at each call. The number of comparisons is therefore proportional to log₂(n).

**Explanation:** Binary Search is applicable only when records are sorted by registration number.

## 5. Hash Table Search

**Basic operation:** Hash-table key lookup, including any key comparisons required to resolve collisions.

**Location:** During lookup using the target registration number.

**Operation count:** Expected constant-time lookup under suitable hashing assumptions. In the worst case, severe collisions may require examining many entries.

**Explanation:** The hash table uses a registration number as a key to retrieve the associated record.

## 6. Comparison

| Algorithm | Basic operation | Expected or worst-case growth |
|---|---|---|
| Linear Search | Registration-number comparison | Θ(n) worst case |
| Recursive Binary Search | Middle-element comparison | Θ(log n) worst case |
| Hash Table Search | Key lookup | Expected Θ(1); worst-case Θ(n) |

## 7. Conclusion
The basic operation provides a measurable way to analyze searching algorithms. Linear Search performs repeated comparisons, Binary Search reduces the search range, and Hash Table Search uses key-based lookup. These operation counts will be used in the following mathematical analysis.
