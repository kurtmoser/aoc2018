class ChocolateMixer():
    def __init__(self, recipes=None):
        if not recipes:
            recipes = [3, 7]

        self.recipes = recipes
        self.elf_1 = 0
        self.elf_2 = 1

    def _create_recipes(self):
        recipe = self.recipes[self.elf_1] + self.recipes[self.elf_2]

        if recipe >= 10:
            self.recipes.append(1)
            self.recipes.append(recipe - 10)
        else:
            self.recipes.append(recipe)

    def _move_elves(self):
        recipes_length = len(self.recipes)

        self.elf_1 = (self.elf_1 + 1 + self.recipes[self.elf_1]) % recipes_length
        self.elf_2 = (self.elf_2 + 1 + self.recipes[self.elf_2]) % recipes_length

    def get_recipes_after(self, idx):
        while len(self.recipes) < (idx + 10):
            self._create_recipes()
            self._move_elves()

        return ''.join(map(str, self.recipes[idx:idx + 10]))

    def count_recipes_before(self, pattern):
        sublist = list(map(int, pattern))

        while True:
            self._create_recipes()
            self._move_elves()

            if self._check_sublist(sublist) > -1:
                return self._check_sublist(sublist)

    def _check_sublist(self, sublist):
        if self.recipes[-(len(sublist) + 1): -1] == sublist:
            return len(self.recipes) - (len(sublist) + 1)

        if self.recipes[-(len(sublist)):] == sublist:
            return len(self.recipes) - len(sublist)

        return -1
