# 🕹️ Tic-Tac-Toe 게임

클래식한 틱택토(Tic-Tac-Toe) 게임을 구현한 프로젝트입니다. 터미널에서 2명이 함께 플레이할 수 있습니다.

---

## 📂 프로젝트 구조

```
tic_tac_toe/
┣ utils/
┃ ┣ __init__.py
┃ ┗ validators.py    # 보드 위치 유효성 검사
┣ game/
┃ ┣ __init__.py
┃ ┣ board.py         # 보드 관리 로직 (구현: @hongham)
┃ ┣ game_state.py    # 게임 상태 및 승리/무승부 판별 (구현: @namhegg)
┃ ┗ player.py        # 플레이어 정보 관리
┗ main.py             # 게임 실행 파일
```

---

## 🚀 실행 방법

### 1. 레포지토리 클론
```bash
git clone https://github.com/yourusername/tic_tac_toe.git
cd tic_tac_toe
```

### 2. 가상환경 설정
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. 패키지 설치
```bash
pip install -r requirements.txt
```

### 4. 게임 실행
```bash
python main.py
```

---

## 🎮 게임 설명

- **목표**: `X` 또는 `O`로 가로, 세로, 대각선 중 한 줄을 먼저 완성하면 승리합니다.
- **게임 방법**:
  1. 게임은 Player 1(`X`)부터 시작합니다.
  2. 플레이어는 0~8 사이의 숫자를 입력하여 보드 위치를 선택합니다:
     ```
      0 | 1 | 2
     -----
      3 | 4 | 5
     -----
      6 | 7 | 8
     ```
  3. 각 턴마다 보드가 업데이트됩니다.
  4. 한 플레이어가 승리하거나 보드가 가득 차면 게임이 종료됩니다.

---

## 🛠️ 기여자

- **@namhegg**: `game_state` 구현 (승리 및 무승부 판별 로직)
- **@hongham**: `board` 구현 (보드 상태 및 출력 관리)
- **@ho8ae**: 통합 및 게임 실행 로직

---

## 🌟 게임 예제

```plaintext
Welcome to Tic-Tac-Toe!


  |   |  
-----
  |   |  
-----
  |   |  


Player 1's turn (X):
Enter a position (0-8): 0


X |   |  
-----
  |   |  
-----
  |   |  


Player 2's turn (O):
Enter a position (0-8): 4


X |   |  
-----
  | O |  
-----
  |   |  
```

---

이 문서를 바탕으로 프로젝트를 실행하고 즐겁게 개발하세요! 🎉
