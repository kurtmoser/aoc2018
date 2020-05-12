from pandemic import Pandemic
import os

filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day24.txt'
with open(filename) as f:
    input_data = f.read().strip().split('\n')

# Part 1
pandemic = Pandemic(input_data)
pandemic.simulate()
print(sum(group['units'] for group in pandemic.groups))

# Part 2
for immune_system_boost in range(100000):
    pandemic = Pandemic(input_data, immune_system_boost)
    pandemic.simulate()

    if pandemic.get_winner() == 'immune system':
        print(sum(group['units'] for group in pandemic.groups))
        break
