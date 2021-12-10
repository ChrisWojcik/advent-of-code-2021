import sys

heightmap = {}
WIDTH = 0
HEIGHT = 0

i = 0

for line in sys.stdin:
  heights = [int(_) for _ in list(line.strip())]

  for j in range(len(heights)):
    heightmap[(i, j)] = heights[j]

  WIDTH = len(heights)
  i += 1

HEIGHT = i

def get_neighbors(location):
  i,j = location

  above = None if i <= 0 else (i - 1, j)
  below = None if i >= HEIGHT - 1 else (i + 1, j)
  left = None if j <= 0 else (i, j - 1)
  right = None if j >= WIDTH - 1 else (i, j + 1)

  return [above, below, left, right]

def is_lowpoint(location):
  [above, below, left, right] = get_neighbors(location)

  if (above == None or heightmap[above] > heightmap[location]) and \
     (below == None or heightmap[below] > heightmap[location]) and \
     (left == None or heightmap[left] > heightmap[location]) and \
     (right == None or heightmap[right] > heightmap[location]):

     return True
  else:
    return False

low_points = []

for location in heightmap.keys():
  if is_lowpoint(location):
    low_points.append(heightmap[location])

print(sum(low_points) + len(low_points))
