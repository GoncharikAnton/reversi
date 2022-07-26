from copy import deepcopy

from model.game import Game


class AIPlayer:
    """
    Class describes a behaviour of the AI-player and its methods.
    """

    def __init__(self, model: Game):
        self.list_of_moves = []
        self.model = model

    def check_score_copy(self, my_model):
        """Checks the score of the AI player on copied board. (MAY BE STATIC)

        :return: int score
        """
        curr_score = 0
        for i in range(my_model.board_size):
            for j in range(my_model.board_size):
                if my_model.board.mat[i][j] == 2:
                    curr_score += 1
        return curr_score

    def check_score(self):
        """Checks the score of the player on original board.

        :return: int score
        """
        curr_score = 0
        for i in range(self.model.board_size):
            for j in range(self.model.board_size):
                if self.model.board.mat[i][j] == 2:
                    curr_score += 1
        return curr_score

    def find_most_efficient_move(self):
        """Finds the most efficient move in self list of moves and returns it.

        :return: list - [row, col]
        """
        step = []
        current_score = self.check_score()
        for i in self.list_of_moves:
            my_model = deepcopy(self.model)
            my_model.make_a_move(i[0][0], i[0][1], my_model.is_valid_move(i[0][0], i[0][1]))
            score = self.check_score_copy(my_model)
            if score >= current_score:
                current_score = score
                step = [i[0][0], i[0][1]]
            # elif score < current_score: # Just for testing with 2 AI
            #     current_score = score
            #     step = [i[0][0], i[0][1]]
            else:
                continue
        return step

    def make_a_move_ai(self):
        """Returns the move of the AI player (after all validations).

        :return: int-row, int-col
        """
        self.list_of_moves = []
        self.find_possible_moves()
        step = self.find_most_efficient_move()
        return step[0], step[1]

    def find_possible_moves(self):
        """Finds possible moves of the AI on the board and returns list with moves.

        :return: list with moves
        """
        for i in range(self.model.board_size):
            for j in range(self.model.board_size):
                validation = self.model.is_valid_move(i, j)
                if len(validation) > 0:
                    self.list_of_moves.append([validation[0][0], validation[0][1], validation[0][2]])
