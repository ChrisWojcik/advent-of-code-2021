import sys

depth = 0
horizontal_position = 0

for line in sys.stdin:
  direction,distance = line.split(' ')
  distance = int(distance)

  if direction == 'forward':
    horizontal_position += distance
  elif direction == 'down':
    depth += distance
  elif direction == 'up':
    depth -= distance

print(depth * horizontal_position)
