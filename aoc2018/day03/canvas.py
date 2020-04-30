import collections
import re

class Canvas():
    def __init__(self):
        self.claims = []
        self.areas = collections.defaultdict(int)

    def add_slices(self, slices):
        for i in slices:
            res = re.search(r'^#(\d+) @ (\d+),(\d+): (\d+)x(\d+)', i)
            groups = list(map(int, res.groups()))
            self.claims.append({
                'id': groups[0],
                'x': groups[1],
                'y': groups[2],
                'w': groups[3],
                'h': groups[4],
            })

        self.calculate_canvas()

    def calculate_canvas(self):
        self.areas.clear()

        for claim in self.claims:
            for x in range(claim['x'], claim['x'] + claim['w']):
                for y in range(claim['y'], claim['y'] + claim['h']):
                    key = str(x) + 'x' + str(y)
                    self.areas[key] += 1

    def get_overlaps_count(self):
        overlaps = 0

        for i in self.areas.values():
            if i > 1:
                overlaps += 1

        return overlaps

    def get_nonoverlapping_claim_id(self):
        for claim in self.claims:
            is_correct_claim = True
            for x in range(claim['x'], claim['x'] + claim['w']):
                for y in range(claim['y'], claim['y'] + claim['h']):
                    key = str(x) + 'x' + str(y)

                    if self.areas[key] > 1:
                        is_correct_claim = False
                        break

            if is_correct_claim:
                return claim['id']

        return -1
