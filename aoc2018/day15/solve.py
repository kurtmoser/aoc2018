from beverage_battle import BeverageBattle
import os

filename = os.path.dirname(os.path.realpath(__file__)) + os.path.sep + 'input-day15.txt'
with open(filename) as f:
    input_data = f.read().strip().split('\n')

# Part 1
battle = BeverageBattle(input_data)
battle.simulate()
print(battle.round * sum(unit['health'] for unit in battle.units))

# Part 2
elf_attack = 3
while True:
    elf_attack += 1
    battle = BeverageBattle(input_data, elf_attack)

    if battle.simulate_until_elf_dies():
        break

print(battle.round * sum(unit['health'] for unit in battle.units))
