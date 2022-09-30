from collections import deque
import sys

input = sys.stdin.readline


def bfs(sy, sx):
    queue = deque([(sy, sx)])
    visited[sy][sx] = True
    total_population = 0
    total_count = 0
    unions = [(sy, sx)]

    while queue:
        y, x = queue.popleft()
        total_population += matrix[y][x]
        total_count += 1

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if visited[ny][nx]:
                continue
            if l <= abs(matrix[y][x] - matrix[ny][nx]) <= r:
                visited[ny][nx] = True
                queue.append((ny, nx))
                unions.append((ny, nx))

    new_population = total_population // total_count
    for i, j in unions:
        matrix[i][j] = new_population

    return True if total_count > 1 else False


DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, l, r = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]
cnt = 0
while True:
    flag = False
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            has_moved = bfs(i, j)
            if has_moved:
                flag = True
    if not flag:
        break
    cnt += 1


print(cnt)
