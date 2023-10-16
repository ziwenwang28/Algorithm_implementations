# python3

import numpy as np
from sys import stdin

VeryBigNumber = 1e9

def create_equation(a, b):
    return {"a": a, "b": b}

def find_pivot_element(a, used_rows, used_columns):
    mm = len(a)
    pivot_element = {"row": 0, "column": 0}

    for row in range(mm):
        if not used_rows[row]:
            for col in range(mm):
                if not used_columns[col] and a[row][col] != 0:
                    pivot_element["row"] = row
                    pivot_element["column"] = col
                    return True, pivot_element

    return False, None

def swap_rows_and_columns(a, b, used_rows, pivot_element):
    a[pivot_element["column"]], a[pivot_element["row"]] = (
        a[pivot_element["row"]],
        a[pivot_element["column"]],
    )
    b[pivot_element["column"]], b[pivot_element["row"]] = (
        b[pivot_element["row"]],
        b[pivot_element["column"]],
    )
    used_rows[pivot_element["column"]], used_rows[pivot_element["row"]] = (
        used_rows[pivot_element["row"]],
        used_rows[pivot_element["column"]],
    )
    pivot_element["row"] = pivot_element["column"]

def update_matrix(a, b, pivot_element):
    row = pivot_element["row"]
    n = len(a)
    mm = len(a[row])
    scale = a[row][pivot_element["column"]]

    # Scale the pivot row
    a[row] = [aj / scale for aj in a[row]]
    b[row] /= scale

    # Perform row operations for other rows
    for i in range(n):
        if i != row:
            scale = a[i][pivot_element["column"]]
            a[i] = [aij - a[row][j] * scale for j, aij in enumerate(a[i])]
            b[i] -= b[row] * scale

def mark_pivot_element_as_used(pivot_element, used_rows, used_columns):
    used_rows[pivot_element["row"]] = True
    used_columns[pivot_element["column"]] = True

def solve_linear_equation(equation):
    a = equation["a"]
    b = equation["b"]
    size = len(a)

    used_columns = [False] * size
    used_rows = [False] * size
    for step in range(size):
        solved, pivot_element = find_pivot_element(a, used_rows, used_columns)
        if not solved:
            return False, None
        swap_rows_and_columns(a, b, used_rows, pivot_element)
        update_matrix(a, b, pivot_element)
        mark_pivot_element_as_used(pivot_element, used_rows, used_columns)

    return True, b

def add_identity_constraints(n, mm, A, b, big_number):
    for i in range(mm):
        e = [0.0] * mm
        e[i] = -1.0
        A.append(e)
        b.append(0.0)
    A.append([1.0] * mm)
    b.append(big_number)

def check_optimal_solution(n, mm, A, b, c, result, last_equation, ans, best_score):
    for r in result:
        if r < -1e-3:
            return False, ans, best_score

    for i in range(n):
        r = sum(A[i][j] * result[j] for j in range(mm))
        if r > b[i] + 1e-3:
            return False, ans, best_score

    score = sum(c[j] * result[j] for j in range(mm))

    if score <= best_score:
        return False, ans, best_score
    elif last_equation:
        return True, 1, score
    else:
        return True, 0, score

def solve_diet_problem(n, mm, A, b, c, big_number=VeryBigNumber):
    add_identity_constraints(n, mm, A, b, big_number)
    l = n + mm + 1
    ans = -1
    best_score = -float("inf")
    best_result = None
    
    for x in range(2 ** l):
        used_indices = [i for i in range(l) if (x >> i) & 1]
        
        if len(used_indices) != mm:
            continue
        
        last_equation = used_indices[-1] == l - 1
        As = [A[i] for i in used_indices]
        bs = [b[i] for i in used_indices]
        
        equation = create_equation(As, bs)
        solved, result = solve_linear_equation(equation)
        
        if solved:
            is_accepted, ans, best_score = check_optimal_solution(n, mm, A, b, c, result, last_equation, ans, best_score)
            if is_accepted:
                best_result = result
    
    return [ans, best_result]

n, mm = list(map(int, stdin.readline().split()))
A = []
for i in range(n):
    A += [list(map(int, stdin.readline().split()))]
b = list(map(int, stdin.readline().split()))
c = list(map(int, stdin.readline().split()))

anst, ansx = solve_diet_problem(n, mm, A, b, c)

if anst == -1:
    print("No solution")
if anst == 0:
    print("Bounded solution")
    print(" ".join(list(map(lambda x: "%.18f" % x, ansx))))
if anst == 1:
    print("Infinity")
