import sys

entries = []

for line in sys.stdin:
  patterns,output = line.strip().split(' | ')
  patterns = patterns.split(' ')
  output = output.split(' ')

  entries.append((patterns, output))

DIGITS = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

count = 0

for patterns,output in entries:
  for digit in output:
    segment_count = len(digit)

    if segment_count == len(DIGITS[1]) or \
       segment_count == len(DIGITS[4]) or \
       segment_count == len(DIGITS[7]) or \
       segment_count == len(DIGITS[8]):

       count += 1

print(count)
