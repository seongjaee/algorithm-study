import sys

input = sys.stdin.readline

INF = 1e10


def bellman_ford():
    dists[1] = 0
    for i in range(n):
        for node, nxt, cost in edges:
            if dists[node] != INF and dists[nxt] > dists[node] + cost:
                dists[nxt] = dists[node] + cost
                if i == n - 1:
                    return True
    return False


n, m = map(int, input().split())
dists = [INF] * (n + 1)

edges = []
for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a, b, c))

has_negative_cycle = bellman_ford()
if has_negative_cycle:
    print(-1)
else:
    for d in dists[2:]:
        print(d if d != INF else -1)
