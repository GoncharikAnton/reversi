from abc import ABC, abstractmethod


class GameView(ABC):
    """Abstract class that represents general methods of the game view"""
    def __init__(self, game) -> None:
        self.game = game

    @abstractmethod
    def display_rules(self):
        pass

    @abstractmethod
    def get_move(self):
        pass

    @abstractmethod
    def draw_board(self):
        pass

    @abstractmethod
    def display_winner(self, player):
        pass
