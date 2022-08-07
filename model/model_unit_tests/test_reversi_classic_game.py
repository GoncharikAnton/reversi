import unittest

from model.players import Player
from model.reversi_classic_game import ReversiClassicGame


class TestAiPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.game = ReversiClassicGame(4)

    def test_change_player(self):
        self.game.change_player()
        self.assertEqual(self.game.curr_player, Player.O)

    def test_is_valid_move_with_valid_value(self):
        self.game.board.start_positions()
        lst_of_moves = self.game.is_valid_move(3, 1)
        self.assertEqual(lst_of_moves, [[[3, 1], [1, 1], (-1, 0)]])
        lst_of_moves = self.game.is_valid_move(2, 1)
        self.assertEqual(lst_of_moves, [])
        lst_of_moves = self.game.is_valid_move(25, 10)
        self.assertEqual(lst_of_moves, [])

    def test_is_valid_move_with_invalid_value(self):
        self.game.board.start_positions()
        lst_of_moves = self.game.is_valid_move(25, 10)
        self.assertEqual(lst_of_moves, [])
        lst_of_moves = self.game.is_valid_move(5, 10)
        self.assertEqual(lst_of_moves, [])


    def test_is_valid_chain(self):
        self.game.board.start_positions()
        chain = self.game.is_valid_chain([3, 1], [3 + -1, 1 + 0], (-1, 0), 1, 2)
        self.assertEqual(chain, [[[3, 1], [1, 1], (-1, 0)]])
