def save_game_state(curr_board, curr_player, player1_game_mode, player2_game_mode):
    save_file = open("load.txt", "w")
    for row in curr_board:
        for char in row:
            save_file.writelines(f"{char}")
    save_file.write(f"{curr_player}")
    save_file.write(f"{player1_game_mode}")
    save_file.write(f"{player2_game_mode}")
    save_file.close()
    print("Saving successful\n")


def is_game_loaded():
    game_state = open("load.txt", "r")
    char = game_state.read(1)
    if char:
        return True
    else:
        return False


def load_game_state():
    save_file = open("load.txt", "r")
    file = save_file.readlines()
    save_file.close()
    file = str(file[0])
    curr_board = [[file[0], file[1], file[2]],[file[3], file[4], file[5]],[file[6], file[7], file[8]]]
    curr_player = file[9]
    player1_game_mode = file[10]
    player2_game_mode = file[11]
    return curr_board, curr_player, player1_game_mode, player2_game_mode
