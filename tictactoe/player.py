"""
the player file is only carrying the Player class, used to initiate different Players

Classes:
    Player
"""
from tictactoe import ai
from tictactoe import view
from tictactoe import model


class Player:
    """
    instantiates a player with an game_mode attribute
    """

    def __init__(self, game_mode):
        """
        Constructor for the Player Class.

        :param game_mode: 1 for human, 2 for find_winning_losing_moves-ai, 3 for minimax-ai
        """
        self.game_mode = game_mode

    def play(self, curr_board, curr_player):
        """
        generic play method which calls upon the specified game mode, saves and renders the board.

        :param curr_board: current game-board
        :param curr_player: player which is to move
        """
        if curr_player == 'X':
            print("\nPlayer One:\n")
        else:
            print("\nPlayer Two:\n")
        if self.game_mode == 1:
            move = view.get_move()
        elif self.game_mode == 2:
            move = ai.find_winning_losing_moves(curr_board, curr_player)
        elif self.game_mode == 3:
            move = ai.minimax_ai(curr_board, curr_player)
        else:
            raise ValueError("game mode is invalid")
        return_value = model.save_move(move, curr_player, curr_board)
        view.render(curr_board)
        return bool(return_value)
