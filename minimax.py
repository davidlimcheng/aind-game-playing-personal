from minimax_helpers import *



def minimax_decision(gameState):
    """ Return the move along a branch of the game tree that
    has the best possible value.  A move is a pair of coordinates
    in (column, row) order corresponding to a legal move for
    the searching player.

    You can ignore the special case of calling this function
    from a terminal state.
    """
    moves = gameState.get_legal_moves()
    scores = []
    for move in moves:
        child_board = gameState.forecast_move(move)
        value = min_value(child_board)
        scores.append(value)
    best_score_index = scores.index(max(scores))
    return moves[best_score_index]