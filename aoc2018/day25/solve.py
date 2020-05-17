from constellations import Constellations
import os

input_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day25.txt'
with open(filename) as f:
    for line in f:
        input_data.append(list(map(int, line.strip().split(','))))

# Part 1
system = Constellations(input_data)
system.build_constellations()
print(len(system.constellations))
