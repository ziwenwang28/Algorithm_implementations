# python3

import itertools

import itertools

def read_input():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    return n, edges

def initialize_data(n):
    clauses = []
    positions = range(1, n + 1)
    adj = [[] for _ in range(n)]
    return clauses, positions, adj

def create_adjacency_list(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    return adj

def calculate_variable_number(n, i, j):
    return n * i + j

def add_exactly_one_of_constraint(clauses, literals):
    clauses.append(literals)
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

def generate_room_position_constraints(clauses, n, positions):
    for i in range(n):
        add_exactly_one_of_constraint(clauses, [calculate_variable_number(n, i, j) for j in positions])

def generate_adjacency_constraints(clauses, n, positions, adj):
    for j in positions:
        add_exactly_one_of_constraint(clauses, [calculate_variable_number(n, i, j) for i in range(n)])

    for j in positions[:-1]:
        for i, nodes in enumerate(adj):
            literals = [-calculate_variable_number(n, i, j)] + [calculate_variable_number(n, n, j + 1) for n in nodes]
            clauses.append(literals)

def generate_cnf_clauses(n, positions, adj):
    clauses = []
    generate_room_position_constraints(clauses, n, positions)
    generate_adjacency_constraints(clauses, n, positions, adj)
    return clauses

def main():
    n, edges = read_input()
    clauses, positions, adj = initialize_data(n)
    adj = create_adjacency_list(n, edges)
    clauses = generate_cnf_clauses(n, positions, adj)

    num_variables = n * n
    num_clauses = len(clauses)

    print(num_clauses, num_variables)
    for c in clauses:
        c.append(0)
        print(' '.join(map(str, c)))

if __name__ == "__main__":
    main()

