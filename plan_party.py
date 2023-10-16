#uses python3

import sys

class Vertex:
    def __init__(self, weight):
        self.weight = weight
        self.children = []

def read_tree():
    vertices_count = int(input())
    tree = [Vertex(0) for _ in range(vertices_count)]

    weights = list(map(int, input().split()))
    for i in range(vertices_count):
        tree[i].weight = weights[i]

    for i in range(1, vertices_count):
        from_, to = map(int, input().split())
        tree[from_ - 1].children.append(to - 1)
        tree[to - 1].children.append(from_ - 1)

    return tree

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

    dp = [[-1, 0] for _ in range(size)]  # dp[vertex][0] -> including current vertex, dp[vertex][1] -> excluding current vertex

    return compute(0, -1, dp)

if __name__ == "__main__":
    tree = read_tree()
    print(compute_max_independent_set(tree))
