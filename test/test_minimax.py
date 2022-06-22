import pytest

from tictactoe.ai import minimax_ai


def test_x_with_empty():
    # arrange
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = 'X'
    # act
    move = minimax_ai(board, player)
    # assert
    assert isinstance(move, tuple)
    assert move == (0, 0)


def test_o_with_empty():
    # arrange
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = 'O'
    # act
    move = minimax_ai(board, player)
    # assert
    assert isinstance(move, tuple)
    assert move == (0, 0)


def test_x_maximize():
    board = [["O", " ", "O"], ["X", " ", "X"], ["O", " ", " "]]
    player = 'X'
    move = minimax_ai(board, player)
    assert isinstance(move, tuple)
    assert move == (1, 1)


def test_o_maximize():
    board = [["X", " ", "X"], ["O", " ", "O"], ["X", " ", " "]]
    player = 'O'
    move = minimax_ai(board, player)
    assert isinstance(move, tuple)
    assert move == (1, 1)


def test_force_draw():
    board = [["O", "X", "O"], ["X", " ", "X"], ["O", "X", " "]]
    player = 'O'
    move = minimax_ai(board, player)
    assert isinstance(move, tuple)
    assert move == (1, 1)


def test_wrong_player():
    board = [["O", "X", "O"], ["X", " ", "X"], ["O", "X", " "]]
    player = 'A'
    with pytest.raises(ValueError) as e:
        minimax_ai(board, player)
        assert str(e) == "character given to _make_move() is invalid"


def test_board_full():
    # arrange
    board = [["O", "X", "O"], ["X", "X", "X"], ["O", "O", "O"]]
    player = 'X'
    # act
    with pytest.raises(ValueError) as e:
        minimax_ai(board, player)
        # assert
        assert str(e) == "minimax_ai(): given board full or invalid!"
