def save_game_state(curr_board, curr_player, player1_game_mode, player2_game_mode):
    """
    saves the given game state in a text-file, named save_file.txt

    :param curr_board: current game-board
    :param curr_player: the player which is to move next
    :param player1_game_mode: the game mode of X
    :param player2_game_mode: the game mode of O
    """
    save_file = open("save_file.txt", "w")
    for row in curr_board:
        for char in row:
            save_file.writelines(f"{char}")
    save_file.write(f"{curr_player}")
    save_file.write(f"{player1_game_mode}")
    save_file.write(f"{player2_game_mode}")
    save_file.close()
    print("\nSaving successful\n")


def is_game_saved():
    """
    checks if a game is saved in save_file.txt, creates it if it doesn't exists

    :return: True or False
    """
    try:
        save_file = open("save_file.txt", "r")
    except FileNotFoundError:
        open("save_file.txt", "x")  # creates save file if it doesn't exist
        return False
    content = save_file.readlines()
    save_file.close()
    if content:
        return True
    else:
        return False


def load_game_state():
    """
    loads the saved game state and returns the saved parameter in following order:

    :return: current board, current player, game mode of player1, game mode of player2
    """
    save_file = open("save_file.txt", "r")
    file = save_file.readlines()
    save_file.close()
    file = str(file[0])
    curr_board = [[file[0], file[1], file[2]], [file[3], file[4], file[5]], [file[6], file[7], file[8]]]
    curr_player = file[9]
    player1_game_mode = file[10]
    player2_game_mode = file[11]
    return curr_board, int(curr_player), int(player1_game_mode), int(player2_game_mode)
