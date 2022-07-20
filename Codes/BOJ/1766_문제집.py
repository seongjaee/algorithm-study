from heapq import heappop, heappush
import sys

input = sys.stdin.readline


def topology_sort():
    res = []
    heap = []
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            heappush(heap, i)

    while heap:
        node = heappop(heap)
        res.append(node)

        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                heappush(heap, nxt)

    return res


n, m = map(int, input().split())
graph = [[] for _ in range(n + 1)]
in_degree = [0] * (n + 1)
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degree[b] += 1

print(*topology_sort())
