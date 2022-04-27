"""imports the computer player"""
import ai


def new_board():
    """ returns new board"""
    return [
        [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]

    ]


def render(curr_board):
    """ prints the given board on the commandline """
    print("   0  1  2")
    print("  ---------")
    print("0|" + curr_board[0][0] + " | " + curr_board[0][1] + " | " + curr_board[0][2] + "|")
    print("1|" + curr_board[1][0] + " | " + curr_board[1][1] + " | " + curr_board[1][2] + "|")
    print("2|" + curr_board[2][0] + " | " + curr_board[2][1] + " | " + curr_board[2][2] + "|")
    print("  ---------")


def get_move():
    """ asks human player for next move, checks if format of given input is right """
    move = input("What is your next move?")
    move = move.strip()
    while len(move) != 2 or not move.isnumeric() or not 0 <= int(move[0]) <= 2 or\
            not 0 <= int(move[1]) <= 2:
        move = input("Please repeat your move as two numbers (0 to 2)"
                     " without whitespaces inbetween: ")
        move.strip()
    return int(move[0]), int(move[1])


def save_move(move, current_player, current_board):
    """ marks given move on the given board and returns it"""
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
    returns 'X' if X has won
    returns 'O' if O has won
    returns 'draw' if game is in a tied state
    returns 0 if game is not over
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
            winner = 1
        else:
            winner = 2
        print('Game Over! Player {winner} has won!')
