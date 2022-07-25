from model.board import Board
from model.data_saver import DataSaver
from model.game import Game
from model.players import Player
from model.directions import Directions



class ReversiClassicGame(Game):

    def __init__(self, board_size=8):
        super().__init__(board_size)
        self.board = Board(board_size)
        self.curr_player = Player.X

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

    def is_valid_move(self, row, col):
        curr_player = self.curr_player
        player_2 = 3 - self.curr_player
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1), (-1, -1), (-1, 1), (1, -1), (1, 1)]
        curr_position = self.board.mat[row][col]
        flag = []
        if curr_position != 0:
            return flag
        else:
            try:
                for i in range(len(directions)):
                    curr_position = self.board.mat[row + directions[i][0]][col + directions[i][1]]
                    if curr_position == 0:
                        continue
                    elif curr_position == curr_player:
                        continue
                    else:
                        flag += self.is_valid_chain([row, col], [row + directions[i][0], col + directions[i][1]],
                                                    directions[i],
                                                    curr_player, player_2)
            except IndexError:
                pass
        return flag

    def make_a_move(self, row, col, validation):
        for i in range(len(validation)):
            if validation[i][2] == Directions.D:
                for q in range(validation[i][0][0], validation[i][1][0]):
                    self.board.update_cell(q, validation[i][1][1], self.curr_player)

            elif validation[i][2] == Directions.U:
                for q in range(validation[i][0][0], validation[i][1][0], -1):
                    self.board.update_cell(q, validation[i][1][1], self.curr_player)

            elif validation[i][2] == Directions.R:
                for q in range(validation[i][0][1], validation[i][1][1]):
                    self.board.update_cell(validation[i][1][0], q, self.curr_player)

            elif validation[i][2] == Directions.L:
                for q in range(validation[i][0][1], validation[i][1][1], -1):
                    self.board.update_cell(validation[i][1][0], q, self.curr_player)

            elif validation[i][2] == Directions.UL:
                tmp_d = validation[i][0][1]
                for q in range(validation[i][0][0], validation[i][1][0], -1):
                    self.board.update_cell(q, tmp_d, self.curr_player)
                    tmp_d -= 1

            elif validation[i][2] == Directions.DL:
                tmp_d = validation[i][0][1]
                for q in range(validation[i][0][0], validation[i][1][0] + 1):
                    self.board.update_cell(q, tmp_d, self.curr_player)
                    tmp_d -= 1

            elif validation[i][2] == Directions.DR:
                tmp_d = validation[i][0][1]
                for q in range(validation[i][0][0], validation[i][1][0] + 1):
                    self.board.update_cell(q, tmp_d, self.curr_player)
                    tmp_d += 1

            elif validation[i][2] == Directions.UR:
                tmp_d = validation[i][0][1]
                for q in range(validation[i][0][0], validation[i][1][0], -1):
                    self.board.update_cell(q, tmp_d, self.curr_player)
                    tmp_d += 1

    def check_winner(self):
        player1_result = 0
        player2_result = 0
        for i in range(self.board.board_size):
            for j in range(self.board.board_size):
                if self.board.mat[i][j] == 0:
                    return 0
                elif self.board.mat[i][j] == 1:
                    player1_result += 1
                elif self.board.mat[i][j] == 2:
                    player2_result += 1

        if player1_result > player2_result:
            DataSaver.data_saver(['Player X win!', player1_result, player2_result])
            return ['Player X win!', player1_result, player2_result]
        elif player2_result > player1_result:
            DataSaver.data_saver(['Player O win!', player1_result, player2_result])
            return ['Player O win!', player1_result, player2_result]
        return 0

    def auto_pass(self):
        for i in range(self.board.board_size):
            for j in range(self.board.board_size):
                validation = self.is_valid_move(i, j)
                if len(validation) > 0:
                    return True
        return False
