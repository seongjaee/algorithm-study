# 0-1 BFS
from collections import deque
import sys

input = sys.stdin.readline

DELTA = [(0, 1), (1, 0), (-1, 0), (0, -1)]


def bfs():
    queue = deque([(0, 0, 0)])
    visited = [[False] * n for _ in range(m)]
    while queue:
        y, x, cnt = queue.popleft()
        for dy, dx in DELTA:
            ny, nx = dy + y, dx + x
            if 0 <= ny < m and 0 <= nx < n and not visited[ny][nx]:
                visited[ny][nx] = True
                if (ny, nx) == (m - 1, n - 1):
                    return cnt
                if matrix[ny][nx] == "0":
                    queue.appendleft((ny, nx, cnt))
                else:
                    queue.append((ny, nx, cnt + 1))

    return cnt


n, m = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(m)]
print(bfs())


#### 다익스트라
from heapq import heappop, heappush
import sys

input = sys.stdin.readline

DELTA = [(0, 1), (1, 0), (-1, 0), (0, -1)]
INF = 1e10


def dijkstra():
    distances = [[INF] * n for _ in range(m)]
    distances[0][0] = 0
    heap = [(0, 0, 0)]

    while heap:
        dist, y, x = heappop(heap)

        for dy, dx in DELTA:
            ny, nx = dy + y, dx + x
            if 0 <= ny < m and 0 <= nx < n:
                nxt_dist = dist + matrix[ny][nx]
                if distances[ny][nx] <= nxt_dist:
                    continue
                distances[ny][nx] = nxt_dist
                heappush(heap, (nxt_dist, ny, nx))

    return distances[-1][-1]


n, m = map(int, input().split())
matrix = [list(map(int, input().rstrip())) for _ in range(m)]
print(dijkstra())
