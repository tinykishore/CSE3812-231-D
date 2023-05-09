# Importing queue module for minimum priority queue
import queue

# Define the tree
tree = {
    'S': [['A', 1], ['B', 4]],
    'A': [['B', 2], ['C', 5], ['D', 12]],
    'B': [['C', 2]],
    'C': [['D', 3]],
}

# Define start and goal node name
start_node = 'S'
goal_node = 'D'

# Define the dictionary heuristic values for each node
heuristic_list = {'S': 7, 'A': 6, 'B': 3, 'C': 1, 'D': 0}

# Define the cost list
cost_list = {start_node: 0}

# Define the queue
queue = queue.PriorityQueue()

# Define the optimal path list
optimal_path = []


# A Star Search Function
def a_star_search():
    # First, insert start node into queue
    queue.put((heuristic_list[start_node], start_node))

    # Loop until the queue becomes empty
    while not queue.empty():
        # Get the current node from the queue
        # The Lowest heuristic value gets more priority
        current_node = queue.get()[1]

        # If the current node is already in optimal path, remove it
        # Because if a node comes twice, the previous path gets discarded
        # by less cost value
        if current_node in optimal_path:
            optimal_path.remove(current_node)

        # Add current node to optimal path list
        optimal_path.append(current_node)

        # Goal node testing, if found break the while loop
        if current_node == goal_node:
            print("Goal Found!")
            break

        # Get the children of current node one by one
        for child in tree[current_node]:
            child_node = child[0]  # Node name in child_node
            child_cost = child[1]  # Edge cost in child_cost

            if child_node not in cost_list or cost_list[current_node] + child_cost < cost_list[child_node]:
                cost_list[child_node] = cost_list[current_node] + child_cost
                queue.put((cost_list[child_node] + heuristic_list[child_node], child_node))


if __name__ == '__main__':
    a_star_search()
    optimal_path_str = ' > '.join(optimal_path)
    print("Optimal Path: ", optimal_path_str)
    print("Total Cost: ", cost_list[goal_node])

# Goal Found!
# Optimal Path:  S > A > B > C > D
# Total Cost:  8
