from heapq import heappop, heappush
import sys

input = sys.stdin.readline

INF = 1e10


def dijkstra(start):
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


T = int(input())
for _ in range(T):
    n, m, t = map(int, input().split())
    s, g, h = map(int, input().split())

    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        a, b, d = map(int, input().split())
        if (a, b) == (g, h) or (a, b) == (h, g):
            that_road = d
        graph[a].append((b, d))
        graph[b].append((a, d))

    dist_s = dijkstra(s)
    dist_g = dijkstra(g)
    dist_h = dijkstra(h)

    results = []
    for _ in range(t):
        x = int(input())
        total = dist_s[x]
        if (
            total == dist_s[g] + that_road + dist_h[x]
            or total == dist_s[h] + that_road + dist_g[x]
        ):
            results.append(x)

    print(*sorted(results))
