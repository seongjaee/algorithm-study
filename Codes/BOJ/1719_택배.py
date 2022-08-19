from heapq import heappop, heappush
import sys

input = sys.stdin.readline


def dijkstra(start):
    dists = [INF] * n
    dists[start] = 0
    parents = [i for i in range(n)]

    heap = [(0, start)]
    while heap:
        dist, node = heappop(heap)

        for nxt_node, nxt_cost in graph[node]:
            nxt_dist = dist + nxt_cost
            if dists[nxt_node] > nxt_dist:
                dists[nxt_node] = nxt_dist
                heappush(heap, (nxt_dist, nxt_node))
                parents[nxt_node] = node

    return parents


INF = 1e9
n, m = map(int, input().split())
graph = [[] for _ in range(n)]

for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

answer = [["-"] * n for _ in range(n)]

for i in range(n):
    parents = dijkstra(i)
    for j in range(n):
        if j == i:
            continue
        answer[j][i] = parents[j] + 1

for row in answer:
    print(*row)
