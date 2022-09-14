import sys

input = sys.stdin.readline


def dfs(sy, sx):
    stack = [(sy, sx)]
    sheep_cnt = 0
    wolf_cnt = 0

    while stack:
        y, x = stack.pop()
        if matrix[y][x] == "v":
            wolf_cnt += 1
        elif matrix[y][x] == "k":
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
        return sheep_cnt, 0
    else:
        return 0, wolf_cnt


DELTA = [(1, 0), (0, 1), (-1, 0), (0, -1)]
r, c = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]

sheep_cnt = 0
wolf_cnt = 0

for i in range(r):
    for j in range(c):
        if matrix[i][j] == "#" or visited[i][j]:
            continue
        visited[i][j] = True
        s, w = dfs(i, j)
        sheep_cnt += s
        wolf_cnt += w

print(sheep_cnt, wolf_cnt)
