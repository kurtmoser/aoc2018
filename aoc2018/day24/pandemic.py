import re

class Pandemic():
    def __init__(self, data, immune_system_boost=0):
        self.groups = []

        for line in data:
            if line == 'Immune System:':
                group_counter = 1
                group_type = 'immune system'
                continue
            elif line == 'Infection:':
                group_counter = 1
                group_type = 'infection'
                continue

            res = re.search(r'(\d+) units each with (\d+) hit points (.*)with an attack that does (\d+) (.*)damage at initiative (\d+)', line)
            if res:
                immune_to = []
                weak_to = []

                immune_res = re.search(r'immune to ([^;)]*)', res.group(3))
                if immune_res:
                    immune_to = immune_res.group(1).split(', ')

                weak_res = re.search(r'weak to ([^;)]*)', res.group(3))
                if weak_res:
                    weak_to = weak_res.group(1).split(', ')

                group_id = f'{group_type} {group_counter}'
                group_counter += 1

                damage = int(res.group(4))
                if group_type == 'immune system':
                    damage += immune_system_boost

                group = {
                    'id': group_id,
                    'type': group_type,
                    'units': int(res.group(1)),
                    'hit_points': int(res.group(2)),
                    'damage': damage,
                    'damage_type': res.group(5).strip(),
                    'initiative': int(res.group(6)),
                    'immune_to': immune_to,
                    'weak_to': weak_to,
                }

                self.groups.append(group)

    def choose_targets(self):
        self.groups.sort(key=lambda i: (i['units'] * i['damage'] * 1e9) + i['initiative'], reverse=True)

        taken_targets = []
        attack_pairs = []

        for attacker in self.groups:
            # Dead group
            if attacker['units'] == 0:
                continue

            best_target = None
            best_damage = -1

            for target in self.groups:
                # Lots of conditional but this keeps things simple
                if target['type'] == attacker['type']:
                    continue

                if target['units'] == 0:
                    continue

                if target['id'] in taken_targets:
                    continue

                attack_damage = self.calculate_attack_damage(attacker, target)

                if attack_damage == 0:
                    continue

                if attack_damage > best_damage:
                    best_target = target
                    best_damage = attack_damage
                elif attack_damage == best_damage:
                    best_effective_power = best_target['units'] * best_target['damage']
                    curr_effective_power = target['units'] * target['damage']

                    if curr_effective_power > best_effective_power:
                        best_target = target
                        best_damage = attack_damage
                    elif curr_effective_power == best_effective_power:
                        if target['initiative'] > best_target['initiative']:
                            best_target = target
                            best_damage = attack_damage

            if best_target:
                taken_targets.append(best_target['id'])
                attack_pairs.append((attacker, best_target))

        return attack_pairs

    def calculate_attack_damage(self, attacker, target):
        if attacker['type'] == target['type']:
            return 0

        if attacker['damage_type'] in target['immune_to']:
            return 0

        attack_damage = attacker['units'] * attacker['damage']
        if attacker['damage_type'] in target['weak_to']:
            attack_damage *= 2

        return attack_damage

    def perform_attacks(self, attack_pairs):
        attack_pairs.sort(key=lambda i: i[0]['initiative'], reverse=True)

        for attack_pair in attack_pairs:
            attacker, target = attack_pair
            attack_damage = self.calculate_attack_damage(attacker, target)
            kill_count = min(attack_damage // target['hit_points'], target['units'])
            target['units'] -= kill_count

    def attacks_possible(self, attack_pairs):
        for attack_pair in attack_pairs:
            attacker, target = attack_pair
            attack_damage = self.calculate_attack_damage(attacker, target)

            if attack_damage >= target['hit_points']:
                return True

        return False

    def simulate(self):
        while True:
            attack_pairs = self.choose_targets()

            if not self.attacks_possible(attack_pairs):
                break

            self.perform_attacks(attack_pairs)

    def get_winner(self):
        immune_system_remaining = 0
        infection_remaining = 0

        for group in self.groups:
            if group['units'] > 0:
                if group['type'] == 'infection':
                    infection_remaining += 1
                else:
                    immune_system_remaining += 1

        if immune_system_remaining > infection_remaining:
            return 'immune system'
        elif infection_remaining > immune_system_remaining:
            return 'infection'
        else:
            return 'tie'
