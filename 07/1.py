import sys
from collections import Counter
import math

submarines = Counter([int(_) for _ in sys.stdin.read().strip().split(',')])
lowest_fuel_cost = math.inf

for target in range(max(submarines)):
  fuel_cost = 0

  for position,count in submarines.items():
    fuel_cost += abs(target - position) * count

  lowest_fuel_cost = min(fuel_cost, lowest_fuel_cost)

print(lowest_fuel_cost)
