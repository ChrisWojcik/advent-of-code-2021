import sys

def matching_character(char):
  if char == ')':
    return '('
  if char == ']':
    return '['
  if char == '}':
    return '{'
  if char == '>':
    return '<'
  if char == '(':
    return ')'
  if char == '[':
    return ']'
  if char == '{':
    return '}'
  if char == '<':
    return '>'

def is_closing_character(char):
  return char in [')', ']', '}', '>']

point_values = {
  ')': 3,
  ']': 57,
  '}': 1197,
  '>': 25137
}

score = 0

for line in sys.stdin:
  line = line.strip()
  stack = []

  for char in line:
    if is_closing_character(char):
      last_char = None if len(stack) == 0 else stack.pop()

      if last_char != matching_character(char):
        score += point_values[char]
        break
    else:
      stack.append(char)

print(score)
