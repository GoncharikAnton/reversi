class Board:
    EMPTY_CELL = 0

    def __init__(self, board_size):
        self.board_size = board_size
        self.mat = [[self.EMPTY_CELL] * board_size for _ in range(board_size)]


    def get_cell(self, row, col):
        return self.mat[row][col]

    def update_cell(self, row, col, player):
        self.mat[row][col] = player

    def start_positions(self):
        center = self.board_size // 2
        self.board.mat[center][center] = 1
        self.board.mat[center][center + 1] = 1
        self.board.mat[center + 1][center + 1] = 2
        self.board.mat[center + 1][center] = 2

