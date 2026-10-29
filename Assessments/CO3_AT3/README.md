# CO3_AT3 – Divide-and-Conquer Engine of a Retail Data Analytics Platform

## 1. Project Overview

This repository contains the solutions for **CO3 – Assessment Tool 3: Case Study – Divide-and-Conquer Engine of a Retail Data Analytics Platform** for the course **CSA06 – Design and Analysis of Algorithms**.

The case study is based on **KartIQ**, a retail data analytics platform that processes millions of orders, maintains a live seller leaderboard, supports order lookups, and calculates product recommendation scores.

The objective is to apply divide-and-conquer algorithms to improve computational efficiency, analyze algorithm performance, and justify the design decisions using theoretical and experimental results.

## 2. Objectives

- Understand the computational requirements of the KartIQ platform.
- Design and implement Merge Sort, Quick Sort, Binary Search, and Strassen's Matrix Multiplication.
- Prepare separate pseudocode and executable source code for each module.
- Demonstrate algorithm execution using sample datasets and intermediate steps.
- Formulate and solve recurrence relations.
- Calculate time and space complexities.
- Compare algorithmic performance using experimental results and graphs.
- Identify limitations, trade-offs, and possible optimizations.
- Propose a final algorithmic design for the retail analytics platform.

## 3. Modules

### Module 1 – Merge Sort for Nightly Order Consolidation

**Objective:** Sort orders by timestamp while preserving the original arrival order of orders with equal timestamps.

**Key tasks:**
- Explain the divide, conquer, and combine steps.
- Trace Merge Sort using the sample order dataset.
- Demonstrate stability for equal timestamps.
- Formulate and solve the recurrence relation.
- Estimate comparisons for 10,000,000 orders.
- Analyze memory requirements and external sorting for datasets that do not fit in RAM.

**Expected complexity:** Time – O(n log n); Auxiliary space – O(n) for a standard array-based implementation.

### Module 2 – Quick Sort for the Live Seller Leaderboard

**Objective:** Sort seller scores efficiently when the scores are frequently updated and are often nearly sorted.

**Key tasks:**
- Trace a partition step using the sample scores.
- Explain the limitations of selecting the first element as the pivot.
- Formulate and solve the best-case and worst-case recurrence relations.
- Estimate comparisons for 100,000 sellers.
- Propose and justify an improved pivot-selection strategy.

**Expected complexity:** Average and best case – O(n log n); Worst case – O(n²).

### Module 3 – Binary Search for Order Lookup

**Objective:** Search for an order by timestamp in the sorted order list and return the first matching order when multiple orders share the same timestamp.

**Key tasks:**
- Explain why sorted data is required.
- Formulate and solve the recurrence relation.
- Calculate the maximum comparisons for 10,000,000 orders.
- Modify Binary Search to return the first occurrence of a timestamp.
- Test successful and unsuccessful searches.

**Expected complexity:** Time – O(log n); Auxiliary space – O(1) for an iterative implementation.

### Module 4 – Strassen's Matrix Multiplication for Recommendation Scores

**Objective:** Compute recommendation scores by multiplying the segment-feature preference matrix A with the feature-product matrix B.

**Key tasks:**
- Explain the seven Strassen products.
- Write the matrix reconstruction formulas.
- Verify the method using the supplied 2 × 2 matrices.
- Formulate and solve the recurrence relation.
- Compare scalar multiplication counts for n = 1,024 against conventional matrix multiplication.
- Explain practical limitations and propose a hybrid multiplication approach.

**Expected complexity:** Time – O(n^log₂7), approximately O(n^2.807); the practical performance depends on implementation and matrix size.

## 4. Repository Structure

```text
CO3_AT3/
│
├── Module_1_Merge_Sort/
│   ├── Pseudocode/
│   ├── Source_Code/
│   └── Report/
│
├── Module_2_Quick_Sort/
│   ├── Pseudocode/
│   ├── Source_Code/
│   └── Report/
│
├── Module_3_Binary_Search/
│   ├── Pseudocode/
│   ├── Source_Code/
│   └── Report/
│
├── Module_4_Strassen_Matrix_Multiplication/
│   ├── Pseudocode/
│   ├── Source_Code/
│   └── Report/
│
├── Final_Design_and_Analysis/
│
├── Supporting_Files/
│
└── README.md
```

Each module contains its pseudocode, source code, and report. The reports include algorithm explanations, execution traces, test cases, complexity analysis, calculations, and experimental results. Store output screenshots and other supporting materials in the appropriate report or supporting folders.

## 5. Technologies Used

- **Programming language:** Python
- **Development environment:** Google Colab or a local Python environment
- **Version control:** Git and GitHub
- **Documentation:** Markdown and Microsoft Word
- **Visualization:** Matplotlib, where required

## 6. Testing and Experimental Analysis

Each algorithm will be tested using the sample datasets specified in the assessment.

The evaluation includes:

- Correctness of the output
- Intermediate execution traces
- Number of comparisons and arithmetic operations
- Theoretical time and space complexity
- Execution time for different input sizes
- Graphical performance comparisons
- Limitations and optimization opportunities

All experimental results and screenshots should correspond to the actual execution of the submitted programs.

## 7. Final Design and Analysis

The final design compares the four algorithms and justifies the selected approach for each KartIQ module.

The analysis considers:

- Computational efficiency
- Additional memory requirements
- Worst-case behaviour
- Data ordering and algorithm preconditions
- Implementation complexity
- Performance trade-offs
- Conditions under which an alternative algorithm may be preferable

## 8. How to Run the Programs

1. Open the required module folder.
2. Navigate to its `Source_Code` directory.
3. Open the Python file in Google Colab or a local Python environment.
4. Execute the program using the supplied sample dataset.
5. Verify the output and intermediate steps.
6. Capture screenshots of the actual program output.
7. Include the results and observations in the corresponding report.

## 9. Conclusion

This assessment demonstrates the application of divide-and-conquer techniques to real-world data analytics problems. By implementing and analyzing Merge Sort, Quick Sort, Binary Search, and Strassen's Matrix Multiplication, the project evaluates algorithmic efficiency, memory usage, worst-case behaviour, and practical optimization strategies.

The final design aims to provide a reasoned and efficient algorithmic foundation for order consolidation, seller ranking, order lookup, and recommendation-score computation in the KartIQ platform.

---

**Course Code:** CSA06 – Design and Analysis of Algorithms  
**Assessment:** CO3 – Assessment Tool 3  
**Case Study:** Divide-and-Conquer Engine of a Retail Data Analytics Platform  
**Student Name:** Konduru Hasini  
**Department:** Computer Science and Engineering  
**Submission Mode:** Individual
