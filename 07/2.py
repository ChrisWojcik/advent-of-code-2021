import sys
from collections import Counter
import math

submarines = Counter([int(_) for _ in sys.stdin.read().strip().split(',')])
lowest_fuel_cost = math.inf

def sum_of_consecutive_integers(start, end):
  return end * (start + end) // 2

for target in range(max(submarines)):
  fuel_cost = 0

  for position,count in submarines.items():
    distance = abs(target - position)
    fuel_cost += sum_of_consecutive_integers(1, distance) * count

  lowest_fuel_cost = min(fuel_cost, lowest_fuel_cost)

print(lowest_fuel_cost)
