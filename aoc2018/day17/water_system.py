import re

class WaterSystem():
    def __init__(self, data):
        self.min_x = 1e9
        self.min_y = 1e9
        self.max_x = -1e9
        self.max_y = -1e9

        # Find min/max edges of the grid
        for line in data:
            res = re.search(r'^(x|y)=(\d+), (x|y)=(\d+)\.\.(\d+)$', line)
            if res:
                if res.group(3) == 'y':
                    self.min_x = min(self.min_x, int(res.group(2)))
                    self.min_y = min(self.min_y, int(res.group(4)))
                    self.max_x = max(self.max_x, int(res.group(2)))
                    self.max_y = max(self.max_y, int(res.group(5)))
                else:
                    self.min_x = min(self.min_x, int(res.group(4)))
                    self.min_y = min(self.min_y, int(res.group(2)))
                    self.max_x = max(self.max_x, int(res.group(5)))
                    self.max_y = max(self.max_y, int(res.group(2)))

        self.max_x += 1
        self.min_x -= 1

        self.grid = [['.' for x in range(0, self.max_x + 1)] for y in range(0, self.max_y + 1)]

        for line in data:
            res = re.search(r'^(x|y)=(\d+), (x|y)=(\d+)\.\.(\d+)$', line)
            if res:
                if res.group(3) == 'y':
                    for y in range(int(res.group(4)), int(res.group(5)) + 1):
                        self.grid[y][int(res.group(2))] = '#'
                else:
                    for x in range(int(res.group(4)), int(res.group(5)) + 1):
                        self.grid[int(res.group(2))][x] = '#'

        # Starting spring
        self.grid[0][500] = '|'

    def print_grid(self):
        for y in range(0, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                if self.grid[y][x] == '.':
                    print(' ', end='')
                else:
                    print(self.grid[y][x], end='')

            print()

    def flow_down(self):
        flow_change = False

        for y in range(0, self.max_y):
            for x in range(self.min_x, self.max_x + 1):
                if self.grid[y][x] == '|' and self.grid[y + 1][x] == '.':
                    self.grid[y + 1][x] = '|'

                    flow_change = True

        return flow_change

    def fill_horizontally(self):
        for y in range(self.max_y - 1, -1, -1):
            for x in range(self.min_x, self.max_x + 1):
                if self.grid[y][x] != '|':
                    continue

                if self.grid[y + 1][x] != '~' and self.grid[y + 1][x] != '#':
                    continue

                water_type = '~'

                right_x = False
                for i in range(x, self.max_x + 1):
                    if self.grid[y + 1][i] != '#' and self.grid[y + 1][i] != '~':
                        right_x = i + 1
                        water_type = '|'
                        break

                    if self.grid[y][i] == '#':
                        right_x = i
                        break

                left_x = False
                for i in range(x, self.min_x - 1, -1):
                    if self.grid[y + 1][i] != '#' and self.grid[y + 1][i] != '~':
                        left_x = i
                        water_type = '|'
                        break

                    if self.grid[y][i] == '#':
                        left_x = i + 1
                        break

                if left_x == False or right_x == False:
                    continue

                for i in range(left_x, right_x):
                    self.grid[y][i] = water_type

    def count_water(self):
        return self.count_flowing_water() + self.count_still_water()

    def count_flowing_water(self):
        total_count = 0

        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                if self.grid[y][x] == '|':
                    total_count += 1

        return total_count

    def count_still_water(self):
        total_count = 0

        for y in range(self.min_y, self.max_y + 1):
            for x in range(self.min_x, self.max_x + 1):
                if self.grid[y][x] == '~':
                    total_count += 1

        return total_count

    def run_until_overflow(self):
        while True:
            flow_change = self.flow_down()
            self.fill_horizontally()
            if not flow_change:
                break
