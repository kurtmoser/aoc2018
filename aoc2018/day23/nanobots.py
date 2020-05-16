import re

class Nanobots():
    def __init__(self, bots):
        self.bots = []

        for bot in bots:
            res = re.search(r'pos=<(-?\d+),(-?\d+),(-?\d+)>, r=(\d+)', bot)
            if res:
                bot_data = list(map(int, res.groups()))
                self.bots.append({
                    'pos': (bot_data[0], bot_data[1], bot_data[2]),
                    'range': bot_data[3],
                })

    def count_nanobots_in_range(self, pos, r):
        in_range = 0

        for bot in self.bots:
            if abs(pos[0] - bot['pos'][0]) + abs(pos[1] - bot['pos'][1]) + abs(pos[2] - bot['pos'][2]) <= r:
                in_range += 1

        return in_range

    def get_local_maximums(self, pos1, pos2):
        x1, y1, z1 = pos1
        x2, y2, z2 = pos2

        xd = (x2 - x1) // 100
        yd = (y2 - y1) // 100
        zd = (z2 - z1) // 100

        res = []

        max_pos = (x1, y1, z1)
        for x in range(x1, x2, xd):
            for y in range(y1, y2, yd):
                for z in range(z1, z2, zd):
                    curr_count = self.count_reaching_nanobots((x + xd // 2, y + yd // 2, z + zd // 2))
                    res.append({
                        'pos': (x + xd // 2, y + yd // 2, z + zd // 2),
                        'in_range': curr_count,
                    })

        return res

    def count_reaching_nanobots(self, pos):
        in_range = 0

        for bot in self.bots:
            if abs(pos[0] - bot['pos'][0]) + abs(pos[1] - bot['pos'][1]) + abs(pos[2] - bot['pos'][2]) <= bot['range']:
                in_range += 1

        return in_range

    def get_starting_point_candidates(self):
        # Order nanobot positions by count in range of other nanobots

        candidates = []

        for bot in self.bots:
            count_in_range = self.count_reaching_nanobots(bot['pos'])
            candidates.append({
                'pos': (bot['pos']),
                'in_range': count_in_range,
            })

        candidates.sort(key=lambda i: i['in_range'], reverse=True)

        return candidates

    def get_maximum_point(self, delta=10000000):
        starting_point_candidates = self.get_starting_point_candidates()

        starting_point = starting_point_candidates[0]['pos']

        while True:
            x1 = starting_point[0] - delta // 2
            y1 = starting_point[1] - delta // 2
            z1 = starting_point[2] - delta // 2
            x2 = starting_point[0] + delta // 2
            y2 = starting_point[1] + delta // 2
            z2 = starting_point[2] + delta // 2

            candidate_areas = self.get_local_maximums((x1, y1, z1), (x2, y2, z2))
            candidate_areas.sort(key=lambda i: i['in_range'], reverse=True)
            starting_point = candidate_areas[0]['pos']

            delta = delta // 10
            if delta < 100:
                break

        return candidate_areas[0]['pos']
