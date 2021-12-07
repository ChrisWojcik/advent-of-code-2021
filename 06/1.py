import sys

DAYS = 80
school = [int(_) for _ in sys.stdin.read().strip().split(',')]

for day in range(DAYS):
  count_at_day_start = len(school)

  for i in range(count_at_day_start):
    if school[i] == 0:
      school.append(8)
      school[i] = 6
    else:
      school[i] -= 1

print(len(school))
