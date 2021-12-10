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

def get_uphill_locations(location):
  neighbors = get_neighbors(location)
  uphill_locations = []

  for neighbor in neighbors:
    if neighbor != None and \
       heightmap[neighbor] != 9 and \
       heightmap[neighbor] > heightmap[location]:
      uphill_locations.append(neighbor)

  return uphill_locations

basins = []

for location in heightmap.keys():
  if is_lowpoint(location):
    basin = set()
    locations_to_check = [location]
    checked_locations = set()

    while len(locations_to_check) > 0:
      location_in_basin = locations_to_check.pop(0)
      basin.add(location_in_basin)

      if location_in_basin not in checked_locations:
        checked_locations.add(location_in_basin)

        for neighbor in get_uphill_locations(location_in_basin):
          if neighbor not in basin:
            locations_to_check.append(neighbor)

    basins.append(basin)

COLORS = []
for i in range(0, 16):
  for j in range(0, 16):
    code = str(i * 16 + j)
    COLORS.append("\u001b[48;5;" + code + "m")

RESET = "\u001B[0m"

visualization = ''
locations_in_basins = { location:i for i,basin in enumerate(basins) for location in basin }

for i in range(HEIGHT):
  for j in range(WIDTH):
    location = (i, j)
    height = heightmap[location]
    in_basin = location in locations_in_basins.keys()

    if in_basin:
      basin = locations_in_basins[location]
      visualization += COLORS[basin]+str(height)+RESET
    else:
      visualization += str(height)

  visualization += '\n'

print(visualization)

basin_sizes = [len(basin) for basin in basins]
basin_sizes.sort(reverse = True)
print(basin_sizes[0] * basin_sizes[1] * basin_sizes[2])
