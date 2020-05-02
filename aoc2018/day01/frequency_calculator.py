class FrequencyCalculator():
    def __init__(self):
        self.frequencies = []

    def load_data(self, data):
        self.frequencies = []

        for i in data:
            self.frequencies.append(int(i))

    def get_resulting_frequency(self):
        result = 0

        for frequency in self.frequencies:
            result += frequency

        return result

    def get_repeating_frequency(self):
        visited_frequencies = set()
        curr_frequency = 0
        visited_frequencies.add(curr_frequency)

        while True:
            for frequency in self.frequencies:
                curr_frequency += frequency

                if curr_frequency in visited_frequencies:
                    return curr_frequency

                visited_frequencies.add(curr_frequency)
