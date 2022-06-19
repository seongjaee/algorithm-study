from heapq import heappop, heappush
import sys

input = sys.stdin.readline
INF = 1e12


def dijkstra(start):
    heap = [(0, start)]
    distance = [INF] * (1 + n)
    distance[start] = 0

    while heap:
        dist, node = heappop(heap)

        for nxt_node, nxt_cost in graph.get(node, []):
            nxt_dist = dist + nxt_cost
            if distance[nxt_node] <= nxt_dist:
                continue
            distance[nxt_node] = nxt_dist
            heappush(heap, (nxt_dist, nxt_node))

    return distance


n, e = map(int, input().split())
graph = {}
for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a] = graph.get(a, []) + [(b, c)]
    graph[b] = graph.get(b, []) + [(a, c)]

v1, v2 = map(int, input().split())

dist1 = dijkstra(1)
distv1 = dijkstra(v1)
distv2 = dijkstra(v2)

result = min(dist1[v1] + distv1[v2] + distv2[n], dist1[v2] + distv2[v1] + distv1[n])
if result >= INF:
    print(-1)
else:
    print(result)
