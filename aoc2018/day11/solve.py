from power_grid import PowerGrid

input_data = 1133

grid = PowerGrid(input_data)

# Part 1
square = grid.find_max_square(3)
print(str(square['x']) + ',' + str(square['y']))

# Part 2
square = grid.find_max_square()
print(str(square['x']) + ',' + str(square['y']) + ',' + str(square['size']))
