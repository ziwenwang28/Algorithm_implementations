# Party Planning Problem

## Problem Description

In this scenario, your task is to create and execute an efficient algorithm for arranging a party where you can invite the most entertaining individuals from your company. The key is to ensure that everyone can fully enjoy the event by avoiding inviting someone if their direct superior has also been invited.

### Task

You are in charge of planning a corporate event, a party. Your goal is to invite the most entertaining employees, each of whom has been assigned a "fun factor" to indicate their level of coolness. The higher the fun factor, the cooler the person. Your objective is to maximize the overall fun factor, which is the sum of the fun factors of all the invited individuals. However, you cannot invite everyone since it would create an uncomfortable situation if the direct boss of an invited person is also present. Your task is to determine the maximum possible total fun factor.

### Input Format

The first line contains an integer 𝑛, which represents the number of individuals in the company. The next line consists of 𝑛 numbers 𝑓𝑖, which correspond to the fun factors of each of the 𝑛 individuals. Each of the subsequent 𝑛−1 lines describes the hierarchical structure within the company. Everyone, except for the CEO, has a single direct boss. There are no cyclical relationships: no one can be the boss of their own boss, creating a regular tree-like hierarchical structure. Each of the 𝑛−1 lines contains two integers 𝑢 and 𝑣, and it is known that either 𝑢 is the boss of 𝑣 or vice versa (the specific designation of "boss" is not necessary, but you can only invite one of them or none of them).

### Constraints

- 1 ≤ 𝑛 ≤ 100,000
- 1 ≤ 𝑓𝑖 ≤ 1,000
- 1 ≤ 𝑢, 𝑣 ≤ 𝑛
- 𝑢 ≠ 𝑣

### Output Format

Provide the maximum possible total fun factor of the party, which is the sum of the fun factors of all the invited individuals.

# Maximum Independent Set in a Tree

## Overview

This Python code aims to find the maximum independent set in a tree. The algorithm used here works by recursively exploring the tree and considering whether to include or exclude each vertex in the independent set. The dynamic programming table (`dp`) stores the results to avoid redundant computations. The final result is the maximum of the independent set size with or without the root vertex (vertex 0).

## Solution Code Structure

### Vertex Class

- I define a `Vertex` class to represent each node in the tree.
- Each `Vertex` object stores the weight of the node and a list of its children.

### Reading the Tree

- I implement the `read_tree()` function:
  - Read the number of vertices.
  - Create a list to hold `Vertex` objects, initializing them with zero weights.
  - Read the weights of each vertex and assign them to the corresponding `Vertex` objects.
  - Read the connections between vertices and construct the tree structure by adding child information to each `Vertex` object.

### Computing the Maximum Independent Set

- I implement the `compute_max_independent_set(tree)` function:
  - Define an inner function called `compute` that recursively computes the maximum independent set.
  - Initialize a dynamic programming table (`dp`) to store results.
  - Recursively compute the maximum independent set size for each vertex, considering two cases:
    - Including the current vertex.
    - Excluding the current vertex.
  - Store and return the maximum of these two cases for each vertex.
  - The computation starts from the root of the tree (vertex 0).

### Main Execution

- Check if the script is executed as the main program using `if __name__ == "__main__":`.

- Read the tree structure and weights using the `read_tree()` function.

- Compute the maximum independent set size using the `compute_max_independent_set(tree)` function.

- Print the maximum independent set size.
