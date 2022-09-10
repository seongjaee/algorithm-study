import sys

input = sys.stdin.readline
INF = 1e10


def dfs(node, visited, dist):
    global result
    if dist == 4:
        result = True
        return

    for nxt in graph[node]:
        if (1 << nxt) & visited:
            continue
        dfs(nxt, visited | (1 << nxt), dist + 1)


n, m = map(int, input().split())
graph = [[] for _ in range(n)]
result = False
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(n):
    dfs(i, 1 << i, 0)
    if result:
        print(1)
        break
else:
    print(0)
