import collections

class MarbleGame():
    def __init__(self, players, marbles):
        self.players = players
        self.marbles = marbles

    def get_winner_score(self):
        marbles = [
            Marble(0),
            Marble(1),
        ]

        # marbles[0].next = marbles[1]
        # marbles[1].next = marbles[0]
        # marbles[0].prev = marbles[1]
        # marbles[1].prev = marbles[0]
        marbles[0].set_next(marbles[1])
        marbles[1].set_next(marbles[0])

        active = marbles[1]
        scores = collections.defaultdict(int)

        for i in range(2, self.marbles + 1):
            if i % 23:
                new_marble = Marble(i)
                new_marble.set_next(active.next.next)
                active = new_marble

                marbles.append(active)
            else:
                for _ in range(7):
                    active = active.prev

                scores[i % self.players] += i + active.value

                active = active.next
                active.prev.remove()

        return(max(scores.values()))

class Marble():
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def set_next(self, next_marble):
        if next_marble.prev:
            next_marble.prev.next = self
            self.prev = next_marble.prev

        self.next = next_marble
        next_marble.prev = self

    def remove(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        del(self)
