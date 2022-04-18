import ai


def new_board():
    return [
        [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]

    ]


def render(current_board):
    print("   0  1  2")
    print("  ---------")
    print("0|" + current_board[0][0] + " | " + current_board[0][1] + " | " + current_board[0][2] + "|")
    print("1|" + current_board[1][0] + " | " + current_board[1][1] + " | " + current_board[1][2] + "|")
    print("2|" + current_board[2][0] + " | " + current_board[2][1] + " | " + current_board[2][2] + "|")
    print("  ---------")


def get_move():
    move = input("What is your next move?")
    move = move.strip()
    while len(move) != 2 or not move.isnumeric() or not 0 <= int(move[0]) <= 2 or not 0 <= int(move[1]) <= 2:
        move = input("Please repeat your input as two numbers without whitespaces inbetween: ")
        move.strip()
    return int(move[0]), int(move[1])


def save_move(move, current_player, current_board):
    while current_board[move[0]][move[1]] != " ":
        print("Square ", move, " is already taken! Pick another one!")
        move = get_move()
    if current_player == 'X':
        current_board[move[0]][move[1]] = "X"
    if current_player == 'O':
        current_board[move[0]][move[1]] = "O"
    return current_board


def is_game_over(current_board):
    empty = 0
    possible_lines = [[None], [None], [None], [None], [None], [None], [None], [None]]
    possible_lines[0] = [current_board[0][2], current_board[1][1], current_board[2][0]]
    possible_lines[1] = [current_board[0][0], current_board[1][1], current_board[2][2]]
    for i in range(3):
        possible_lines[i + 2] = [current_board[i][0], current_board[i][1], current_board[i][2]]
    for i in range(3):
        possible_lines[i + 5] = [current_board[0][i], current_board[1][i], current_board[2][i]]
    for i in range(len(possible_lines)):
        empty += possible_lines[i].count(' ')
        if possible_lines[i].count('X') == 3:
            return 1
        elif possible_lines[i].count('O') == 3:
            return 2
    if empty == 0:
        return 3
    else:
        return 0


# TODO Testing
if __name__ == '__main__':
    board = new_board()
    print("Game Starts!")
    render(board)
    while is_game_over(board) == 0:
        player = 'X'
        print("Player One")
        board = save_move(ai.find_winning_moves_ai(board, player), player, board)
        render(board)
        if is_game_over(board) == 0:
            print("Player Two")
            player = 'O'
            board = save_move(ai.find_winning_moves_ai(board, player), player, board)
            render(board)
        else:
            break
    status = is_game_over(board)
    if status == 3:
        print("Game Over! It's a draw")
    else:
        print("Game Over! Player", is_game_over(board), " has won!")
