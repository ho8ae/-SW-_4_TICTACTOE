# 보고서 제출 : TIC TAC TOE

----
4조_오픈소스SW의이해_깃헙프로젝트.pdf  
---- 
김태호 20205151 
<br>
남형석 20195154
<br>
홍성도 20XXXXXX

# 1) 프로젝트소개    
클래식한 틱택토(Tic-Tac-Toe) 게임을 구현한 프로젝트입니다. 터미널에서 2명이 함께 플레이할 수 있습니다.  
## 🎮 게임 설명  
**목표**: `X` 또는 `O`로 가로, 세로, 대각선 중 한 줄을 먼저 완성하면 승리합니다.
**게임 방법**:
 1. 게임은 Player 1(`X`)부터 시작합니다.  
 2. 플레이어는 0~8 사이의 숫자를 입력하여 보드 위치를 선택합니다.  
 3. 각 턴마다 보드가 업데이트됩니다.  
 4. 한 플레이어가 승리하거나 보드가 가득 차면 게임이 종료됩니다  
## 🛠️ 기여자
- **@namhegg**: `game_state` 구현 (승리 및 무승부 판별 로직)
- **@hongham**: `board` 구현 (보드 상태 및 출력 관리)
- **@ho8ae**: 통합 및 게임 실행 로직  
# 2) Milestone  
![마일스톤](https://github.com/user-attachments/assets/840dea96-6b6e-4adf-9e89-298230d1deba)

# 3) Open 상태인 issue  
![open_issue](https://github.com/user-attachments/assets/ceae77ca-7f71-495d-9c61-8c08b9469e4d)

# 4) Closed 상태인 issue  

![closed_issue](https://github.com/user-attachments/assets/ee77926d-38f9-494a-84dd-156297cf2a18)



<br>

# 5) 최종적 Project 보드  
<img width="1502" alt="스크린샷 2024-11-19 오후 1 31 47" src="https://github.com/user-attachments/assets/7de7f5fd-d0ef-458b-8b64-263b2be063dc">
<br>

# 6) Requirements.txt

```
blinker==1.9.0
click==8.1.7
Flask==3.1.0
itsdangerous==2.2.0
Jinja2==3.1.4
MarkupSafe==3.0.2
pygame==2.6.1
Werkzeug==3.1.3
```

<br>

# 7) PR한 기록

<img width="1408" alt="image" src="https://github.com/user-attachments/assets/bd4c0ffb-8e99-40a3-a6cb-f38c7763606f">

<br>
<img width="1400" alt="image" src="https://github.com/user-attachments/assets/7ac7e110-10a6-48d0-9243-4a7f1f9fffd9">

<br>
<img width="1316" alt="image" src="https://github.com/user-attachments/assets/58132c9a-3e26-4171-9fd6-48930b402e7f">


<br>

# 8) 실행화면

<img width="1502" alt="스크린샷 2024-11-19 오후 1 31 47" src="https://github.com/user-attachments/assets/7de7f5fd-d0ef-458b-8b64-263b2be063dc">

# 부록 :
## 질문
```
utils
 ┣ __init__.py
 ┗ validators.py

game
 ┣ __init__.py
 ┣ board.py
 ┣ game_state.py
 ┗ player.py
main.py 이 구조에 맞게 코드 작성해줘
```
## 답변
ChatGPT의 말:
ChatGPT
아래는 요청하신 디렉토리 구조에 맞게 간단한 틱택토(Tic-Tac-Toe) 게임 코드 예제입니다. 이 구조는 모듈화를 통해 각 파일이 명확한 역할을 가지도록 설계되었습니다.

프로젝트 구조
markdown
코드 복사
tic_tac_toe/
┣ utils/
┃ ┣ __init__.py
┃ ┗ validators.py
┣ game/
┃ ┣ __init__.py
┃ ┣ board.py
┃ ┣ game_state.py
┃ ┗ player.py
┗ main.py
1. utils/validators.py
유효성 검사를 처리하는 파일입니다.

python
코드 복사
def validate_position(position, board):
    """Validate if the chosen position is valid and not already taken."""
    if not (0 <= position < len(board)):
        raise ValueError("Position out of range. Choose a valid position.")
    if board[position] != " ":
        raise ValueError("Position already taken. Choose another.")
    return True
2. game/board.py
게임 보드를 관리하는 파일입니다.

python
코드 복사
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
3. game/player.py
플레이어 정보를 관리하는 파일입니다.

python
코드 복사
class Player:
    def __init__(self, name, marker):
        """Initialize a player with a name and a marker (X or O)."""
        self.name = name
        self.marker = marker
4. game/game_state.py
게임 상태를 관리하는 파일입니다.

python
코드 복사
class GameState:
    def __init__(self, board):
        """Initialize the game state with a board."""
        self.board = board

    def check_winner(self):
        """Check if there's a winner."""
        win_positions = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
            [0, 4, 8], [2, 4, 6]              # Diagonals
        ]

        for line in win_positions:
            if (
                self.board[line[0]] == self.board[line[1]] == self.board[line[2]]
                and self.board[line[0]] != " "
            ):
                return self.board[line[0]]  # Return the winner's marker
        return None

    def is_draw(self):
        """Check if the game is a draw."""
        return self.board.is_full() and self.check_winner() is None
5. main.py
게임의 메인 실행 파일입니다.

python
코드 복사
from game.board import Board
from game.player import Player
from game.game_state import GameState
from utils.validators import validate_position

def main():
    board = Board()
    game_state = GameState(board.board)
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
코드 요약
validators.py: 유효성 검사 함수 작성.
board.py: 보드 상태 관리 및 표시.
player.py: 플레이어 클래스 정의.
game_state.py: 승리 조건 및 무승부 확인.
main.py: 게임의 실행 로직.
이 구조를 따라가면 코드가 모듈화되어 유지보수와 확장이 쉽습니다. 필요하면 각 모듈에 더 많은 기능을 추가할 수 있습니다.
