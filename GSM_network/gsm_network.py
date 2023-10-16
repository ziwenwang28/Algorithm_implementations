# python3

n, m = map(int, input().split())
edges = [list(map(int, input().split())) for _ in range(m)]
K = 3

def generate_SAT_formula():
    C, V, cnt = K * len(edges) + n, n * K, 1
    clauses = []

    for i in range(1, n + 1):
        clauses.append([cnt, cnt + 1, cnt + 2, 0])
        cnt += 3

    for edge in edges:
        for k in range(1, K + 1):
            clauses.append([-((edge[0] - 1) * K + k), -((edge[1] - 1) * K + k), 0])

    return C, V, clauses

def print_SAT_formula(C, V, clauses):
    print("{0} {1}".format(C, V))
    for clause in clauses:
        print(" ".join(map(str, clause)))

C, V, clauses = generate_SAT_formula()
print_SAT_formula(C, V, clauses)
