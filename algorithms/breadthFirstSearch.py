#Andrew J Miller

#This is BFS, the old code is there if this needs to be implemented alone.
#Would highly suggest implementing with Generic Search.
#NOTE: Queue is a FIFO helper function.

def breadthFirstSearch(problem):
    """
  Search the shallowest nodes in the search tree first.
  [2nd Edition: p 73, 3rd Edition: p 82]
  """
    "*** YOUR CODE HERE ***"

    fringe = util.Queue()

    def add_to_fringe_fn(fringe, state, cost):
        fringe.push(state)

    return generic_search(problem, fringe, add_to_fringe_fn)


"""
OLD:
    # So the difference in BFS and DFS is just how we prioritize our frontier.
    # Luckyily, we are given a FIFO function. Queue. The rest has already been defined in DFS.
    frontier = util.Queue()
    # Set just eliminates duplicate values.
    visited = set()
    # this pushes the start state onto our frontier to start us.
    # it assigns an empty list with the score zero as well.
    frontier.push((problem.getStartState(), [], 0))
    # This is the magic part.
    # I got this part right minus the above within the loop.
    while not frontier.isEmpty():
        stata, successors, costa = frontier.pop()
        # NOTE: this is for when stuff is added to the recursive function.
        # Initially this will not be implemented.
        # NOTE: that continue reissues the while loop beginning. I learned this (:
        if (stata in visited):
            continue
        # so when we don't continue, we add the state to the visited set.
        visited.add(stata)
        # So if we somehow get the goal... (The dots are the goal :))
        if problem.isGoalState(stata):
            return successors
        # This part was extremely helpful and I took it from the stack article.
        for state, direction, cost in problem.getSuccessors(stata):
            frontier.push((state, successors + [direction], costa))
    return []
"""