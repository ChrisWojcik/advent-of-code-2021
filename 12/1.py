import sys
from collections import deque

cave_map = {}

for line in sys.stdin:
  caves = line.strip().split('-')
  cave_map.setdefault(caves[0], set())
  cave_map.setdefault(caves[1], set())
  cave_map[caves[0]].add(caves[1])
  cave_map[caves[1]].add(caves[0])

def is_small_cave(cave):
  return cave.islower()

def can_visit_cave(cave, path):
  small_caves = list(filter(is_small_cave, path))

  if cave in small_caves:
    return False
  else:
    return True

paths = []
q = deque()
q.append(['start'])

while len(q) > 0:
  path = q.popleft()
  tail = path[len(path) - 1]

  if tail == 'end':
    paths.append(path)
    continue

  for cave in cave_map[tail]:
    if can_visit_cave(cave, path):
      new_path = path.copy()
      new_path.append(cave)
      q.append(new_path)

print(len(paths))
