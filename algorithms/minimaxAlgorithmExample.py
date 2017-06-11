#Andrew J Miller

#This is an example of a minimax code I used to solve a problem.
#Warning: It uses helper functions that I think are hard to generalize.
#I tried to keep everything explained so that it was easy to take a look at and understand.
#The player is adapted to play isolation.

class MinimaxPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using depth-limited minimax
    search. You must finish and test this player to make sure it properly uses
    minimax to return a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.
        **************  YOU DO NOT NEED TO MODIFY THIS FUNCTION  *************
        For fixed-depth search, this function simply wraps the call to the
        minimax method, but this method provides a common interface for all
        Isolation agents, and you will replace it in the AlphaBetaPlayer with
        iterative deepening search.
        Parameters
        ----------
        game : `isolation.Board`
            An instance of `isolation.Board` encoding the current state of the
            game (e.g., player locations and blocked cells).
        time_left : callable
            A function that returns the number of milliseconds left in the
            current turn. Returning with any less than 0 ms remaining forfeits
            the game.
        Returns
        -------
        (int, int)
            Board coordinates corresponding to a legal move; may return
            (-1, -1) if there are no available legal moves.
        """
        self.time_left = time_left

        # Initialize the best move so that this function returns something
        # in case the search fails due to timeout
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            return self.minimax(game, self.search_depth)

        except SearchTimeout:
            pass  # Handle any actions required after timeout as needed

        # Return the best move from the last completed search iteration
        return best_move

    def minimax(self, game, depth):
        """Implement depth-limited minimax search algorithm as described in
        the lectures.
        This should be a modified version of MINIMAX-DECISION in the AIMA text.
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Minimax-Decision.md
        **********************************************************************
            You MAY add additional methods to this class, or define helper
                 functions to implement the required functionality.
        **********************************************************************
        Parameters
        ----------
        game : isolation.Board
            An instance of the Isolation game `Board` class representing the
            current game state
        depth : int
            Depth is an integer representing the maximum number of plies to
            search in the game tree before aborting
        Returns
        -------
        (int, int)
            The board coordinates of the best move found in the current search;
            (-1, -1) if there are no legal moves
        Notes
        -----
            (1) You MUST use the `self.score()` method for board evaluation
                to pass the project tests; you cannot call any other evaluation
                function directly.
            (2) If you use any helper functions (e.g., as shown in the AIMA
                pseudocode) then you must copy the timer check into the top of
                each helper function or else your agent will timeout during
                testing.
        """

        # OK so first we need to check to make sure we haven't timed out the function.
        # I didn't make this. This was given.
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # First let's define our default values for the score and the best possible move.
        # If we get a better score or a better move this will change.
        # We need the score here to determine what the max/min score is.
        best_move = (-1, -1)
        highest_saved_score = float("-inf")

        # Now let's get the actual moves available, if we have any:
        legal_moves = game.get_legal_moves(game.active_player)

        # My intuition here was to first make an if statement asking for the length of our legal moves.
        # However, I got help, I can see now, if there are no legal moves, then there's nothing to do.
        # I was overthinking the problem.
        # So for each move in our legal_moves...
        for move in legal_moves:
            # We get a copy of the move for the forecasted game board if we make that move.
            forcasted_move = game.forecast_move(move)

            # We get the score of this move, and the depth is a step below and it is also at a minimizing edge.
            temporary_score = self.minum(forcasted_move, depth - 1)

            # If this score is greater than our highest saved score then our highest saved score is this score.
            if temporary_score > highest_saved_score:
                highest_saved_score = temporary_score

                # Our best_move is the move with the highest score.
                best_move = move

        # Now we return best_move to complete the interface.
        return best_move

    # This is the maximizing function for the minimax algorithm
    # If we're on a maximizing edge we should maximize the node at the next level.
    def maxim(self, game, depth):
        # This function takes self, the game state, and the depth as an argument.
        # This function outputs the score of the best move.

        # First let's make sure we have time to do this:
        # This if statement is given and I did not make it.
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # Now let's check to make sure we're not at the root node:
        # NOTE: active_player took me forever to figure out.
        # I kept implementing it as 'self, game', kind of embarrassing.
        if depth == 0:
            return self.score(game, game.active_player)

        # Let's get that max score:
        # First we set it to negative infinity as a baseline
        opt_score = float("-inf")

        # Next we get the children of the current node our active player is standing at.
        children = game.get_legal_moves(game.active_player)

        # Now for each child of the set of children we find out what they're really worth.
        # We set the new child as equal to the best child if they're worth more.
        # This is recursion on our base case.
        # Check out the move score variable and the minum function. This is confusing and still makes my head spin.
        # At the next level down, we're taking the minimum score, that's why it looks kind of confusing.
        for child in children:
            move = game.forecast_move(child)  # Copy of gamestate with new move kind of applied, no commitment.
            move_score = self.minum(move, depth - 1)
            if move_score > opt_score:
                opt_score = move_score

        # For the longest time I was getting this wrong.
        # For some reason I thought the function must need to return the move and the score.
        # However this simplifies everything.
        return opt_score

    # Now we do the opposite of maxim:
    def minum(self, game, depth):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if depth == 0:
            # I was stuck on this part for a very long time.
            # I am a fool.
            return self.score(game, game.inactive_player)

        opt_score = float("inf")
        children = game.get_legal_moves(game.active_player)
        for child in children:
            move = game.forecast_move(child)
            move_score = self.maxim(move, depth - 1)
            if move_score <= opt_score:
                opt_score = move_score

        return opt_score