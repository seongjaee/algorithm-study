from heapq import heappop, heappush
import sys

input = sys.stdin.readline

DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]


def delete_biggest_block_group():
    def dfs(sy, sx):
        visited[sy][sx] = True
        color = matrix[sy][sx]
        stack = [(sy, sx)]
        points = [(sy, sx)]
        rainbow_points = []
        while stack:
            y, x = stack.pop()
            for dy, dx in DELTA:
                ny, nx = y + dy, x + dx
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if visited[ny][nx]:
                    continue
                if matrix[ny][nx] == color:
                    visited[ny][nx] = True
                    stack.append((ny, nx))
                    points.append((ny, nx))
                elif matrix[ny][nx] == 0:
                    visited[ny][nx] = True
                    stack.append((ny, nx))
                    points.append((ny, nx))
                    rainbow_points.append((ny, nx))

        for y, x in rainbow_points:
            visited[y][x] = False

        return (points, len(rainbow_points))

    heap = []
    points_d = {}
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0 and not visited[i][j]:
                points, rainbow_cnt = dfs(i, j)
                if len(points) >= 2:
                    points_d[(i, j)] = points
                    heappush(heap, (-len(points), -rainbow_cnt, -i, -j))

    if not heap:
        return 0

    cnts, rainbow_cnt, i, j = map(lambda x: -x, heappop(heap))
    points = points_d[(i, j)]
    for y, x in points:
        matrix[y][x] = -2

    return cnts**2


def drop():
    for j in range(n):
        for i in range(n - 1, 0, -1):
            if matrix[i][j] == -2:
                for k in range(i - 1, -1, -1):
                    if matrix[k][j] == -1:
                        break
                    if matrix[k][j] != -2:
                        matrix[k][j], matrix[i][j] = matrix[i][j], matrix[k][j]
                        break


def rotate():
    new_matrix = [[None] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] = matrix[j][n - 1 - i]
    return new_matrix


n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]
score = 0

while True:
    res = delete_biggest_block_group()
    if not res:
        break
    score += res
    drop()
    matrix = rotate()
    drop()

print(score)
