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
            parents[y] = x
        else:
            parents[x] = y

    parents = [i for i in range(n)]
    weight = 0
    cnt = 0
    for cost, i, j in edges:
        if find(i) != find(j):
            weight += cost
            union(i, j)
            cnt += 1
        if cnt == n - 1:
            break

    return weight


n = int(input())
points = []
for i in range(n):
    x, y, z = map(int, input().split())
    points.append((i, x, y, z))

edges = []
for k in range(1, 4):
    points.sort(key=lambda arr: arr[k])
    for i in range(n - 1):
        edges.append((points[i + 1][k] - points[i][k], points[i + 1][0], points[i][0]))

edges.sort(key=lambda arr: arr[0])
print(kruskal())
