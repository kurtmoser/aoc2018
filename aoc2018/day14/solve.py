from chocolate_mixer import ChocolateMixer

input_data = 110201

# Part 1
print(ChocolateMixer([3, 7]).get_recipes_after(input_data))

# Part 2
print(ChocolateMixer([3, 7]).count_recipes_before(str(input_data)))
