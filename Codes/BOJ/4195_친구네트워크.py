import sys


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return

    if x < y:
        parents[x] = y
        cnt[y] += cnt[x]
    else:
        parents[y] = x
        cnt[x] += cnt[y]


input = sys.stdin.readline
t = int(input())

for _ in range(t):
    f = int(input())
    parents = {}
    cnt = {}
    for _ in range(f):
        a, b = input().split()

        if a not in parents:
            parents[a] = a
            cnt[a] = 1
        if b not in parents:
            parents[b] = b
            cnt[b] = 1

        union(a, b)
        print(cnt[find(a)])
