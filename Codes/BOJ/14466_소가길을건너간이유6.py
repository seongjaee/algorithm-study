import sys

input = sys.stdin.readline


def find(x):
    if x != parents[x]:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x == y:
        return
    elif x < y:
        parents[y] = x
    else:
        parents[x] = y


DELTA = [(-1, 0), (0, 1), (0, -1), (1, 0)]
n, k, r = map(int, input().split())

parents = {(i, j): (i, j) for i in range(n) for j in range(n)}

roads = set()
for _ in range(r):
    y1, x1, y2, x2 = map(int, input().split())
    roads.add((y1 - 1, x1 - 1, y2 - 1, x2 - 1))
    roads.add((y2 - 1, x2 - 1, y1 - 1, x1 - 1))

for i in range(n):
    for j in range(n):
        for di, dj in DELTA:
            ni, nj = i + di, j + dj
            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                continue
            if find((i, j)) == find((ni, nj)):
                continue
            if (i, j, ni, nj) in roads:
                continue
            if (ni, nj, i, j) in roads:
                continue
            union((i, j), (ni, nj))

cows = []
for _ in range(k):
    y, x = map(int, input().split())
    cows.append((y - 1, x - 1))

answer = 0
for i in range(k - 1):
    for j in range(i + 1, k):
        if find(cows[i]) != find(cows[j]):
            answer += 1

print(answer)
