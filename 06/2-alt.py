import sys
from collections import defaultdict,Counter

DAYS = 256
timer_counts = Counter([int(_) for _ in sys.stdin.read().strip().split(',')])
timer_counts = defaultdict(int, timer_counts)

for day in range(DAYS):
  new_counts = defaultdict(int)

  for i in range(9):
    if i == 6:
      new_counts[6] = timer_counts[0] + timer_counts[7]
    elif i == 8:
      new_counts[8] = timer_counts[0]
    else:
      new_counts[i] = timer_counts[i + 1]

  timer_counts = new_counts

print(sum(timer_counts.values()))
