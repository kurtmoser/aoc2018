import collections

class Greenhouse():
    def __init__(self):
        pass

    def set_rules(self, rules):
        self.rules = collections.defaultdict(lambda:'.', rules)

        return self

    def set_plants(self, plants):
        self.start_pos = 0
        self.plants = plants

        return self

    def evolve(self, steps=1):
        # If steps > 1 then call itself steps times and return immediately
        if steps > 1:
            for i in range(steps):
                self.evolve()

            return self

        plants = '....' + self.plants + '....'
        evolved = ''

        for i in range(len(plants) - 4):
            evolved += self.rules[plants[i:i + 5]]

        self.start_pos -= 2
        while evolved[0] == '.':
            evolved = evolved[1:]
            self.start_pos += 1

        self.plants = evolved.rstrip('.')

        return self

    def get_plants_checksum(self):
        res = 0

        for i in range(len(self.plants)):
            if self.plants[i] == '#':
                res += i + self.start_pos

        return res
