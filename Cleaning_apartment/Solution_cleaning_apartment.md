# Cleaning the Apartment Problem

## Problem Description

### Problem Introduction

In this problem, the task is to determine the feasibility of cleaning an apartment after a party while leaving no evidence of the event. To achieve this, you must clean all the rooms in a specific sequence. Once you finish cleaning a room, you can't return to it to avoid accidentally messing it up. The challenge is to find a path that allows you to visit each room exactly once and clean it, moving only to neighboring rooms. This problem can be reduced to the well-known Hamiltonian Path problem, and the goal is to devise an efficient algorithm to transform it into a SAT (Boolean satisfiability) problem.

### Problem Description

You've recently hosted a large party at your parents' house, and they will return home tomorrow. The task is not only to clean the apartment thoroughly but also to ensure there are no traces of the party. Cleaning must be carried out in a specific order where you move from room to room, visiting each room precisely once. Once you've cleaned a room, you can't go back to it. You can only move to rooms that share a corridor. The primary objective is to determine whether it's possible to achieve this.

This problem can be reduced to the classic Hamiltonian Path problem, which involves finding a path that visits each vertex (room) exactly once in a graph. The rooms represent the vertices of the graph, and the corridors between neighboring rooms represent the edges. The Hamiltonian Path problem is NP-complete, making it computationally challenging to solve directly. To overcome this, you need to convert it into a SAT problem so that a SAT-solver can efficiently handle it.

### Input Format

The input begins with two integers, 𝑛 and 𝑚, indicating the number of rooms and the number of corridors connecting these rooms, respectively. Subsequently, each of the following 𝑚 lines describes a corridor with two integers, 𝑢 and 𝑣, signifying a corridor going from room 𝑢 to room 𝑣. These corridors are bidirectional. Corridors can be listed multiple times, and it's possible to have both a corridor from 𝑢 to 𝑣 and from 𝑣 to 𝑢. No corridor connects a room to itself.

### Constraints

- 1 ≤ 𝑛 ≤ 30
- 0 ≤ 𝑚 ≤ 𝑛(𝑛−1)/2
- 1 ≤ 𝑢, 𝑣 ≤ 𝑛

### Output Format

You must generate a boolean formula in CNF (Conjunctive Normal Form) with specific formatting. The output must indicate whether it's possible to clean all the rooms as required or not. The total number of variables used in each clause should not exceed 120,000.

1. Output 𝐶 (the number of clauses in the formula) and 𝑉 (the number of variables) on the first line.
2. On each of the following 𝐶 lines, output the description of a single clause in the form (𝑥4 𝑂𝑅 𝑥1 𝑂𝑅 𝑥8), where 𝑘 is the number of terms in the clause, e.g., 𝑘 = 3 for 𝑥4, 𝑥1, and 𝑥8.
3. Output each term as an integer number, using positive integers to represent variables 𝑥1, 𝑥2, ... 𝑥𝑉, and negative integers to represent negations of these variables (e.g., −1, −2, ... −𝑉).
4. End each line with 0 to indicate the end of the clause.
5. Ensure that the total number of non-zero integers in the 𝐶 lines describing the clauses does not exceed 120,000.

Examples below provide further clarification on the output format. If multiple valid formulas can satisfy these requirements, any of them can be output.

# Cleaning the Apartment Solution

## Algorithm Overview

I used the following algorithms and techniques to tackle the Cleaning the Apartment problem:

### Constraint Generation

I generate constraints that represent the conditions and requirements of the problem in CNF. These constraints ensure that the cleaning can be done according to the specified rules.

### Reduction to SAT

The core of the algorithm involves reducing the problem of finding a valid cleaning sequence to a SAT problem. I use Boolean variables to represent the presence of cleaning in each room at each position, and then define constraints to ensure that rooms are cleaned in a specific order while respecting adjacency constraints.

### Exactly One Constraint

I create constraints to ensure that exactly one room is in a particular position. This satisfies the requirement that each room should be visited exactly once.

### Adjacency Constraints

I enforce constraints to ensure that rooms connected by corridors are cleaned in a specific order. This accounts for the requirement that I can only move to neighboring rooms.

## Code Structure

The structure of my code is as follows:

1. **Input Reading**: The code starts by reading input, which includes the number of rooms, the number of corridors, and the list of corridor connections.

2. **Data Initialization**: I initialize data structures, such as the list of clauses, positions (room positions), and an adjacency list to represent the relationships between rooms.

3. **Adjacency List Creation**: The code creates an adjacency list to represent the connections between rooms based on the input.

4. **Variable Calculation**: I calculate variable numbers based on room numbers and positions, mapping the problem to SAT variables.

5. **Constraint Generation**: The core part of the code generates constraints for room positions and adjacency. These constraints are added to the list of clauses.

6. **CNF Clause Generation**: I generate CNF clauses based on the constraints and problem requirements. The generated clauses are ready for output in CNF format.

7. **Output Generation**: Finally, the code outputs the number of variables and clauses, followed by the generated CNF clauses, in the specified format.

This structured approach to problem-solving involves reducing the problem to SAT and then efficiently generating constraints and CNF clauses to represent the problem's constraints and requirements. This allows SAT solvers to find a solution to the Cleaning the Apartment problem.

## Getting Started

To run the Cleaning the Apartment solver, follow these steps:

1. Provide the input parameters, including the number of rooms and corridor connections.
2. Execute the code to generate the CNF representation of the problem.
3. Use a SAT solver to find a solution based on the generated CNF clauses.
