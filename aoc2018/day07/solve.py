from dependency_list import DependencyList
import os

input_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day07.txt'
with open(filename) as f:
    for line in f:
        splits = line.split()
        input_data.append((splits[1], splits[7]))

deps_list = DependencyList(input_data)

# Part 1
print(deps_list.get_resolve_order())

# Part 2
print(deps_list.get_construction_time(5))
