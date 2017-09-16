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
    value = 1
    if terminal_test(gameState):
        return value
    else:
        legal_moves = gameState.get_legal_moves()
        for move in legal_moves:
            child_board = gameState.forecast_move(move)
            value = min(value, max_value(child_board))
    return value


def max_value(gameState):
    """ Return the value for a loss (-1) if the game is over,
    otherwise return the maximum value over all legal child
    nodes.
    """
    value = -1
    if terminal_test(gameState):
        return value
    else:
        legal_moves = gameState.get_legal_moves()
        for move in legal_moves:
            child_board = gameState.forecast_move(move)
            value = max(value, min_value(child_board))
    return value