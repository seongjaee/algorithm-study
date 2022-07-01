from heapq import heappop, heappush
import sys

input = sys.stdin.readline

INF = 1e11


def dijkstra():
    heap = [(0, 0, 1)]
    distances = [[INF] * (k + 1) for _ in range(n + 1)]
    for i in range(k + 1):
        distances[1][i] = 0

    while heap:
        dist, cnt, node = heappop(heap)
        if distances[node][cnt] < dist:
            continue

        for nxt_node, nxt_cost in graph[node]:
            nxt_dist = nxt_cost + dist
            if distances[nxt_node][cnt] > nxt_dist:
                distances[nxt_node][cnt] = nxt_dist
                heappush(heap, (nxt_dist, cnt, nxt_node))

            if cnt < k and distances[nxt_node][cnt + 1] > dist:
                distances[nxt_node][cnt + 1] = dist
                heappush(heap, (dist, cnt + 1, nxt_node))

    return distances[-1]


n, m, k = map(int, input().split())

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))


result = dijkstra()
print(min(result))
