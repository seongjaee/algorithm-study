from collections import deque
import sys

input = sys.stdin.readline

DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
MAX = 10000


def bfs(starts):
    global answer
    queue = deque()
    visited = [[False] * n for _ in range(n)]
    result = 0

    for sy, sx in starts:
        queue.append((sy, sx, 0))
        visited[sy][sx] = True

    while queue:
        y, x, cnt = queue.popleft()
        if cnt >= answer:
            return MAX
        result = max(result, cnt)

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= n:
                continue
            if visited[ny][nx] or matrix[ny][nx] == 1:
                continue
            visited[ny][nx] = True
            queue.append((ny, nx, cnt + 1))

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and matrix[i][j] != 1:
                return MAX

    return result


def comb(n, r):
    global answer
    if r == 0:
        result = bfs(selected)
        answer = min(answer, result)
        return

    if n < r:
        return

    selected[r - 1] = placeables[n - 1]
    comb(n - 1, r - 1)
    comb(n - 1, r)


n, m = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(n)]

placeables = []
for i in range(n):
    for j in range(n):
        if matrix[i][j] == 2:
            placeables.append((i, j))

selected = [None for _ in range(m)]
answer = MAX
comb(len(placeables), m)
print(answer if answer != MAX else -1)
