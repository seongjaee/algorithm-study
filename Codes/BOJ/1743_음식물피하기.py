import sys

input = sys.stdin.readline


def dfs(sy, sx):
    stack = [(sy, sx)]
    visited[sy][sx] = True
    cnt = 0
    while stack:
        y, x = stack.pop()
        cnt += 1

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx] or not matrix[ny][nx]:
                continue
            visited[ny][nx] = True
            stack.append((ny, nx))

    return cnt


DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m, k = map(int, input().split())
visited = [[False] * m for _ in range(n)]

matrix = [[False] * m for _ in range(n)]
for _ in range(k):
    r, c = map(int, input().split())
    matrix[r - 1][c - 1] = True

answer = 0
for i in range(n):
    for j in range(m):
        if matrix[i][j] and not visited[i][j]:
            answer = max(answer, dfs(i, j))

print(answer)
