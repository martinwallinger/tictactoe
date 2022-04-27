"""imports the computer player"""
import ai


def new_board():
    """
    :return: empty list
    """
    return [
        [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]

    ]


def render(curr_board):
    """
    prints the given board on the commandline.

    :param curr_board: game-board to be printed
    """

    print("   0  1  2")
    print("  ---------")
    print("0|" + curr_board[0][0] + " | " + curr_board[0][1] + " | " + curr_board[0][2] + "|")
    print("1|" + curr_board[1][0] + " | " + curr_board[1][1] + " | " + curr_board[1][2] + "|")
    print("2|" + curr_board[2][0] + " | " + curr_board[2][1] + " | " + curr_board[2][2] + "|")
    print("  ---------")


def get_move():
    """
    asks human player for next move, checks if format of given input is right.

    :return: move the player has entered as tuple
    """
    move = input("What is your next move?")
    move = move.strip()
    while len(move) != 2 or not move.isnumeric() or not 0 <= int(move[0]) <= 2 or\
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
        print("Square ", move, " is already taken! Pick another one!")
        move = get_move()
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


if __name__ == '__main__':
    board = new_board()
    print("Game Starts!")
    render(board)
    while is_game_over(board) == 0:
        player = 'X'
        print("Player One")
        board = save_move(ai.find_winning_losing_moves(board, player), player, board)
        render(board)
        if is_game_over(board) == 0:
            print("Player Two")
            player = 'O'
            board = save_move(ai.find_winning_losing_moves(board, player), player, board)
            render(board)
        else:
            break
    if is_game_over(board) == 'draw':
        print("Game Over! It's a draw")
    else:
        if is_game_over(board) == 'X':
            WINNER = 1
        else:
            WINNER = 2
        print(F'Game Over! Player {WINNER} has won!')
