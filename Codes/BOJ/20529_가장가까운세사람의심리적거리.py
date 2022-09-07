from collections import Counter
from itertools import combinations
import sys

input = sys.stdin.readline


def get_distance(a, b):
    result = 0
    for i in range(4):
        if a[i] != b[i]:
            result += 1
    return result


t = int(input())
for _ in range(t):
    n = int(input())
    mbtis = input().split()
    counter = Counter(mbtis)
    if counter.most_common()[0][1] >= 3:
        print(0)
        continue
    combs = list(combinations(mbtis, 3))
    min_value = 10
    for a, b, c in combs:
        dists = get_distance(a, b) + get_distance(b, c) + get_distance(c, a)
        min_value = min(min_value, dists)
    print(min_value)
