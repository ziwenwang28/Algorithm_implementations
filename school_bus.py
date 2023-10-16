# python3

import sys

INF = 10**9

class Node:
    def __init__(self):
        self.dist = INF
        self.parent = 0

def read_data():
    vertex_count, edge_count = map(int, input().split())
    graph = [[INF] * vertex_count for _ in range(vertex_count)]

    for _ in range(edge_count):
        from_, to, weight = map(int, input().split())
        from_ -= 1
        to -= 1
        graph[from_][to] = graph[to][from_] = weight

    return vertex_count, graph

class TSP:
    def __init__(self, complete_graph):
        self.N = len(complete_graph)
        self.C = [[Node() for _ in range(self.N)] for _ in range(1 << self.N)]
        self.dist = complete_graph

        for k in range(1, self.N):
            self.C[1 << k][k].dist = self.dist[0][k]

    def optimal_tour(self):
        for s in range(2, 1 << self.N):
            if s & (s - 1):
                S = self.combinations(s)
                bits = s * 2

                for k in S:
                    prev = bits ^ (1 << k)
                    min_node = Node()

                    for m in S:
                        if self.C[prev][m].dist + self.dist[m][k] < min_node.dist and k != m:
                            min_node.dist = self.C[prev][m].dist + self.dist[m][k]
                            min_node.parent = m

                    self.C[bits][k] = min_node

        return self.backtrack_optimal()

    def combinations(self, n):
        combs = []
        k = 0
        while n:
            if n & 1:
                combs.append(k)
            n >>= 1
            k += 1
        return combs

    def backtrack_optimal(self):
        min_node = Node()
        bits = (1 << self.N) - 2

        for k in range(1, self.N):
            if min_node.dist > self.C[bits][k].dist + self.dist[k][0]:
                min_node.dist = self.C[bits][k].dist + self.dist[k][0]
                min_node.parent = k

        if min_node.dist == INF:
            return -1, []

        optimal_tour = []
        optimal_tour.append(0)  

        for _ in range(self.N - 1):
            optimal_tour.append(min_node.parent)
            min_node.parent = self.C[bits][min_node.parent].parent
            bits ^= 1 << optimal_tour[-1]

        return min_node.dist, [v + 1 for v in optimal_tour]  

def print_answer(answer):
    print(answer[0])
    if answer[0] == -1:
        return
    for p in answer[1]:
        print(p, end=' ')
    print()

if __name__ == "__main__":
    vertex_count, graph = read_data()
    tsp = TSP(graph)
    print_answer(tsp.optimal_tour())
