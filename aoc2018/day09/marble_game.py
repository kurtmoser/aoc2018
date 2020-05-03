import collections

class MarbleGame():
    def __init__(self, players, marbles):
        self.players = players
        self.marbles = marbles

    def get_winner_score(self):
        circle = collections.deque()
        circle.append(0)
        circle.append(1)

        scores = collections.defaultdict(int)

        for i in range(2, self.marbles + 1):
            if i % 23:
                circle.rotate(2)
                circle.append(i)
            else:
                circle.rotate(-7)
                scores[i % self.players] += i + circle.pop()

        return(max(scores.values()))
