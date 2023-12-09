

from collections import deque

def water_jug_problem(jug1_capacity, jug2_capacity, target):
    visited = set()
    queue = deque([(0, 0, [])])

    if (target > jug1_capacity and target > jug2_capacity):
        print("Target volume cannot be achieved.")
        return
    
    if (jug1_capacity%2==0 and jug2_capacity%2==0 and target%2!=0):
        print("Target cannot be achieved.")
        return

    while queue:
        jug1, jug2, path = queue.popleft()

        if (jug1 == target or jug2 == target):
            print("Target can be achieved.")
            print("Steps : ")
            print("Initially jug1,jug2 -> (0,0)")
            length = len(path)
            for step in path:
              print(step)
            print(f"No. of steps required : {length}")
            return

        visited.add((jug1, jug2))

        # Fill jug 1 :
        if (jug1 < jug1_capacity):
            queue.append((jug1_capacity, jug2, path +
                         [f"Fill jug1 -> ({jug1_capacity},{jug2})"]))
        # Fill jug 2 :
        if (jug2 < jug2_capacity):
            queue.append((jug1, jug2_capacity, path +
                         [f"Fill jug2 -> ({jug1},{jug2_capacity})"]))
        # Empty jug 1 :
        if (jug1 > 0):
            queue.append((0, jug2, path + [f"Empty jug1 -> ({0},{jug2})"]))
        # Empty jug 2 :
        if (jug2 > 0):
            queue.append((jug1, 0, path + [f"Empty jug2 -> ({jug1},{0})"]))
        # Pour water from jug 1 to jug 2 :
        if (jug1 > 0 and jug2 < jug2_capacity):
            pour_amount = min(jug1, jug2_capacity-jug2)
            queue.append((jug1-pour_amount, jug2+pour_amount, path +
                         [f"Pour from jug1 to jug2 -> ({jug1-pour_amount},{jug2+pour_amount})"]))
        #Pour from jug 2 to jug 1 :
        if (jug2 > 0 and jug1 < jug1_capacity):
            pour_amount = min(jug2, jug1_capacity - jug1)
            queue.append((jug1 + pour_amount, jug2 - pour_amount, path +
                 [f"Pour from jug 2 to jug 1 -> ({jug1 + pour_amount},{jug2 - pour_amount})"]))


print("Water Jug Problem")
jug1_capacity = int(input("Enter capacity of jug 1 : "))
jug2_capacity = int(input("Enter capacity of jug 2 : "))
target = int(input("Enter target volume that you want in any of the two jugs : "))

water_jug_problem(jug1_capacity, jug2_capacity, target)