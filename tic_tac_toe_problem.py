
class TicTacToe:
    def __init__(self, board, player, opponent):
        """
        :param board: 3x3 list representing the Tic-Tac-Toe board
        :param player: Symbol for the current player (e.g., 'X')
        :param opponent: Symbol for the opponent (e.g., 'O')
        """
        self.board = board
        self.player = player
        self.opponent = opponent

    def is_open_line(self, line, symbol):
        """Check if a line (row, column, or diagonal) is open for a given symbol."""
        return all(cell == symbol or cell == '_' for cell in line)

    def calculate_heuristic(self):
        """Calculate the heuristic value e(p) for the current board."""
        open_for_player = 0
        open_for_opponent = 0

        # Check rows
        for row in self.board:
            if self.is_open_line(row, self.player):
                open_for_player += 1
            if self.is_open_line(row, self.opponent):
                open_for_opponent += 1

        # Check columns
        for col in range(3):
            column = [self.board[row][col] for row in range(3)]
            if self.is_open_line(column, self.player):
                open_for_player += 1
            if self.is_open_line(column, self.opponent):
                open_for_opponent += 1

        # Check diagonals
        diagonal1 = [self.board[i][i] for i in range(3)]
        diagonal2 = [self.board[i][2 - i] for i in range(3)]
        if self.is_open_line(diagonal1, self.player):
            open_for_player += 1
        if self.is_open_line(diagonal1, self.opponent):
            open_for_opponent += 1
        if self.is_open_line(diagonal2, self.player):
            open_for_player += 1
        if self.is_open_line(diagonal2, self.opponent):
            open_for_opponent += 1

        # Calculate heuristic value
        return open_for_player - open_for_opponent

    def display_board(self):
        """Display the current board."""
        for row in self.board:
            print(' '.join(row))


# Define the board and players
board = [
    ['X', '_', 'O'],
    ['_', 'X', '_'],
    ['O', '_', '_']
]

# Initialize TicTacToe with the current board, player, and opponent
tic_tac_toe = TicTacToe(board, player='X', opponent='O')

# Display the board
print("Current Board:")
tic_tac_toe.display_board()

# Calculate and print the heuristic value
heuristic_value = tic_tac_toe.calculate_heuristic()
print(f"\nHeuristic Value (e(p)): {heuristic_value}")
