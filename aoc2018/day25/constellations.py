class Constellations():
    def __init__(self, points):
        self.points = points

    def build_constellations(self):
        self.constellations = []

        for point in self.points:
            in_const = False

            for constellation in self.constellations:
                for const_point in constellation:
                    if self.in_constellation(point, const_point):
                        constellation.append(point)
                        in_const = True
                        break

                if in_const:
                    break

            if not in_const:
                self.constellations.append([point])

        self.merge_constellations()

    def merge_constellations(self):
        for const_1_id in range(len(self.constellations) - 1, 0, -1):
            for const_2_id in range(const_1_id - 1, -1, -1):
                in_const = False

                for point_1 in self.constellations[const_1_id]:
                    for point_2 in self.constellations[const_2_id]:
                        if self.in_constellation(point_1, point_2):
                            self.constellations[const_2_id].extend(self.constellations[const_1_id])
                            del(self.constellations[const_1_id])
                            in_const = True
                            break

                    if in_const:
                        break

                if in_const:
                    break

    def in_constellation(self, point_1, point_2, max_distance=3):
        return sum(abs(point_1[i] - point_2[i]) for i in range(4)) <= max_distance
