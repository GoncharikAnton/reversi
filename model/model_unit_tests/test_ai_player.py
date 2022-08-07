import unittest

from model.reversi_classic_game import ReversiClassicGame
from model.ai_player import AIPlayer


class TestAiPlayer(unittest.TestCase):
    def setUp(self) -> None:
        self.game = ReversiClassicGame(4)
        self.ai = AIPlayer(self.game)

    def test_check_score_and_copy(self):
        self.game.board.start_positions()
        score = self.ai.check_score_copy(self.game)
        self.assertEqual(score, 2)
        score2 = self.ai.check_score()
        self.assertEqual(score2, 2)

    def test_check_score_and_copy_with_empty_board(self):
        score = self.ai.check_score_copy(self.game)
        self.assertEqual(score, 0)
        score2 = self.ai.check_score()
        self.assertEqual(score2, 0)

    def test_find_possible_moves(self):
        self.game.board.start_positions()
        self.ai.find_possible_moves()
        count_of_moves = len(self.ai.list_of_moves)
        self.assertEqual(count_of_moves, 4)
