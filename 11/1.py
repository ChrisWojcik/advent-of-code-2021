import sys

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

for step in range(STEPS):
  cascade = []
  flashed = set()

  for r in range(GRID_SIZE):
    for c in range(GRID_SIZE):
      grid[(r,c)] += 1

      if grid[(r,c)] > 9:
        cascade.append((r,c))
        flashed.add((r,c))

  while len(cascade) > 0:
    cell = cascade.pop(0)
    neighbors = get_neighbors(cell)

    for neighbor in neighbors:
      if neighbor not in flashed:
        grid[neighbor] += 1

        if grid[neighbor] > 9:
          cascade.append(neighbor)
          flashed.add(neighbor)

  for cell in flashed:
    grid[cell] = 0

  flashes += len(flashed)

print(flashes)
