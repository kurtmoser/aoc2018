from sleep_tracker import SleepTracker
import os

input_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day04.txt'
with open(filename) as f:
    for line in f:
        input_data.append(line.strip())

input_data.sort()
tracker = SleepTracker()
tracker.load_data(input_data)

# Part 1
biggest_sleeper = tracker.get_biggest_sleeper()
sleepiest_minute = tracker.get_sleepiest_minute(biggest_sleeper)
print(biggest_sleeper * sleepiest_minute)

# Part 2
deepest_sleeper = tracker.get_deepest_sleeper()
sleepiest_minute = tracker.get_sleepiest_minute(deepest_sleeper)
print(deepest_sleeper * sleepiest_minute)
