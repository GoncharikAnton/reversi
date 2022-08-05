import datetime
from copy import deepcopy

from model.board import Board
from model.data_saver import DataSaver
from model.game import Game
from model.players import Player
from model.directions import Directions


class ReversiClassicGame(Game):
    """Represents classic mode of the reversi game.
    """

    def __init__(self, board_size):
        super().__init__(board_size)
        self.board = Board(board_size)
        self.curr_player = Player.X

    def change_player(self):
        """Changes the current player.

        :return: void
        """
        self.curr_player = 3 - self.curr_player

    def is_valid_chain(self, start_position, end_position, direction, current_player, second_player):
        """Checks the chain that starts from start_position and goes by the direction until another players chip.

        :param start_position: list: [row, col]
        :param end_position: list: [row, col]
        :param direction: tuple: (x , y)
        :return: list with valid chain of the move.
        """
        curr_player = current_player
        player_2 = second_player
        chain_list = [[start_position, end_position, direction]]
        for i in range(self.board.board_size):
            if self.board.mat[end_position[0]][end_position[1]] == player_2 \
                    and end_position[0] >= 0 \
                    and end_position[1] >= 0:
                end_position[0] += direction[0]
                end_position[1] += direction[1]
                continue
            elif self.board.mat[end_position[0]][end_position[1]] == curr_player:
                return chain_list

        return []

    def is_valid_move(self, row, col, curr_player=0):
        """Checks the validity of the move.
        :param row: int
        :param col: int
        :return: list with valid chains of moves (e.g.
        [[start_row, start_col][point_row, point_col](direction_x, direction_y)])
        """
        list_of_moves = []
        if curr_player == 0:
            curr_player = self.curr_player
        else:
            curr_player = curr_player
        second_player = 3 - curr_player
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        try:
            curr_position = self.board.mat[row][col]
        except IndexError:
            print('This cell doesn\'t exist')
            return []
        if curr_position != 0:
            return []
        else:
            for i in range(len(directions)):
                try:
                    direction_row, direction_col = directions[i][0], directions[i][1]
                    if (col == self.board_size - 1 and directions[i][1] == 1) \
                            or (col == 0 and directions[i][1] == -1):
                        direction_row, direction_col = directions[i][0], 0

                    if (row == self.board_size - 1 and directions[i][0] == 1) \
                            or (row == 0 and directions[i][0] == -1):
                        direction_row, direction_col = 0, directions[i][1]

                    if (row == self.board_size - 1 and directions[i][0] == 1) and \
                            (col == self.board_size - 1 and directions[i][1] == 1):
                        direction_row, direction_col = 0, 0

                    if (row == 0 and directions[i][0] == -1) \
                            and (col == 0 and directions[i][1] == -1):
                        direction_row, direction_col = 0, 0
                    curr_position = self.board.mat[row + direction_row][col + direction_col]

                    if curr_position == 0:
                        continue
                    elif curr_position == curr_player:
                        continue
                    else:
                        list_of_moves += self.is_valid_chain([row, col], [row + direction_row, col + direction_col],
                                                             directions[i], curr_player, second_player)
                except IndexError:
                    # print(f'INDEX ERROR with direction {directions[i]}')
                    pass
        return list_of_moves

    def make_a_move(self, row, col, list_of_valid_move_chain):
        """Makes a move on the board (updates cells in accordance with current player and validation).

        :param row: int
        :param col: int
        :param list_of_valid_move_chain: list with valid chains of moves.
        [[start_row, start_col][pont_row, point_col](direction_x, direction_y)] ...  [[][]()])
        :return: void
        """
        for i in range(len(list_of_valid_move_chain)):
            start_cell = list_of_valid_move_chain[i][0]
            end_cell = list_of_valid_move_chain[i][1]
            direction = list_of_valid_move_chain[i][2]

            if direction == Directions.D:
                for q in range(start_cell[0], end_cell[0]):
                    self.board.update_cell(q, end_cell[1], self.curr_player)

            elif direction == Directions.U:
                for q in range(start_cell[0], end_cell[0], -1):
                    self.board.update_cell(q, end_cell[1], self.curr_player)

            elif direction == Directions.R:
                for q in range(start_cell[1], end_cell[1]):
                    self.board.update_cell(end_cell[0], q, self.curr_player)

            elif direction == Directions.L:
                for q in range(start_cell[1], end_cell[1], -1):
                    self.board.update_cell(end_cell[0], q, self.curr_player)

            elif direction == Directions.UL:
                tmp_d = start_cell[1]
                for q in range(start_cell[0], end_cell[0], -1):
                    self.board.update_cell(q, tmp_d, self.curr_player)
                    tmp_d -= 1

            elif direction == Directions.DL:
                tmp_d = start_cell[1]
                for q in range(start_cell[0], end_cell[0] + 1):
                    self.board.update_cell(q, tmp_d, self.curr_player)
                    tmp_d -= 1

            elif direction == Directions.DR:
                tmp_d = start_cell[1]
                for q in range(start_cell[0], end_cell[0] + 1):
                    self.board.update_cell(q, tmp_d, self.curr_player)
                    tmp_d += 1

            elif direction == Directions.UR:
                tmp_d = start_cell[1]
                for q in range(start_cell[0], end_cell[0], -1):
                    self.board.update_cell(q, tmp_d, self.curr_player)
                    tmp_d += 1

    def check_winner(self):
        """Checks for the winner.
        If winner -> saves the data with the match by DataSaver into external .txt file.
        :return: list with winner and score
        """
        player1_result = 0
        player2_result = 0
        for i in range(self.board.board_size):
            for j in range(self.board.board_size):
                if self.board.mat[i][j] == 1:
                    player1_result += 1
                elif self.board.mat[i][j] == 2:
                    player2_result += 1
        if player1_result > player2_result:
            DataSaver.data_saver(['Player X win!', 'Score of player 1: ' + str(player1_result),
                                  'Score of player 2: ' + str(player2_result), str(datetime.datetime.now())])
        elif player1_result == player2_result:
            DataSaver.data_saver(['DRAW!', 'Score of player 1: ' + str(player1_result),
                                  'Score of player 2: ' + str(player2_result), str(datetime.datetime.now())])
        else:
            DataSaver.data_saver(['Player O win!', 'Score of player 1: ' + str(player1_result),
                                  'Score of player 2: ' + str(player2_result), str(datetime.datetime.now())])
        return [player1_result, player2_result]

    def auto_pass(self):
        """Checks the board on possible steps. If there are no steps for the current player, returns boolean False.
        :return: boolean
        """
        for i in range(self.board.board_size):
            for j in range(self.board.board_size):
                validation = self.is_valid_move(i, j)
                if len(validation) > 0:
                    return True
        return False
