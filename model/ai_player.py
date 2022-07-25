from copy import deepcopy

from model.game import Game


class AIPlayer:

    def __init__(self, model: Game):
        self.move = set()
        self.list_of_moves = []
        self.player = 2
        self.model = model

    def check_score_copy(self, my_model):
        curr_score = 0
        for i in range(my_model.board_size):
            for j in range(my_model.board_size):
                if my_model.board.mat[i][j] == 2:
                    curr_score += 1
        return curr_score

    def check_score(self):
            curr_score = 0
            for i in range(self.model.board_size):
                for j in range(self.model.board_size):
                    if self.model.board.mat[i][j] == 2:
                        curr_score += 1
            return curr_score

    def find_most_efficient_move(self):
        step = []
        current_score = self.check_score()
        for i in self.list_of_moves:
            my_model = deepcopy(self.model)
            my_model.make_a_move(i[0][0], i[0][1], my_model.is_valid_move(i[0][0], i[0][1]))
            score = self.check_score_copy(my_model)
            if score > current_score:
                current_score = score
                step = [i[0][0], i[0][1]]
            else:
                continue
        return step

    def make_a_move_ai(self):
        self.list_of_moves = []
        self.find_possible_moves()
        step = self.find_most_efficient_move()
        return step[0], step[1]

    def find_possible_moves(self):
        for i in range(self.model.board_size):
            for j in range(self.model.board_size):
                validation = self.model.is_valid_move(i, j)
                if len(validation) > 0:
                    self.list_of_moves.append([validation[0][0], validation[0][1],  validation[0][2]])
