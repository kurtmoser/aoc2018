from cave import Cave

input_depth = 4080
input_x = 14
input_y = 785

cave = Cave(input_depth, input_x, input_y)

# Part 1
print(cave.get_risk_level())

# Part 2
print(len(cave.get_min_path()))
