import sys

input = sys.stdin.readline
sys.setrecursionlimit(1000000)


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
        parents[y] = x
    else:
        parents[x] = y


n, m = map(int, input().split())
parents = [i for i in range(n + 1)]

for _ in range(m):
    cmd, a, b = map(int, input().split())
    if cmd:
        print("YES" if find(a) == find(b) else "NO")
    else:
        union(a, b)
