import sys

entries = []

for line in sys.stdin:
  patterns,output = line.strip().split(' | ')
  patterns = [''.join(sorted(_)) for _ in patterns.split(' ')]
  output = [''.join(sorted(_)) for _ in output.split(' ')]

  entries.append((patterns, output))

SEGMENTS = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
DIGITS = ['abcefg', 'cf', 'acdeg', 'acdfg', 'bcdf', 'abdfg', 'abdefg', 'acf', 'abcdefg', 'abcdfg']

def difference(string, excluded):
  result = ''
  for char in string:
    if char not in excluded:
      result += char

  return result

def find_keys(fn, dict):
  keys = []
  for k,v in dict.items():
    if fn(k, dict):
      keys.append(k)

  return keys

sum_of_displays = 0

for patterns,output in entries:
  segment_mapping = { _:'' for _ in SEGMENTS }
  digit_mapping = [None for _ in range(10)]
  patterns_with_segment = { _:[] for _ in SEGMENTS }

  for i, pattern in enumerate(patterns):
    length = len(pattern)

    for _ in SEGMENTS:
      if _ in pattern:
        patterns_with_segment[_].append(i)

    if length == len(DIGITS[1]):
      digit_mapping[1] = pattern
    if length == len(DIGITS[4]):
      digit_mapping[4] = pattern
    if length == len(DIGITS[7]):
      digit_mapping[7] = pattern
    if length == len(DIGITS[8]):
      digit_mapping[8] = pattern

  segment_mapping['a'] = difference(digit_mapping[7], digit_mapping[1])
  segment_mapping['b'] = find_keys(lambda k,_: len(_[k]) == 6, patterns_with_segment)[0]
  segment_mapping['f'] = find_keys(lambda k,_: len(_[k]) == 9, patterns_with_segment)[0]
  segment_mapping['e'] = find_keys(lambda k,_: len(_[k]) == 4, patterns_with_segment)[0]
  segment_mapping['c'] = difference(digit_mapping[7], ''.join([segment_mapping['a'], segment_mapping['f']]))
  segment_mapping['d'] = difference(digit_mapping[4], ''.join([segment_mapping['b'], segment_mapping['c'], segment_mapping['f']]))
  segment_mapping['g'] = difference(''.join(SEGMENTS), ''.join(segment_mapping.values()))

  digit_mapping[0] = ''.join(sorted([segment_mapping[_] for _ in DIGITS[0]]))
  digit_mapping[2] = ''.join(sorted([segment_mapping[_] for _ in DIGITS[2]]))
  digit_mapping[3] = ''.join(sorted([segment_mapping[_] for _ in DIGITS[3]]))
  digit_mapping[5] = ''.join(sorted([segment_mapping[_] for _ in DIGITS[5]]))
  digit_mapping[6] = ''.join(sorted([segment_mapping[_] for _ in DIGITS[6]]))
  digit_mapping[9] = ''.join(sorted([segment_mapping[_] for _ in DIGITS[9]]))

  display = 0

  for i in range(4):
    output_digit = output[i]

    for j,digit in enumerate(digit_mapping):
      if output_digit == digit:
        display += pow(10, 3 - i) * j
        break

  sum_of_displays += display

print(sum_of_displays)
