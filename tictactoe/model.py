"""
the model file contains a few model exclusive methods

Functions:
    is_game_over(list) -> string or int
    new_board() -> list
    save_move(int, string, list) -> list or boolean
"""
from tictactoe import view


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
