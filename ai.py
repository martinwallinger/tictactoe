import copy
import random
import main


def _find_legal_moves(curr_board):
    legal_moves = []
    for x in range(len(curr_board)):
        for y in range(len(curr_board)):
            if curr_board[x][y] == ' ':
                legal_moves.append((x, y))

    return legal_moves


def _find_winning_moves_ai(curr_board, curr_player):
    legal_moves = _find_legal_moves(curr_board)
    for i in range(len(legal_moves)):
        # vertical
        if legal_moves[i][1] == 0:
            if curr_board[legal_moves[i][0]][legal_moves[i][1] + 1] == str(curr_player) and \
                    curr_board[legal_moves[i][0]][legal_moves[i][1] + 2] == str(curr_player):
                return legal_moves[i]

        elif legal_moves[i][1] == 1:
            if curr_board[legal_moves[i][0]][legal_moves[i][1] - 1] == str(curr_player) and \
                    curr_board[legal_moves[i][0]][legal_moves[i][1] + 1] == str(curr_player):
                return legal_moves[i]

        elif legal_moves[i][1] == 2:
            if curr_board[legal_moves[i][0]][legal_moves[i][1] - 2] == str(curr_player) and \
                    curr_board[legal_moves[i][0]][legal_moves[i][1] - 1] == str(curr_player):
                return legal_moves[i]
        # horizontal
        elif legal_moves[i][1] == 0:
            if curr_board[legal_moves[i][0] + 1][legal_moves[i][1]] == str(curr_player) and \
                    curr_board[legal_moves[i][0] + 2][legal_moves[i][1]] == str(curr_player):
                return legal_moves[i]

        elif legal_moves[i][1] == 1:
            if curr_board[legal_moves[i][0] - 1][legal_moves[i][1]] == str(curr_player) and \
                    curr_board[legal_moves[i][0] + 1][legal_moves[i][1]] == str(curr_player):
                return legal_moves[i]

        elif legal_moves[i][1] == 2:
            if curr_board[legal_moves[i][0] - 2][legal_moves[i][1]] == str(curr_player) and \
                    curr_board[legal_moves[i][0] - 1][legal_moves[i][1]] == str(curr_player):
                return legal_moves[i]
        # diagonal
        elif legal_moves[i] == (0, 0):
            if curr_board[1][1] == str(curr_player) and \
                    curr_board[2][2] == str(curr_player):
                return legal_moves[i]

        elif legal_moves[i] == (1, 1):
            if (curr_board[0][0] == str(curr_player) and curr_board[2][2] == str(curr_player)) \
                    or curr_board[2][0] == str(curr_player) and curr_board[0][2] == str(curr_player):
                return legal_moves[i]

        elif legal_moves[i] == (2, 2):
            if curr_board[1][1] == str(curr_player) and \
                    curr_board[0][0] == str(curr_player):
                return legal_moves[i]

        elif legal_moves[i] == (2, 0):
            if curr_board[1][1] == str(curr_player) and \
                    curr_board[0][2] == str(curr_player):
                return legal_moves[i]

        elif legal_moves[i] == (0, 2):
            if curr_board[1][1] == str(curr_player) and \
                    curr_board[2][0] == str(curr_player):
                return legal_moves[i]
    return legal_moves[int(random.uniform(0, len(legal_moves)))]


def _make_move(board, move, player):
    if player == 'X':
        board[move[0]][move[1]] = "X"
    if player == 'O':
        board[move[0]][move[1]] = "O"
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


def _minmax_score(board, curr_player, player_to_optimize):
    winner = main.is_game_over(board)
    if winner != 0:
        if winner == player_to_optimize:
            return 10
        else:
            return -10
    elif winner == 'draw':
        return 0

    legal_moves = _find_legal_moves(board)

    scores = []
    for move in legal_moves:
        _board = copy.deepcopy(board)
        _make_move(_board, move, curr_player)
        opponent = get_opponent(curr_player)
        score = _minmax_score(_board, opponent, player_to_optimize)
        scores.append(score)

    if curr_player == player_to_optimize:
        return max(scores)
    else:
        return min(scores)


def minmax_ai(curr_board, curr_player):
    best_move = None
    best_score = None

    for move in _find_legal_moves(curr_board):
        _board = copy.deepcopy(curr_board)
        _make_move(curr_player, _board, move)

        opp = get_opponent(curr_player)
        score = _minmax_score(_board, opp, curr_player)
        if best_score is None or score > best_score:
            best_move = move
            best_score = score

    return best_move


def get_opponent(curr_player):
    if curr_player == 'X':
        return 'O'
    else:
        return 'X'
