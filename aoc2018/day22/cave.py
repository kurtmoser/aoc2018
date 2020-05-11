class Cave():
    def __init__(self, depth, x, y):
        self.depth = depth
        self.target_x = x
        self.target_y = y
        self.erosion_grid = [[0 for x in range(self.target_x + 50)] for y in range(self.target_y + 50)]

        for y in range(self.target_y + 50):
            for x in range(self.target_x + 50):
                self.erosion_grid[y][x] = self.calculate_cell(x, y)

    def calculate_cell(self, x, y):
        if x == 0 and y == 0:
            geo_index = 0
        elif x == self.target_x and y == self.target_y:
            geo_index = 0
        elif y == 0:
            geo_index = x * 16807
        elif x == 0:
            geo_index = y * 48271
        else:
            geo_index = self.erosion_grid[y][x - 1] * self.erosion_grid[y - 1][x]

        return (geo_index + self.depth) % 20183

    def get_risk_level(self):
        return sum((self.erosion_grid[y][x] % 3) for x in range(self.target_x + 1) for y in range(self.target_y + 1))

    def get_landscape(self, x, y):
        # Landscapes: R - rocky, W - wet, N - narrow
        landscapes = ['R', 'W', 'N']

        return landscapes[self.erosion_grid[y][x] % 3]

    def get_next_gear(self, curr_landscape, next_landscape, curr_gear):
        if curr_landscape == next_landscape:
            return curr_gear

        # Landscapes: R - rocky, W - wet, N - narrow
        # Gears: c - climbing gear, t - torch, n - neither
        next_gear_map = {
            'R': {'W': 'c', 'N': 't'},
            'W': {'R': 'c', 'N': 'n'},
            'N': {'R': 't', 'W': 'n'},
        }

        return next_gear_map[curr_landscape][next_landscape]

    def get_min_path(self):
        # Fill queue with starting coords
        # State contains of x,y coordinates + gear we arrived there with
        visit_queue = [{
            'state': (0, 0, 't'),
            'path': '',
        }]
        visited = []

        while True:
            curr_x, curr_y, curr_gear = visit_queue[0]['state']
            curr_path = visit_queue[0]['path']

            visited.append((curr_x, curr_y, curr_gear))

            if curr_x == self.target_x and curr_y == self.target_y:
                # We reached destination coordinates
                return curr_path

            next_coords = [
                (curr_x, curr_y - 1, 'N'),
                (curr_x - 1, curr_y, 'W'),
                (curr_x + 1, curr_y, 'E'),
                (curr_x, curr_y + 1, 'S'),
            ]

            for next_x, next_y, next_dir in next_coords:
                # Skip out of bounds coordinates
                # coord+50 as longer (around) paths may be quicker due to less
                # time-consuming gear changes needed there
                if next_x < 0 or next_x >= self.target_x + 50:
                    continue
                if next_y < 0 or next_y >= self.target_y + 50:
                    continue

                curr_landscape = self.get_landscape(curr_x, curr_y)
                next_landscape = self.get_landscape(next_x, next_y)
                next_gear = self.get_next_gear(curr_landscape, next_landscape, curr_gear)

                # If switching gear then we want to make our path longer to
                # simulate time it takes to change gear
                if next_gear != curr_gear:
                    delay = next_gear.lower() * 7
                else:
                    delay = ''

                next_path = curr_path + delay + next_dir

                # Special case - make sure we are holding a torch at end coordinates
                if next_x == self.target_x and next_y == self.target_y and next_gear != 't':
                    next_path += 7 * 't'

                visit_queue.append({
                    'state': (next_x, next_y, next_gear),
                    'path': next_path,
                })

            # Remove just worked through path
            visit_queue = visit_queue[1:]

            # Sort remaining paths by length - this is important as some paths
            # contain gear change and are longer in duration then others despite
            # same (or shorter) distance
            visit_queue.sort(key=lambda i: len(i['path']))

            # Remove visited positions from the beginning of queue
            for i in range(len(visit_queue)):
                if not visit_queue[i]['state'] in visited:
                    break
            visit_queue = visit_queue[i:]
