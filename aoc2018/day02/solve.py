from box_scanner import BoxScanner
import os

scanner = BoxScanner()
data = []

filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day02.txt'
with open(filename) as f:
    for line in f:
        data.append(line.strip())

# Part 1

two_letter_boxes = 0
three_letter_boxes = 0

for word in data:
    if scanner.is_n_letter_code(word, 2):
        two_letter_boxes += 1
    if scanner.is_n_letter_code(word, 3):
        three_letter_boxes += 1

print(two_letter_boxes * three_letter_boxes)

# Part 2

for i in range(len(data) - 1):
    for j in range(i + 1, len(data)):
        if scanner.codes_differ_by_one(data[i], data[j]):
            for letter in range(len(data[i])):
                if data[i][letter] != data[j][letter]:
                    print(data[i][:letter] + data[i][letter + 1:])
                    break
