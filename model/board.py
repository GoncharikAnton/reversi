class Board:
    """
    Represents classic board 8x8 for game.
    Board size is flexible.
    """
    EMPTY_CELL = 0

    def __init__(self, board_size=8):
        self.board_size = board_size
        self.mat = [[self.EMPTY_CELL] * board_size for _ in range(board_size)]

    def get_cell(self, row, col):
        """Returns the value of the requested cell.

        :param row: int
        :param col: int
        :return: value of the cell[row][col] on the board
        """
        return self.mat[row][col]

    def update_cell(self, row, col, player):
        """Changes the value of the requested cell on passed player-value.

        :param row: int
        :param col: int
        :param player: int
        :return: void
        """
        self.mat[row][col] = player

    def start_positions(self):
        """Defines the start positions on the board

        :return: void
        """
        center = (self.board_size // 2) - 1
        self.mat[center][center] = 1
        self.mat[center + 1][center + 1] = 1
        self.mat[center][center + 1] = 2
        self.mat[center + 1][center] = 2
