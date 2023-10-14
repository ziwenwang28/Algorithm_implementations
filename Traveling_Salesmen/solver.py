import math
import itertools
import time
from collections import namedtuple
import math
from collections import namedtuple
import random

Point = namedtuple("Point", ['x', 'y'])

def length(point1, point2):
    return math.sqrt((point1.x - point2.x)**2 + (point1.y - point2.y)**2)

class TspSolver:
    def __init__(self, points):
        self.points = points
        self.COMPARISON_THRESHOLD = 10 ** -6
        self.tour = list(range(len(points))) + [0]
        self.objective = self.calculate_tour_length()

    def __str__(self):
        length = self.calculate_tour_length()
        optimal = 0
        if not self.is_valid_solution():
            raise ValueError("Solution is not valid")
        output_str = "{:.2f} {}\n".format(length, optimal)
        output_str += ' '.join(map(str, self.tour[:-1]))
        return output_str

    @staticmethod
    def calculate_distance(point1, point2):
        return math.sqrt((point1.x - point2.x) ** 2 + (point1.y - point2.y) ** 2)

    def is_valid_solution(self):
        return len(set(self.tour[:-1])) == len(self.points) == len(self.tour[:-1])

    def edge_length(self, vertex1, vertex2):
        point1 = self.points[vertex1]
        point2 = self.points[vertex2]
        return self.calculate_distance(point1, point2)

    def calculate_tour_length(self):
        return sum(self.edge_length(v1, v2) for v1, v2 in zip(self.tour[:-1], self.tour[1:]))

    def greedy(self):
        self.tour = [0]  # Start with the first point
        remaining_points = set(self.tour[1:-1])  # Remaining points to visit

        while remaining_points:
            current_vertex = self.tour[-1]
            nearest_neighbor = min(
                remaining_points,
                key=lambda neighbor: self.edge_length(current_vertex, neighbor)
            )
            self.tour.append(nearest_neighbor)
            remaining_points.remove(nearest_neighbor)

        self.tour.append(0)  # Return to the starting point
        self.objective = self.calculate_tour_length()  # Update the objective value
        return self.__str__()

    def swap(self, start, end):
        original_tour = self.tour
        new_tour = (
            original_tour[:start] +
            original_tour[start:end + 1][::-1] +
            original_tour[end + 1:]
        )
        original_length = self.objective
        new_length = (
            original_length -
            (self.edge_length(original_tour[start - 1], original_tour[start]) +
            self.edge_length(original_tour[end], original_tour[end + 1])) +
            (self.edge_length(new_tour[start - 1], new_tour[start]) +
            self.edge_length(new_tour[end], new_tour[end + 1]))
        )

        if new_length < original_length - self.COMPARISON_THRESHOLD:
            self.tour = new_tour
            self.objective = new_length
            return True  # Improvement
        else:
            return False  # No improvement

    def solve(self, t_threshold=None):
        start_time = time.time()
        while True:
            if t_threshold and time.time() - start_time >= t_threshold:
                break
            improved = False
            for start, end in itertools.combinations(range(1, len(self.tour) - 1), 2):
                if self.swap(start, end):
                    improved = True
                    break
            if not improved:
                break
        return self.__str__()

def solve_it(input_data):
    # Parse the input
    lines = input_data.split('\n')
    nodeCount = int(lines[0])

    points = []
    for i in range(1, nodeCount+1):
        line = lines[i]
        parts = line.split()
        points.append(Point(float(parts[0]), float(parts[1])))

    if nodeCount <= 1000:
        # Use TSP solver with 2-opt local search for smaller datasets
        tsp_solver = TspSolver(points)
        solution = tsp_solver.solve()
    else:
        # Use the original TSP solver for larger datasets
        # Initialize with a random tour
        tour = list(range(nodeCount))
        random.shuffle(tour)

        def calculate_tour_length(tour):
            return sum(length(points[tour[i]], points[tour[i + 1]]) for i in range(nodeCount - 1)) + length(points[tour[-1]], points[tour[0]])

        def two_opt_swap(tour, i, j):
            new_tour = tour[:i] + tour[i:j+1][::-1] + tour[j+1:]
            return new_tour

        # Local search: 2-opt algorithm
        improved = True
        while improved:
            improved = False
            for i in range(nodeCount - 2):
                for j in range(i + 2, nodeCount):
                    if length(points[tour[i]], points[tour[i + 1]]) + length(points[tour[j]], points[tour[(j + 1) % nodeCount]]) > length(points[tour[i]], points[tour[j]]) + length(points[tour[i + 1]], points[tour[(j + 1) % nodeCount]]):
                        tour = two_opt_swap(tour, i + 1, j)
                        improved = True

        # Calculate the tour length
        tour_length = calculate_tour_length(tour)

        # Prepare the solution in the specified output format
        solution = f"{tour_length:.2f} 0\n"
        solution += " ".join(map(str, tour))

    return solution

import sys

if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        print(solve_it(input_data))
    else:
        print('This test requires an input file. Please select one from the data directory. (i.e., python solver.py ./data/tsp_51_1)')
