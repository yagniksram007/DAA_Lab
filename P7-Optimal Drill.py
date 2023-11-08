import itertools

def calculate_distance(x1, y1, x2, y2):
    # Compute the Euclidean distance between two points
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5

def calculate_total_distance(points_order, distances):
    # Calculate the total distance for a given order of points
    total_distance = 0
    num_points = len(points_order)
    for i in range(num_points - 1):
        point1 = points_order[i]
        point2 = points_order[i + 1]
        total_distance += distances[point1][point2]
    return total_distance

def find_optimal_drilling_time(points, toolbox_time):
    num_points = len(points)
    distances = [[0] * num_points for _ in range(num_points)]
    
    # Calculate distances between all pairs of points
    for i in range(num_points):
        x1, y1, d1 = points[i]
        for j in range(num_points):
            x2, y2, d2 = points[j]
            distances[i][j] = calculate_distance(x1, y1, x2, y2)
    
    # Generate all possible permutations of points
    point_permutations = list(itertools.permutations(range(num_points)))
    
    # Initialize optimal drilling time to a large value
    optimal_drilling_time = float('inf')
    
    # Find the optimal drilling time
    for permutation in point_permutations:
        total_distance = calculate_total_distance(permutation, distances)
        drilling_time = total_distance + (num_points - 1) * toolbox_time
        if drilling_time < optimal_drilling_time:
            optimal_drilling_time = drilling_time
    
    return optimal_drilling_time

def main():
    # Example usage
    points = [(0, 0, 1), (3, 0, 2), (0, 4, 1), (3, 4, 2)]  # (x, y, diameter) of each hole
    toolbox_time = 5  # Time required to change the drill at the toolbox
    optimal_time = find_optimal_drilling_time(points, toolbox_time)
    print("Optimal Drilling Time:", optimal_time)

if __name__ == "__main__":
    main()
