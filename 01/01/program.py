import sys

num_increases = 0
previous_depth = None

for line in sys.stdin:
  current_depth = int(line)

  if previous_depth and current_depth > previous_depth:
    num_increases += 1

  previous_depth = current_depth

print(num_increases)
