from collections import defaultdict
from heapq import heappop, heappush

# Define the Edge class to represent edges in the flow network
class Edge:
    def __init__(self, u, v, capacity):
        self.u = u
        self.v = v
        self.capacity = capacity
        self.flow = 0

# Define the FlowGraph class to model the entire flow network
class FlowGraph:
    def __init__(self, n):
        # Initialize a list to store all edges
        self.edges = []
        # Initialize an adjacency list for graph representation
        self.graph = [[] for _ in range(n)]

    # Add both forward and backward edges to the graph
    def add_edge(self, from_, to, capacity):
        forward_edge = Edge(from_, to, capacity)
        backward_edge = Edge(to, from_, 0)
        # Store the index of the forward edge in the adjacency list
        self.graph[from_].append(len(self.edges))
        # Add the forward and backward edges to the list of edges
        self.edges.append(forward_edge)
        self.graph[to].append(len(self.edges))
        self.edges.append(backward_edge)

    # Return the number of vertices in the graph
    def size(self):
        return len(self.graph)

    # Return the indices of edges connected to a vertex
    def get_ids(self, from_):
        return self.graph[from_]

    # Return the edge object given its index
    def get_edge(self, id):
        return self.edges[id]

    # Update the flow through an edge and its corresponding backward edge
    def add_flow(self, id, flow):
        self.edges[id].flow += flow
        # Update the backward edge's flow to maintain conservation of flow
        self.edges[id ^ 1].flow -= flow

# Read input data and construct the flow network
def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = FlowGraph(vertex_count)
    for _ in range(edge_count):
        u, v, capacity = map(int, input().split())
        graph.add_edge(u - 1, v - 1, capacity)
    return graph

# Implement a modified BFS algorithm to find augmenting paths in the residual graph
def bfs(graph, from_, to):
    weight = float('inf')
    dist = defaultdict(lambda: float('inf'))
    dist[from_] = 0
    prev = defaultdict(lambda: (None, None))
    path = []
    nodes = []
    heappush(nodes, (0, from_))
    while nodes:
        _, curr_node = heappop(nodes)
        for id in graph.get_ids(curr_node):
            curr_edge = graph.get_edge(id)
            if float('inf') == dist[curr_edge.v] and curr_edge.capacity > 0:
                dist[curr_edge.v] = dist[curr_node] + 1
                prev[curr_edge.v] = (curr_node, id)
                heappush(nodes, (dist[curr_edge.v], curr_edge.v))
                if curr_edge.v == to:
                    while True:
                        path.insert(0, id)
                        curr_weight = graph.get_edge(id).capacity
                        weight = min(curr_weight, weight)
                        if curr_node == from_:
                            break
                        curr_node, id = prev[curr_node]
                    return True, path, weight
    return False, path, weight

# Calculate the maximum flow in the flow network using the Ford-Fulkerson algorithm
def max_flow(graph, from_, to):
    flow = 0
    while True:
        path_exists, path, weight = bfs(graph, from_, to)
        if not path_exists:
            return flow
        for id in path:
            graph.add_flow(id, weight)
        flow += weight

if __name__ == '__main__':
    graph = read_data()
    # Calculate and print the maximum flow from the source (0) to the target (size of the graph - 1)
    print(max_flow(graph, 0, graph.size() - 1))
