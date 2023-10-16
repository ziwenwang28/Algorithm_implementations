# Import necessary libraries
import itertools

# Function to read input
def read_input():
    n, m = map(int, input().split())
    edges = [list(map(int, input().split())) for i in range(m)]
    return n, edges

# Initialize data structures for clauses, positions, and adjacency list
def initialize_data(n):
    clauses = []
    positions = range(1, n + 1)
    adj = [[] for _ in range(n)]
    return clauses, positions, adj

# Create an adjacency list from the given edges
def create_adjacency_list(n, edges):
    adj = [[] for _ in range(n)]
    for u, v in edges:
        u -= 1
        v -= 1
        adj[u].append(v)
        adj[v].append(u)
    return adj

# Calculate the variable number based on room number and position
def calculate_variable_number(n, i, j):
    return n * i + j

# Add a constraint that ensures exactly one of the given literals is true
def add_exactly_one_of_constraint(clauses, literals):
    clauses.append(literals)
    for pair in itertools.combinations(literals, 2):
        clauses.append([-l for l in pair])

# Generate constraints for room position (each room in one position)
def generate_room_position_constraints(clauses, n, positions):
    for i in range(n):
        add_exactly_one_of_constraint(clauses, [calculate_variable_number(n, i, j) for j in positions])

# Generate constraints for adjacent rooms (connected by a corridor)
def generate_adjacency_constraints(clauses, n, positions, adj):
    for j in positions:
        add_exactly_one_of_constraint(clauses, [calculate_variable_number(n, i, j) for i in range(n)])

    for j in positions[:-1]:
        for i, nodes in enumerate(adj):
            literals = [-calculate_variable_number(n, i, j)] + [calculate_variable_number(n, n, j + 1) for n in nodes]
            clauses.append(literals)

# Generate CNF (Conjunctive Normal Form) clauses for the problem
def generate_cnf_clauses(n, positions, adj):
    clauses = []
    generate_room_position_constraints(clauses, n, positions)
    generate_adjacency_constraints(clauses, n, positions, adj)
    return clauses

# Main function
def main():
    # Read input
    n, edges = read_input()
    # Initialize data structures
    clauses, positions, adj = initialize_data(n)
    # Create an adjacency list
    adj = create_adjacency_list(n, edges)
    # Generate CNF clauses
    clauses = generate_cnf_clauses(n, positions, adj)

    num_variables = n * n
    num_clauses = len(clauses)

    # Output the number of clauses and variables followed by the clauses
    print(num_clauses, num_variables)
    for c in clauses:
        c.append(0)
        print(' '.join(map(str, c)))

if __name__ == "__main__":
    main()
