from collections import deque
import sys

input = sys.stdin.readline


def bfs(start):
    queue = deque([(start, INF)])
    visited = [False] * (N + 1)
    visited[start] = True

    while queue:
        node, cost = queue.popleft()

        for nxt_node, nxt_cost in graph[node]:
            if visited[nxt_node]:
                continue
            visited[nxt_node] = True
            usado[start][nxt_node] = min(cost, nxt_cost)
            queue.append((nxt_node, min(cost, nxt_cost)))


INF = 1e16
N, Q = map(int, input().split())

graph = [[] for _ in range(N + 1)]
usado = [[0] * (N + 1) for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for i in range(1, N + 1):
    bfs(i)

for _ in range(Q):
    k, v = map(int, input().split())
    res = 0
    for i in range(1, N + 1):
        if usado[i][v] >= k:
            res += 1
    print(res)

# 2번째 풀이

from collections import deque
import sys

input = sys.stdin.readline


def bfs(start):
    queue = deque([(start, 1e10)])
    visited = [False] * (N + 1)
    visited[start] = True

    usado = [1e10] * (N + 1)

    while queue:
        node, dist = queue.popleft()

        for nxt_node, nxt_cost in graph[node]:
            if visited[nxt_node]:
                continue
            visited[nxt_node] = True
            nxt_dist = min(dist, nxt_cost)
            usado[nxt_node] = nxt_dist
            queue.append((nxt_node, nxt_dist))

    return usado


N, Q = map(int, input().split())

graph = [[] for _ in range(N + 1)]
for _ in range(N - 1):
    p, q, r = map(int, input().split())
    graph[p].append((q, r))
    graph[q].append((p, r))

for _ in range(Q):
    k, v = map(int, input().split())
    usado = bfs(v)
    result = 0
    for i in range(1, N + 1):
        if usado[i] >= k:
            result += 1
    print(result - 1)
