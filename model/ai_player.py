from copy import deepcopy

from model.game import Game
from model.players import Player


class AIPlayer:
    DEPTH = 0
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

    @staticmethod
    def find_possible_moves_copy(model, player):
        """Finds possible moves of the AI on the copied board and returns list with moves.

        :return: list with moves
        """
        moves = []
        for i in range(model.board_size):
            for j in range(model.board_size):
                validation = model.is_valid_move(i, j, player)
                if len(validation) > 0:
                    moves.append([validation[0][0], validation[0][1], validation[0][2]])
        return moves

    def choose_move(self, model):
        """Finds and return the most efficient move for AI with minimax algorithm.

        :param model: models of the board and of the game.
        :return: Chosen move: list - [row][col]
        """
        self.list_of_moves = []
        self.find_possible_moves()
        worst_case = -1
        main_move = []
        self.DEPTH = 0
        for move in self.list_of_moves:
            new_model = deepcopy(model)
            new_model.make_a_move(move[0][0], move[0][1], new_model.is_valid_move(move[0][0], move[0][1]))
            board_value = self.minimax(new_model, Player.X, Player.O)
            if board_value > worst_case:
                worst_case = board_value
                main_move = move
            else:
                main_move = move
        return main_move[0]

    def minimax(self, model, max_player, min_player):

        """Recursive function that represents minimax algorithm. It finds the most efficient move of the AI by
        checking all possible game scenarios and returning the weight of each scenario.

        :param model: deep copied model of the game and the board.
        :param max_player:
        :param min_player:
        :return: result - int -  (depends on winner of the last recursive step)
        """
        self.DEPTH += 1
        if self.DEPTH > 86659:
            p1_winner, p2_winner = model.check_winner(flag=False)
            if p1_winner > p2_winner:
                return -1
            elif p2_winner > p1_winner:
                return 1
            elif p1_winner == p2_winner:
                return 0
        if self.board_in_terminal_state(model):
            p1_winner, p2_winner = model.check_winner(flag=False)
            if p1_winner > p2_winner:
                return -1
            elif p2_winner > p1_winner:
                return 1
            elif p1_winner == p2_winner:
                return 0
        values = []
        possible_moves = self.find_possible_moves_copy(model, max_player)
        if possible_moves:
            for move in possible_moves:
                new_model = deepcopy(model)
                new_model.change_player()
                new_model.make_a_move(move[0][0], move[0][1], new_model.is_valid_move(move[0][0], move[0][1]))
                board_value = self.minimax(new_model, min_player, max_player)
                values.append(board_value)
            if Player.X == max_player:
                return max(values)
            else:
                return min(values)
        else:
            p1_winner, p2_winner = model.check_winner(flag=False)
            if p1_winner > p2_winner:
                return -1
            elif p2_winner > p1_winner:
                return 1
            elif p1_winner == p2_winner:
                return 0


    @staticmethod
    def board_in_terminal_state(model):
        """Checks the board for the terminal state (no possible moves for each player).

        :param model: deep copied model of the game and the board.
        :return: void
        """
        for i in range(len(model.board.mat)):
            for j in range(len(model.board.mat)):
                move_p1 = model.is_valid_move(i, j, Player.X)
                move_p2 = model.is_valid_move(i, j, Player.O)
                if move_p1 or move_p2:
                    return False
        return True
