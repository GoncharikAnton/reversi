from view.game_view import GameView
from model.reversi_classic_game import Game
from model.ai_player import AIPlayer

class GameController:
    def __init__(self, view: GameView, model: Game) -> None:
        self.view = view
        self.model = model
        self.ai = AIPlayer(model)

    def run_game(self):
        self.model.board.start_positions()
        while len(self.model.check_winner()) == 0:
            self.view.draw_board()

            # if self.model.curr_player == 1:
            #     row, col = self.view.get_move()
            # else:
            #     row, col = self.ai.make_a_move_ai()
            row, col = self.ai.make_a_move_ai()
            not_auto_pass = self.model.auto_pass()
            if not_auto_pass:
                validation = self.model.is_valid_move(row, col)
                while len(validation) == 0:
                    # print('This cell is not valid, try again')
                    # row, col = self.view.get_move()
                    row, col = self.ai.make_a_move_ai()
                    validation = self.model.is_valid_move(row, col)
                self.model.make_a_move(row, col, validation)
                self.model.change_player()
            else:
                self.model.change_player()
            self.model.check_winner()




