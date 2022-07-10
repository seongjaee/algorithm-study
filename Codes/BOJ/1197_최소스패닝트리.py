import sys

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
            parents[x] = y
        else:
            parents[y] = x

    parents = [i for i in range(v + 1)]
    weight = 0
    for cost, x, y in edges:
        if find(x) != find(y):
            union(x, y)
            weight += cost

    return weight


v, e = map(int, input().split())


edges = []
for _ in range(e):
    a, b, c = map(int, input().split())
    edges.append((c, a, b))

edges.sort(key=lambda edge: edge[0])

print(kruskal())
