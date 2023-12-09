from queue import PriorityQueue

def a_star(graph, start, goal, heuristic):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0 + heuristic[start], start))  # Initial cost is 0

    # Create a dictionary to track the path and its cost
    path_info = {start: (None, 0)}

    while not priority_queue.empty():
        _, current_node = priority_queue.get()

        if current_node == goal:
            # Reconstruct and print the path
            path = []
            while current_node is not None:
                path.append(current_node)
                current_node, _ = path_info[current_node]
            path.reverse()
            print("Path:", " -> ".join(path))
            return True  # Goal found

        visited.add(current_node)

        for neighbor, cost in graph[current_node]:
            if neighbor not in visited:
                new_cost = path_info[current_node][1] + cost
                if neighbor not in path_info or new_cost < path_info[neighbor][1]:
                    # Update the path information if this path is shorter
                    path_info[neighbor] = (current_node, new_cost)
                    heuristic_value = heuristic[neighbor]
                    priority_queue.put((new_cost + heuristic_value, neighbor))

    return False  # Goal not found

# # Example usage:
# graph = {
#     'A': [('B', 2), ('C', 3)],
#     'B': [('A', 2), ('D', 4), ('E', 5)],
#     'C': [('A', 3), ('F', 6)],
#     'D': [('B', 4)],
#     'E': [('B', 5), ('F', 7)],
#     'F': [('C', 6), ('E', 7)]
# }

# heuristic = {
#     'A': 5,
#     'B': 4,
#     'C': 7,
#     'D': 2,
#     'E': 3,
#     'F': 1
# }

# start_node = 'A'
# goal_node = 'F'


# Define the complete graph as a dictionary
graph = {
    'A': [('B', 3), ('C', 5), ('D', 7)],
    'B': [('A', 3), ('E', 5), ('F', 4)],
    'C': [('A', 5)],
    'D': [('A', 7), ('H', 7)],
    'E': [('B', 5)],
    'F': [('B', 4)],
    'G': [],
    'H': [('D', 7)]
}

# Define heuristic values for A* search
heuristic = {
    'A': 8,
    'B': 6,
    'C': 5,
    'D': 7,
    'E': 5,
    'F': 4,
    'G': 3,
    'H': 0  # Heuristic value for the goal is typically 0
}

# Start node and goal node
start_node = 'A'
goal_node = 'H'
if a_star(graph, start_node, goal_node, heuristic):
    print("Goal found!")
else:
    print("Goal not found!")