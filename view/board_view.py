from abc import ABC, abstractmethod
from model.board import Board


class BoardView(ABC):
    """Abstract class that represents general methods of the board view"""
    def __init__(self, board: Board):
        self.board = board

    @abstractmethod
    def draw_board(self):
        pass
