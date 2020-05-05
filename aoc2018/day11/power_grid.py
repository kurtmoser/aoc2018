import copy

class PowerGrid():
    def __init__(self, serial_number):
        self.serial_number = serial_number
        self.grid_size = 300

        # Icky oneliner, but lets keep it to comprehend Python syntax capabilities
        self.grid = [[self.calculate_cell(x, y) for y in range(self.grid_size + 1)] for x in range(self.grid_size + 1)]

    def calculate_cell(self, x, y):
        rack_id = x + 10
        power_level_start = rack_id * y
        with_serial = power_level_start + self.serial_number
        multiplied = with_serial * rack_id
        hundreth = (multiplied // 100) % 10
        res = hundreth - 5

        return res

    def find_max_fixed_size_square(self, size):
        power_columns = [0]
        res_power = -2 ** 32
        res_x = -1
        res_y = -1

        for y in range(1, self.grid_size + 1 - size):
            if y == 1:
                for i in range(1, self.grid_size + 1):
                    power_columns.append(sum(self.grid[i][y:y + size]))
            else:
                for i in range(1, self.grid_size + 1):
                    power_columns[i] -= self.grid[i][y - 1]
                    power_columns[i] += self.grid[i][y + size - 1]

            for x in range(1, self.grid_size + 1 - size):
                if x == 1:
                    square_power = sum(power_columns[1:size + 1])
                else:
                    square_power -= power_columns[x - 1]
                    square_power += power_columns[x + size - 1]

                if square_power > res_power:
                    res_power = square_power
                    res_x = x
                    res_y = y

        return({
            'x': res_x,
            'y': res_y,
            'power': res_power,
        })

    def find_max_square(self, size=0):
        if size:
            size_start = size
            size_end = size
        else:
            size_start = 1
            size_end = self.grid_size

        res_power = -2 ** 32
        res_x = -1
        res_y = -1
        res_size = -1

        for i in range(size_start, size_end + 1):
            square = self.find_max_fixed_size_square(i)
            if square['power'] > res_power:
                res_power = square['power']
                res_x = square['x']
                res_y = square['y']
                res_size = i

        return {
            'x': res_x,
            'y': res_y,
            'power': res_power,
            'size': res_size,
        }
