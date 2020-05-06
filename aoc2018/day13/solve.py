from mine_tracks import MineTracks
import os

input_data = []
filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day13.txt'
with open(filename) as f:
    for line in f:
        input_data.append(line[:-1])

tracks = MineTracks(input_data)

# Part 1
while not tracks.collisions:
    tracks.move_carts()

coords = list(tracks.collisions.keys())[0]
print(','.join(map(str, coords)))

tracks.remove_collisions()

# Part 2
while len(tracks.carts) > 1:
    tracks.move_carts()
    tracks.remove_collisions()

print(str(tracks.carts[0]['x']) + ',' + str(tracks.carts[0]['y']))
