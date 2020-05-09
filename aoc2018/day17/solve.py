from water_system import WaterSystem
import os

input_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day17.txt'
with open(filename) as f:
    for line in f:
        input_data.append(line.strip())

water_system = WaterSystem(input_data)

# Part 1
water_system.run_until_overflow()
print(water_system.count_water())

# Part 2
print(water_system.count_still_water())
