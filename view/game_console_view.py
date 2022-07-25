from model.game import Game
from view.game_view import GameView
# from model.reversi_classic_game import ReversiClassicGame
from view.board_console_view import BoardConsoleView
from view.board_view import BoardView


class GameConsoleView(GameView):
    def __init__(self, game: Game):
        super().__init__(game)
        self.board_view = BoardConsoleView(game.board)

    def display_rules(self):
        print('Rules of the game:\n '
              'Each piece played must be laid adjacent to an opponent\'s piece so that the opponent\'s '
              'piece or a row of opponent\'s pieces is flanked by the new piece and another piece of '
              'the player\'s colour. All of the opponent\'s pieces between these two pieces are \'captured\' '
              'and turned over to match the player\'s colour.')

    def get_move(self):
        s = input(f'Player {self.game.curr_player}, enter your move (row, col):').split(',')
        row, col = int(s[0]) - 1, int(s[1]) - 1
        return row, col

    def draw_board(self):
        self.board_view.draw_board()

    def display_winner(self, player):
        pass
