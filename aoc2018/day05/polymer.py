from string import ascii_lowercase

class Polymer():
    def __init__(self, polymer):
        self.polymer = polymer

    def reduce(self):
        reducable_pairs = self._build_reducable_pairs()
        polymer = self.polymer
        polymer_length = len(polymer)

        while True:
            for pair in reducable_pairs:
                polymer = polymer.replace(pair, '')

            if len(polymer) == polymer_length:
                break

            polymer_length = len(polymer)

        return polymer

    def _build_reducable_pairs(self):
        pairs = []

        for char in ascii_lowercase:
            pairs.append(char + char.upper())
            pairs.append(char.upper() + char)

        return pairs
