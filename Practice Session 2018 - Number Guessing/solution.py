# Rationale:
# It's a binary search :).

import math
import sys

def solve(A, B):
    while True:
        guess = A + math.ceil((B - A) / 2)
        print(guess)
        res = input()
        if res == "CORRECT":
            return 1
        if res == "TOO_SMALL":
            A = guess
        if res == "TOO_BIG":
            B = guess - 1
        if res == "WRONG_ANSWER":
            return 0

cases_count = int(input())
for i in range(cases_count):
    A, B = input().split()
    N = input().split()
    res = solve(int(A), int(B))
    if res == 0:
        sys.exit(0)
