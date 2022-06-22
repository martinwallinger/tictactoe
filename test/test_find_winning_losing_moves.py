import pytest

from tictactoe.ai import find_winning_losing_moves


def test_empty_board_x():
    # arrange
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = 'X'
    # act
    move = find_winning_losing_moves(board, player)
    # assert
    assert isinstance(move, tuple)


def test_empty_board_o():
    # arrange
    board = [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]
    player = 'O'
    # act
    move = find_winning_losing_moves(board, player)
    # assert
    assert isinstance(move, tuple)


def test_with_x():
    # arrange
    board = [["O", " ", "O"], ["X", " ", "X"], ["O", " ", " "]]
    player = 'X'
    # act
    move = find_winning_losing_moves(board, player)
    # assert
    assert isinstance(move, tuple)
    assert move == (1, 1) or move == (0, 1)


def test_with_o():
    # arrange
    board = [["O", " ", "O"], ["X", " ", "X"], ["O", "X", " "]]
    player = 'O'
    # act
    move = find_winning_losing_moves(board, player)
    # assert
    assert isinstance(move, tuple)
    assert move == (1, 1) or move == (0, 1)


def test_board_full():
    # arrange
    board = [["O", "X", "O"], ["X", "X", "X"], ["O", "O", "O"]]
    player = 'X'
    # act
    with pytest.raises(ValueError) as e:
        find_winning_losing_moves(board, player)
        # assert
        assert str(e) == "find_winning_losing_moves_ai(): given board full or invalid!"
