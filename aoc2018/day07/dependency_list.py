import copy

class DependencyList():
    def __init__(self, data):
        self.deps = {}

        for parent, child in data:
            if not parent in self.deps:
                self.deps[parent] = set()

            if not child in self.deps:
                self.deps[child] = set()

            self.deps[child].add(parent)

    def get_resolve_order(self):
        order = []
        deps = copy.deepcopy(self.deps)

        while True:
            candidates = []

            for i in deps.copy():
                if not deps[i]:
                    candidates.append(i)

            order.append(sorted(candidates)[0])

            i = sorted(candidates)[0]

            del(deps[i])

            for j in deps:
                deps[j].discard(i)

            if not deps:
                return ''.join(order)

    def get_construction_time(self, num_workers, step_time_add=60):
        deps = copy.deepcopy(self.deps)
        workers = {}
        total_time_spent = 0

        while True:
            if workers:
                min_finish_time = min(finish_time for finish_time in workers.values())

                for i in workers.copy():
                    if workers[i] == min_finish_time:
                        del(deps[i])

                        for j in deps:
                            deps[j].discard(i)

                        del(workers[i])

                total_time_spent = min_finish_time

            candidates = []
            for i in deps:
                if not deps[i] and not i in workers:
                    candidates.append(i)
            candidates.sort()

            while len(workers) < num_workers and candidates:
                workers[candidates[0]] = total_time_spent + ord(candidates[0]) - 64 + step_time_add
                candidates = candidates[1:]

            if not deps:
                return total_time_spent
