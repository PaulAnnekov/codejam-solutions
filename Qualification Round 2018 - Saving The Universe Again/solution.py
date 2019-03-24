# Rationale:
# 1. Each swap of rightmost "C" with "S" to the right of it will decrease damage
#    to 2 ^ [#"C"] / 2
# 2. What decreases damage the most is swapping rightmost "C" with "S" to the
#    right of it

import math

def solve(D, P):
    sum = 0
    strength = 1
    for action in P:
        if action == "C":
            strength = strength * 2
        if action == "S":
            sum = sum + strength
    excess = sum - D
    if excess <= 0:
        return 0
    s_count = 0
    c_list = []
    for action in P[::-1]:
        if action == "S":
            s_count += 1
        if action == "C":
            c_list.append(s_count)
    swaps = 0
    for i, s in enumerate(c_list):
        damage_per_s = 2 ** (len(c_list) - i - 1)
        s_need = math.ceil(excess / damage_per_s)
        if s - s_need >= 0:
            swaps = swaps + s_need
            excess = 0
            break
        else:
            swaps = swaps + s
            excess = excess - s * damage_per_s
    return swaps if excess == 0 else "IMPOSSIBLE"

cases_count = int(input())
for i in range(cases_count):
    D, P = input().split()
    res = solve(int(D), P)
    print('Case #{}: {}'.format(i+1, res))
