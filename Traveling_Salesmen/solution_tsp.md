# Traveling Salesman Problem (TSP) Solver

## Problem Description

Develop an algorithm to tackle the Traveling Salesman Problem (TSP), a classic optimization challenge faced by traveling salespeople. The problem can be summarized as follows:

Every traveling salesperson starts from their home, travels to various cities to sell their goods, and completes their journey by returning home. The goal is to minimize the total travel distance by finding an optimal visitation order for all cities, thus minimizing the sum of distances traveled when moving from one city to another.

Write an algorithm to solve the TSP, which is also known as minimizing the length of a Hamiltonian cycle in a graph. Mathematically, the problem is formulated as follows:

minimize: ∑
i∈0...n−1
dist(vi, vi+1) + dist(vn, v0)

subject to:

- vi are a permutation of N

In this variant of the TSP, we assume that the salesperson can travel directly in a straight line from one point to another, as if traveling by helicopter.

## Data Format Specification

The input data is formatted as follows:

### Input Format

- The first line contains a single number, |N|, representing the number of locations.
- This is followed by |N| lines, each containing two values, x and y, representing the coordinates of a location.

The output data is formatted as follows:

### Output Format

- The first line contains two values, obj and opt. 
  - obj represents the length of the Hamiltonian cycle (i.e., the objective value) as a real number.
  - opt should be 1 if your algorithm has proven optimality and 0 otherwise.
- The next line consists of a list of n values in N, one for each of the vi variables, encoding the solution.

# Traveling Salesman Problem Solver

## Introduction

The Traveling Salesman Problem (TSP) is a classic optimization challenge where a salesperson needs to find the shortest possible route that allows them to visit a given set of cities exactly once and return to their starting point. Solving the TSP efficiently has practical applications in logistics, transportation, and manufacturing.

This repository provides a Python-based solution to the TSP using a combination of heuristics and optimization techniques.

## Problem Statement

The TSP is about finding the optimal route for visiting a set of cities, with the objective of minimizing the total distance traveled or cost incurred. The challenges of the TSP include its NP-hard nature, which makes finding an optimal solution computationally difficult, especially for large instances.

## Algorithms Used

1. **Greedy Heuristic**:
   - A greedy heuristic is used to construct the initial tour.
   - It starts with the first city and iteratively selects the nearest neighbor until all cities are visited.
   
2. **2-Opt Local Search**:
   - The primary algorithm is the 2-opt local search.
   - It explores pairwise swaps of edges in the tour to improve its quality.
   - The search continues until no further improvement can be made.

## Potential Improvements

1. **Advanced Heuristics**:
   - Incorporate more advanced heuristics for initializing the tour.
   - Examples include nearest neighbor with randomization or the Christofides algorithm for smaller datasets.

2. **Hybrid Approaches**:
   - Explore hybrid algorithms that combine different heuristic and optimization techniques to find high-quality solutions.

3. **Performance Profiling**:
   - Profile the code to identify performance bottlenecks and optimize critical sections for efficiency.

## Usage

1. Clone this repository to your local machine.
2. Execute the `solve_it` function by providing an input file as an argument.
3. The solution will be printed to the standard output.

For example:

```shell
python solver.py ./data/(dataset of choice, for example, tsp_51_1)