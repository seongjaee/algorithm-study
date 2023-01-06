from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]
visited = [[False] * m for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == 2:
            sy, sx = i, j
            matrix[i][j] = 0
            visited[i][j] = True

DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]

queue = deque([(sy, sx, 0)])
while queue:
    y, x, cnt = queue.popleft()

    for dy, dx in DELTA:
        ny, nx = y + dy, x + dx
        if ny < 0 or nx < 0 or ny >= n or nx >= m:
            continue
        if matrix[ny][nx] == 0 or visited[ny][nx]:
            continue
        matrix[ny][nx] = cnt + 1
        visited[ny][nx] = True
        queue.append((ny, nx, cnt + 1))

for i in range(n):
    for j in range(m):
        if not visited[i][j] and matrix[i][j] == 1:
            matrix[i][j] = -1

for row in matrix:
    print(*row)
