from model.reversi_classic_game import ReversiClassicGame
from view.game_console_view import GameConsoleView
from controller.reversi_controller import GameController


model = ReversiClassicGame(board_size=4)
view = GameConsoleView(model)

controller = GameController(view, model)

controller.run_game()
