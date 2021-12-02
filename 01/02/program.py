import sys

num_increases = 0
measurements = []

for line in sys.stdin:
  measurement = int(line)
  measurements.append(measurement)
  i = len(measurements) - 1

  if i >= 3:
    current_window_sum = measurements[i] + measurements[i - 1] + measurements[i - 2]
    previous_window_sum = measurements[i - 1] + measurements[i - 2] + measurements[i - 3]

    if current_window_sum > previous_window_sum:
      num_increases += 1

print(num_increases)
