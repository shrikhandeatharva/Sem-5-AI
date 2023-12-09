from queue import PriorityQueue

# Define the new goal state and initial state as lists
goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
initial_state = [1, 2, 3, 5, 0, 6, 4, 7, 8]

# Define a function to calculate the misplaced tiles heuristic
def misplaced_tiles(state):
    count = 0
    for i in range(9):
        if state[i] != goal_state[i]:
            count += 1
    return count

# Define a function to find the possible moves from a given state
def possible_moves(state):
    moves = []
    zero_index = state.index(0)
    if zero_index % 3 > 0:
        moves.append(zero_index - 1)
    if zero_index % 3 < 2:
        moves.append(zero_index + 1)
    if zero_index // 3 > 0:
        moves.append(zero_index - 3)
    if zero_index // 3 < 2:
        moves.append(zero_index + 3)
    return moves

# Define the A* search function
def a_star(initial_state, goal_state, heuristic):
    visited = set()
    priority_queue = PriorityQueue()
    priority_queue.put((0 + heuristic(initial_state), initial_state))  # Initial cost is 0

    # Create a dictionary to track the path and its cost
    path_info = {tuple(initial_state): (None, 0)}

    while not priority_queue.empty():
        _, current_state = priority_queue.get()

        if current_state == goal_state:
            # Reconstruct and print the path
            path = []
            while current_state is not None:
                path.append(current_state)
                current_state, _ = path_info[tuple(current_state)]
            path.reverse()
            for step in path:
                print("----")
                for i in range(0, 9, 3):
                    print(step[i:i+3])
            return path

        visited.add(tuple(current_state))

        zero_index = current_state.index(0)

        for move in possible_moves(current_state):
            new_state = current_state[:]
            new_state[zero_index], new_state[move] = new_state[move], new_state[zero_index]
            if tuple(new_state) not in visited:
                new_cost = path_info[tuple(current_state)][1] + 1
                if tuple(new_state) not in path_info or new_cost < path_info[tuple(new_state)][1]:
                    # Update the path information if this path is shorter
                    path_info[tuple(new_state)] = (current_state, new_cost)
                    heuristic_value = heuristic(new_state)
                    priority_queue.put((new_cost + heuristic_value, new_state))

    return None  # Goal not found

# Example usage:
start_node = initial_state
goal_node = goal_state

result = a_star(start_node, goal_node, misplaced_tiles)

if result:
    print("Solution found:")
    for i in range(0, 9, 3):
        print(result[-1][i:i+3])
else:
    print("No solution found!")
