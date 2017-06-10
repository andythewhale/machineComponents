#Andrew J Miller

#This is a generic search algorithm from another project.
#This search algorith can be easily generalized to work with DFS BFS or A* 
#These are the aspects it was expanded to.
#It can also easily be expanded to MinMax, AB, NegaMax, or ExpectaMax if you expand it correctly

def generic_search(problem, fringe, add_to_fringe_fn):
    # This code will take in a position and a givin board state and return a path.
    # The path will be based on the calls that are fed to it from the utils.py file.
    # The code will output the best path to take for our pacman.

    # Closed, meaning we've searched this space.
    closed = set()
    # Start gives us our start state, 0 is our cost, [] is our path.
    start = (problem.getStartState(), 0, [])  # (node, cost, path)

    # We add our start state to the fringe so the fringe isn't empty.
    add_to_fringe_fn(fringe, start, 0)

    # While our fringe is not empty...
    while not fringe.isEmpty():

        # pope the node the cost and the path off of the fringe!
        (node, cost, path) = fringe.pop()

        # If it's a goal node...
        if problem.isGoalState(node):
            # Get the path because we're going to take it.
            return path

        # If it's not the path add it to the closed set so we don't search it again.
        if not node in closed:
            closed.add(node)

            # For the next step's node, action, and cost... in the node, get the node's successors.
            for child_node, child_action, child_cost in problem.getSuccessors(node):
                # The new cost is the cost + the child's, this is a running total.
                new_cost = cost + child_cost
                # The new path is the current path + the child location.
                new_path = path + [child_action]
                # This is the new state of the board. Take note sir.
                new_state = (child_node, new_cost, new_path)
                add_to_fringe_fn(fringe, new_state, new_cost)