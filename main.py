from game.board import Board
from game.player import Player
from game.game_state import GameState
from utils.validators import validate_position

def main():
    board = Board()
    game_state = GameState(board)  # Pass the Board object
    player1 = Player("Player 1", "X")
    player2 = Player("Player 2", "O")

    players = [player1, player2]
    current_player_idx = 0

    print("Welcome to Tic-Tac-Toe!")
    board.display()

    while True:
        current_player = players[current_player_idx]
        print(f"{current_player.name}'s turn ({current_player.marker}):")
        try:
            position = int(input("Enter a position (0-8): "))
            validate_position(position, board.board)
            board.update(position, current_player.marker)
            board.display()

            winner = game_state.check_winner()
            if winner:
                print(f"{current_player.name} wins!")
                break

            if game_state.is_draw():
                print("It's a draw!")
                break

            # Switch players
            current_player_idx = 1 - current_player_idx

        except ValueError as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    main()
