import sys

numbers_to_call = None
board = []
boards = []

for line in sys.stdin:
  line = line.rstrip()

  if numbers_to_call == None:
    numbers_to_call = [int(_) for _ in line.split(',')]
  else:
    if line:
      row = [[int(line[pos:pos+2].strip()), False] for pos in range(0, len(line), 3)]
      board.append(row)
    elif len(board):
      boards.append(board)
      board = []

boards.append(board)
board = None

def bingo(board):
  for i in range(5):
    row = board[i]
    if False not in [_[1] for _ in row]:
      return True

  for i in range(5):
    col = [row[i] for row in board]
    if False not in [_[1] for _ in col]:
      return True

  return False

def mark_square(called_number, board):
  for row in range(5):
    for col in range(5):
      square = board[row][col]

      if square[0] == called_number:
        square[1] = True
        return

def last_board_to_win(boards, numbers_to_call):
  board_won = [False for board in boards]
  winners = []

  for called_number in numbers_to_call:
    for i, board in enumerate(boards):
      if not board_won[i]:
        mark_square(called_number, board)

        if bingo(board):
          board_won[i] = True
          winners.append((called_number, board))

  return winners[len(winners) - 1]

def score(winning_number, winning_board):
  squares_on_board = [square for row in winning_board for square in row]
  sum_of_unmarked_squares = 0

  for row in winning_board:
    for square in row:
      if not square[1]:
        sum_of_unmarked_squares += square[0]

  return winning_number * sum_of_unmarked_squares

winning_number, winning_board = last_board_to_win(boards, numbers_to_call)
print(score(winning_number, winning_board))
