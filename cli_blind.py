import chess
import chess_utils
import os

clear = lambda: os.system('clear')

clear()

board = chess_utils.start_game()

user_colour = chess.WHITE
bot_colour = not user_colour


#######
# Test games
scholars = ["e4", "e5", "Qh5", "Nc6", "Bc4", "Nf6", "Qf7"]
draw_rep = ["e4", "e5", "Ke2", "Ke7",
            "Ke1", "Ke8", "Ke2", "Ke7",
            "Ke1", "Ke8", "Ke2", "Ke7"]
#######
while not chess_utils.is_game_over(board):

    if board.turn == user_colour:
        #user move subprocess
        user_move = draw_rep.pop(0) #input("User to move:")

        chess_utils.make_move(user_move, board)

    else:
        #bot move subprocess

        bot_move = draw_rep.pop(0) #chess_utils.bot_move(board)

        chess_utils.make_move(bot_move, board)

        print(bot_move)

print("GAME SUMMARY")

chess_utils.game_summary(board)
