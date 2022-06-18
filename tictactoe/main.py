"""
main file of tictactoe game.

Functions:
    run(list, int, int, int)
    get_parameters() -> (list, int, int, int)
"""
from tictactoe import save_game as sg
from tictactoe import view
from tictactoe import model
from tictactoe import player


def run(curr_board, curr_player, game_mode1, game_mode2):
    """
    plays the game. instantiates the players, calls upon play to make a move.
    active as long the game is running. stops if game over or game has been saved.

    :param curr_board: current game-board
    :param curr_player: player which moves first
    :param game_mode1: the game mode of X
    :param game_mode2: the game mode of O
    """
    running = True
    while running:
        if game_mode1 and game_mode2:
            player1 = player.Player(game_mode1)
            player2 = player.Player(game_mode2)
            print("\nGame Continues!")
        else:
            player1 = player.Player(view.select_player(1))
            player2 = player.Player(view.select_player(2))
            print("\nGame Starts!")

        view.render(curr_board)
        game_state = 0

        while game_state == 0:

            if curr_player == 1:
                running = player1.play(curr_board, "X")
                if running is False:
                    curr_player = 1
                    sg.save_game_state(curr_board, curr_player, player1.game_mode,
                                       player2.game_mode)
                    return
                game_state = model.is_game_over(curr_board)
                curr_player = 2
            if game_state == 0:

                if curr_player == 2:
                    running = player2.play(curr_board, "O")
                    if running is False:
                        curr_player = 2
                        sg.save_game_state(curr_board, curr_player, player1.game_mode,
                                           player2.game_mode)
                        return
                game_state = model.is_game_over(curr_board)
                curr_player = 1

        view.print_winner(game_state)
        return


def get_parameters():
    """
    gets the parameters either from the save file or creates a new game.

    :return:current board, current player, game mode of X, game mode of O
    """
    if sg.is_game_saved() and input("Do you want to load the saved game? (type y/n): ") == "y":
        return sg.load_game_state()

    print("\nPreparing a new game ... ")
    return model.new_board(), 1, 0, 0


if __name__ == '__main__':
    while True:
        try:
            run(*get_parameters())
        except KeyboardInterrupt:
            sg.delete_game_state()
            break
