from abc import ABC, abstractmethod

from model.board import Board
from model.game import Game
from model.players import Player
from model.directions import Directions


class ReversiClassicGame(Game):

    def __init__(self, board_size):
        super().__init__(board_size)
        self.board = Board(board_size)
        self.curr_player = Player.B

    def change_player(self):
        self.curr_player = 3 - self.curr_player

    def is_valid_chain(self, start_position, curr_position, direction, curr_player, player_2):
        chain_list = [[start_position, curr_position, direction]]
        for i in range(8):
            if self.board.mat[curr_position[0]][curr_position[1]] == player_2:
                curr_position[0] += direction[0]
                curr_position[1] += direction[1]
                continue
            elif self.board.mat[curr_position[0]][curr_position[1]] == curr_player:
                return chain_list
        return []

    def is_valid_move(self, row, col, curr_player, player_2):
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        curr_position = self.board.mat[row][col]
        flag = []
        if curr_position != 0:
            return flag
        else:
            for i in range(len(directions)):
                curr_position = self.board.mat[row + directions[i][0]][col + directions[i][1]]
                print(self.board.mat)
                if curr_position == 0:
                    continue
                elif curr_position == curr_player:
                    continue
                else:
                    flag += self.is_valid_chain([row, col], [row + directions[i][0], col + directions[i][1]],
                                                directions[i],
                                                curr_player, player_2)
        return flag

    def make_a_move(self, row, col, validation):
        if len(validation) != 0:
            for i in range(len(validation)):
                if validation[i][2] == (1, 0):
                    for q in range(validation[i][0][0], validation[i][1][0]):
                        self.board.update_cell(q, validation[i][1][0], self.curr_player)

            # self.board.update_cell(row, col, self.curr_player)

    def check_winner(self):
        pass
