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

# Knapsack Problem Solver

## My code implementation
Dynamic programming and a greedy approach.

## Algorithms

### Dynamic Programming Solver (`dynamic_programming_solver`)

- **Algorithm Used:** This solver employs dynamic programming to find the optimal solution. It creates a 2D table (`dp`) to store the maximum value achievable for each combination of items and knapsack capacity.

- **Complexity:** Time complexity is O(item_count * capacity), and space complexity is also O(item_count * capacity).

### Greedy Solver (`greedy_solver`)

- **Algorithm Used:** This solver adopts a greedy strategy by sorting items based on their value-to-weight ratio in descending order. It iterates through the sorted list, selecting items as long as they fit within the knapsack's capacity.

- **Complexity:** The sorting step results in a time complexity of O(item_count * log(item_count)).

## Usage

1. **Input Format:** The input is provided as a text file. The first line contains the number of items and the knapsack's capacity. Subsequent lines list the value and weight of each item.

2. **Command Line Interface:** You can run the script from the command line, providing the input file as an argument. The script reads the input data, determines the appropriate solver based on the item count, and prints the solution in the specified output format.

3. **Output Format:** The solution is presented in two lines. The first line contains the total value and an optimality indicator (1 for optimal, 0 for not). The second line includes binary values indicating which items are selected (1) or not (0).

## Benefits

- Provides a choice between dynamic programming for small instances and a faster greedy approach for larger instances.
- Uses namedtuples to organize item data, improving code readability.

## Possible Improvements

1. **Hybrid Approach:** Consider implementing a hybrid approach that combines dynamic programming and a greedy algorithm for the best of both worlds.

2. **Advanced Heuristics:** Investigate advanced heuristics and metaheuristic algorithms to improve the accuracy of the greedy approach for larger instances.

3. **Handle Edge Cases:** Address edge cases and unusual input scenarios to enhance code robustness.

## Usage

1. Clone this repository to your local machine.
2. Execute the `solve_it` function by providing an input file as an argument.
3. The solution will be printed to the standard output.

For example:

```shell
python solver.py ./data/(dataset of choice, for example, ks_200_0)