# Knapsack Problem Solver

## Description

This project tackles the Knapsack Problem, a classic optimization challenge where you have a knapsack with limited capacity and a set of items with varying values and weights. Your goal is to create an algorithm to maximize the total value of items placed in the knapsack without exceeding its weight limit.

## Assignment

Your task is to design an algorithm to solve the Knapsack Problem, which can be mathematically defined as follows:

**Maximize**:
∑ (i ∈ 0...n-1) vi * xi

**Subject to**:
∑ (i ∈ 0...n-1) wi * xi ≤ K

**Where**:
- `n`: Number of items
- `K`: Knapsack capacity
- `vi`: Value of item i
- `wi`: Weight of item i
- `xi`: Binary variable (0 or 1) indicating whether item i is selected

## Input Format

The input is structured as follows:
- The first line contains two integers: `n` (number of items) and `K` (knapsack capacity).
- The subsequent lines provide data for each item, with each line containing two integers: the item's value `vi` followed by its weight `wi`.


## Output Format

The output is presented in two lines:
- The first line contains two values: `obj` (total objective value) and `opt` (optimality indicator, 1 for optimal, 0 for not).
- The second line consists of a list of binary values `xi`, each corresponding to an item, indicating whether it is selected (1) or not (0).
