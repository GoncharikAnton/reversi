import unittest

from model.reversi_classic_game import ReversiClassicGame
from view.game_console_view import GameConsoleView


class TestGameConsoleView(unittest.TestCase):
    def setUp(self) -> None:
        self.game = ReversiClassicGame(4)
        self.view = GameConsoleView(self.game)

    def test_get_move_with_valid_input(self):
        s = self.view.get_move()
        self.assertEqual(s, (0, 0))

    def test_get_opponent_with_valid_input(self):
        s = self.view.get_opponent()
        self.assertEqual(s, 'easy')
