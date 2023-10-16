# Crew Assignment for Airline Flights

## Problem Description

In this problem, the goal is to efficiently assign airline crews to various flights using an algorithm that finds the maximum matching in a bipartite graph.

### Task

An airline company offers a range of flights, and there is a set of crews available to work on these flights. However, due to different departure cities and times, not all crews can work on every flight. The task is to determine crew assignments for as many flights as possible, while ensuring each flight is staffed with a compatible crew.

### Input Format

The input consists of the following:
- The first line contains two integers, 𝑛 and 𝑚, representing the number of flights and the number of available crews, respectively.
- The next 𝑛 lines contain 𝑚 binary integers (0 or 1). If the 𝑗-th integer in the 𝑖-th line is 1, it indicates that crew member 𝑗 can work on flight 𝑖, while 0 means they cannot.

### Constraints

1 ≤ 𝑛, 𝑚 ≤ 100

### Output Format

The output should consist of 𝑛 integers, each representing the 1-based index of the crew assigned to a specific flight. If no crew is assigned to a flight, output -1 as the corresponding crew index. Positive indices in the output must be between 1 and 𝑚, and they should be unique. You can include any number of -1's in the output. If there are multiple assignments with the maximum possible number of flights having a crew assigned, you can choose any of them.


## How to Use

1. Provide input data in the specified format.
2. Use the algorithm to find crew assignments for flights.
3. Output the results in the specified format.

## Code Overview

### `write_response(matching)`
This function is responsible for formatting and printing the output. The `matching` list contains the assigned crews for each flight, and this function ensures the output is in the correct format, accounting for 1-based indexing.

### `MaxMatching` Class
I encapsulated the operations related to finding the maximum matching in a bipartite graph within the `MaxMatching` class.

#### Constructor
In the constructor of the `MaxMatching` class, I read the input data, which includes the number of flights and crews, as well as the adjacency matrix describing the compatibility between crews and flights.

#### `bfs` Function
This function performs a modified Breadth-First Search (BFS) to identify augmenting paths in the graph. The primary goal is to find augmenting paths that can increase the matching between crews and flights.

#### `find_matching` Method
The `find_matching` method initializes essential data structures and iteratively calls the `bfs` function to find augmenting paths and update the matching until no more augmenting paths can be found. It effectively determines the assignments of crews to flights based on their compatibility, optimizing the crew scheduling process.

#### `solve` Method
In the `solve` method, I call the `find_matching` method to find the maximum matching in the bipartite graph, and then I call the `write_response` function to print the results in the desired format.

## Usage

To use this code to solve the crew assignment problem for airline flights, follow these steps:
1. Provide the input data in the specified format.
2. Create an instance of the `MaxMatching` class.
3. Call the `solve` method on the created instance.
4. The code will find the maximum matching and output the crew assignments for each flight.
