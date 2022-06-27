import pytest

from tictactoe import player


def test_player_move(mocker):
    mocker.patch('builtins.print')
    mocker.patch('builtins.input')
    input.return_value = "01"
    player1 = player.Player(1)
    value = player1.play([["X", " ", " "], [" ", "O", " "], [" ", " ", " "]], 'X')
    assert value is True


def test_player_save(mocker):
    mocker.patch('builtins.print')
    mocker.patch('builtins.input')
    input.return_value = "save"
    player1 = player.Player(1)
    value = player1.play([["X", " ", " "], [" ", "O", " "], [" ", " ", " "]], 'X')
    assert value is False


def test_player_ai(mocker):
    mocker.patch('builtins.print')
    mocker.patch('builtins.input')
    player1 = player.Player(3)
    value = player1.play([["X", " ", " "], [" ", "O", " "], [" ", " ", " "]], 'X')
    assert value is True


def test_player_invalid_player(mocker):
    mocker.patch('builtins.print')
    mocker.patch('builtins.input')
    player1 = player.Player(3)
    with pytest.raises(ValueError):
        player1.play([["X", " ", " "], [" ", "O", " "], [" ", " ", " "]], 1)


def test_player_invalid_game_mode(mocker):
    mocker.patch('builtins.print')
    mocker.patch('builtins.input')
    player1 = player.Player("3")
    with pytest.raises(ValueError):
        player1.play([["X", " ", " "], [" ", "O", " "], [" ", " ", " "]], "X")
