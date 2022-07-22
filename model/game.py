from python_project_reversi.model.board import Board
from python_project_reversi.model.players import Player


class Game:

    def __init__(self, board_size, board: Board, plyer: Player):
        self.board_size = board_size
        self.board = board
        self.player = plyer
        self.curr_player = Player.B

    def change_player(self):
        self.curr_player = 3 - self.curr_player

    def is_valid_move(self, row, col):
        is_valid = False
        for i in range(1, self.board_size + 1):

            for j in range(1, self.board_size + 1):
                pass
        return False



    def make_a_move(self, row, col, validation):
        if validation:
            self.board.update_cell(row, col, self.curr_player)
