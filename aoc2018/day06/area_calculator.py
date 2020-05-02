class AreaCalculator:
    def __init__(self, points):
        self.points = points

    def _get_minmax_coords(self):
        return [
            min(point[0] for point in self.points),
            min(point[1] for point in self.points),
            max(point[0] for point in self.points),
            max(point[1] for point in self.points),
        ]

    def _get_owner(self, x, y):
        owner = -1
        min_dist = 2 ** 32

        for i in self.points:
            dist = abs(x - i[0]) + abs(y - i[1])
            if dist < min_dist:
                min_dist = dist
                owner = self.points.index(i)

        return owner

    def get_infinite_areas(self):
        min_x, min_y, max_x, max_y = self._get_minmax_coords()
        infinite_areas = set()

        for x in range(min_x, max_x + 1):
            infinite_areas.add(self._get_owner(x, min_y - 1))
            infinite_areas.add(self._get_owner(x, max_y + 1))

        for y in range(min_y, max_y + 1):
            infinite_areas.add(self._get_owner(min_x - 1, y))
            infinite_areas.add(self._get_owner(max_x + 1, y))

        return infinite_areas

    def get_largest_noninfinite_area(self):
        min_x, min_y, max_x, max_y = self._get_minmax_coords()
        infinite_areas = self.get_infinite_areas()
        owners = {}

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                owner = self._get_owner(x, y)

                if owner in infinite_areas:
                    continue

                if not owner in owners:
                    owners[owner] = 0

                owners[owner] += 1

        return max(owners.values())

    def get_central_area(self, max_distance):
        min_x, min_y, max_x, max_y = self._get_minmax_coords()
        central_area = 0

        for y in range(min_y, max_y + 1):
            for x in range(min_x, max_x + 1):
                # Can be optimized by breaking out of loop once max_distance
                # gets exceeded
                distance = sum(abs(x - point[0]) + abs(y - point[1]) for point in self.points)

                if distance < max_distance:
                    central_area += 1

        return central_area
