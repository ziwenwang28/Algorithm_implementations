# Import the sys module, although it's not used in this code
import sys

# Create a Vertex class to represent each node in the tree
class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []

# Function to read the tree, its structure, and weights
def read_tree():
    vertices_count = int(input())  # Read the number of vertices
    tree = [Vertex(0) for _ in range(vertices_count)]  # Create a list to hold Vertex objects

    weights = list(map(int, input().split()))  # Read the weights of each vertex
    for i in range(vertices_count):
        tree[i].weight = weights[i]  # Assign weights to each Vertex object

    for i in range(1, vertices_count):
        from_, to = map(int, input().split())  # Read the connections in the tree
        tree[from_ - 1].children.append(to - 1)  # Add child information to each Vertex
        tree[to - 1].children.append(from_ - 1)

    return tree

# Function to compute the maximum independent set in the tree
def compute_max_independent_set(tree):
    def compute(vertex, parent, dp):
        if dp[vertex][0] != -1:
            return dp[vertex][0]

        independent_set_size_with_current = tree[vertex].weight
        for child in tree[vertex].children:
            if child != parent:
                independent_set_size_with_current += compute(child, vertex, dp)

        independent_set_size_without_current = 0
        for child in tree[vertex].children:
            if child != parent:
                independent_set_size_without_current += compute(child, vertex, dp)

        dp[vertex][0] = max(independent_set_size_with_current, independent_set_size_without_current)
        return dp[vertex][0]

    size = len(tree)
    if size == 0:
        return 0

    dp = [[-1, 0] for _ in range(size)]  # Create a dynamic programming table
    # dp[vertex][0] -> including current vertex, dp[vertex][1] -> excluding current vertex

    return compute(0, -1, dp)  # Start the computation from the root (vertex 0)

if __name__ == "__main__":
    tree = read_tree()  # Read the tree structure and weights
    print(compute_max_independent_set(tree))  # Print the maximum independent set
