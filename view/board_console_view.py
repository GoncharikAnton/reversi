from model.board import Board
from view.board_view import BoardView


class BoardConsoleView(BoardView):
    """Represents console view of the board"""

    symbols = {0: ' ', 1: 'X', 2: 'O'}

    def __init__(self, board: Board):
        super().__init__(board)
        self.board = board

    def draw_board(self):
        """Draws the board in the console.

        :return: void
        """
        board_size = self.board.board_size

        for i in range(board_size):
            if i == 0:
                print('\n')
                print('  ', end='')
            print(f'{i + 1}' + ' | ', end='')
        print('\t')
        for i in range(board_size):
            print('+', end='')
            print('---+' * board_size)

            for j in range(board_size):
                cell = self.board.get_cell(i, j)
                print(f'| {self.symbols[cell]} ', end='')
            print(f'| {i+1}')
        print('+' + '---+' * board_size)





