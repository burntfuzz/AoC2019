#!/usr/bin/python3

from collections import defaultdict
import sys

def count_orbits(orbit, depth):
     return depth + sum([count_orbits(o, depth + 1) for o in orbit_children[orbit]])

def find_santa(orbit, visited, count):
     if "SAN" in orbit_children[orbit]:
          print("Part 2: " + str(count))
          sys.exit()
     for o in orbit_neighbors[orbit]:
          if o in visited:
               continue
          find_santa(o, visited+[o], count+1)

with open("day6_input.txt", 'r') as f:
    orbits = [line.strip().split(')') for line in f.readlines()]

orbit_children = defaultdict(list)
orbit_neighbors = defaultdict(set)
for orbit in orbits:
    orbit_children[orbit[0]].append(orbit[1])
    orbit_neighbors[orbit[1]].add(orbit[0])
    orbit_neighbors[orbit[0]].add(orbit[1])
    if orbit[1] == "YOU":
         start = orbit[0]

print("Part 1: " + str(count_orbits("COM", 0)))
find_santa(start, ["YOU"], 0)
