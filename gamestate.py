""""
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
"""

from copy import deepcopy

xlim, ylim = 3, 2  # board dimensions


class GameState:
    """
    Attributes
    ----------
    _board: list(list)
        Represent the board with a 2d array _board[x][y]
        where open spaces are 0 and closed spaces are 1

    _parity: bool
        Keep track of active player initiative (which
        player has control to move) where 0 indicates that
        player one has initiative and 1 indicates player 2

    _player_locations: list(tuple)
        Keep track of the current location of each player
        on the board where position is encoded by the
        board indices of their last move, e.g., [(0, 0), (1, 0)]
        means player 1 is at (0, 0) and player 2 is at (1, 0)

    """

    def __init__(self):
        self._board = [[0] * ylim for _ in range(xlim)]
        self._board[-1][-1] = 1  # block lower-right corner
        self._parity = 0
        self._player_locations = [None, None]

    def forecast_move(self, move):
        """ Return a new board object with the specified move
        applied to the current game state.

        Parameters
        ----------
        move: tuple
            The target position for the active player's next move
        """
        if move not in self.get_legal_moves():
            raise RuntimeError("Attempted forecast of illegal move")
        newBoard = deepcopy(self)
        newBoard._board[move[0]][move[1]] = 1
        newBoard._player_locations[self._parity] = move
        newBoard._parity ^= 1
        return newBoard

    def get_legal_moves(self):
        """ Return a list of all legal moves available to the
        active player.  Each player should get a list of all
        empty spaces on the board on their first move, and
        otherwise they should get a list of all open spaces
        in a straight line along any row, column or diagonal
        from their current position. (Players CANNOT move
        through obstacles or blocked squares.) Moves should
        be a pair of integers in (column, row) order specifying
        the zero-indexed coordinates on the board.
        """
        loc = self._player_locations[self._parity]
        if not loc:
            return self._get_blank_spaces()
        moves = []
        rays = [(1, 0), (1, -1), (0, -1), (-1, -1),
                (-1, 0), (-1, 1), (0, 1), (1, 1)]
        for dx, dy in rays:
            _x, _y = loc
            while 0 <= _x + dx < xlim and 0 <= _y + dy < ylim:
                _x, _y = _x + dx, _y + dy
                if self._board[_x][_y]:
                    break
                moves.append((_x, _y))
        return moves

    def _get_blank_spaces(self):
        """ Return a list of blank spaces on the board."""
        return [(x, y) for y in range(ylim) for x in range(xlim)
                if self._board[x][y] == 0]
