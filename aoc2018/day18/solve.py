from magic_forest import MagicForest
import os

input_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day18.txt'
with open(filename) as f:
    for line in f:
        input_data.append(line.strip())

# Part 1
forest = MagicForest(input_data)
[forest.evolve() for i in range(10)]
print(forest.get_resource_value())

# Part 2
forest = MagicForest(input_data)
forest.evolve_bulk(1000000000)
print(forest.get_resource_value())
