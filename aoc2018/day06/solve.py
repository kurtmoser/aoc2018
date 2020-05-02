from area_calculator import AreaCalculator
import os

input_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day06.txt'
with open(filename) as f:
    for line in f:
        x, y = line.split()
        x = int(x[:-1])
        y = int(y)
        input_data.append((x, y))

calc = AreaCalculator(input_data)

# Part 1
print(calc.get_largest_noninfinite_area())

# Part 2
print(calc.get_central_area(10000))
