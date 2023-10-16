# School Bus Routing Optimization

## Problem Description

### Introduction

In this problem, the objective is to determine the most efficient route for a school bus to start from the depot, pick up all the children from their homes, transport them to school, and return to the depot.

### Problem Details

A school bus needs to start from the depot early in the morning, pick up all the children from their homes in some order, get them all to school, and return to the depot. You are aware of the time it takes to travel from the depot to each home, from each home to each other home, from each home to the school, and from the school to the depot. The challenge is to define the order in which to visit children's homes to minimize the total time spent on the route.

This problem is a variation of the Traveling Salesman Problem, a classical NP-complete problem. Given a graph with weighted edges, the task is to find the shortest cycle that visits each vertex exactly once. In this context, the vertices represent children's homes, the school, and the depot.

### Input Format

- The first line contains two integers, 'n' and 'm,' representing the number of vertices and edges in the graph. The vertices are numbered from 1 through 'n.'
- The next 'm' lines each contain three integers: 'u,' 'v,' and 't,' representing an edge in the graph. This edge connects vertices 'u' and 'v,' and it takes 't' time to travel from 'u' to 'v.' These edges are bidirectional, meaning you can travel from 'u' to 'v' or from 'v' to 'u' in the same amount of time.
- There are no edges connecting a vertex to itself, and no two vertices are connected by more than one edge.

### Constraints

- 2 ≤ 'n' ≤ 17
- 1 ≤ 'm' ≤ n(n-1)/2
- 1 ≤ 'u,' 'v' ≤ 'n,' where 'u' ≠ 'v'
- 1 ≤ 't' ≤ 10^9

### Output Format

If it is possible to start at a specific vertex, visit each other vertex exactly once in a particular order using graph edges, and return to the starting vertex, the output should include:

- The first line should contain the minimum possible time to complete the circular route, visiting all vertices exactly once, except for the first vertex (visited at the beginning and end).
- The second line should specify the order in which you should visit the vertices to achieve the minimum time on the route. The numbers from 1 through 'n' should be listed in the order corresponding to the vertex visitation. Do not include the starting vertex twice. However, account for the time to return from the last vertex to the starting vertex.
If there are multiple solutions, you can output any one of them. If there is no feasible circular route, simply output -1 on a single line. For 'n = 2,' it is considered a valid circular route to go from one vertex to another through an edge and then return back through the same edge.

# Traveling Salesman Problem Solver

## Overview

This Python program aims to solve the Traveling Salesman Problem (TSP) using a variation of the Held-Karp algorithm. The TSP involves finding the shortest possible route for a traveling salesman to visit a given set of cities (vertices) and return to the starting city. In this description, we use the first-person perspective, with "I" and "me" representing the traveling salesman.

## Algorithm: Held-Karp Algorithm

The algorithm used in this code is a variation of the Held-Karp algorithm, a dynamic programming approach to solve the TSP.

1. **Initialization**:
   - I initialize a dynamic programming table, represented as a 2D array, to store intermediate results. Each entry `C[mask][k]` in the table represents the minimum distance for me to reach vertex `k` while visiting all vertices in the subset `mask` exactly once.

2. **Base Cases**:
   - For the Held-Karp algorithm, base cases are set for all subsets of size 1 (individual vertices). The minimum distance for me to reach each vertex directly from the depot is computed and stored in the dynamic programming table.

3. **Iteration over Subsets**:
   - I iterate over all non-empty subsets of vertices, starting from subsets of size 2 and gradually building larger subsets.
   - For each subset `S` of size greater than 1, I calculate the minimum distance for me to reach vertex `k` within that subset. This is done by considering all possible previous vertices `m` within `S`.

4. **Backtracking to Reconstruct the Optimal Tour**:
   - After filling the dynamic programming table with optimal distances, I backtrack to reconstruct the optimal tour. This involves identifying the best final vertex (usually the depot) and finding the entire tour.

5. **Final Output**:
   - The algorithm returns the minimum distance of the optimal tour and the order of vertices in the tour for me.

## Structure of the Code

- The code is organized into classes and functions for modularity and clarity.
- A `Node` class is used to represent individual nodes in the dynamic programming table, storing the minimum distance and parent information.
- The `TSP` class encapsulates the entire algorithm, with methods for initialization, computing the optimal tour, generating combinations of visited vertices, and backtracking to reconstruct the tour.
- The `read_data` function reads input, including the number of vertices and edge information.
- The `print_answer` function prints the results, including the total length of the optimal tour and the order of vertices in the tour.

## Usage

To use this code, follow these steps:

1. Provide input by specifying the number of vertices and edge weights in the specified format.
2. Run the code, and it will compute the optimal tour for the traveling salesman.
3. The code will print the total length of the optimal tour and the order of vertices in the tour.
