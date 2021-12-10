import sys
import itertools

entries = []

for line in sys.stdin:
  patterns,output = line.strip().split(' | ')
  patterns = [''.join(sorted(_)) for _ in patterns.split(' ')]
  output = [''.join(sorted(_)) for _ in output.split(' ')]

  entries.append((patterns, output))

SEGMENTS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
DIGITS = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

sum_of_displays = 0

for patterns,output in entries:
  display = 0

  for perm in itertools.permutations(SEGMENTS):
    segment_mapping = { SEGMENTS[i]:perm[i] for i in range(len(SEGMENTS)) }
    digit_mapping = []

    for i in range(10):
      decoded_digit = ''.join(sorted([segment_mapping[_] for _ in DIGITS[i]]))

      if decoded_digit in patterns:
        digit_mapping.append(decoded_digit)

    if len(digit_mapping) != 10:
      continue

    for i in range(4):
      for j,digit in enumerate(digit_mapping):
        if digit == output[i]:
          display += pow(10, 3 - i) * j
          break

  sum_of_displays += display

print(sum_of_displays)
