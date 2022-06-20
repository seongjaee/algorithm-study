from heapq import heappop, heappush
import sys

input = sys.stdin.readline
INF = 1e12


def dijkstra(graph, start):
    distances = [INF] * (n + 1)
    distances[start] = 0
    heap = [(0, start)]
    while heap:
        dist, node = heappop(heap)

        for nxt_node, nxt_cost in graph[node]:
            nxt_dist = nxt_cost + dist
            if distances[nxt_node] <= nxt_dist:
                continue
            distances[nxt_node] = nxt_dist
            heappush(heap, (nxt_dist, nxt_node))

    return distances


n, m, x = map(int, input().split())
from_graph = [[] for _ in range(1 + n)]
to_graph = [[] for _ in range(1 + n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    from_graph[a].append((b, c))
    to_graph[b].append((a, c))

from_dists = dijkstra(from_graph, x)
to_dists = dijkstra(to_graph, x)

max_value = 0
for i in range(1, n + 1):
    max_value = max(max_value, from_dists[i] + to_dists[i])

print(max_value)
