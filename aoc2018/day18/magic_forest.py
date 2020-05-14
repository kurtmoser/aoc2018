import copy

class MagicForest():
    def __init__(self, data):
        self.max_x = len(data[0])
        self.max_y = len(data)

        self.grid = [[data[y][x] for x in range(self.max_x)] for y in range(self.max_y)]

    def evolve(self):
        evolved_grid = []

        for y in range(self.max_y):
            row = []

            for x in range(self.max_x):
                row.append(self.get_evolved_cell(x, y))

            evolved_grid.append(row)

        self.grid = evolved_grid
        return self

    def get_evolved_cell(self, x, y):
        trees = 0
        lumberyards = 0
        opens = 0

        for j in range(y - 1, y + 2):
            if j < 0 or j >= self.max_y:
                continue        # Skip of bounds

            for i in range(x - 1, x + 2):
                if i < 0 or i >= self.max_x:
                    continue    # Skip out of bounds

                if i == x and j == y:
                    continue    # Skip itself

                if self.grid[j][i] == '|':
                    trees += 1
                elif self.grid[j][i] == '#':
                    lumberyards += 1
                if self.grid[j][i] == '.':
                    opens += 1

        if self.grid[y][x] == '.' and trees >= 3:
            evolved_cell = '|'
        elif self.grid[y][x] == '|' and lumberyards >= 3:
            evolved_cell = '#'
        elif self.grid[y][x] == '#' and (lumberyards == 0 or trees == 0):
            evolved_cell = '.'
        else:
            evolved_cell = self.grid[y][x]

        return evolved_cell

    def print_grid(self):
        for row in self.grid:
            print(''.join(row))

    def get_resource_value(self):
        trees = 0
        lumberyards = 0
        opens = 0

        for j in range(self.max_y):
            for i in range(self.max_x):
                if self.grid[j][i] == '|':
                    trees += 1
                elif self.grid[j][i] == '#':
                    lumberyards += 1
                if self.grid[j][i] == '.':
                    opens += 1

        return trees * lumberyards

    def evolve_bulk(self, bulk_count):
        # After large number of iterations we will have repeating pattern for
        # resource values. Calculate up to 1000 evolutions, find repeat interval,
        # calculate bulk_count's mod and then evolve forest beyond 1000 until
        # mods match.

        evolve_history = []

        for _ in range(1000):
            self.evolve()
            evolve_history.append(self.get_resource_value())

        evolve_history.reverse()
        interval = evolve_history.index(evolve_history[0], 1)
        mod = bulk_count % interval

        for _ in range(interval - (1000 % interval) + mod):
            self.evolve()
