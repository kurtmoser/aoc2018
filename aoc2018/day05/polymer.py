class Polymer():
    def __init__(self, polymer):
        self.polymer = polymer

    def reduce(self):
        stack = []

        for unit in self.polymer:
            if stack and stack[-1] == unit.swapcase():
                stack.pop()
            else:
                stack.append(unit)

        return ''.join(stack)
