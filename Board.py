import numpy as np
import copy


class Board:
    """
    Board object that represents a board of one turn of play.
    """
    def __init__(self, board=None):
        """
        Default Constructor with copy constructor
        :param board:
        """
        # Non copy constructor
        if board is None:
            self._cells = np.array([['.', '.', '.'], ['.', '.', '.'], ['.', '.', '.']])
            self._player = 'n'
            self._played_turn = False
        # Copy constructor
        elif board is not None and isinstance(board, Board):
            self = copy.deepcopy(board)
        else:
            raise Exception('board parameter is not an instance of Board')

    def make_move(self, player='x', row=0, col=0):
        """
        Makes the move to the appropriate spot on the board.
        :param player: the letter representing the current player's value (x or o)
        :param row: The row which the player wants to play
        :param col: the column which the player wants to play
        :return: True or False depending on if the player chose a correct and playable position.
        """
        # Set who's turn it is
        self._player = player
        # Check to see if the move is viable
        if self._cells[row][col] == '.':
            # Make the move.
            self._cells[row][col] = self._player
            self._played_turn = True
            return True
        else:
            return False

    def is_winner(self):
        """
        Check for being a winner of the game.
        :return: True if winnner or False if not.
        """
        # Check to see if the turn has been played before checking status.
        if self._played_turn:
            # Check to see if horizontal winner.
            if self.__is_horizontal_winner():
                return True
            elif self.__is_vertical_winner():
                return True
            elif self.__is_diagonal_winner():
                return True
            else:
                return False
        else:
            raise Exception('player has not made a move')


    def __is_horizontal_winner(self):
        """
        Check for being a horizontal winner
        :return: True or False
        """
        if self._cells[0][0] == self._player and \
                self._cells[0][1] == self._player and \
                self._cells[0][2] == self._player:
            return True
        elif self._cells[1][0] == self._player and \
                self._cells[1][1] == self._player and \
                self._cells[1][2] == self._player:
            return True
        elif self._cells[2][0] == self._player and \
                self._cells[2][1] == self._player and \
                self._cells[2][2] == self._player:
            return True
        else:
            return False

    def __is_vertical_winner(self):
        """
        Check for being a vertical winner
        :return: True or False
        """
        if self._cells[0][0] == self._player and \
                self._cells[1][0] == self._player and \
                self._cells[2][0] == self._player:
            return True
        elif self._cells[0][1] == self._player and \
                self._cells[1][1] == self._player and \
                self._cells[2][1] == self._player:
            return True
        elif self._cells[0][2] == self._player and \
                self._cells[1][2] == self._player and \
                self._cells[2][2] == self._player:
            return True
        else:
            return False

    def __is_diagonal_winner(self):
        """
        Check for being a diagonal winner
        :return: True or False
        """
        if self._cells[0][0] == self._player and \
                self._cells[1][1] == self._player and \
                self._cells[2][2] == self._player:
            return True
        elif self._cells[0][2] == self._player and \
                self._cells[1][1] == self._player and \
                self._cells[2][0] == self._player:
            return True
        else:
            return False

    def to_single_array(self):
        """
        Flatten the two dimensional to on dimensional array.
        :return: flattened version of the board.
        """
        return np.concatenate(self._cells)

    def __str__(self):
        """
        Override the tostring method
        :return: a string representation of the board.
        """
        _board_str = ""
        for row in range(3):
            _board_str += "-------------\n"
            for col in range(3):
                _board_str += "| "
                _board_str += self._cells[row][col] + " "
            _board_str += "|\n"
        _board_str += "-------------\n"

        return _board_str
