import random


def random_ai(curr_board, curr_player):
    legal_moves = []
    for i in range(len(curr_board)):
        for x in range(len(curr_board)):
            if curr_board[i][x] == ' ':
                legal_moves.append((i, x))

    return legal_moves[int(random.uniform(0, len(legal_moves)))]
