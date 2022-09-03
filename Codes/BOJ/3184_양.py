import sys

input = sys.stdin.readline


def dfs(sy, sx):
    stack = [(sy, sx)]
    visited[sy][sx] = True
    sheep_cnt = 0
    wolf_cnt = 0

    while stack:
        y, x = stack.pop()
        if matrix[y][x] == "v":
            wolf_cnt += 1
        elif matrix[y][x] == "o":
            sheep_cnt += 1

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if visited[ny][nx] or matrix[ny][nx] == "#":
                continue
            visited[ny][nx] = True
            stack.append((ny, nx))

    if sheep_cnt > wolf_cnt:
        answer[0] += sheep_cnt
    else:
        answer[1] += wolf_cnt


DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r, c = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

answer = [0, 0]
for i in range(r):
    for j in range(c):
        if matrix[i][j] != "#" and not visited[i][j]:
            dfs(i, j)

print(*answer)
