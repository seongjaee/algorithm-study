import sys

input = sys.stdin.readline


def dfs(start):
    visited[start] = True
    stack = [(start, 0, 1 << start)]
    flag = False

    while stack:
        node, parent, now_visited = stack.pop()
        for nxt in graph[node]:
            if nxt == parent:
                continue
            if is_shields[nxt]:
                flag = True
            if now_visited & (1 << nxt):
                flag = True
                continue

            visited[nxt] = True
            stack.append((nxt, node, now_visited | (1 << nxt)))

    return flag


n, m = map(int, input().split())
edges = set()
is_shields = [False] * (n + 1)

for _ in range(m):
    a, b = map(int, input().split())
    edges.add((a, b))

graph = [[] for _ in range(n + 1)]

for a, b in edges:
    if (b, a) in edges:
        graph[a].append(b)
        continue
    else:
        is_shields[b] = True

visited = [False] * (n + 1)

for i in range(1, n + 1):
    if not is_shields[i] and not visited[i]:
        result = dfs(i)
        if not result:
            print("NO")
            break
else:
    print("YES")
