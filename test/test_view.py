import pytest

from tictactoe import view


def test_render(mocker):
    mocker.patch('builtins.print')
    view.render([["X", " ", " "], [" ", "O", " "], [" ", " ", " "]])
    print.assert_called()


def test_render_invalid_values(mocker):
    mocker.patch('builtins.print')
    with pytest.raises(IndexError):
        view.render("Lorem ipsum")
    with pytest.raises(TypeError):
        view.render(42)


def test_select_player_1(mocker):
    mocker.patch('builtins.input')
    mocker.patch('builtins.print')
    input.return_value = '1'

    player = view.select_player(1)
    assert player == 1


def test_select_player_2(mocker):
    mocker.patch('builtins.input')
    mocker.patch('builtins.print')
    input.return_value = '2'

    player = view.select_player(1)
    assert player == 2


def test_select_player_3(mocker):
    mocker.patch('builtins.input')
    mocker.patch('builtins.print')
    input.return_value = '3'

    player = view.select_player(1)
    assert player == 3


def test_print_winner(mocker):
    mocker.patch('builtins.print')
    view.print_winner('O')
    print.assert_called_once()


def test_print_winner_invalid_value(mocker):
    mocker.patch('builtins.print')
    with pytest.raises(ValueError):
        view.print_winner(1)
        print.assert_called_once()


def test_get_move(mocker):
    mocker.patch('builtins.input')
    mocker.patch('builtins.print')
    input.return_value = "11"
    move = view.get_move()
    assert move == (1, 1)


def test_get_move_save(mocker):
    mocker.patch('builtins.input')
    mocker.patch('builtins.print')
    input.return_value = "save"
    move = view.get_move()
    assert move == "save"


def test_get_move_invalid_input(mocker):
    mocker.patch('builtins.input')
    mocker.patch('builtins.print')
    input.side_effect = ["sdhjköf", "1324678", "1 1", " 12", "12"]
    move = view.get_move()
    assert move == (1, 2)
    print.assert_called()

