#!/usr/bin/python3

from collections import defaultdict

class Orbit:
     def __init__(self, chksum):
          self.chksum = chksum
          self.parent = None
          self.children = []

     def add_child(self, orbit):
          orbit.parent = self
          self.children.append(orbit)

     def print_children(self):
          for c in self.children:
               print(c.chksum, end='')
          print()

def sum_children(orbit, depth):
     return depth + sum([sum_children(c, depth + 1) for c in orbit.children])
          
with open("day6_input_test.txt", 'r') as f:
    orbits = [line.strip().split(')') for line in f.readlines()]

orbital_system = []

orbit_dict = defaultdict(list)
for orbit in orbits:
    orbit_dict[orbit[0]].append(orbit[1])

COM_orbit = None

for key in orbit_dict:      
     orbit = Orbit(key)
     [orbit.add_child(Orbit(c)) for c in orbit_dict[key]]
     orbital_system.append(orbit)
     #print(orbit.chksum)
     #orbit.print_children()
     if orbit.chksum == "COM":
          COM_orbit = orbit

print(sum_children(COM_orbit, 0))





