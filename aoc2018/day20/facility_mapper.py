import re

class FacilityMapper():
    def __init__(self, data):
        self.regex_path = data

    def decode_regex_paths(self, path, path_limit=0):
        # Get every decoded regex path with at least path_limit length

        depth = 0
        splits = []

        for i, v in enumerate(path):
            if v == '(':
                depth += 1
                if depth == 1:
                    splits.append(i)
            elif v == '|':
                if depth == 1:
                    splits.append(i)
                pass
            elif v == ')':
                depth -= 1
                if depth == 0:
                    splits.append(i)
                    break

        if not splits:
            # We've got fully decoded path
            return [path]

        prefix = path[0:splits[0]]

        reg_parts = []
        for i in range(len(splits) - 1):
            reg_parts.append(path[splits[i] + 1:splits[i + 1]])

        suffix = path[splits[-1] + 1:]

        paths = []
        for i in reg_parts:
            # Skip empty subparts as they are contained already in longer ones.
            # This reduces branching complexity significantly.
            if not i:
                continue

            new_path = prefix + i + suffix

            if len(new_path) < path_limit:
                continue

            paths.extend(self.decode_regex_paths(new_path, path_limit))

        return paths

    def get_child_paths(self, paths, path_limit=0):
        # Get all paths to unique coordinates that source paths lead to or
        # pass through having at least path_limit length

        visited = {}

        for path in paths:
            x = 0
            y = 0

            # Get all visited paths
            for i, v in enumerate(path):
                if v == 'E':
                    x += 1
                elif v == 'W':
                    x -= 1
                elif v == 'S':
                    y += 1
                elif v == 'N':
                    y -= 1

                if not visited.get((x, y), False):
                    visited[(x, y)] = path[:i + 1]

        res = []
        for path in visited.values():
            path = self.normalize_path(path)

            if len(path) >= path_limit:
                res.append(path)

        return res

    def normalize_path(self, path):
        # Remove forward-backward moves from path

        opposites = {
            'N': 'S',
            'S': 'N',
            'W': 'E',
            'E': 'W',
        }
        stack = []

        for direction in path:
            if stack and stack[-1] == opposites[direction]:
                stack.pop()
            else:
                stack.append(direction)

        return ''.join(stack)

    def get_long_paths(self, path_limit=0):
        regex_paths = self.decode_regex_paths(self.regex_path[1:-1], path_limit)
        return self.get_child_paths(regex_paths, path_limit)
