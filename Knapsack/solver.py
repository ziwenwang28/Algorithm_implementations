from collections import namedtuple

# Define a named tuple to represent an item with an index, value, and weight
Item = namedtuple("Item", ['index', 'value', 'weight'])

def dynamic_programming_solver(item_count, capacity, items):
    # Create a 2D table (dp) for dynamic programming
    dp = [[0] * (capacity + 1) for _ in range(item_count + 1)]

    # Fill the dynamic programming table
    for i in range(1, item_count + 1):
        for w in range(1, capacity + 1):
            # Check if the current item can fit in the knapsack
            if items[i - 1].weight <= w:
                # Decide whether to take the current item or not
                dp[i][w] = max(dp[i - 1][w], dp[i - 1][w - items[i - 1].weight] + items[i - 1].value)
            else:
                # If the item is too heavy, don't take it
                dp[i][w] = dp[i - 1][w]

    # Determine which items to take based on the dp table
    taken = [0] * item_count
    w = capacity
    for i in range(item_count, 0, -1):
        if dp[i][w] != dp[i - 1][w]:
            taken[i - 1] = 1
            w -= items[i - 1].weight

    total_value = dp[item_count][capacity]
    return total_value, taken

def greedy_solver(item_count, capacity, items):
    # Sort items by value-to-weight ratio in descending order (high ratio is better)
    items.sort(key=lambda x: x.value / x.weight, reverse=True)

    total_value = 0
    total_weight = 0
    taken = [0] * item_count

    # Iterate through the sorted items to decide which to take
    for item in items:
        if total_weight + item.weight <= capacity:
            taken[item.index] = 1
            total_value += item.value
            total_weight += item.weight

    return total_value, taken

def solve_it(input_data):
    # Parse the input
    lines = input_data.strip().split('\n')
    item_count, capacity = map(int, lines[0].split())
    items = []

    for i in range(1, item_count + 1):
        v, w = map(int, lines[i].split())
        items.append(Item(i - 1, v, w))

    # Decide whether to use dynamic programming or greedy approach based on item count
    if item_count <= 200:
        total_value, taken = dynamic_programming_solver(item_count, capacity, items)
    else:
        total_value, taken = greedy_solver(item_count, capacity, items)

    # Prepare the solution in the specified output format
    output_data = f"{total_value} 0\n{' '.join(map(str, taken))}"
    return output_data

if __name__ == '__main__':
    import sys
    if len(sys.argv) > 1:
        file_location = sys.argv[1].strip()
        with open(file_location, 'r') as input_data_file:
            input_data = input_data_file.read()
        # Print the solution
        print(solve_it(input_data))
    else:
        print('This test requires an input file. Please select one from the data directory. (e.g., python solver.py ./data/ks_4_0)')
