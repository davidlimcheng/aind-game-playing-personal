from copy import deepcopy

class GameState:

    def __init__(self):
        # 0: Open, 1: Closed
        self._board = [[0, 0], [0, 0], [0, 0]]
        # The bottom right square is already blocked off before the game starts
        self._board[2][1] = 1

        # 0: Player 1, 1: Player 2
        self._turn = 0

        # Player locations as a list (size 2) of tuples
        self._players = [None, None]

    # Returns a list of available moves to the active player in the current state
    def get_legal_moves(self):
        available_moves = [(x, y) for x in range(3) for y in range(2) if self._board[x][y] == 0]

        active_player = self._turn
        active_player_location = self._players[active_player]

        # If the active player is on the (2, 0) space, they cannot legally move to (0, 1), and vice versa
        if active_player_location:
            if active_player_location[0] == 2:
                try:
                    available_moves.remove((0, 1))
                except ValueError:
                    pass
            if active_player_location == (0, 1):
                try:
                    available_moves.remove((2, 0))
                except ValueError:
                    pass

            # If the active_player has a location, then the inactive player may also have a location
            # Only exception is the first move
            inactive_player = 0 if self._turn else 1
            inactive_player_location = self._players[inactive_player]
            # The only location that is able to block the other player is (1, 0)
            if inactive_player_location and inactive_player_location == (1, 0):
                if active_player_location[1] == 0:
                    if active_player_location[0] == 0:
                        try:
                            available_moves.remove((2, 0))
                        except ValueError:
                            pass
                    if active_player_location[0] == 2:
                        try:
                            available_moves.remove((0, 0))
                        except ValueError:
                            pass


        return available_moves

    # Returns a new GameState object with the player's desired move recorded
    def forecast_move(self, move):
        game = deepcopy(self)
        legal_moves = game.get_legal_moves()

        if move in legal_moves:
            game._board[move[0]][move[1]] = 1
            game._players[game._turn] = move
            game._turn = 0 if game._turn == 1 else 1

        return game