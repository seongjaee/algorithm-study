import sys

input = sys.stdin.readline


def dfs(sy, sx):
    stack = [(sy, sx)]
    art_size = 0

    while stack:
        y, x = stack.pop()
        art_size += 1
        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if (
                0 <= ny < n
                and 0 <= nx < m
                and not visited[ny][nx]
                and matrix[ny][nx] == 1
            ):
                visited[ny][nx] = True
                stack.append((ny, nx))

    return art_size


DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]
visited = [[False] * m for _ in range(n)]

max_art_size = 0
art_cnt = 0
for i in range(n):
    for j in range(m):
        if not visited[i][j] and matrix[i][j] == 1:
            visited[i][j] = True
            art_cnt += 1
            max_art_size = max(max_art_size, dfs(i, j))

print(art_cnt)
print(max_art_size)
