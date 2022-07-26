from abc import ABC, abstractmethod


class Game(ABC):
    """Abstract class that represents general methods of the reversi game
    """

    def __init__(self, board_size):
        self.board_size = board_size

    @abstractmethod
    def change_player(self):
        pass

    @abstractmethod
    def is_valid_move(self, row, col):
        pass

    @abstractmethod
    def is_valid_chain(self, start_position, curr_position, direction):
        pass

    @abstractmethod
    def make_a_move(self, row, col, validation):
        pass

    @abstractmethod
    def check_winner(self):
        pass

    @abstractmethod
    def auto_pass(self):
        pass
