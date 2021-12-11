import sys
import os
import time

STEPS = 100
GRID_SIZE = 0
grid = {}

r = 0

for line in sys.stdin:
  for c, _ in enumerate(line.strip()):
    grid[(r, c)] = int(_)

  r += 1

GRID_SIZE = r

def get_neighbors(cell):
  r,c = cell

  neighbors = [
    (r - 1, c -1),
    (r - 1, c),
    (r - 1, c + 1),
    (r, c - 1),
    (r, c + 1),
    (r + 1, c - 1),
    (r + 1, c),
    (r + 1, c + 1)
  ]

  return list(filter(lambda _: _ in grid.keys(), neighbors))

flashes = 0

def visualization(grid_state):
  FLASHING = '\u001b[46m\u001b[37m'
  ZERO = '\u001b[36m'
  RESET = '\u001b[0m'

  visualization = ''

  for r in range(GRID_SIZE):
    for c in range(GRID_SIZE):
      cell = grid_state[(r,c)]

      if cell > 9:
        visualization += FLASHING + '9' + RESET
      elif cell == 0:
        visualization += ZERO + '0' + RESET
      else:
        visualization += str(cell)

    visualization += '\n'

  return visualization

def to_screen(grid_state):
  os.system('cls' if os.name == 'nt' else 'clear')
  sys.stdout.write(visualization(grid))
  sys.stdout.flush()
  time.sleep(0.005)

for step in range(STEPS):
  cascade = []
  flashed = set()

  to_screen(grid)

  for r in range(GRID_SIZE):
    for c in range(GRID_SIZE):
      grid[(r,c)] += 1

      if grid[(r,c)] > 9:
        cascade.append((r,c))
        flashed.add((r,c))

  to_screen(grid)

  while len(cascade) > 0:
    cell = cascade.pop(0)
    neighbors = get_neighbors(cell)

    for neighbor in neighbors:
      if neighbor not in flashed:
        grid[neighbor] += 1

        if grid[neighbor] > 9:
          cascade.append(neighbor)
          flashed.add(neighbor)

    to_screen(grid)

  for cell in flashed:
    grid[cell] = 0

  flashes += len(flashed)

  to_screen(grid)
  time.sleep(0.1)

print(flashes)
