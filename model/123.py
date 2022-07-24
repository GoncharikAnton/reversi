from reversi_classic_game import ReversiClassicGame
from board import Board

game = ReversiClassicGame(8)

game.board.start_positions()

print(game.make_a_move(2, 4, game.is_valid_move(2, 4, 1, 2)))
print(game.board.mat)

# mat = [[0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 1, 1, 0, 0],
#        [0, 0, 0, 1, 2, 0, 0, 0],
#        [0, 0, 0, 2, 1, 0, 0, 0],
#        [0, 0, 1, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0],
#        [0, 0, 0, 0, 0, 0, 0, 0]]
[0, 0, 0, 0, 0, 0, 0, 0], \
[0, 0, 0, 0, 0, 0, 0, 0], \
[0, 0, 0, 0, 1, 0, 0, 0], \
[0, 0, 0, 1, 1, 0, 0, 0], \
[0, 0, 0, 2, 1, 0, 0, 0], \
[0, 0, 0, 0, 0, 0, 0, 0], \
[0, 0, 0, 0, 0, 0, 0, 0], \
[0, 0, 0, 0, 0, 0, 0, 0]