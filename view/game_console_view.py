from model.game import Game
from view.game_view import GameView
# from model.reversi_classic_game import ReversiClassicGame
from view.board_console_view import BoardConsoleView
from view.board_view import BoardView


class GameConsoleView(GameView):
    """Represents console view of the game"""

    def __init__(self, game: Game):
        super().__init__(game)
        self.board_view = BoardConsoleView(game.board)

    def display_rules(self):
        print('Rules of the game:\n'
              'Each piece played must be laid adjacent to an opponent\'s piece so \nthat the opponent\'s '
              'piece or a row of opponent\'s pieces is flanked by the new piece and \nanother piece of '
              'the player\'s colour. All of the opponent\'s pieces between these two \npieces are \'captured\' '
              'and turned over to match the player\'s colour.\n')

    def get_move(self):
        """Returns the move, that the player passed.

        :return: int:row, int:col
        """
        flag = True
        while flag:
            try:
                s = input(f'Player {self.game.curr_player}, enter your move (row, col):').split(',')
                row, col = abs(int(s[0])) - 1, abs(int(s[1])) - 1
                flag = False
            except IndexError:
                print('Entered value is not valid, try again...')
            except ValueError:
                print('Entered value is not valid, try again...')
        return row, col

    def draw_board(self):
        """Draw the board from self.board"""
        self.board_view.draw_board()

    def display_winner(self, players):
        if players[0] > players[1]:
            print('Player X win!')
        else:
            print('Player O win!')

    def msg_wrong_move(self):
        print('This cell is not valid, try again')
