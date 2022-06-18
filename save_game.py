"""
handles the saving and loading of the tictactoe game.
provides a method to check if a game is already saved.

Functions:
    save_game_state(list, int, int, int)
    is_game_saved() -> boolean
    load_game_state() -> (list, int, int, int)
    delete_game_state()
"""


def save_game_state(curr_board, curr_player, player1_game_mode, player2_game_mode):
    """
    saves the given game state in a text-file, named save_file.txt

    :param curr_board: current game-board
    :param curr_player: the player which is to move next
    :param player1_game_mode: the game mode of X
    :param player2_game_mode: the game mode of O
    """
    with open("save_file.txt", "w", encoding="utf-8") as save_file:
        for row in curr_board:
            for char in row:
                save_file.writelines(f"{char}")
        save_file.write(f"{curr_player}")
        save_file.write(f"{player1_game_mode}")
        save_file.write(f"{player2_game_mode}")
    print("\nSaving successful\n")


def is_game_saved():
    """
    checks if a game is saved in save_file.txt, creates it if it doesn't exists

    :return: True or False
    """
    try:
        with open("save_file.txt", "r", encoding="utf-8") as save_file:
            content = save_file.readlines()
    except FileNotFoundError:
        with open("save_file.txt", "x", encoding="utf-8"):  # creates save file if it doesn't exist
            return False
    return bool(content)


def load_game_state():
    """
    loads the saved game state and returns the saved parameter in following order:

    :return: current board, current player, game mode of player1, game mode of player2
    """
    with open("save_file.txt", "r", encoding="utf-8") as save_file:
        txt = save_file.readlines()
    txt = str(txt[0])
    curr_board = [[txt[0], txt[1], txt[2]], [txt[3], txt[4], txt[5]], [txt[6], txt[7], txt[8]]]
    curr_player = txt[9]
    player1_game_mode = txt[10]
    player2_game_mode = txt[11]
    return curr_board, int(curr_player), int(player1_game_mode), int(player2_game_mode)


def delete_game_state():
    """
    deletes the data written in the save file.
    """
    with open("save_file.txt", "w", encoding="utf-8") as save_file:
        save_file.write("")
    print("\n\ngame state deleted\n")
