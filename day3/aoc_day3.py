#!/usr/bin/python3

# Calculates manhattan distance between two points.
def manhattan_dist(p1, p2=(0, 0)):
    return abs(p1[0] - p2[0]) + abs(p1[1] - p2[1])

# Traces a single line formed by applying a step to a given coordinate.
def trace_line(step, pos):
    shift = int(step[1:])
    direction = step[0]
    x = pos[0]
    y = pos[1]
    if direction == "D":
        line = [(x, y-j) for j in range(1, shift+1)]
    elif direction == "U":
        line = [(x, y+j) for j in range(1, shift+1)]
    elif direction == "L":
        line = [(x-i, y) for i in range(1, shift+1)]
    elif direction == "R":
        line = [(x+i, y) for i in range(1, shift+1)]
    return line

# Draws a wire formed by following a sequence of steps from a given starting position.
def trace_wire(pos, path):
    wire = []
    for step in path:
        line = trace_line(step, pos)
        pos = line[-1]  # Update pos based on the last point in the line.
        wire += line
    return wire

# Returns a list of intersecting points
def intersect(paths):
    wire1 = trace_wire((0, 0), paths[0]) 
    wire2 = trace_wire((0, 0), paths[1])
    intersect_points = set(wire1) & set(wire2)
    return intersect_points

# Gets the distances travelled by each wire to each of their intersection points.
def intersect_distances(paths):
    wire1 = trace_wire((0, 0), paths[0]) 
    wire2 = trace_wire((0, 0), paths[1])
    intersect_points = intersect(paths)
    point_dict = {point: [None, None] for point in intersect_points}
    for idx, pair in enumerate(wire1):
        if pair in intersect_points:
            point_dict[pair][0] = point_dict[pair][0] or idx+1
    for idx, pair in enumerate(wire2):
        if pair in intersect_points:
            point_dict[pair][1] = point_dict[pair][1] or idx+1
    return point_dict

with open("day3_input.txt", 'r') as file:
    paths = [line.rstrip().split(",") for line in file.readlines()]

print("Part 1: " + str(min(manhattan_dist(cross) for cross in intersect(paths))))
print("Part 2: " + str(min(sum(pair) for pair in intersect_distances(paths).values())))