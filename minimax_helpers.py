def terminal_test(gameState):
    if len(gameState.get_legal_moves()) == 0:
        return True
    else:
        return False


def min_value(gameState):
    if terminal_test(gameState):
        return 1
    value = float("inf")
    legal_moves = gameState.get_legal_moves()
    for move in legal_moves:
        child_board = gameState.forecast_move(move)
        value = min(value, max_value(child_board))
    return value


def max_value(gameState):
    if terminal_test(gameState):
        return -1
    value = float("-inf")
    legal_moves = gameState.get_legal_moves()
    for move in legal_moves:
        child_board = gameState.forecast_move(move)
        value = max(value, min_value(child_board))
    return value

