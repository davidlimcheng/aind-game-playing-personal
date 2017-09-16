def terminal_test(gameState):
    """ Return True if the game is over for the active player
    and False otherwise.
    """
    if len(gameState.get_legal_moves()) == 0:
        return True
    else:
        return False


def min_value(gameState):
    """ Return the value for a win (+1) if the game is over,
    otherwise return the minimum value over all legal child
    nodes.
    """
    if terminal_test(gameState):
        return 1
    else:
        legal_moves = gameState.get_legal_moves()
        child_boards = []
        for move in legal_moves:
            child_boards.add(gameState.forecast_move(move))



def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    pass