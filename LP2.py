import heapq

# Directions (up, down, left, right)
directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

class Node:
    def __init__(self, position, g_cost, h_cost, parent=None):
        self.position = position
        self.g_cost = g_cost  # Cost from start to node
        self.h_cost = h_cost  # Estimated cost from node to goal
        self.f_cost = g_cost + h_cost  # Total cost (f = g + h)
        self.parent = parent  # To track the path

    def __lt__(self, other):
        # Compare nodes based on their f_cost (for priority queue)
        return self.f_cost < other.f_cost

def heuristic(a, b):
    # Manhattan distance heuristic (use a different one if needed)
    return abs(a[0] - b[0]) + abs(a[1] - b[1])

def a_star(grid, start, goal):
    open_list = []
    closed_list = set()

    # Initialize start node and add it to the open list
    start_node = Node(start, 0, heuristic(start, goal))
    heapq.heappush(open_list, start_node)

    while open_list:
        current_node = heapq.heappop(open_list)  # Get node with lowest f_cost
        current_position = current_node.position

        if current_position == goal:
            # Goal reached, reconstruct path
            path = []
            while current_node:
                path.append(current_node.position)
                current_node = current_node.parent
            return path[::-1]  # Return path from start to goal

        closed_list.add(current_position)  # Add to closed list

        # Explore neighbors
        for direction in directions:
            neighbor = (current_position[0] + direction[0], current_position[1] + direction[1])

            # Check if neighbor is within grid bounds
            if 0 <= neighbor[0] < len(grid) and 0 <= neighbor[1] < len(grid[0]):
                if grid[neighbor[0]][neighbor[1]] == 1:  # Obstacle (1 means obstacle)
                    continue  # Skip obstacles

                if neighbor in closed_list:
                    continue  # Skip already evaluated

                g_cost = current_node.g_cost + 1  # Movement cost (can be adjusted)
                h_cost = heuristic(neighbor, goal)
                neighbor_node = Node(neighbor, g_cost, h_cost, current_node)

                # Check if neighbor is in open list and has a higher f_cost
                if not any(node.position == neighbor and node.f_cost <= neighbor_node.f_cost for node in open_list):
                    heapq.heappush(open_list, neighbor_node)

    return None  # Return None if no path found

def print_grid(grid):
    for row in grid:
        print(" ".join(str(cell) for cell in row))

# Example Usage:
# 0 = free space, 1 = obstacle
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 1, 0],
    [0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0]
]
start = (0, 0)  # Starting point
goal = (4, 4)  # Goal point

path = a_star(grid, start, goal)

if path:
    print("Path found:", path)
else:
    print("No path found")