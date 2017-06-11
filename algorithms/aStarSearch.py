#Andrew J Miller

#Same deal here with UCS. You must use generic search.
#The PriorityQueue defines your highest value moves.
#You must define a heuristic that takes the place of the null.

def nullHeuristic(state, problem=None):
    """
  A heuristic function estimates the cost from the current state to the nearest
  goal in the provided SearchProblem.  This heuristic is trivial.
  """
    return 0


def aStarSearch(problem, heuristic=nullHeuristic):
    "Search the node that has the lowest combined cost and heuristic first."
    "*** YOUR CODE HERE ***"
    fringe = util.PriorityQueue()
    def add_to_fringe_fn(fringe, state, cost):
        new_cost = cost + heuristic(state[0], problem)
        fringe.push(state, new_cost)

    return generic_search(problem, fringe, add_to_fringe_fn)