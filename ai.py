"""
the computer-player of the tictactoe game.

Functions:
    find_winning_losing_moves(list, string) -> int
    minimax_ai(list, string) -> int

"""
import random
import main


def _find_legal_moves(curr_board):
    """
    finds moves which haven't been done yet.

    :param curr_board: board to analyze
    :return: List of possible moves
    """
    legal_moves = []
    for x_coord in range(len(curr_board)):
        for y_coord in range(len(curr_board)):
            if curr_board[x_coord][y_coord] == ' ':
                legal_moves.append((x_coord, y_coord))

    return legal_moves


def find_winning_losing_moves(curr_board, curr_player=str):
    """
    an ai which can detect winning or drawing moves and plays them out.
    if none of these gets detected, a random move will be returned.

    :param curr_board: current game-board
    :param curr_player: player which is to move
    :return: winning/drawing move or a random one if no hit found
    """
    opponent = _get_opponent(curr_player)
    legal_moves = _find_legal_moves(curr_board)

    for move in legal_moves:
        hit = False

        # vertical
        if move[0] == 0:
            if curr_board[move[0] + 1][move[1]] == (opponent or curr_player) and \
                    curr_board[move[0] + 2][move[1]] == (opponent or curr_player):
                hit = True

        if move[0] == 1:
            if curr_board[move[0] - 1][move[1]] == (opponent or curr_player) and \
                    curr_board[move[0] + 1][move[1]] == (opponent or curr_player):
                hit = True

        if move[0] == 2:
            if curr_board[move[0] - 1][move[1]] == (opponent or curr_player) and \
                    curr_board[move[0] - 2][move[1]] == (opponent or curr_player):
                hit = True

        # horizontal
        if move[1] == 0:
            if curr_board[move[0]][move[1] + 1] == (opponent or curr_player) and \
                    curr_board[move[0]][move[1] + 2] == (opponent or curr_player):
                hit = True

        if move[1] == 1:
            if curr_board[move[0]][move[1] - 1] == (opponent or curr_player) and \
                    curr_board[move[0]][move[1] + 1] == opponent:
                hit = True

        if move[1] == 2:
            if curr_board[move[0]][move[1] - 1] == (opponent or curr_player) and \
                    curr_board[move[0]][move[1] - 2] == opponent:
                hit = True

        # diagonal
        if move == (0, 0):
            if curr_board[1][1] == (opponent or curr_player) and \
                    curr_board[2][2] == opponent:
                hit = True

        if move == (1, 1):
            if (curr_board[0][0] == (opponent or curr_player) and
                curr_board[2][2] == (opponent or curr_player)) or \
                    (curr_board[2][0] == (opponent or curr_player) and
                     curr_board[0][2] == (opponent or curr_player)):
                hit = True

        if move == (2, 2):
            if curr_board[1][1] == (opponent or curr_player) and \
                    curr_board[0][0] == (opponent or curr_player):
                hit = True

        if move == (2, 0):
            if curr_board[1][1] == (opponent or curr_player) and \
                    curr_board[0][2] == (opponent or curr_player):
                hit = True

        if move == (0, 2):
            if curr_board[1][1] == (opponent or curr_player) and \
                    curr_board[2][0] == (opponent or curr_player):
                hit = True

        if hit:
            return move

    return legal_moves[int(random.uniform(0, len(legal_moves)))]


def _make_move(board, move, character):
    """
    adds the given character on the given board.

    :raises ValueError: if character is invalid
    :param board: current game-board
    :param move: where the character is to add
    :param character: character which is to add ('X', 'O' or ' ')
    :return: the new game-board
    """
    if character == 'X':
        board[move[0]][move[1]] = "X"
    elif character == 'O':
        board[move[0]][move[1]] = "O"
    elif character == " ":
        board[move[0]][move[1]] = " "
    else:
        raise ValueError("character given to _make_move() is invalid")
    return board


def _minimax_score(board, player):
    """
    this method scores the given board if it is terminal or makes all possible moves to
    return the best possible score for the current player and board

    :param board: the game-state to be analyzed
    :param player: the player which is to move
    :return: the best score which is possible with the given board,
    or if the game is in a terminal state:
    10 if X has won, -10 if O has won, 0 if it is a draw
    """
    winner = main.is_game_over(board)
    if winner == 'X':
        return 10
    if winner == 'O':
        return -10
    if winner == 'draw':
        return 0

    if player == 'X':
        best_score = -100

        for move in _find_legal_moves(board):
            _make_move(board, move, 'X')
            score = _minimax_score(board, 'O')
            _make_move(board, move, " ")
            if score > best_score:
                best_score = score
        return best_score

    best_score = 100

    for move in _find_legal_moves(board):
        _make_move(board, move, 'O')
        score = _minimax_score(board, 'X')
        _make_move(board, move, " ")
        if score < best_score:
            best_score = score
    return best_score


def minimax_ai(board, player):
    """
    implementation of the minimax-algorithm.
    if X is to move, the method wants to maximize.
    if O is to move, the method wants to minimize.
    tries all currently possible moves and calls minimax_score() to evaluate each.

    :param board: the current game state
    :param player: the player which is to move
    :return: the best possible move
    """

    if board == [[" ", " ", " "], [" ", " ", " "], [" ", " ", " "]]:
        # if the board is empty, the chosen move will always be 0, 0
        return 0, 0

    if player == 'X':
        best_score = -100
    else:
        best_score = 100
    best_move = None

    for move in _find_legal_moves(board):
        _make_move(board, move, player)
        score = _minimax_score(board, _get_opponent(player))
        _make_move(board, move, " ")
        if player == 'X':
            if score > best_score:
                best_score = score
                best_move = move
        if player == 'O':
            if score < best_score:
                best_score = score
                best_move = move
    return best_move


def _get_opponent(player):
    """
    :param player: the player of which the opponent is searched
    :return: X if player is O, O if player is X
    """
    if player == 'X':
        return 'O'
    return 'X'
