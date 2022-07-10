import sys, math

input = sys.stdin.readline


def kruskal():
    def find(x):
        if x != parents[x]:
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

    parents = [i for i in range(n + 1)]
    weight = 0

    for cost, a, b in edges:
        if find(a) != find(b):
            weight += cost
            union(a, b)
    return weight


n, m = map(int, input().split())

points = [()]
for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

connected = set()
for _ in range(m):
    a, b = map(int, input().split())
    connected.add((min(a, b), max(a, b)))

edges = []
for i in range(1, n + 1):
    for j in range(i + 1, n + 1):
        if (i, j) in connected:
            edges.append((0, i, j))
        else:
            edges.append((math.dist(points[i], points[j]), i, j))

edges.sort(key=lambda abc: abc[0])
weight = kruskal()
print(f"{weight:.2f}")
