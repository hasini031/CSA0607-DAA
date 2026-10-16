# Task 7 – Recurrence Solution

## 1. Aim
To solve the recurrence relation for Recursive Binary Search and determine its asymptotic time complexity.

## 2. Given Recurrence

T(n) = T(n/2) + c

T(1) = d

Here, c and d are constants.

## 3. Step-by-Step Expansion

First expansion:

T(n) = T(n/2) + c

Second expansion:

T(n) = T(n/4) + 2c

Third expansion:

T(n) = T(n/8) + 3c

After k expansions:

T(n) = T(n/2^k) + kc

## 4. Finding the Number of Levels

The recurrence stops when the input size becomes 1.

n / 2^k = 1

Therefore:

n = 2^k

Taking logarithms to base 2:

k = log₂(n)

## 5. Substitution

Substitute k = log₂(n) into the expanded recurrence:

T(n) = T(1) + c log₂(n)

Since T(1) = d:

T(n) = d + c log₂(n)

The constants do not change the asymptotic growth rate.

Therefore:

T(n) = Θ(log n)

## 6. Result

The worst-case time complexity of Recursive Binary Search is Θ(log n).

Its auxiliary recursion-stack space complexity is O(log n).

## 7. Conclusion
The step-by-step expansion demonstrates that the number of recursive calls grows logarithmically because the search range is repeatedly halved. This makes Binary Search efficient for large sorted datasets.
