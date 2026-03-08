# 1. Setup the Map (Graph) and the Hunches (Heuristics)

# Connections: 'Node': {'Neighbor': Cost}
graph = {
    'A': {'B': 1, 'C': 3},
    'B': {'D': 3},
    'C': {'D': 1, 'E': 2},
    'D': {'G': 5},
    'E': {'G': 2},
    'G': {}
}

# Heuristics: Straight line distance to Goal 'G'
heuristics = {'A': 6, 'B': 5, 'C': 4, 'D': 3, 'E': 1, 'G': 0}


def solve_path_astar():
    # User Input
    start = input("Enter start node (A-G): ").upper()
    goal = input("Enter goal node (A-G): ").upper()

    # Step 1: Place starting node in OPEN list
    # We store: [node_name, f_value]
    open_list = [[start, heuristics[start]]]
    closed_list = []

    g_costs = {start: 0}       # Real cost to reach the node
    parents = {start: None}    # To remember the path

    # Step 2: Check if OPEN list is empty
    while len(open_list) > 0:

        # Step 3: Select node with smallest f (g + h)
        open_list.sort(key=lambda x: x[1])
        n_data = open_list.pop(0)
        n = n_data[0]

        # Check if node n is the goal
        if n == goal:
            print("\nSUCCESS!! Path found.")
            show_result(parents, goal, g_costs[goal])
            return

        # Step 4: Expand node n (move to CLOSED)
        closed_list.append(n)

        # Generate successors (neighbors)
        for neighbor, cost in graph[n].items():
            new_g = g_costs[n] + cost
            new_f = new_g + heuristics[neighbor]

            # If neighbor not in OPEN and not in CLOSED
            if neighbor not in closed_list and neighbor not in [item[0] for item in open_list]:
                g_costs[neighbor] = new_g
                open_list.append([neighbor, new_f])
                parents[neighbor] = n
            else:
                # If seen before, check if this new path is cheaper
                if new_g < g_costs.get(neighbor, 9999):
                    g_costs[neighbor] = new_g
                    parents[neighbor] = n

                    # Update f value in open_list if it's there
                    for item in open_list:
                        if item[0] == neighbor:
                            item[1] = new_f

    # If OPEN becomes empty and goal not found
    print("FAILURE: No path found.")


def show_result(parents, goal, total_cost):
    path = []
    curr = goal

    while curr is not None:
        path.append(curr)
        curr = parents[curr]

    print("Path:", " -> ".join(path[::-1]))
    print("Total Cost:", total_cost)


# Run the program
solve_path_astar()