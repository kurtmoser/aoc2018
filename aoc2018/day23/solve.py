from nanobots import Nanobots
import os

input_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day23.txt'
with open(filename) as f:
    for line in f:
        input_data.append(line.strip())

system = Nanobots(input_data)

# Part 1
system.bots.sort(key=lambda i: i['range'], reverse=True)
print(system.count_nanobots_in_range(system.bots[0]['pos'], system.bots[0]['range']))

# Part 2
print(sum(system.get_maximum_point()))
