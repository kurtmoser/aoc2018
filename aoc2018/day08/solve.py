from license_node import LicenseNode
import os

input_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day08.txt'
with open(filename) as f:
    input_data = list(map(int, f.readline().strip().split()))

license_node = LicenseNode(input_data)

# Part 1
print(license_node.get_cumulative_metadata_sum())

# Part 2
print(license_node.get_complex_metadata_sum())
