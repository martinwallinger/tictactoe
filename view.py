"""
the view part of the tictactoe game.

Functions:
    render(list)
    select_player(int) -> int
    get_move() -> (int, int) or string
    print_winner(string)
"""


def render(curr_board):
    """
    prints the given board on the commandline.

    :param curr_board: game-board to be printed
    """

    print("   0  1  2")
    print("  ---------")
    print(F"0| {curr_board[0][0]}| {curr_board[0][1]}| {curr_board[0][2]}|")
    print(F"1| {curr_board[1][0]}| {curr_board[1][1]}| {curr_board[1][2]}|")
    print(F"2| {curr_board[2][0]}| {curr_board[2][1]}| {curr_board[2][2]}|")
    print("  ---------")


def select_player(number):
    """
    asks the user what game-mode the specified Player should be in.

    :param number: Player Number (1 or 2)
    :return: Key of the chosen game-mode (1, 2 or 3)
    """
    user_input = None
    print(F"\nSelect Player {number}")
    while user_input not in ('1', '2', '3'):
        user_input = input("type 1 for human, 2 for naive ai or 3 for perfect ai: ")
    return int(user_input)


def get_move():
    """
    asks human player for next move, checks if format of given input is right.

    :return: move the player has entered as tuple or "save"
    """
    print("To save the current game state, enter 'save'")
    move = input("What is your next move?")
    move = move.strip()
    if move == "save":
        return move
    while len(move) != 2 or not move.isnumeric() or not 0 <= int(move[0]) <= 2 or \
            not 0 <= int(move[1]) <= 2:
        move = input("Please repeat your move as two numbers (0 to 2)"
                     " without whitespaces inbetween: ")
        move.strip()
        if move == "save":
            return move
    return int(move[0]), int(move[1])


def print_winner(state):
    """
    Prints the winner or "draw" on the commandline

    :param state: 'draw', 'X' or 'O'
    """
    if state == 'draw':
        print("Game Over! It's a draw")
    else:
        if state == 'X':
            winner = 1
        else:
            winner = 2
        print(F'\nGame Over! Player {winner} has won!')
