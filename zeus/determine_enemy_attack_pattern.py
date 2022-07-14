attack_turns = [10]
attack_turn_diffs = []
# attack_turn_second_diffs = []

def determine_attack_pattern():
    for i in range(0, len(attack_turns) - 1, 1):
        attack_turn_diffs.append(attack_turns[i+1] - attack_turns[i])
    for j in range(0, len(attack_turn_diffs) - 1, 1):
        if attack_turn_diffs[j] != attack_turn_diffs[j+1]:
            return False
    return attack_turn_diffs[0]



    # note index letter
    #     attack_turn_second_diff = attack_turn_diffs[i+1] - attack_turn_diffs[i]
    #     attack_turn_second_diffs.append(attack_turn_second_diff)
    # for k in range(0, len(attack_turn_second_diffs), 1):
    #     attack_turn_second_diffs

print(determine_attack_pattern())
