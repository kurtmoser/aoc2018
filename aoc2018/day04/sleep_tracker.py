import re

class SleepTracker():
    def __init__(self):
        # sleep_data is dict where key is guard id and value is int[60]
        # representing minutes when guard sleeps (list value of 2 means guard
        # slept on 2 different days at that timepoint)
        self.sleep_data = {}

    def load_data(self, data):
        guard_id = 0
        start_minute = 0

        for line in data:
            res = re.search(r'Guard #(\d+) begins shift', line)
            if res:
                guard_id = int(res.group(1))
                continue

            res = re.search(r':(\d+)\] falls asleep', line)
            if res:
                start_minute = int(res.group(1))
                continue

            res = re.search(r':(\d+)\] wakes up', line)
            if res:
                if not guard_id in self.sleep_data:
                    self.sleep_data[guard_id] = []
                    for _ in range(60):
                        self.sleep_data[guard_id].append(0)

                end_minute = int(res.group(1))
                for i in range(start_minute, end_minute):
                    self.sleep_data[guard_id][i] += 1

    def get_biggest_sleeper(self):
        biggest_sleeper = -1
        max_slept_minutes = 0

        for guard_id in self.sleep_data:
            slept_minutes = sum(self.sleep_data[guard_id])
            if slept_minutes > max_slept_minutes:
                biggest_sleeper = guard_id
                max_slept_minutes = slept_minutes

        return biggest_sleeper

    def get_deepest_sleeper(self):
        deepest_sleeper = -1
        max_sleep_depth = 0

        for guard_id in self.sleep_data:
            sleep_depth = max(self.sleep_data[guard_id])
            if sleep_depth > max_sleep_depth:
                deepest_sleeper = guard_id
                max_sleep_depth = sleep_depth

        return deepest_sleeper

    def get_sleepiest_minute(self, guard_id):
        max_sleep_score = max(self.sleep_data[guard_id])
        return self.sleep_data[guard_id].index(max_sleep_score)
