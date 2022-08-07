import unittest
from model.board import Board


class TestBoard(unittest.TestCase):
    def setUp(self) -> None:
        self.board = Board(4)

    def test_get_cell_with_valid_index(self):
        cell = self.board.get_cell(1, 1)
        self.assertEqual(cell, 0)
        cell = self.board.get_cell(1, 3)
        self.assertEqual(cell, 0)

    def test_get_cell_with_invalid_index(self):
        with self.assertRaises(IndexError):
            cell = self.board.get_cell(5, 3)

    def test_update_cell_with_valid_index(self):
        self.board.update_cell(1, 1, 1)
        cell = self.board.get_cell(1, 1)
        self.assertEqual(cell, 1)

    def test_update_cell_with_invalid_index(self):
        with self.assertRaises(IndexError):
            self.board.update_cell(4, 3, 1)

    def test_start_positions(self):
        self.board.start_positions()
        cell1 = self.board.get_cell(1, 1)
        cell2 = self.board.get_cell(1, 2)
        cell3 = self.board.get_cell(2, 1)
        cell4 = self.board.get_cell(2, 2)
        self.assertEqual(cell1, 1)
        self.assertEqual(cell2, 2)
        self.assertEqual(cell3, 2)
        self.assertEqual(cell4, 1)

