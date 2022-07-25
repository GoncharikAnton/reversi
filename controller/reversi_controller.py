from view.game_view import GameView
from model.reversi_classic_game import ReversiClassicGame


class GameController:
    def __init__(self, view: GameView, model: ReversiClassicGame) -> None:
        self.view = view
        self.model = model

    def run_game(self):
        self.model.board.start_positions()
        while True:
            self.view.draw_board()

            row, col = self.view.get_move()
            validation = self.model.is_valid_move(row, col)
            while len(validation) == 0:
                print('This cell is not valid, try again')
                row, col = self.view.get_move()
            self.model.make_a_move(row, col, validation)
            self.model.change_player()

