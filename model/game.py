from abc import ABC, abstractmethod

from model.board import Board
from model.players import Player


class Game(ABC):

    def __init__(self, board_size):
        self.board_size = board_size

    @abstractmethod
    def change_player(self):
        pass

    @abstractmethod
    def is_valid_move(self, row, col):
        pass

    @abstractmethod
    def is_valid_chain(self, start_position, curr_position, direction, curr_player, player_2):
        pass

    @abstractmethod
    def make_a_move(self, row, col, validation):
        pass

    @abstractmethod
    def check_winner(self):
        pass
