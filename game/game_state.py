class GameState:
    def __init__(self, board):
        """Initialize the game state with a Board object."""
        self.board = board

    def check_winner(self):
        """Check if there's a winner."""
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for line in win_positions:
            b = self.board.board  # Access the Board's internal list
            if b[line[0]] == b[line[1]] == b[line[2]] and b[line[0]] != " ":
                return b[line[0]]  # Return the winner's marker
        return None

    def is_draw(self):
        """Check if the game is a draw."""
        return self.board.is_full() and self.check_winner() is None
