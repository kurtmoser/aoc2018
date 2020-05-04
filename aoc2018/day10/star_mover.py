class StarMover():
    def __init__(self, data):
        self.data = data
        self.steps = 0

    def step_forward(self):
        for i in range(len(self.data)):
            self.data[i][0] += self.data[i][2]
            self.data[i][1] += self.data[i][3]

    def step_backward(self):
        for i in range(len(self.data)):
            self.data[i][0] -= self.data[i][2]
            self.data[i][1] -= self.data[i][3]

    def get_corners(self):
        min_x = min(i[0] for i in self.data)
        min_y = min(i[1] for i in self.data)
        max_x = max(i[0] for i in self.data)
        max_y = max(i[1] for i in self.data)

        return [min_x, min_y, max_x, max_y]

    def move_until_minimum_area(self):
        corners = self.get_corners()
        area = (corners[2] - corners[0]) * (corners[3] - corners[1])

        while True:
            self.step_forward()

            corners = self.get_corners()
            new_area = (corners[2] - corners[0]) * (corners[3] - corners[1])

            if new_area >= area:
                self.step_backward()
                return

            self.steps += 1
            area = new_area

    def to_string(self):
        res = ''
        corners = self.get_corners()
        grid = []

        for y in range(corners[1], corners[3] + 1):
            grid.append([])
            for x in range(corners[0], corners[2] + 1):
                grid[y - corners[1]].append(' ')

        for i in self.data:
            grid[i[1] - corners[1]][i[0] - corners[0]] = 'X'

        for y in range(len(grid)):
            for x in range(len(grid[y])):
                res += grid[y][x]
            res += '\n'

        return res[0:-1]    # Strip final newline
