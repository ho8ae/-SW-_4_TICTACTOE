class Board:
    def __init__(self):
        self.board = [[" " for _ in range(3)] for _ in range(3)]

    def display(self):
        for row in self.board:
            print("|".join(row))
            print("-" * 5)

    def update_board(self, row, col, symbol):
        if self.board[row][col] == " ":
            self.board[row][col] = symbol
            return True
        return False

    def is_full(self):
        return all(cell != " " for row in self.board for cell in row)

    def check_winner(self):
        for row in self.board:
            if row[0] == row[1] == row[2] != " ":
                return row[0]

        for col in range(3):
            if self.board[0][col] == self.board[1][col] == self.board[2][col] != " ":
                return self.board[0][col]

        if self.board[0][0] == self.board[1][1] == self.board[2][2] != " ":
            return self.board[0][0]

        if self.board[0][2] == self.board[1][1] == self.board[2][0] != " ":
            return self.board[0][2]

        return None