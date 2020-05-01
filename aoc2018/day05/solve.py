import os
from polymer import Polymer
from string import ascii_lowercase
import time
import re

input_data = ''
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day05.txt'
with open(filename) as f:
    input_data = f.read().strip()

# Part 1
polymer = Polymer(input_data)
print(len(polymer.reduce()))

# Part 2
min_length = 2 ** 32

for letter in ascii_lowercase:
    polymer = Polymer(input_data.replace(letter, '').replace(letter.upper(), ''))
    min_length = min(min_length, len(polymer.reduce()))

print(min_length)
