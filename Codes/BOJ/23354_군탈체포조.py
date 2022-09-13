# TSP
from heapq import heappop, heappush
import sys

input = sys.stdin.readline
INF = 1e10
DELTA = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dijkstra(sy, sx):
    distances = [[INF] * n for _ in range(n)]
    distances[sy][sx] = 0
    heap = [(0, sy, sx)]

    while heap:
        dist, y, x = heappop(heap)

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if distances[ny][nx] <= dist + matrix[ny][nx]:
                continue

            distances[ny][nx] = dist + matrix[ny][nx]
            heappush(heap, (dist + matrix[ny][nx], ny, nx))

    return distances


def dp(node, visited):
    if visited == (1 << m) - 1:
        return graph[node][0]

    if cache[node][visited] != INF:
        return cache[node][visited]

    temp = INF
    for nxt in range(m):
        if visited & (1 << nxt):
            continue
        cost = graph[node][nxt] + dp(nxt, visited | (1 << nxt))
        temp = min(temp, cost)

    cache[node][visited] = temp
    return temp


n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]
nodes = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            nodes.append((i, j))

        elif matrix[i][j] == -1:
            nodes.append((i, j))
            army = (i, j)

matrix[army[0]][army[1]] = 0
m = len(nodes)
graph = [[0] * m for _ in range(m)]
for i in range(m):
    y, x = nodes[i]
    distances = dijkstra(y, x)
    for j in range(i + 1, m):
        ny, nx = nodes[j]
        graph[i][j] = distances[ny][nx]
        graph[j][i] = distances[ny][nx]

cache = [[INF] * (1 << m) for _ in range(m)]
print(dp(0, 1))


# permutations 이용

from itertools import permutations as pmts
from heapq import heappop, heappush
import sys

input = sys.stdin.readline
INF = 1e10
DELTA = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def dijkstra(sy, sx):
    distances = [[INF] * n for _ in range(n)]
    distances[sy][sx] = 0
    heap = [(0, sy, sx)]

    while heap:
        dist, y, x = heappop(heap)

        if distances[y][x] < dist:
            continue

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue

            if distances[ny][nx] <= dist + matrix[ny][nx]:
                continue

            distances[ny][nx] = dist + matrix[ny][nx]
            heappush(heap, (dist + matrix[ny][nx], ny, nx))

    return distances


n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]
nodes = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 0:
            nodes.append((i, j))

        elif matrix[i][j] == -1:
            nodes.append((i, j))
            army = (i, j)

matrix[army[0]][army[1]] = 0
m = len(nodes)
graph = [[0] * m for _ in range(m)]
for i in range(m):
    y, x = nodes[i]
    distances = dijkstra(y, x)
    for j in range(i + 1, m):
        ny, nx = nodes[j]
        graph[i][j] = distances[ny][nx]
        graph[j][i] = distances[ny][nx]


def find_least_cost():
    if m == 1:
        return 0

    answer = INF
    for order in list(pmts(range(1, m))):
        result = graph[0][order[0]]
        for i in range(m - 2):
            result += graph[order[i]][order[i + 1]]
        result += graph[order[-1]][0]
        answer = min(answer, result)
    return answer


print(find_least_cost())
