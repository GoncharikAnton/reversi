from view.game_view import GameView
from model.reversi_classic_game import Game
from model.ai_player import AIPlayer


class GameController:
    """
    Class that manages Game and View.
    """
    def __init__(self, view: GameView, model: Game):
        self.view = view
        self.model = model
        self.ai = AIPlayer(model)

    def run_game(self):
        self.view.display_rules()
        self.model.board.start_positions()
        result = []
        while len(result) == 0:
            self.view.draw_board()

            if self.model.curr_player == 1:
                row, col = self.view.get_move()
            else:
                row, col = self.ai.make_a_move_ai()
            # row, col = self.ai.make_a_move_ai() # with 2 AI
            not_auto_pass = self.model.auto_pass()
            if not_auto_pass:
                validation = self.model.is_valid_move(row, col)
                while len(validation) == 0:
                    self.view.msg_wrong_move()
                    row, col = self.view.get_move()
                    # row, col = self.ai.make_a_move_ai() # with 2 AI
                    validation = self.model.is_valid_move(row, col)
                self.model.make_a_move(row, col, validation)
                self.model.change_player()
            else:
                self.model.change_player()
            result = self.model.check_winner()
            if len(result) > 0:
                self.view.display_winner(result)

