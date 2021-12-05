import sys

values = []

for line in sys.stdin:
  values.append(line.strip())

def get_bits_at_position(values, position):
  return list(map(lambda _: _[position], values))

def most_common_bit(bits):
  count_zeroes = bits.count('0')
  count_ones = bits.count('1')

  if count_zeroes > count_ones:
    return '0'
  elif count_ones > count_zeroes:
    return '1'
  else:
    return None

def least_common_bit(bits):
  count_zeroes = bits.count('0')
  count_ones = bits.count('1')

  if count_zeroes < count_ones:
    return '0'
  elif count_ones < count_zeroes:
    return '1'
  else:
    return None

def find_rating(values, comparison_fn, default):
  positions_to_compare = len(values[0])
  remaining_values = values.copy()

  for i in range(positions_to_compare):
    bits_at_position = get_bits_at_position(remaining_values, i)
    target_bit = comparison_fn(bits_at_position) or default
    remaining_values = list(filter(lambda _: _[i] == target_bit, remaining_values))

    if len(remaining_values) == 1:
      return remaining_values[0]

oxygen_generator_rating = find_rating(values, most_common_bit, '1')
co2_scrubber_rating = find_rating(values, least_common_bit, '0')

print(int(oxygen_generator_rating, 2) * int(co2_scrubber_rating, 2))
