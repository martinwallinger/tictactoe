import tictactoe.view
from tictactoe import model
from tictactoe import view
import pytest_mock


class Test:
    def test_is_game_over__not_over(self):
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        answer = model.is_game_over(board)
        assert answer == 0

    def test_is_game_over__draw(self):
        board = [["X", "O", "X"], ["X ", "O", "O"], ["O", "X", "X"]]
        answer = model.is_game_over(board)
        assert answer == 'draw'

    def test_is_game_over__o_won(self):
        board = [["O", "O", "O"], [" ", " ", " "], [" ", " ", " "]]
        answer = model.is_game_over(board)
        assert answer == 'O'

    def test_is_game_over__x_won(self):
        board = [["X", "X", "X"], [" ", " ", " "], [" ", " ", " "]]
        answer = model.is_game_over(board)
        assert answer == 'X'

    def test_new_board(self):
        board = model.new_board()

        assert isinstance(board, list)

        for row in board:
            for element in row:
                assert element == " "

    def test_save_move__empty_board(self):
        move = (1, 1)
        player = 'X'
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        board = model.save_move(move, player, board)
        player = 'O'
        move = (0, 0)
        board = model.save_move(move, player, board)

        assert isinstance(board, list)
        assert board == [["O", " ", " "], [" ", "X", " "], [" ", " ", " "]]

    def test_save_move__save(self):
        move = "save"
        player = 'X'
        board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
        assert model.save_move(move, player, board) is False

    def test_save_move__move_taken(self, mocker):
        mocker.patch('tictactoe.view.get_move')
        tictactoe.view.get_move.return_value = (0, 0)
        move = (1, 1)
        player = 'X'
        board = [[" ", " ", " "], [" ", "O", " "], [" ", " ", " "]]
        board = model.save_move(move, player, board)

        tictactoe.view.get_move.assert_called_once()
        assert board == [["X", " ", " "], [" ", "O", " "], [" ", " ", " "]]

    def test_save_move__move_save(self, mocker):
        mocker.patch('tictactoe.view.get_move')
        tictactoe.view.get_move.return_value = "save"
        move = (1, 1)
        player = 'O'
        board = [[" ", " ", " "], [" ", "O", " "], [" ", " ", " "]]
        board = model.save_move(move, player, board)

        tictactoe.view.get_move.assert_called_once()
        assert board is False

