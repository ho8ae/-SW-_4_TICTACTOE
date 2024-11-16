from .board import Board
from .player import Player

class GameState:
    def __init__(self, player1, player2):
        self.board = Board()
        self.player1 = player1
        self.player2 = player2
        self.current_player = player1

    def switch_player(self):
        self.current_player = self.player1 if self.current_player == self.player2 else self.player2

    def play_turn(self, row, col):
        if self.board.update_board(row, col, self.current_player.symbol):
            winner = self.board.check_winner()
            self.switch_player()
            return winner
        return None