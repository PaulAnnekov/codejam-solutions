# Rationale:
# 1. You can always evacuate senator from party with the most members.
# 2. If only 3 senators left in 3 parties, evacuate only one of them.

def pop_highest(buckets, check):
    if len(buckets) == 0:
        return ""
    if check and len(buckets) == 1 and len(buckets[0]["p"]) == 2:
        return ""
    highest = buckets[0]["p"].pop(0)
    if buckets[0]["s"] != 1:
        if len(buckets) > 1 and buckets[1]["s"] == buckets[0]["s"]-1:
            buckets[1]["p"].append(highest)
        else:
            buckets.insert(1, {"p": [highest], "s": buckets[0]["s"]-1})
    if len(buckets[0]["p"]) == 0:
        del buckets[0]
    return highest

def solve(P):
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    parties = []
    for n, s in enumerate(P):
        parties.append({"n": alphabet[n], "s": s})
    parties.sort(key=lambda p: p["s"], reverse=True)
    
    buckets = []
    for p in parties:
        if len(buckets) == 0 or buckets[len(buckets)-1]["s"] != p["s"]:
            buckets.append({"p": [], "s": p["s"]})
        buckets[len(buckets)-1]["p"].append(p["n"])
    
    sequence = []
    while len(buckets) != 0:
        first = pop_highest(buckets, False)
        second = pop_highest(buckets, True)
        sequence.append(first+second)
            
    return " ".join(sequence)

cases_count = int(input())
for i in range(cases_count):
    N = input().split()
    P = map(lambda x: int(x), input().split(' ')) 
    res = solve(P)
    print("Case #{}: {}".format(i+1, res))
