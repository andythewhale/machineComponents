#Andrew J Miller

#This is an alpha beta pruning example that was adapted from the minimax player. The algorithm uses the exact same code formatting structure as the minimax file.
#Again, I apologize for the helpe functions. Maybe in the future I could make a more complete example that generalizes to all cases.

class AlphaBetaPlayer(IsolationPlayer):
    """Game-playing agent that chooses a move using iterative deepening minimax
    search with alpha-beta pruning. You must finish and test this player to
    make sure it returns a good move before the search time limit expires.
    """

    def get_move(self, game, time_left):
        """Search for the best move from the available legal moves and return a
        result before the time limit expires.
        Modify the get_move() method from the MinimaxPlayer class to implement
        iterative deepening search instead of fixed-depth search.
        **********************************************************************
        NOTE: If time_left() < 0 when this function returns, the agent will
              forfeit the game due to timeout. You must return _before_ the
              timer reaches 0.
        **********************************************************************
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

        # TODO: finish this function!
        # Not sure why but it was really scary for me to try and start this part of the project.
        # It took me about 2 days to actually sit down and look at alphabeta.
        # But to get started let's look at what needs to happen.
        # Most of this was easy by looking at the MiniMaxPlayer and copying it.
        # We need a default move if there is no default move.
        best_move = (-1, -1)

        try:
            # The try/except block will automatically catch the exception
            # raised when the timer is about to expire.
            # The first thing I tried was just to copy the MiniMaxPlayer, it did not work.
            # So we need to start at the root and go down the tree using iterative deepening.
            # This is similar to depth first search but with pruning I think.
            depth = 1

            # The implementation of this while loop doesn't really matter, this is just a good way of doing it.
            # Keep in mind, without the except statement, this runs forever
            while True:
                best_move = self.alphabeta(game, depth)
                depth = depth + 1

                # This will run until we get a SearchTimeOut:
        except SearchTimeout:

            pass

        return best_move

    def alphabeta(self, game: object, depth: object, a: object = float("-inf"), b: object = float("inf")) -> object:
        """Implement depth-limited minimax search with alpha-beta pruning as
        described in the lectures.
        This should be a modified version of ALPHA-BETA-SEARCH in the AIMA text
        https://github.com/aimacode/aima-pseudocode/blob/master/md/Alpha-Beta-Search.md
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
        alpha : float
            Alpha limits the lower bound of search on minimizing layers
        beta : float
            Beta limits the upper bound of search on maximizing layers
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
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()

        # TODO: finish this function!
        # The additions here were hardest for me, not sure why:

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
            temporary_score = self.abminum(forcasted_move, depth - 1, a, b)

            # If this score is greater than our highest saved score then our highest saved score is this score.
            if temporary_score > highest_saved_score:
                highest_saved_score = temporary_score

                # Our best_move is the move with the highest score.
                best_move = move

            # The difference between alphabeta and minimax is here:
            if temporary_score >= b:
                return move

            # This just makes a equal to the higher value, for now.
            a = max(a, temporary_score)

        # Now we return best_move to complete the interface.
        return best_move

    # AB Maxim is very similar to normal Maxim but with AB.

    def abmaxim(self, game, depth, a, b):
        # This function takes self, the game state, the depth, a and b as an argument.
        # This function outputs the score of the best move.
        # This function also prunes nodes that could not possibly possess an optimal strategy for us.

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
            move_score = self.abminum(move, depth - 1, a, b)
            if move_score > opt_score:
                opt_score = move_score

                # Here's where things get way different:
            if opt_score >= b:
                return opt_score

            a = max(a, opt_score)

        # For the longest time I was getting this wrong.
        # For some reason I thought the function must need to return the move and the score.
        # However this simplifies everything.
        return opt_score

    # Now we do the opposite of abmaxim, which is the same as minim with beta:
    def abminum(self, game, depth, a, b):
        if self.time_left() < self.TIMER_THRESHOLD:
            raise SearchTimeout()
        if depth == 0:
            # I was stuck on this part for a very long time.
            # I couldn't understand to call this on the inactive player.
            return self.score(game, game.inactive_player)

        opt_score = float("inf")
        children = game.get_legal_moves(game.active_player)
        for child in children:
            move = game.forecast_move(child)
            move_score = self.abmaxim(move, depth - 1, a, b)
            if move_score < opt_score:
                opt_score = move_score

            if opt_score <= a:
                return opt_score

            b = min(b, opt_score)

        return opt_score