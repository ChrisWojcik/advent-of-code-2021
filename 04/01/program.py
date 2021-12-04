import sys

lines = []

for line in sys.stdin:
  lines.append(line.rstrip())

numbers_to_call = [num for num in lines[0].split(',')]
boards = []

for i in range(2, len(lines), 6):
  board = {
    'numbers': {},
    'rows': [],
    'winning_number': None
  }

  for row_number in range(0, 5):
    line = lines[i + row_number]
    row = [line[pos:pos+2].strip() for pos in range(0, len(line), 3)]

    for col_number, num in enumerate(row):
      board['numbers'][num] = {
        'row': row_number,
        'col': col_number,
        'marked': False
      }

    board['rows'].append(row)

  boards.append(board)

def bingo_in_row(board, row_number):
  row = board['rows'][row_number]
  unmarked_numbers = list(filter(lambda _: not _['marked'], map(lambda _: board['numbers'][_], row)))

  return len(unmarked_numbers) == 0

def bingo_in_col(board, col_number):
  col = [board['rows'][row_number][col_number] for row_number in range(0, 5)]
  unmarked_numbers = list(filter(lambda _: not _['marked'], map(lambda _: board['numbers'][_], col)))

  return len(unmarked_numbers) == 0

def first_board_to_win(boards, numbers_to_call):
  for called_number in numbers_to_call:
    for board in boards:
      if called_number in board['numbers'].keys():
        number_on_board = board['numbers'][called_number]
        number_on_board['marked'] = True

        row = number_on_board['row']
        col = number_on_board['col']

        if bingo_in_row(board, row) or bingo_in_col(board, col):
          board['winning_number'] = called_number
          return board

def score(winner):
  sum_of_unmarked_numbers = 0

  for (key, value) in winner['numbers'].items():
    if not value['marked']:
      sum_of_unmarked_numbers += int(key)

  return sum_of_unmarked_numbers * int(winner['winning_number'])

print(score(first_board_to_win(boards, numbers_to_call)))
