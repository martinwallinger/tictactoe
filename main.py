"""imports the computer player"""
import ai
import save_game as sg


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
            move = get_move()
            if move == "save":
                return False
        elif self.game_mode == 2:
            move = ai.find_winning_losing_moves(curr_board, curr_player)
        elif self.game_mode == 3:
            move = ai.minimax_ai(curr_board, curr_player)
        else:
            raise ValueError("game mode is invalid")
        save_move(move, curr_player, curr_board)
        render(curr_board)
        return True


def select_player(number):
    """
    asks the user what game-mode the specified Player should be in.

    :param number: Player Number (1 or 2)
    :return: Key of the chosen game-mode (1, 2 or 3)
    """
    user_input = None
    print(F"\nSelect Player {number}")
    while user_input not in ('1', '2', '3'):
        user_input = input("type 1 for human, 2 for naive ai or 3 for perfect ai: ")
    return int(user_input)


def new_board():
    """
    :return: empty list
    """
    return [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]


def render(curr_board):
    """
    prints the given board on the commandline.

    :param curr_board: game-board to be printed
    """

    print("   0  1  2")
    print("  ---------")
    print(F"0| {curr_board[0][0]}| {curr_board[0][1]}| {curr_board[0][2]}|")
    print(F"1| {curr_board[1][0]}| {curr_board[1][1]}| {curr_board[1][2]}|")
    print(F"2| {curr_board[2][0]}| {curr_board[2][1]}| {curr_board[2][2]}|")
    print("  ---------")


def get_move():
    """
    asks human player for next move, checks if format of given input is right.

    :return: move the player has entered as tuple
    """
    print("To save the current game state, enter 'save'")
    move = input("What is your next move?")
    move = move.strip()
    if move == "save":
        return move
    while len(move) != 2 or not move.isnumeric() or not 0 <= int(move[0]) <= 2 or \
            not 0 <= int(move[1]) <= 2:
        move = input("Please repeat your move as two numbers (0 to 2)"
                     " without whitespaces inbetween: ")
        move.strip()
    return int(move[0]), int(move[1])


def save_move(move, current_player, current_board):
    """
    adds given move on the given board.

    :param move: where the character is to add
    :param current_player: player-character which is to add
    :param current_board: current game-board
    :return: the new game-board
    """
    while current_board[move[0]][move[1]] != " ":
        print(F"Square {move} is already taken! Pick another one!")
        move = get_move()
    if current_player == 'X':
        current_board[move[0]][move[1]] = "X"
    if current_player == 'O':
        current_board[move[0]][move[1]] = "O"
    return current_board


# TODO bessere complexität möglich?
# @lru_cache?
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


def output_winner(state):
    if state == 'draw':
        print("Game Over! It's a draw")
    else:
        if state == 'X':
            winner = 1
        else:
            winner = 2
        print(F'\nGame Over! Player {winner} has won!')


def run(board, player, game_mode1, game_mode2):
    running = True
    while running:
        if game_mode1 and game_mode2:
            player1 = Player(game_mode1)
            player2 = Player(game_mode2)
        else:
            player1 = Player(select_player(1))
            player2 = Player(select_player(2))

        print("\nGame Starts!")
        render(board)
        game_state = 0

        while game_state == 0:

            if player == 1:
                running = player1.play(board, "X")
                if running is False:
                    curr_player = 1
                    sg.save_game_state(board, curr_player, player1.game_mode, player2.game_mode)
                    return
                game_state = is_game_over(board)
                player = 2
            if game_state == 0:

                if player == 2:
                    running = player2.play(board, "O")
                    if running is False:
                        curr_player = 2
                        sg.save_game_state(board, curr_player, player1.game_mode, player2.game_mode)
                        return
                game_state = is_game_over(board)
                player = 1

        output_winner(game_state)


# TODO time/memory profiling, speed up game-logic
# TODO write report
if __name__ == '__main__':
    while True:
        if sg.is_game_loaded() is True and input("Do you want to continue the loaded game? (type y/n): ") == "y":
            curr_board, curr_player, player1_game_mode, player2_game_mode = sg.load_game_state()
        else:
            print("\nPreparing a new game ... ")
            curr_board = new_board()
            curr_player = 1
            player1_game_mode = 0
            player2_game_mode = 0

        run(curr_board, int(curr_player), int(player1_game_mode), int(player2_game_mode))
