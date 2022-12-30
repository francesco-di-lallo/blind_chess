import chess
import random

class chessBot(object):
    def __init__(self, regime='random'):
        self.regime = regime

    def move(self, board):

        if self.regime == 'random':
            possible_moves = list(board.legal_moves)

            return board.san(random.choice(possible_moves))
        else:
            raise Exception('Non-random bot not implemented')


if __name__ == '__main__':
    print('Chess bot')
