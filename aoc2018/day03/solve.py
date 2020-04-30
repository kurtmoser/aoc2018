from canvas import Canvas
import os

input_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day03.txt'
with open(filename) as f:
    for line in f:
        input_data.append(line.strip())

canvas = Canvas()
canvas.add_slices(input_data)

# Part 1
print(canvas.get_overlaps_count())

# Part 2
print(canvas.get_nonoverlapping_claim_id())
