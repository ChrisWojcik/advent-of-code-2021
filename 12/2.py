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

def can_visit_cave(cave, small_caves_visited):
  if cave == 'start':
    return False

  if is_small_cave(cave) and \
     2 in small_caves_visited.values() and \
     small_caves_visited[cave] > 0:
      return False

  return True

answer = 0

small_caves_visited = { _:0 for _ in list(filter(is_small_cave, cave_map.keys())) }
small_caves_visited['start'] = 1

q = deque()
q.append(('start', small_caves_visited))

while len(q) > 0:
  tail, small_caves_visited = q.popleft()

  if tail == 'end':
    answer += 1
    continue

  for cave in cave_map[tail]:
    if can_visit_cave(cave, small_caves_visited):
      new_small_caves_visited = small_caves_visited.copy()

      if is_small_cave(cave):
        new_small_caves_visited[cave] += 1

      q.append((cave, new_small_caves_visited))

print(answer)
