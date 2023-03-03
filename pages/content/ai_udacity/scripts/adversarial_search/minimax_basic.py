# Solution using an explicit loop based on max_value()
def _minimax_decision(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    best_score = float("-inf")
    best_move = None
    for m in gameState.actions():
        v = min_value(gameState.result(m))
        if v > best_score:
            best_score = v
            best_move = m
    return best_move


# This solution does the same thing using the built-in `max` function
# Note that "lambda" expressions are Python's version of anonymous functions
def minimax_decision(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.
    
    You can ignore the special case of calling this function
    from a terminal state.
    """
    # The built in `max()` function can be used as argmax!
    return max(gameState.actions(),
               key=lambda m: min_value(gameState.result(m)))

def min_value(gameState):
    """ Return the game state utility if the game is over,
    otherwise return the minimum value over all legal successors
    """
    if gameState.terminal_test():
        return gameState.utility(0)
    v = float("inf")
    for a in gameState.actions():
        v = min(v, max_value(gameState.result(a)))
    return v


def max_value(gameState):
    """ Return the game state utility if the game is over,
    otherwise return the maximum value over all legal successors
    """
    if gameState.terminal_test():
        return gameState.utility(0)
    v = float("-inf")
    for a in gameState.actions():
        v = max(v, min_value(gameState.result(a)))
    return v