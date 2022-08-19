import sys
from copy import deepcopy

input = sys.stdin.readline


def local_spin(sy, sx, M):
    m = M // 2
    left_up = [[matrix[i][j] for j in range(sx, sx + m)] for i in range(sy, sy + m)]
    left_down = [
        [matrix[i][j] for j in range(sx, sx + m)] for i in range(sy + m, sy + M)
    ]
    right_up = [
        [matrix[i][j] for j in range(sx + m, sx + M)] for i in range(sy, sy + m)
    ]
    right_down = [
        [matrix[i][j] for j in range(sx + m, sx + M)] for i in range(sy + m, sy + M)
    ]
    for i in range(m):
        for j in range(m):
            matrix[sy + i][sx + j] = left_down[i][j]
            matrix[sy + m + i][sx + j] = right_down[i][j]
            matrix[sy + i][sx + m + j] = left_up[i][j]
            matrix[sy + m + i][sx + m + j] = right_up[i][j]


def rotate(level):
    if level == 0:
        return
    M = 2**level
    m = M // 2
    for y in range(0, N, M):
        for x in range(0, N, M):
            local_spin(y, x, M)


def melt():
    new_matrix = deepcopy(matrix)

    for y in range(N):
        for x in range(N):
            if new_matrix[y][x] == 0:
                continue

            cnt = 0
            for dy, dx in DELTA:
                ny, nx = y + dy, x + dx
                if ny < 0 or ny >= N or nx < 0 or nx >= N:
                    continue
                if new_matrix[ny][nx]:
                    cnt += 1

            if cnt < 3:
                matrix[y][x] -= 1


def dfs(sy, sx):
    stack = [(sy, sx)]
    visited[sy][sx] = True
    size = 1
    cnt = matrix[sy][sx]

    while stack:
        y, x = stack.pop()

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= N or nx < 0 or nx >= N:
                continue
            if visited[ny][nx] or matrix[ny][nx] == 0:
                continue
            visited[ny][nx] = True
            stack.append((ny, nx))
            size += 1
            cnt += matrix[ny][nx]

    return size, cnt


n, q = map(int, input().split())
N = 2**n
matrix = [list(map(int, input().split())) for _ in range(N)]
levels = list(map(int, input().split()))
DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
visited = [[False] * N for _ in range(N)]


for level in levels:
    rotate(level)
    melt()

max_size = 0
total_cnt = 0
for i in range(N):
    for j in range(N):
        if not matrix[i][j]:
            continue
        if not visited[i][j]:
            size, cnt = dfs(i, j)
            max_size = max(max_size, size)
            total_cnt += cnt

print(total_cnt)
print(max_size)
