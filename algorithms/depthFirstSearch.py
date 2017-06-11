#Andrew J Miller

#You should really use this with generic search.
#But the old code is there if this is wanted to be used alone.
#Stack is a LIFO helper function.


def depthFirstSearch(problem):
    """
  Search the deepest nodes in the search tree first
  [2nd Edition: p 75, 3rd Edition: p 87]
  Your search algorithm needs to return a list of actions that reaches
  the goal.  Make sure to implement a graph search algorithm
  [2nd Edition: Fig. 3.18, 3rd Edition: Fig 3.7].
  To get started, you might want to try some of these simple commands to
  understand the search problem that is being passed in:
  print "Start:", problem.getStartState()
  print "Is the start a goal?", problem.isGoalState(problem.getStartState())
  print "Start's successors:", problem.getSuccessors(problem.getStartState())
  """
    "*** YOUR CODE HERE ***"
    fringe = util.Stack()

    def add_to_fringe_fn(fringe, state, cost):
        fringe.push(state)

    return generic_search(problem, fringe, add_to_fringe_fn)


"""
OLD:
    # The best method I got hear was my method plus a few I researched on Stack Overflow.
    # I'm going to mix and match the methods to the one that works best.
    # I'm glad I found the Stack Overflow article on DFS. It taught me a lot.
    # At first I was defining the starting position (inside the loop) with the get start function
    # However, this was misguided. This resets the point of reference each time (duh?)
    # First thing we need to do when implementing a search is to grab the frontier states.
    # util.stack() gives us what we need on a LIFO basis. So we search "all the way left" on our graph first
    # Queue is the FIFO version.
    # Util has some useful functions:
    # push puts an item into the stack.
    # pop kicks it out
    # isEmpty tells you it's empty.
    frontier = util.Stack()
    # Set just eliminates duplicate values.
    # This is where our visited stuff goes.
    visited = set()
    # this pushes the start state onto our frontier to start us.
    # it assigns an empty list with the score zero as well.
    frontier.push((problem.getStartState(), [], 0))
    # This is the magic part.
    # I got this part right minus the above within the loop.
    # while we do not have an frontier ...
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