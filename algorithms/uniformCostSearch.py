#Andrew J Miller

#I got bored of writing the old code. You MUST use generic search with this.
#PriorityQueue queues up your next moves based on how you define what the highest value move is.

def uniformCostSearch(problem):
    "Search the node of least total cost first. "
    "*** YOUR CODE HERE ***"

    # Okay so for this we can grab the BFS as a skeleton.
    # There's a function in priority queue that should be taken advantage of.
    # Queue doesn't give us the order we need to tackle all of the dots.
    # PriorityQueue gives us what we need and when we need it to decide the most effective path based on cost.
    fringe = util.PriorityQueue()

    def add_to_fringe_fn(fringe, state, cost):
        fringe.push(state, cost)

    return generic_search(problem, fringe, add_to_fringe_fn)
