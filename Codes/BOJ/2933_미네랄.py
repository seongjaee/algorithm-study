import sys

input = sys.stdin.readline
DELTA = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def cy_throw(h):
    i = r - h
    for j in range(c):
        if matrix[i][j] == "x":
            return i, j


def sg_throw(h):
    i = r - h
    for j in range(c - 1, -1, -1):
        if matrix[i][j] == "x":
            return i, j


def remove_mineral(point):
    def dfs(sy, sx):
        res = [(sy, sx)]
        stack = [(sy, sx)]
        visited[sy][sx] = True
        flag = True
        bottom = {sx: sy}
        while stack:
            y, x = stack.pop()

            for dy, dx in DELTA:
                ny, nx = y + dy, x + dx
                if ny < 0 or ny >= r or nx < 0 or nx >= c:
                    continue
                if visited[ny][nx]:
                    continue
                if matrix[ny][nx] != "x":
                    continue
                if ny == r - 1:
                    flag = False

                res.append((ny, nx))
                visited[ny][nx] = True
                stack.append((ny, nx))
                bottom[nx] = max(bottom.get(nx, 0), ny)
        return (res, bottom) if flag else False

    if not point:
        return

    i, j = point
    matrix[i][j] = "."

    visited = [[False] * c for _ in range(r)]
    cluster = []
    bottom = {}
    for di, dj in DELTA:
        ni, nj = i + di, j + dj
        if ni < 0 or ni >= r or nj < 0 or nj >= c:
            continue
        if matrix[ni][nj] != "x":
            continue
        if visited[ni][nj]:
            continue
        # 이 미네랄이 바닥에 닿아있는지 확인
        res = dfs(ni, nj)
        if not res:
            continue
        else:
            cluster, bottom = res
            break

    if not cluster or not bottom:
        return

    for y, x in cluster:
        matrix[y][x] = "."

    drop_h = r
    for x, y in bottom.items():
        for k in range(1, r + 1):
            if y + k == r:
                drop_h = min(drop_h, k - 1)
                break
            if matrix[y + k][x] == "x":
                drop_h = min(drop_h, k - 1)
                break

    for y, x in cluster:
        matrix[y + drop_h][x] = "x"


r, c = map(int, input().split())

matrix = [list(input().rstrip()) for _ in range(r)]
n = int(input())
heights = [*map(int, input().split())]

for idx, h in enumerate(heights):
    if idx % 2 == 0:
        remove_mineral(cy_throw(h))
    else:
        remove_mineral(sg_throw(h))

for row in matrix:
    print("".join(row))
