from collections import deque
import sys

input = sys.stdin.readline

slash_delta = [(1, 0), (1, -1), (0, 1), (0, -1), (-1, 1), (-1, 0)]
reverse_delta = [(1, 1), (1, 0), (0, 1), (0, -1), (-1, 0), (-1, -1)]

INF = 1e10


def bfs():
    visited = [[INF] * m for _ in range(n)]
    if matrix[0][0] == "/":
        visited[0][0] = 1
        queue = deque([(0, 0, True)])
    else:
        visited[0][0] = 0
        queue = deque([(0, 0, False)])

    while queue:
        y, x, rv = queue.popleft()
        if (matrix[y][x] == "/" and not rv) or (matrix[y][x] == "\\" and rv):
            for dy, dx in slash_delta:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m:
                    # 뒤집을 필요 없을 때
                    if (matrix[ny][nx] == "/" and dy + dx == 0) or (
                        matrix[ny][nx] != "/" and dy + dx != 0
                    ):
                        if visited[ny][nx] > visited[y][x]:
                            visited[ny][nx] = visited[y][x]
                            queue.appendleft((ny, nx, False))
                    # 뒤집어야 할 때
                    else:
                        if visited[ny][nx] > visited[y][x] + 1:
                            visited[ny][nx] = visited[y][x] + 1
                            queue.append((ny, nx, True))

        else:
            for dy, dx in reverse_delta:
                ny, nx = y + dy, x + dx
                if 0 <= ny < n and 0 <= nx < m:
                    # 뒤집을 필요 없을 때
                    if (matrix[ny][nx] == "\\" and dy - dx == 0) or (
                        matrix[ny][nx] != "\\" and dy - dx != 0
                    ):
                        if visited[ny][nx] > visited[y][x]:
                            visited[ny][nx] = visited[y][x]
                            queue.appendleft((ny, nx, False))
                    else:
                        if visited[ny][nx] > visited[y][x] + 1:
                            visited[ny][nx] = visited[y][x] + 1
                            queue.append((ny, nx, True))

    return visited


n, m = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(n)]

if (n % 2) != (m % 2):
    print("no solution")
    sys.exit()

dists = bfs()
print(dists[-1][-1])


# 더 짧은 풀이
from collections import deque
import sys

input = sys.stdin.readline

INF = 1e10
DELTA = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def bfs():
    dist[0][0] = 0
    queue = deque([(0, 0)])

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            dy, dx = DELTA[i]
            ny, nx = y + dy, x + dx
            if 0 <= ny <= n and 0 <= nx <= m:
                if dist[ny][nx] <= dist[y][x] + graph[y][x][i]:
                    continue
                dist[ny][nx] = dist[y][x] + graph[y][x][i]

                if graph[y][x][i] == 0:
                    queue.appendleft((ny, nx))
                else:
                    queue.append((ny, nx))


n, m = map(int, input().split())

graph = [[[1, 1, 1, 1] for _ in range(m + 1)] for _ in range(n + 1)]
for i in range(n):
    row = input().rstrip()
    for j in range(m):
        if row[j] == "/":
            graph[i][j + 1][1] = 0
            graph[i + 1][j][2] = 0
        else:
            graph[i][j][0] = 0
            graph[i + 1][j + 1][3] = 0

dist = [[INF] * (m + 1) for _ in range(n + 1)]

bfs()
print(dist[-1][-1] if dist[-1][-1] != INF else "NO SOLUTION")
