from itertools import combinations
from math import gcd
import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    case = list(map(int, input().split()))
    n = case[0]
    numbers = case[1:]
    answer = 0
    for a, b in combinations(numbers, 2):
        answer += gcd(a, b)
    print(answer)
