import chess
import random
import os

def start_game():
    """
    Returns chess.Board object
    """
    return chess.Board()


def is_game_over(board: chess.Board):
    """
    Trigger function for determining if game is over
    """

    return board.is_checkmate() or board.is_stalemate() or board.is_repetition() or board.is_insufficient_material() or board.is_fifty_moves()

def game_over_type(board: chess.Board):

    if board.is_checkmate():
        return "checkmate"

    else:
        return "draw"

def make_move(move:str, board: chess.Board):

    try:
        board.push_san(move)

        os.system('clear')
    except ValueError:
        if move == "peek":
            print(board)
        else:
            print("Invalid move")

def bot_move(board):
    possible_moves = list(board.legal_moves)

    return board.san(random.choice(possible_moves))

def game_summary(board: chess.Board):

    os.system('clear')

    end_condition = game_over_type(board)

    if end_condition == "checkmate":
        print("Checkmate")

    elif end_condition == "draw":
        print("Draw")

    move_list = list(board.move_stack)

    board.reset()


    for move in range(len(move_list)//2):

        white_move = board.san(move_list.pop(0))

        board.push_san(white_move)

        black_move = board.san(move_list.pop(0))

        board.push_san(black_move)

        print("{}. {} {}".format(move + 1, white_move, black_move))

    if len(move_list) != 0:

        white_move = board.san(move_list[-1])

        board.push_san(white_move)

        print("{}. {}".format(move + 2, white_move))

    print(board)

if __name__ == '__main__':
    print("Utility classes for blind chess")
