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
        parents[x] = y
    else:
        parents[y] = x


n, m = map(int, input().split())
parents = [i for i in range(n + 1)]
mw = [" "] + input().split()

weights = []
for _ in range(m):
    u, v, d = map(int, input().split())
    if mw[u] != mw[v]:
        weights.append((u, v, d))

weights.sort(key=lambda arr: arr[2])

edge_cnt = 0
total_weight = 0
i = 0
while i < len(weights) and edge_cnt < n - 1:
    u, v, d = weights[i]
    if find(u) != find(v):
        union(u, v)
        total_weight += d
        edge_cnt += 1
    i += 1

if edge_cnt == n - 1:
    print(total_weight)
else:
    print(-1)
