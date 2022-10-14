def permutation(level):
    if level == m:
        result.append(now[:m])
        return

    for i in range(level, n):
        now[i], now[level] = now[level], now[i]
        permutation(level + 1)
        now[i], now[level] = now[level], now[i]


n, m = map(int, input().split())

now = [i for i in range(1, n + 1)]
result = []
permutation(0)
result.sort()
for r in result:
    print(*r)


# permutations
from itertools import permutations as pmts

n, m = map(int, input().split())

pmt = pmts(range(1, n + 1), m)
for p in pmt:
    print(*p)
