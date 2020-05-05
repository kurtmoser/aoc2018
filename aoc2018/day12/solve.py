from greenhouse import Greenhouse
import os
import re

filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day12.txt'
with open(filename) as f:
    res = re.search(r'initial state: (.+)', f.readline().strip())
    plants = res.group(1)

    f.readline()

    rules = {}
    for line in f:
        res = re.search(r'(.{5}) => (.{1})', line)
        rules[res.group(1)] = res.group(2)

greenhouse = Greenhouse()
greenhouse.set_rules(rules)

# Part 1
greenhouse.set_plants(plants)
print(greenhouse.evolve(20).get_plants_checksum())

# Part 2
greenhouse.set_plants(plants)
print(greenhouse.evolve(1000).get_plants_checksum() * 50000000)
