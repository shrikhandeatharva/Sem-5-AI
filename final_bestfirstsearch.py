def bestfirstsearch(graphnodes, start, goal):
    visited = []
    queue = [(start, 0)]  # Priority queue to store (node, heuristic_distance) pairs

    while queue:
        queue.sort(key=lambda x: x[1])  # Sort the queue based on heuristic distance
        current_node, _ = queue.pop(0)  # Get the node with the lowest heuristic distance
        print(current_node, end=" ")

        if current_node == goal:
            print("\nGoal node is reached.")
            return

        visited.append(current_node)

        for neighbor in graphnodes.get(current_node, []):
            if neighbor not in visited:
                heuristic_distance = H_dist.get(neighbor, float('inf'))
                queue.append((neighbor, heuristic_distance))

# Heuristic distances to the goal node
# Graph_nodes={
#     'A':['B','C','D'],
#     'B':['E','F'],
#     'C':['B','F'],
#     'D':['F'],
#     'E':['H'],
#     'F':['G'],
#     'H':['G'],
#     'E': ['G']
# }
# H_dist={
#     'A':40,
#     'B':2,
#     'C':25,
#     'D':35,
#     'E':20,
#     'F':19,
#     'H':10,
#     'G':0
# }

Graph_nodes={
    "S": ["A", "B"],
    "B": ["E", "F"],
    "A": ["C", "D"],
    "E": ["H"],
    "F": ["I", "G"],
    "H": ["M"],
    "I": ["M"],
    "G": ["M"],
}

H_dist={
   "A": 4,
    "B": 7,
    "C": 2,
    "D": 5,
    "E": 1,
    "F": 5,
    "H": 2,
    "I": 5,
    "S": 8,
    "G": 1,
    "M":0,
}

bestfirstsearch(Graph_nodes, 'S', 'M')
