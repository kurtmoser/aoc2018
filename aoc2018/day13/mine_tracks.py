class MineTracks():
    def __init__(self, data):
        self.grid = []
        self.carts = []
        self.collisions = {}

        for y, line in enumerate(data):
            grid_row = list(line)

            for x, value in enumerate(grid_row):
                if value == '>':
                    grid_row[x] = '-'
                    self._add_cart(x, y, 1, 0)
                elif value == '<':
                    grid_row[x] = '-'
                    self._add_cart(x, y, -1, 0)
                elif value == 'v':
                    grid_row[x] = '|'
                    self._add_cart(x, y, 0, 1)
                elif value == '^':
                    grid_row[x] = '|'
                    self._add_cart(x, y, 0, -1)

            self.grid.append(grid_row)

    def _add_cart(self, x, y, dx, dy):
        self.carts.append({
            'x': x,
            'y': y,
            'dx': dx,
            'dy': dy,
            'state': 0,
        })

    def print_grid(self):
        for line in self.grid:
            print(*line, sep='')

    def move_carts(self):
        self.collisions = {}
        self.carts.sort(key=lambda i: i['y'] * len(self.grid[0]) + i['x'])

        for cart in self.carts:
            self._move_cart(cart)
            self._detect_collisions()

    def _move_cart(self, cart):
        cart['x'] += cart['dx']
        cart['y'] += cart['dy']

        if self.grid[cart['y']][cart['x']] == '/':
            if cart['dx']:
                self._turn_cart_left(cart)
            else:
                self._turn_cart_right(cart)
        elif self.grid[cart['y']][cart['x']] == '\\':
            if cart['dx']:
                self._turn_cart_right(cart)
            else:
                self._turn_cart_left(cart)
        elif self.grid[cart['y']][cart['x']] == '+':
            if cart['state'] == 0:
                self._turn_cart_left(cart)
            elif cart['state'] == 2:
                self._turn_cart_right(cart)

            cart['state'] = (cart['state'] + 1) % 3

    def _turn_cart_left(self, cart):
        rules = {
            (1, 0): (0, -1),
            (0, -1): (-1, 0),
            (-1, 0): (0, 1),
            (0, 1): (1, 0),
        }
        cart['dx'], cart['dy'] = rules[(cart['dx'], cart['dy'])]

    def _turn_cart_right(self, cart):
        rules = {
            (1, 0): (0, 1),
            (0, 1): (-1, 0),
            (-1, 0): (0, -1),
            (0, -1): (1, 0),
        }
        cart['dx'], cart['dy'] = rules[(cart['dx'], cart['dy'])]

    def _detect_collisions(self):
        for i in range(len(self.carts) - 1):
            for j in range(i + 1, len(self.carts)):
                if self.carts[i]['x'] == self.carts[j]['x'] and self.carts[i]['y'] == self.carts[j]['y']:
                    self.collisions[(self.carts[i]['x'], self.carts[j]['y'])] = (i, j)

    def remove_collisions(self):
        to_remove = set()

        for cart_1, cart_2 in self.collisions.values():
            to_remove.add(cart_1)
            to_remove.add(cart_2)

        for cart_id in sorted(to_remove, reverse=True):
            del(self.carts[cart_id])
