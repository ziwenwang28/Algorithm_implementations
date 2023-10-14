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