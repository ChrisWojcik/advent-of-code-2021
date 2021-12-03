import sys

depth = 0
horizontal_position = 0
aim = 0

for line in sys.stdin:
  direction,distance = line.split(' ')
  distance = int(distance)

  if direction == 'forward':
    horizontal_position += distance
    depth += aim * distance
  elif direction == 'down':
    aim += distance
  elif direction == 'up':
    aim -= distance

print(depth * horizontal_position)
