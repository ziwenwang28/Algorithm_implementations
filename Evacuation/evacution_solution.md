# Evacuation Optimization Problem

## Problem Statement

### Problem Introduction

In this problem, you will apply an algorithm for finding the maximum flow in a network to determine how fast people can be evacuated from the given city.

### Problem Description

**Task**: A tornado is approaching the city, and we need to evacuate the people quickly. There are several roads outgoing from the city to the nearest cities and other roads going further. The goal is to evacuate everybody from the city to the capital, as it is the only other city which is able to accommodate that many newcomers. We need to evacuate everybody as fast as possible, and your task is to find out what is the maximum number of people that can be evacuated each hour given the capacities of all the roads.

**Input Format**: The input contains integers 𝑛 and 𝑚 — the number of cities and the number of roads respectively. Each of the next 𝑚 lines contains three integers 𝑢, 𝑣 and 𝑐 describing a particular road — start of the road, end of the road and the number of people that can be transported through this road in one hour. 𝑢 and 𝑣 are the 1-based indices of the corresponding cities.

The city from which people are evacuating is the city number 1, and the capital city is the city number 𝑛.

**Output Format**: Output a single integer — the maximum number of people that can be evacuated from the city number 1 each hour.

## Constraints

- 1 ≤ 𝑛 ≤ 100
- 0 ≤ 𝑚 ≤ 10,000
- 1 ≤ 𝑢, 𝑣 ≤ 𝑛
- 1 ≤ 𝑐 ≤ 10,000
- 𝑚 * EvacuatePerHour ≤ 2 * 10^8, where EvacuatePerHour is the maximum number of people that can be evacuated from the city each hour — the number which you need to output.

# Ford-Fulkerson Algorithm Implementation

## Edge Class

In this implementation, I've defined an `Edge` class to represent the edges within the flow network. Each edge object encapsulates information about the source vertex (`u`), target vertex (`v`), edge capacity, and the current flow through the edge. This class plays a crucial role in tracking the flow through each edge in the network.

## FlowGraph Class

I've utilized the `FlowGraph` class to comprehensively model the entire flow network. It features methods to add edges, retrieve edge information, and manage the flow. Some key aspects of this class include:

- Maintenance of a list called `self.edges` to store all edges in the graph, encompassing both forward and backward edges.
- Utilization of adjacency lists within `self.graph` to efficiently store indices of edges from the `self.edges` list.
- Distinction of forward edges at even indices and backward edges at odd indices within the `self.edges` list.

## add_edge Method

When adding an edge to the graph, I ensured the inclusion of both a forward edge (with a specified capacity) and a corresponding backward edge (with a capacity of 0). This dual-edge approach represents the concept of residual capacity in the network.

## bfs Method

I've implemented a modified Breadth-First Search (BFS) algorithm, tailored for identifying augmenting paths in the residual graph. This method serves the purpose of locating paths from the source vertex (`from_`) to the target vertex (`to`) and provides information about the path and its weight. Key features of this method include:

- A slightly altered BFS algorithm to accommodate the flow problem by returning both the path and the minimum weight (capacity) along that path.

## max_flow Method

The `max_flow` method serves as the core of the implementation, employing the Ford-Fulkerson algorithm to determine the maximum flow within the network. Highlights of this method include:

- The repetitive invocation of the `bfs` method to identify augmenting paths from the source to the target.
- Updates to the flow through the edges based on identified paths.
- Continuation of the process until no further augmenting paths can be found.
- The ultimate output of the maximum flow value.

## read_data Function

For the input data processing, I've included the `read_data` function. It is responsible for gathering essential information about the flow network, such as the number of vertices, the number of edges, and edge capacities. The function initializes a `FlowGraph` object and populates it with the provided data.

## Main Section

In the main section of the code, the input data is read, the flow graph is constructed, and the maximum flow from the source vertex (0) to the target vertex (size of the graph - 1) is calculated.
