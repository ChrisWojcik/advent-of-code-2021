import sys

counts_zeroes = []
counts_ones = []

for line in sys.stdin:
  bits = line.strip()

  for i in range(len(bits)):
    if len(counts_zeroes) == i:
      counts_zeroes.append(0)

    if bits[i] == '0':
      counts_zeroes[i] += 1

    if len(counts_ones) == i:
      counts_ones.append(0)

    if bits[i] == '1':
      counts_ones[i] += 1

gamma_rate = ''
epsilon_rate = ''

for i in range(len(counts_zeroes)):
  if counts_ones[i] > counts_zeroes[i]:
    gamma_rate += '1'
    epsilon_rate += '0'
  elif counts_ones[i] < counts_zeroes[i]:
    gamma_rate += '0'
    epsilon_rate += '1'
  else:
    raise Exception('Two bit positions had equal occurances of 0 and 1')

print(int(gamma_rate, 2) * int(epsilon_rate, 2))
