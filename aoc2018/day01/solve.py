from frequency_calculator import FrequencyCalculator

input_data = []
with open('input-day01.txt') as f:
    for line in f:
        input_data.append(line.strip())

calc = FrequencyCalculator()
calc.load_data(input_data)

# Part 1

print(calc.get_resulting_frequency())

# Part 2

print(calc.get_repeating_frequency())
