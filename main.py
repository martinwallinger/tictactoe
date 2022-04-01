def new_board():
    return [
        [" ", " ", " "], [" ", " ", " "], [" ", " ", " "]

    ]


def render(board):
    print("   0  1  2")
    print("  ---------")
    print("0|" + board[0][0] + " | " + board[0][1] + " | " + board[0][2] + "|")
    print("1|" + board[1][0] + " | " + board[1][1] + " | " + board[1][2] + "|")
    print("2|" + board[2][0] + " | " + board[2][1] + " | " + board[2][2] + "|")
    print("  ---------")


def get_move():
    move = input("What is your next move?")
    move = move.strip()
    while len(move) != 2:
        move = input("Please repeat your input without whitespaces inbetween: ")
        move.strip()
    return int(move[0]), int(move[1])


def save_move(getmove=int, player=int, board=list):
    if player == 1:
        board[getmove[0]][getmove[1]] = "X"
    if player == 2:
        board[getmove[0]][getmove[1]] = "O"
    return board


if __name__ == '__main__':
    board = new_board()
    render(board)
    player = 1
    save_move(get_move(), player, board)
    render(board)
    player = 2
    save_move(get_move(), player, board)
    render(board)
