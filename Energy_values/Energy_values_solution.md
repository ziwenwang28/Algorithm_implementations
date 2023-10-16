# Estimating Ingredient Energy Values from Menu Data

## Introduction

This task involves using Gaussian Elimination to estimate the energy values of individual ingredients based on a restaurant menu. The menu provides calorie counts and ingredient quantities for each dish. The objective is to calculate the energy values of individual ingredients, enabling the estimation of the total energy values for various dishes.

## Problem Description

### Task
You are presented with a restaurant menu that contains a list of ingredients, their quantities, and the total estimated energy value in calories for each dish. Your goal is to determine the energy values of each individual ingredient, which will allow you to compute the total energy values for your preferred dishes.

### Input Format
The input format consists of the following:
- The first line contains an integer 𝑛, which represents the number of dishes on the menu. Importantly, the number of distinct ingredients is also equal to 𝑛.
- Each of the following 𝑛 lines contains a description 𝑎1, 𝑎2, . . . , 𝑎𝑛, 𝐸 of a single menu item. Here, 𝑎𝑖 represents the quantity of the 𝑖-th ingredient in the dish, and 𝐸 is the estimated total energy value of the dish. If an ingredient is not used in the dish, its quantity is specified as 𝑎𝑖 = 0. It's worth noting that this algorithm must handle cases with negative ingredient quantities (𝑎𝑖 < 0).

### Constraints
- 0 ≤ 𝑛 ≤ 20
- −1000 ≤ 𝑎𝑖 ≤ 1000

### Output Format
The output should consist of 𝑛 real numbers, each representing the energy value of an ingredient. These values can have decimal fractions and should be displayed with at least three digits after the decimal point.

Your output will be considered correct if, for a given test input, each number in the output has an absolute or relative error of less than 10^-2 compared to the correct value. In other words, if the correct number is 5.245000, and you output 5.235001, your output will be considered correct. However, 5.225500 will not be accepted. Similarly, if the correct answer is 1001, and you output 1000, your answer will be considered correct due to the relative error being less than 10^-2. However, if the correct answer is 0.1, and you output 0.05, your answer will not be accepted because both the absolute error (0.05) and the relative error (0.5) are greater than 10^-2. Although we ask for at least 3 digits after the decimal point, precision of 10^-2 is the requirement to avoid rounding issues.

# My solution: Gaussian Elimination for Estimating Ingredient Energy Values

In this code solution, I employed Gaussian elimination to solve a system of equations for estimating the energy values of individual ingredients based on a restaurant menu. Here is the structure of my code:

## Constants:

I defined two important constants:

- `EPS`: A small value (1e-6) used for numerical comparisons.
- `PRECISION`: The number of decimal places used for rounding the output.

## Function: `solve_equations(equations)`:

I implemented this function to solve the system of linear equations. The key steps include:

- Using Gaussian elimination to transform the matrix of equations into an upper triangular form.
- Employing back-substitution to determine the values of the variables (ingredient energy values in this context).

## Function: `main()`:

I created this function to manage the main execution of the code:

- Reading the input from the standard input.
- Parsing the number of dishes (n) and the equations (ingredients and energy values).
- Calling the `solve_equations` function to calculate the energy values of individual ingredients.
- Printing the results, formatted to have at least three decimal places.

## Main Execution Block:

This section checks whether the script is being run as the main program (not imported as a module):

- If it is the main program, I call the `main()` function to execute the solution.

The core algorithmic steps in my code are:

- Utilizing Gaussian elimination to solve the system of linear equations.
- Performing back-substitution to find the values of the variables.

The code structure is well-organized and adheres to best practices for solving linear systems using Gaussian elimination. It also ensures that precision and rounding requirements are met as specified in the problem statement.