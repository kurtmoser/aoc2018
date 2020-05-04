from star_mover import StarMover
import os
import re

input_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day10.txt'
with open(filename) as f:
    for line in f:
        res = re.search(r'position=<([^,]+),([^>]+)> velocity=<([^,]+),([^>]+)>', line)
        input_data.append(list(map(int, res.groups())))

star_mover = StarMover(input_data)

# Part 1
star_mover.move_until_minimum_area()
print(star_mover.to_string())

# Part 2
print(star_mover.steps)
