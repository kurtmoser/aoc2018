import collections
import copy

class BeverageBattle():
    def __init__(self, data, elf_attack=3):
        self.grid = []
        self.units = []
        self.round = 0
        self.elf_attack = elf_attack

        for y, line in enumerate(data):
            row = []

            for x, cell in enumerate(list(line)):
                if cell == 'G' or cell == 'E':
                    self.add_unit(cell, x, y)
                    row.append('.')
                else:
                    row.append(cell)

            self.grid.append(row)

    def add_unit(self, race, x, y):
        if race == 'E':
            attack = self.elf_attack
        else:
            attack = 3

        self.units.append({
            'race': race,
            'x': x,
            'y': y,
            'attack': attack,
            'health': 200,
        })

    def find_path(self, start_pos, end_pos, grid=None, visited=None, referrals=None):
        x, y = start_pos

        if not grid:
            grid = copy.deepcopy(self.grid)

        if not visited:
            visited = [start_pos]
            referrals = [None]

        if start_pos == end_pos:
            res = [start_pos]
            tmp = start_pos
            while True:
                if tmp in visited:
                    idx = visited.index(tmp)
                    res.append(referrals[idx])
                    tmp = referrals[idx]
                    if tmp == None:
                        break

            res.reverse()
            return res[1:]

        to_visit = []
        if not (x, y - 1) in visited and grid[y - 1][x] == '.':
            visited.append((x, y - 1))
            referrals.append(start_pos)
        if not (x - 1, y) in visited and grid[y][x - 1] == '.':
            visited.append((x - 1, y))
            referrals.append(start_pos)
        if not (x + 1, y) in visited and grid[y][x + 1] == '.':
            visited.append((x + 1, y))
            referrals.append(start_pos)
        if not (x, y + 1) in visited and grid[y + 1][x] == '.':
            visited.append((x, y + 1))
            referrals.append(start_pos)

        next_index = visited.index(start_pos) + 1
        if next_index >= len(visited):
            return None

        return self.find_path(visited[next_index], end_pos, grid, visited, referrals)

        return None

    def print_grid(self, grid=None):
        res = []

        if not grid:
            grid = copy.deepcopy(self.grid)

        grid = copy.deepcopy(grid)

        for i in self.units:
            grid[i['y']][i['x']] = i['race'].lower()

        for row in grid:
            res.append(''.join(row))

        res = '\n'.join(res)

        print(res)

    def sort_units(self):
        self.units.sort(key=lambda i: i['y'] * len(self.grid[0]) + i['x'])

    def move_unit(self, unit_id):
        unit = self.units[unit_id]

        if unit['health'] <= 0:
            return

        # Check if already adjacent to enemy
        for another_id, another in enumerate(self.units):
            distance = abs(another['x'] - unit['x']) + abs(another['y'] - unit['y'])

            if another['race'] != unit['race'] and distance == 1 and another['health'] > 0:
                return

        unit_grid = copy.deepcopy(self.grid)

        for another_id, another in enumerate(self.units):
            if another['health'] > 0:
                unit_grid[another['y']][another['x']] = '#'

        # Find move spots
        move_spots = []
        for another_id, another in enumerate(self.units):
            if another['race'] == unit['race']:
                continue

            if another['health'] <= 0:
                continue

            if unit_grid[another['y'] - 1][another['x']] == '.':
                move_spots.append((another['x'], another['y'] - 1))
            if unit_grid[another['y']][another['x'] - 1] == '.':
                move_spots.append((another['x'] - 1, another['y']))
            if unit_grid[another['y']][another['x'] + 1] == '.':
                move_spots.append((another['x'] + 1, another['y']))
            if unit_grid[another['y'] + 1][another['x']] == '.':
                move_spots.append((another['x'], another['y'] + 1))

        # Return early if nowhere to move
        if not move_spots:
            return

        # Filter out closest (reachable) move spot
        best_path = None
        for end_pos in move_spots:
            res = self.find_path((unit['x'], unit['y']), end_pos, copy.deepcopy(unit_grid))

            if not res:
                continue

            if not best_path:
                best_path = res
                continue

            if len(res) == len(best_path):
                if (res[-1][1] * 1e9 + res[-1][0]) < (best_path[-1][1] * 1e9 + best_path[-1][0]):
                    best_path = res

            if len(res) < len(best_path):
                best_path = res

        # Still nowhere to move
        if not best_path:
            return

        # Finally move unit
        unit['x'], unit['y'] = best_path[1]

    def attack_neighbors(self, unit_id):
        unit = self.units[unit_id]

        if unit['health'] <= 0:
            return

        targets = []
        for another_id, another in enumerate(self.units):
            distance = abs(another['x'] - unit['x']) + abs(another['y'] - unit['y'])

            if another['race'] != unit['race'] and distance == 1 and another['health'] > 0:
                targets.append(another_id)

        if not targets:
            return

        # Find best target (minimum health, if equal then top-bottom, left-right)
        best_target = self.units[targets[0]]
        for i in targets[1:]:
            new_target = self.units[i]

            if new_target['health'] < best_target['health']:
                best_target = new_target
            elif best_target['health'] == new_target['health']:
                best_priority = best_target['y'] * 1e9 + best_target['x']
                new_priority = new_target['y'] * 1e9 + new_target['x']
                if new_priority < best_priority:
                    best_target = new_target

        best_target['health'] -= unit['attack']
        if best_target['health'] < 0:
            best_target['health'] = 0

    def opponents_exist(self, unit_id):
        unit = self.units[unit_id]

        if unit['health'] <= 0:
            return True

        for another in self.units:
            if another['race'] != unit['race'] and another['health'] > 0:
                return True

        return False

    def simulate(self):
        self.round = 0

        while True:
            self.sort_units()

            for unit_id, unit in enumerate(self.units):
                if not self.opponents_exist(unit_id):
                    return

                self.move_unit(unit_id)
                self.attack_neighbors(unit_id)

            self.round += 1

    def simulate_until_elf_dies(self):
        # Return true if no elf dies, false otherwise

        self.round = 0

        while True:
            self.sort_units()

            for unit_id, unit in enumerate(self.units):
                if unit['race'] == 'E' and unit['health'] <= 0:
                    return False

                if not self.opponents_exist(unit_id):
                    return True

                self.move_unit(unit_id)
                self.attack_neighbors(unit_id)

            self.round += 1
