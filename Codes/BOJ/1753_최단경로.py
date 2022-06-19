from heapq import heappop, heappush
import sys

input = sys.stdin.readline

INF = 1e12


def dijkstra(start):
    heap = [(0, start)]
    distances[start] = 0

    while heap:
        dist, node = heappop(heap)

        for nxt_node, nxt_cost in graph[node]:
            nxt_dist = dist + nxt_cost
            if distances[nxt_node] <= nxt_dist:
                continue
            distances[nxt_node] = nxt_dist
            heappush(heap, (nxt_dist, nxt_node))


v, e = map(int, input().split())
k = int(input())
distances = [INF] * (1 + v)

graph = [[] for _ in range(1 + v)]
for _ in range(e):
    u, v, w = map(int, input().split())
    graph[u].append((v, w))

dijkstra(k)
for d in distances[1:]:
    print("INF" if d == INF else d)
