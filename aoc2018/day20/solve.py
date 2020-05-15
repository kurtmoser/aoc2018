from facility_mapper import FacilityMapper
import os

filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day20.txt'
with open(filename) as f:
    input_data = f.readline().strip()

mapper = FacilityMapper(input_data)
long_paths = mapper.get_long_paths(1000)

# Part 1
long_paths.sort(key=lambda i: len(i), reverse=True)
print(len(long_paths[0]))

# Part 2
print(len(long_paths))
