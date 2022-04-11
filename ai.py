import random


def find_legal_moves(curr_board):
    legal_moves = []
    for i in range(len(curr_board)):
        for x in range(len(curr_board)):
            if curr_board[i][x] == ' ':
                legal_moves.append((i, x))

    return legal_moves

# TODO es werden nur waagerechten auf winning_moves geprüft, vertikale und diagonale hinzufügen!
def find_winning_moves_ai(curr_board, curr_player):
    winning_move = None
    legal_moves = find_legal_moves(curr_board)
    for i in range(len(legal_moves)):
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

    return legal_moves[int(random.uniform(0, 2))]
