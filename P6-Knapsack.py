def knapsack_max_profit(weights, values, capacity):
    num_items = len(weights)
    
    # Initialize a table to store the maximum achievable profit for different capacities and items
    dp_table = [[0] * (capacity + 1) for _ in range(num_items + 1)]
    
    # Iterate through items and capacities to calculate the maximum profit
    for item in range(1, num_items + 1):
        for curr_capacity in range(1, capacity + 1):
            if weights[item - 1] <= curr_capacity:
                # If the current item fits, calculate the maximum profit with and without including it
                dp_table[item][curr_capacity] = max(values[item - 1] + dp_table[item - 1][curr_capacity - weights[item - 1]],
                dp_table[item - 1][curr_capacity])
            else:
                # If the current item doesn't fit, inherit the value from the previous row
                dp_table[item][curr_capacity] = dp_table[item - 1][curr_capacity]
    
    # The maximum achievable profit is stored in the last cell of the table
    return dp_table[num_items][capacity]

# Example usage
weights = [2, 3, 4, 5] # Weights of the coffee beans in pounds
values = [10, 20, 30, 40] # Values (cost in rupees) of the coffee beans
capacity = 10 # Capacity of the bag in pounds
max_profit = knapsack_max_profit(weights, values, capacity)
print("Maximum Profit:", max_profit)
