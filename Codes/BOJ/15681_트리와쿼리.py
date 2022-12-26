import sys

sys.setrecursionlimit(100001)

input = sys.stdin.readline


def f(node):
    result = 1
    for nxt in graph[node]:
        if visited[nxt]:
            continue
        visited[nxt] = True
        result += f(nxt)

    memo[node] = result
    return result


n, r, q = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    u, v = map(int, input().split())
    graph[u].append(v)
    graph[v].append(u)

memo = [0] * (n + 1)
visited = [False] * (n + 1)
visited[r] = True
f(r)

for _ in range(q):
    query = int(input())
    print(memo[query])
