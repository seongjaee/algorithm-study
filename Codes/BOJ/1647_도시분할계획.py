from heapq import heappop, heappush
import sys

input = sys.stdin.readline


def prim(start):
    visited = [False] * (n + 1)
    heap = [(0, start)]
    weight = 0
    max_weight = 0

    while heap:
        cost, node = heappop(heap)
        if visited[node]:
            continue

        visited[node] = True
        weight += cost
        max_weight = max(max_weight, cost)

        for nxt_node, nxt_cost in graph[node]:
            if visited[nxt_node]:
                continue
            heappush(heap, (nxt_cost, nxt_node))

    return weight - max_weight


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

print(prim(1))
