import sys

line_segments = []

for line in sys.stdin:
  end_points = list(map(lambda _: _.split(','), line.strip().split(' -> ')))
  line_segments.append([(int(point[0]), int(point[1])) for point in end_points])

diagram = {}

def intersect_point_on_diagram(point):
  if point in diagram:
    diagram[point] += 1
  else:
    diagram[point] = 1

for line_segment in line_segments:
  x1 = line_segment[0][0]
  y1 = line_segment[0][1]
  x2 = line_segment[1][0]
  y2 = line_segment[1][1]

  rise = y2 - y1
  run = x2 - x1

  if run == 0:
    step = 1 if y2 > y1 else -1

    for y in range(y1, y2 + step, step):
      point = (x1, y)
      intersect_point_on_diagram(point)
  elif rise == 0:
    step = 1 if x2 > x1 else -1

    for x in range(x1, x2 + step, step):
      point = (x, y1)
      intersect_point_on_diagram(point)

def is_point_dangerous(intersections):
  return intersections >= 2

points = diagram.values()

print(len(list(filter(is_point_dangerous, points))))
