# Define Constants
EPS = 1e-6
PRECISION = 20

# Function to Solve Equations using Gaussian Elimination
def solve_equations(equations):
    n = len(equations)
    
    # Gaussian Elimination: Transform the matrix to an upper triangular form
    for i in range(n):
        max_row = i
        for j in range(i + 1, n):
            if abs(equations[j][i]) > abs(equations[max_row][i]):
                max_row = j
        equations[i], equations[max_row] = equations[max_row], equations[i]

        # Perform elimination in the matrix
        for j in range(i + 1, n):
            factor = equations[j][i] / equations[i][i]
            for k in range(i, n + 1):
                equations[j][k] -= factor * equations[i][k]

    # Back-Substitution: Find the values of the variables
    x = [0.0] * n
    for i in range(n - 1, -1, -1):
        x[i] = equations[i][n] / equations[i][i]
        for j in range(i - 1, -1, -1):
            equations[j][n] -= equations[j][i] * x[i]
    return x

# Main Function
def main():
    n = int(input())  # Read the number of dishes
    equations = []

    # Read equations (ingredients and energy values) and store in a list
    for _ in range(n):
        equation = list(map(int, input().split()))
        equations.append(equation)

    # Solve the equations to estimate ingredient energy values
    result = solve_equations(equations)

    # Print the estimated energy values with at least three decimal places
    for energy in result:
        print("{:.3f}".format(energy))

# Check if the script is run as the main program
if __name__ == "__main__":
    main()
