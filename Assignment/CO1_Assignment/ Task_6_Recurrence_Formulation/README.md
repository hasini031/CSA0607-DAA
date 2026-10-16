# Task 6 – Recurrence Formulation

## 1. Aim
To formulate the recurrence relation for Recursive Binary Search and identify its base case.

## 2. Introduction
A recurrence relation expresses the running time of a recursive algorithm in terms of the running time of a smaller input.

Recursive Binary Search divides the sorted search range into approximately two equal halves at each recursive call.

## 3. Recurrence Derivation

Let T(n) represent the worst-case running time for searching n records.

Each call performs:
- A constant amount of work to calculate the middle index.
- A constant amount of work to compare the target.
- One recursive call on at most half of the remaining records.

Therefore, the recurrence is:

T(n) = T(n/2) + c, for n > 1

where c is a constant.

The base case is:

T(1) = d

where d is a constant representing the work required when one record remains.

If the search range becomes empty, the algorithm returns NOT_FOUND.

## 4. Meaning of the Recurrence

- T(n): Time for the current input.
- T(n/2): Time for the smaller search range.
- c: Constant work in each call.
- T(1): Base-case cost.

## 5. Recursion Tree

At each level, the search range becomes approximately half its previous size.

| Level | Remaining records |
|---|---|
| 0 | n |
| 1 | n/2 |
| 2 | n/4 |
| 3 | n/8 |
| k | n/2^k |

The recursion stops when the range contains one record or becomes empty.

## 6. Conclusion
The recurrence for Recursive Binary Search is T(n) = T(n/2) + c, with a constant base case. It represents the repeated halving of the search range and will be solved in Task 7.
