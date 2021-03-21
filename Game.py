from Board import Board
import re


class Game:
    def __init__(self):
        """
        Default Constructor
        """
        self.__reset_game()

    def __reset_game(self):
        """
        Resets the game back to factory defaults
        :return:
        """
        self._board_plays = []
        self._current_player = 'x'
        self._game_over = False

    def start(self):
        """
        Start the game
        :return:
        """
        # reset the game back to normal
        self.__reset_game()

        while self._game_over is False:
            # Set who is the next player to play
            self.__set_current_player('x')
            # Play the turn.
            if not self._board_plays:
                _board: Board = self.__player1_turn()
            else:
                _board: Board = self.__player1_turn(self._board_plays[0])
            # Check for the winner.
            if _board.is_winner():
                # If winner, then game over.
                self.__game_over()
                break
            # print the board.
            print(_board)
            # Store the results
            self._board_plays.insert(0, _board)

            # Set who is the next player to play
            self.__set_current_player('o')
            # Play the turn.
            if not self._board_plays:
                _board: Board = self.__player2_turn()
            else:
                _board: Board = self.__player2_turn(self._board_plays[0])
            # Check for the winner.
            if _board.is_winner():
                # If winner, then game over.
                self.__game_over()
                break
            # print the board.
            print(_board)
            # Store the results
            self._board_plays.insert(0, _board)

    def __set_current_player(self, who):
        """
        Sets who is the current player for the next move.
        :param who: Sets who turn it is. (ex. x or o)
        :return:
        """
        self._current_player = who

    def __game_over(self):
        """
        Sets the game over flag to True
        :return:
        """
        self._game_over = True

    def __player1_turn(self, board=None):
        """
        This is the method used for player 1.
        :param board:
        :return: The board after the player's play
        """
        _good_move = False
        while _good_move is False:
            res: str = input("What position would you like to play? Ex. 2,2\n")
            # Search to make sure we are in the correct format
            _correct_format = re.search('[0-2],[0-2]', res)
            if _correct_format:
                try:
                    # Get the player's position.
                    row, col = Game.__get_position(res)
                    if board is None:
                        board: Board = Board()
                    _good_move = board.make_move(self._current_player, row, col)
                    if _good_move is False:
                        print("Incorrect position choice. Please try again.\n")
                except:
                    print("Incorrect character for position element.")
            else:
                print("Not a valid position choice.")
        return board

    def __player2_turn(self, board=None):
        """
        This is the method used for player 2.
        :param board: The last played board to continue the game.
        :return: The board after the player's play.
        """
        _good_move = False
        while _good_move is False:
            res: str = input("What position would you like to play? Ex. 2,2\n")
            # Search to make sure we are in the correct format
            _correct_format = re.search('[0-2],[0-2]', res)
            if _correct_format:
                try:
                    # Get the player's position.
                    row, col = Game.__get_position(res)
                    if board is None:
                        board: Board = Board()
                    _good_move = board.make_move(self._current_player, row, col)
                    if _good_move is False:
                        print("Incorrect position choice. Please try again.\n")
                except:
                    print("Incorrect character for position element.")
            else:
                print("Not a valid position choice.")
        return board

    @staticmethod
    def __get_position(res):
        """
        Get the position coordinates from a response string from the input.
        :param res:
        :return: A tuple of the player's chosen position (row, col)
        """
        if "," in res:
            # split it by the comma
            position = res.split(',')
            # Check to see if it's an int
            if position[0].isdigit():
                # Get the row position.
                _row = int(position[0])
            else:
                raise Exception("Not a set of number [0]")
            # Check to see if it's an int
            if position[1].isdigit():
                # Get the col position.
                _col = int(position[1])
            else:
                raise Exception("Not a set of numbers [1]")
            # Return the correct values.
            return _row, _col
        else:
            raise Exception("Not correct formatting. Ex. 1,2")



