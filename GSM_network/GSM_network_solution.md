# Problem Statement: Assign Frequencies to the Cells of a GSM Network

## Introduction

This problem involves addressing real-world challenges in assigning frequencies to transmitting towers within a GSM (Global System for Mobile Communications) network. We aim to simplify this problem by transforming it into a graph coloring problem, which can then be further reduced to an instance of the Boolean satisfiability problem (SAT).

## Problem Description

A GSM network comprises transmitting towers, each operating on distinct frequencies. These towers are typically located at the center of hexagonal cells. Mobile phones connect to these towers based on signal strength and other factors. To ensure efficient signal differentiation, neighboring towers must use different frequencies. The challenge is to allocate three different frequencies, as provided by the government, to these towers while adhering to the constraint of ensuring neighboring towers use different frequencies.

This problem is equivalent to the classical graph coloring problem: given a graph, we must assign three different colors (representing frequencies) to its vertices (representing cells) in such a way that any two vertices connected by an edge (representing neighboring cells) have different colors. Graph coloring is an NP-complete problem, and we aim to reduce it to an instance of the SAT problem. While SAT is also NP-complete, specialized SAT solvers can often provide efficient solutions in practice.

## Input Format

The input format is as follows:

- The first line of input contains two integers, `n` and `m`, representing the number of vertices (cells) and edges (connections) in the graph.
- The following `m` lines contain pairs of integers, `u` and `v`, representing vertices connected by an edge. It is guaranteed that a vertex cannot connect to itself.

### Constraints:

- 2 ≤ `n` ≤ 500
- 1 ≤ `m` ≤ 1000
- 1 ≤ `u`, `v` ≤ `n` (where `u` ≠ `v`)

## Output Format

The output format is as follows:

1. The number of clauses (`C`) and variables (`V`) in the CNF formula.
2. Each of the following `C` lines describes a single clause, expressed as `(x1 OR x2 OR ... OR xk 0)`, where `k` is the number of terms in the clause.
3. Variables `x1`, `x2`, ..., `xk` are represented as integer numbers. Variables are numbered from 1 to `V` for positive values and from -1 to -`V` for negations.
4. Each integer (other than the last '0') in each line must be a non-zero integer between -`V` and `V`.

### Constraints:

- 1 ≤ `C` ≤ 5000
- 1 ≤ `V` ≤ 3000

**Note:** If there are multiple valid formulas that meet the above requirements, any one of them can be output.

# GSM Network Frequencies Assignment

## Introduction

In this problem, I address the challenge of assigning frequencies to transmitting towers within a GSM (Global System for Mobile Communications) network. To simplify this real-world problem, I transform it into a graph coloring problem, which can then be reduced to an instance of the Boolean Satisfiability Problem (SAT).

## Problem Description

A GSM network consists of transmitting towers, each operating on distinct frequencies. These towers are typically located at the center of hexagonal cells. Mobile phones connect to these towers based on signal strength and other factors. To ensure efficient signal differentiation, neighboring towers must use different frequencies. The challenge is to allocate three different frequencies, as provided by the government, to these towers while adhering to the constraint of ensuring neighboring towers use different frequencies.

This problem is equivalent to the classical graph coloring problem: given a graph, I must assign three different colors (representing frequencies) to its vertices (representing cells) in such a way that any two vertices connected by an edge (representing neighboring cells) have different colors. Graph coloring is an NP-complete problem, and I aim to reduce it to an instance of the SAT problem. While SAT is also NP-complete, specialized SAT solvers can often provide efficient solutions in practice.

## Input Format

The input format is as follows:

- The first line of input contains two integers, `n` and `m`, representing the number of vertices (cells) and edges (connections) in the graph.
- The following `m` lines contain pairs of integers, `u` and `v`, representing vertices connected by an edge. It is guaranteed that a vertex cannot connect to itself.

### Constraints:

- 2 ≤ `n` ≤ 500
- 1 ≤ `m` ≤ 1000
- 1 ≤ `u`, `v` ≤ `n` (where `u` ≠ `v`)

## My solution for the GSM network problem.

I employ the following algorithm to reduce the problem to a SAT instance:

1. Initialize variables and read input values.
2. Generate clauses to ensure that each vertex is assigned one of the `K` colors (frequencies).
3. Generate clauses to ensure that adjacent vertices (connected by edges) do not have the same color.
4. Print the generated SAT formula in the required format.

### Code Structure

Here is the structure of my Python code:

1. **Input Reading:**
   - I read the number of vertices `n` and edges `m`, as well as the pairs of vertices connected by edges into the `edges` list.

2. **Initialization:**
   - I set the number of available colors (frequencies) `K` to 3.

3. **Generate SAT Formula:**
   - I have a function `generate_SAT_formula` that constructs the SAT formula based on the input graph.
   - It calculates the number of clauses `C`, variables `V`, and initializes a count variable `cnt`.
   - It creates clauses to ensure that each vertex is assigned one of the `K` colors, and adjacent vertices have different colors.
   - The generated clauses are stored in the `clauses` list.

4. **Print SAT Formula:**
   - I have a function `print_SAT_formula` to print the SAT formula in the required format.
   - It prints the number of clauses and variables, and then iterates through the list of clauses to print them in the specified format.

5. **Generate and Print SAT Formula:**
   - I call `generate_SAT_formula` to generate the SAT formula.
   - Then, I call `print_SAT_formula` to print the formula in the required format.

The overall structure of my code follows a modular approach. It first reads the input, then defines functions for generating and printing the SAT formula, and finally, it generates and prints the SAT formula using those functions. This code is designed to transform a real-world graph coloring problem into a SAT problem, which can be solved using SAT solvers to determine the feasibility of assigning frequencies to GSM network cells.

