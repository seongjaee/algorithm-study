"""
Find : min(d(A, x) + d(B, x) + d(S, x)) for x in [1, ..., n]
"""
from heapq import heappop, heappush

INF = 1e10


def dijkstra(n, graph, start):
    distance = [INF] * (1 + n)
    heap = [(0, start)]
    distance[start] = 0

    while heap:
        dist, node = heappop(heap)

        for nxt_node, nxt_cost in graph.get(node, []):
            nxt_dist = nxt_cost + dist
            if nxt_dist >= distance[nxt_node]:
                continue
            distance[nxt_node] = nxt_dist
            heappush(heap, (nxt_dist, nxt_node))

    return distance


def solution(n, s, a, b, fares):
    answer = INF
    graph = {}
    for i, j, cost in fares:
        graph[i] = graph.get(i, []) + [(j, cost)]
        graph[j] = graph.get(j, []) + [(i, cost)]

    dist_s = dijkstra(n, graph, s)
    dist_a = dijkstra(n, graph, a)
    dist_b = dijkstra(n, graph, b)

    for x in range(1, n + 1):
        answer = min(answer, dist_s[x] + dist_a[x] + dist_b[x])

    return answer
