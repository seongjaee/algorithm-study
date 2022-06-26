from heapq import heappop, heappush
import sys

input = sys.stdin.readline

INF = 1e12
"""
모든 간선 * 2 + 정점 * 차수 + 시작 정점
"""


def prim(start):
    visited = [False] * (n + 1)
    total_weight = 0
    heap = [(v_costs[start], start)]
    while heap:
        cost, node = heappop(heap)
        if visited[node]:
            continue
        visited[node] = True
        total_weight += cost

        for nxt_node, nxt_cost in graph[node]:
            if visited[nxt_node]:
                continue
            heappush(heap, (nxt_cost + v_costs[nxt_node] + v_costs[node], nxt_node))

    return total_weight


n, p = map(int, input().split())
v_costs = [0] + [int(input()) for _ in range(n)]

graph = [[] for _ in range(n + 1)]

for _ in range(p):
    s, e, l = map(int, input().split())
    graph[s].append((e, 2 * l))
    graph[e].append((s, 2 * l))


min_value = INF
min_v = 0
for i in range(1, n + 1):
    if v_costs[i] < min_value:
        min_v = i
        min_value = v_costs[i]

print(prim(min_v))
