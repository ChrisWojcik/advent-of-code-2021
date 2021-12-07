import sys

DAYS = 256
school = [int(_) for _ in sys.stdin.read().strip().split(',')]

def memoize(fn):
  memo = {}

  def memozied(*args):
    if args in memo:
      return memo[args]
    else:
      result = fn(*args)
      memo[args] = result
      return result

  return memozied

@memoize
def spawn_fish(timer, days_left):
  count = 1

  for day in range(days_left, 0, -1):
    if timer == 0:
      timer = 6
      count += spawn_fish(8, day - 1)
    else:
      timer -= 1

  return count

total_fish = 0

for fish in school:
  total_fish += spawn_fish(fish, DAYS)

print(total_fish)
