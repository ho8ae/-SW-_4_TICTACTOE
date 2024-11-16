class Board:
    def __init__(self):
        """Initialize a 3x3 tic-tac-toe board."""
        self.board = [" "] * 9

    def display(self):
        """Display the current state of the board."""
        print("\n")
        for row in range(3):
            print(" | ".join(self.board[row * 3:(row + 1) * 3]))
            if row < 2:
                print("-" * 5)
        print("\n")

    def update(self, position, marker):
        """Update the board with the player's marker."""
        self.board[position] = marker

    def is_full(self):
        """Check if the board is full."""
        return " " not in self.board
