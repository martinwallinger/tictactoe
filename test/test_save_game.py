import pytest

from tictactoe import save_game as sg
from os.path import exists
from os import remove


@pytest.fixture
def patch(mocker):
    mocker.patch('builtins.print')


def test_is_game_saved_file_empty(patch):
    # arrange
    if exists("../save_file.txt"):
        with open("../save_file.txt", "w", encoding="utf-8") as save_file:
            save_file.write("")
    else:
        with open("../save_file.txt", "x", encoding="utf-8"):
            pass
    # act
    is_saved = sg.is_game_saved()
    # assert
    assert is_saved is False


def test_is_game_saved_file_filled(patch):
    # arrange
    if exists("../save_file.txt"):
        with open("../save_file.txt", "w", encoding="utf-8") as save_file:
            save_file.write("Lorem ipsum")
    else:
        with open("../save_file.txt", "x", encoding="utf-8") as save_file:
            save_file.write("Lorem ipsum")
    # act
    is_saved = sg.is_game_saved()
    # assert
    assert is_saved is True
    with open("../save_file.txt", "w", encoding="utf-8") as save_file:
        save_file.write("")


def test_is_game_saved_file_doesnt_exist(patch):
    if exists("../save_file.txt"):
        remove("../save_file.txt")
    is_saved = sg.is_game_saved()
    assert is_saved is False
    assert exists("../save_file.txt")


def test_delete_game_state(patch):
    if exists("../save_file.txt"):
        with open("../save_file.txt", "w", encoding="utf-8") as save_file:
            save_file.write("Lorem ipsum")
    else:
        with open("../save_file.txt", "x", encoding="utf-8") as save_file:
            save_file.write("Lorem ipsum")

    sg.delete_game_state()
    with open("../save_file.txt", "r", encoding="utf-8") as save_file:
        content = save_file.readlines()

    assert not bool(content)


def test_delete_game_state_file_doesnt_exist(patch):
    if exists("../save_file.txt"):
        remove("../save_file.txt")

    sg.delete_game_state()
    with open("../save_file.txt", "r", encoding="utf-8") as save_file:
        content = save_file.readlines()

    assert not bool(content)


def test_load_game_state(patch):
    if exists("../save_file.txt"):
        with open("../save_file.txt", "w", encoding="utf-8") as save_file:
            save_file.write("XOXOXOXOX213")
    else:
        with open("../save_file.txt", "x", encoding="utf-8") as save_file:
            save_file.write("XOXOXOXOX213")
    board, player, player1_gm, player2_gm = sg.load_game_state()
    assert isinstance(board, list)
    assert isinstance(player, int)
    assert isinstance(player1_gm, int)
    assert isinstance(player2_gm, int)
    assert board == [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
    assert player == 2
    assert player1_gm == 1
    assert player2_gm == 3
    remove("../save_file.txt")


def test_load_game_state_file_doesnt_exist(patch):
    if exists("../save_file.txt"):
        remove("../save_file.txt")
    with pytest.raises(FileNotFoundError):
        sg.load_game_state()


def test_save_gamestate_file_doesnt_exist(patch):
    if exists("../save_file.txt"):
        remove("../save_file.txt")
    board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
    player = 2
    player1_gm = 1
    player2_gm = 3
    sg.save_game_state(board, player, player1_gm, player2_gm)
    with open("../save_file.txt", "r", encoding="utf-8") as save_file:
        content = save_file.readlines()
    assert content == ["XOXOXOXOX213"]
    with open("../save_file.txt", "w", encoding="utf-8") as save_file:
        save_file.write("")


def test_save_gamestate_file_empty(patch):
    if exists("../save_file.txt"):
        with open("../save_file.txt", "w", encoding="utf-8") as save_file:
            save_file.write("")
    else:
        with open("../save_file.txt", "x", encoding="utf-8"):
            pass
    board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
    player = 2
    player1_gm = 1
    player2_gm = 3
    sg.save_game_state(board, player, player1_gm, player2_gm)
    with open("../save_file.txt", "r", encoding="utf-8") as save_file:
        content = save_file.readlines()
    assert content == ["XOXOXOXOX213"]
    with open("../save_file.txt", "w", encoding="utf-8") as save_file:
        save_file.write("")


def test_save_game_saved_file_filled(patch):
    if exists("../save_file.txt"):
        with open("../save_file.txt", "w", encoding="utf-8") as save_file:
            save_file.write("Lorem ipsum")
    else:
        with open("../save_file.txt", "x", encoding="utf-8") as save_file:
            save_file.write("Lorem ipsum")
    board = [["X", "O", "X"], ["O", "X", "O"], ["X", "O", "X"]]
    player = 2
    player1_gm = 1
    player2_gm = 3
    sg.save_game_state(board, player, player1_gm, player2_gm)
    with open("../save_file.txt", "r", encoding="utf-8") as save_file:
        content = save_file.readlines()
    assert content == ["XOXOXOXOX213"]
    with open("../save_file.txt", "w", encoding="utf-8") as save_file:
        save_file.write("")
