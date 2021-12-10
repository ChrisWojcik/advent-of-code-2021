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
  ')': 1,
  ']': 2,
  '}': 3,
  '>': 4
}

scores = []

for line in sys.stdin:
  line = line.strip()
  stack = []
  error = False
  score = 0

  for char in line:
    if is_closing_character(char):
      last_char = None if len(stack) == 0 else stack.pop()

      if last_char != matching_character(char):
        error = True
        break
    else:
      stack.append(char)

  if not error:
    while len(stack) > 0:
      next_char = matching_character(stack.pop())
      score = (score * 5) + point_values[next_char]

    scores.append(score)

scores.sort()
print(scores[len(scores) // 2])
