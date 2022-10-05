from heapq import heappop, heappush
import sys

input = sys.stdin.readline

INF = 1e10


def dijkstra(n, graph, start):
    dists = [INF] * (n + 1)
    dists[start] = 0
    heap = [(0, start)]

    while heap:
        dist, node = heappop(heap)

        if dists[node] < dist:
            continue

        for nxt_node, nxt_cost in graph[node]:
            if dists[nxt_node] <= nxt_cost + dist:
                continue
            dists[nxt_node] = nxt_cost + dist
            heappush(heap, (nxt_cost + dist, nxt_node))

    return dists


t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    parents = [i for i in range(1, n + 1)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, c = map(int, input().split())
        graph[a].append((b, c))
        graph[b].append((a, c))

    k = int(input())
    friends = list(map(int, input().split()))

    result = [0] * (n + 1)
    for i in friends:
        dists = dijkstra(n, graph, i)
        for j in range(1, n + 1):
            result[j] += dists[j]

    min_value = INF
    min_idx = 0
    for i in range(1, n + 1):
        if min_value > result[i]:
            min_value = result[i]
            min_idx = i

    print(min_idx)
