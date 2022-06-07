"""
main file of tictactoe game.

Classes:
    Player

Functions:
    new_board() -> list
    save_move(int, string, list) -> list
    is_game_over(list) -> string or int
    run(list, int, int, int)
    get_parameters() -> (list, int, int, int)
"""
import ai
import save_game as sg
import view


class Player:
    """
    instantiates a player with an game_mode attribute
    """

    def __init__(self, game_mode):
        """
        Constructor for the Player Class.

        :param game_mode: 1 for human, 2 for find_winning_losing_moves-ai, 3 for minimax-ai
        """
        self.game_mode = game_mode

    def play(self, curr_board, curr_player):
        """
        generic play method which calls upon the specified game mode, saves and renders the board.

        :param curr_board: current game-board
        :param curr_player: player which is to move
        """
        if curr_player == 'X':
            print("\nPlayer One:\n")
        else:
            print("\nPlayer Two:\n")
        if self.game_mode == 1:
            move = view.get_move()
        elif self.game_mode == 2:
            move = ai.find_winning_losing_moves(curr_board, curr_player)
        elif self.game_mode == 3:
            move = ai.minimax_ai(curr_board, curr_player)
        else:
            raise ValueError("game mode is invalid")
        return_value = save_move(move, curr_player, curr_board)
        view.render(curr_board)
        return bool(return_value)


def new_board():
    """
    :return: empty list
    """
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def save_move(move, current_player, current_board):
    """
    adds given move on the given board.

    :param move: where the character is to add
    :param current_player: player-character which is to add
    :param current_board: current game-board
    :return: the new game-board or False if move is "save"
    """
    if move == 'save':
        return False
    while current_board[move[0]][move[1]] != " ":
        print(F"Square {move} is already taken! Pick another one!")
        move = view.get_move()
        if move == 'save':
            return False
    if current_player == 'X':
        current_board[move[0]][move[1]] = "X"
    if current_player == 'O':
        current_board[move[0]][move[1]] = "O"
    return current_board


def is_game_over(current_board):
    """
    checks if game is over

    :param current_board: current game-board
    :return: 'X' if X has won, 'O' if O has won,
    'draw' if game is in a tied state, 0 if game is not over
    """
    empty = 0
    possible_lines = [[], [], [], [], [], [], [], []]
    possible_lines[0] = [current_board[0][2], current_board[1][1], current_board[2][0]]
    possible_lines[1] = [current_board[0][0], current_board[1][1], current_board[2][2]]
    for i in range(3):
        possible_lines[i + 2] = [current_board[i][0], current_board[i][1], current_board[i][2]]
    for i in range(3):
        possible_lines[i + 5] = [current_board[0][i], current_board[1][i], current_board[2][i]]
    for line in possible_lines:
        empty += line.count(' ')
        if line.count('X') == 3:
            return 'X'
        if line.count('O') == 3:
            return 'O'
    if empty == 0:
        return 'draw'
    return 0


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
            player1 = Player(game_mode1)
            player2 = Player(game_mode2)
            print("\nGame Continues!")
        else:
            player1 = Player(view.select_player(1))
            player2 = Player(view.select_player(2))
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
                game_state = is_game_over(curr_board)
                curr_player = 2
            if game_state == 0:

                if curr_player == 2:
                    running = player2.play(curr_board, "O")
                    if running is False:
                        curr_player = 2
                        sg.save_game_state(curr_board, curr_player, player1.game_mode,
                                           player2.game_mode)
                        return
                game_state = is_game_over(curr_board)
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
    return new_board(), 1, 0, 0


if __name__ == '__main__':
    while True:
        run(*get_parameters())
