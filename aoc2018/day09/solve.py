from marble_game import MarbleGame
import os
import re

input_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day09.txt'
with open(filename) as f:
    res = re.search(r'(\d+) players; last marble is worth (\d+) points', f.readline())

players = int(res.group(1))
marbles = int(res.group(2))

# Part 1
print(MarbleGame(players, marbles).get_winner_score())

# Part 2
print(MarbleGame(players, marbles * 100).get_winner_score())
