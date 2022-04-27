import random
import main


def _find_legal_moves(curr_board):
    legal_moves = []
    for x in range(len(curr_board)):
        for y in range(len(curr_board)):
            if curr_board[x][y] == ' ':
                legal_moves.append((x, y))

    return legal_moves


def find_winning_losing_moves(curr_board, curr_player):
    opponent = get_opponent(curr_player)
    legal_moves = _find_legal_moves(curr_board)
    for move in legal_moves:
        # draw vertical
        if move[1] == 0:
            if curr_board[move[0]][move[1] + 1] == str(opponent) and \
                    curr_board[move[0]][move[1] + 2] == str(opponent):
                return move

        if move == 1:
            if curr_board[move[0]][move[1] - 1] == str(opponent) and \
                    curr_board[move[0]][move[1] + 1] == str(opponent):
                return move

        if move[1] == 2:
            if curr_board[move[0]][move[1] - 2] == str(opponent) and \
                    curr_board[move[0]][move[1] - 1] == str(opponent):
                return move
        # draw horizontal
        if move[1] == 0:
            if curr_board[move[0]][move[1] + 1] == str(opponent) and \
                    curr_board[move[0]][move[1] + 2] == str(opponent):
                return move

        if move[1] == 1:
            if curr_board[move[0]][move[1] - 1] == str(opponent) and \
                    curr_board[move[0]][move[1] + 1] == str(opponent):
                return move

        if move[1] == 2:
            if curr_board[move[0]][move[1] - 2] == str(opponent) and \
                    curr_board[move[0]][move[1] - 1] == str(opponent):
                return move
        # draw diagonal
        if move == (0, 0):
            if curr_board[1][1] == str(opponent) and \
                    curr_board[2][2] == str(opponent):
                return move

        if move == (1, 1):
            if (curr_board[0][0] == str(opponent) and curr_board[2][2] == str(opponent)) \
                    or curr_board[2][0] == str(opponent) and curr_board[0][2] == str(opponent):
                return move

        if move == (2, 2):
            if curr_board[1][1] == str(opponent) and \
                    curr_board[0][0] == str(opponent):
                return move

        if move == (2, 0):
            if curr_board[1][1] == str(opponent) and \
                    curr_board[0][2] == str(opponent):
                return move

        if move == (0, 2):
            if curr_board[1][1] == str(opponent) and \
                    curr_board[2][0] == str(opponent):
                return move
        # win vertical
        if move[1] == 0:
            if curr_board[move[0]][move[1] + 1] == str(curr_player) and \
                    curr_board[move[0]][move[1] + 2] == str(curr_player):
                return move

        elif move[1] == 1:
            if curr_board[move[0]][move[1] - 1] == str(curr_player) and \
                    curr_board[move[0]][move[1] + 1] == str(curr_player):
                return move

        if move[1] == 2:
            if curr_board[move[0]][move[1] - 2] == str(curr_player) and \
                    curr_board[move[0]][move[1] - 1] == str(curr_player):
                return move
        # win horizontal
        if move[1] == 0:
            if curr_board[move[0]][move[1] + 1] == str(curr_player) and \
                    curr_board[move[0]][move[1] + 2] == str(curr_player):
                return move

        if move[1] == 1:
            if curr_board[move[0]][move[1] - 1] == str(curr_player) and \
                    curr_board[move[0]][move[1] + 1] == str(curr_player):
                return move

        if move[1] == 2:
            if curr_board[move[0]][move[1] - 2] == str(curr_player) and \
                    curr_board[move[0]][move[1] - 1] == str(curr_player):
                return move
        # win diagonal
        if move == (0, 0):
            if curr_board[1][1] == str(curr_player) and \
                    curr_board[2][2] == str(curr_player):
                return move

        if move == (1, 1):
            if (curr_board[0][0] == str(curr_player) and curr_board[2][2] == str(curr_player)) \
                    or curr_board[2][0] == str(curr_player) and curr_board[0][2] == str(curr_player):
                return move

        if move == (2, 2):
            if curr_board[1][1] == str(curr_player) and \
                    curr_board[0][0] == str(curr_player):
                return move

        if move == (2, 0):
            if curr_board[1][1] == str(curr_player) and \
                    curr_board[0][2] == str(curr_player):
                return move

        if move == (0, 2):
            if curr_board[1][1] == str(curr_player) and \
                    curr_board[2][0] == str(curr_player):
                return move
    return legal_moves[int(random.uniform(0, len(legal_moves)))]


def _make_move(board, move, character):
    if character == 'X':
        board[move[0]][move[1]] = "X"
    if character == 'O':
        board[move[0]][move[1]] = "O"
    if character == " ":
        board[move[0]][move[1]] = " "
    return board


def _get_ids(curr_player):
    if curr_player == 'X':
        opponent_id = 2
        opponent = 'O'
        player_id = 1
    else:
        opponent_id = 1
        opponent = 'X'
        player_id = 2
    return [player_id, opponent, opponent_id]


def _minimax_score(board, player):
    winner = main.is_game_over(board)
    if winner == 'X':
        return 10
    elif winner == 'O':
        return -10
    elif winner == 'draw':
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
    else:
        best_score = 100

        for move in _find_legal_moves(board):
            _make_move(board, move, 'O')
            score = _minimax_score(board, 'X')
            _make_move(board, move, " ")
            if score < best_score:
                best_score = score
        return best_score


# X wants max / O wants min
def minimax_ai(board, player):
    if player == 'X':
        best_score = -100
    else:
        best_score = 100
    best_move = None

    for move in _find_legal_moves(board):
        _make_move(board, move, player)
        score = _minimax_score(board, get_opponent(player))
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


def get_opponent(curr_player):
    if curr_player == 'X':
        return 'O'
    else:
        return 'X'
