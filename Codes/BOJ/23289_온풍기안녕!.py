import sys

input = sys.stdin.readline

# 우좌상하
DELTA = [(0, 1), (0, -1), (-1, 0), (1, 0)]
OPPOSITE_D = [1, 0, 3, 2]

r, c, k = map(int, input().split())
matrix = [list(map(int, input().split())) for _ in range(r)]
heaters = []
check_points = []
for i in range(r):
    for j in range(c):
        if 0 < matrix[i][j] < 5:
            heaters.append((i, j, matrix[i][j] - 1))
            matrix[i][j] = 0
        elif matrix[i][j] == 5:
            check_points.append((i, j))
            matrix[i][j] = 0


w = int(input())
walls = {}
for _ in range(w):
    x, y, t = map(int, input().split())
    x -= 1
    y -= 1
    if t == 0:
        walls[(x, y)] = walls.get((x, y), []) + [2]
        walls[(x - 1, y)] = walls.get((x - 1, y), []) + [3]
    else:
        walls[(x, y)] = walls.get((x, y), []) + [0]
        walls[(x, y + 1)] = walls.get((x, y + 1), []) + [1]


def heat_blow(sx, sy, d):
    visited = [[False] * c for _ in range(r)]

    def dfs(x, y, d, tem):
        if tem == 0:
            return
        matrix[x][y] += tem

        nds = [0, 1] if d > 1 else [2, 3]

        for nd in nds:
            diag_x = x + DELTA[nd][0] + DELTA[d][0]
            diag_y = y + DELTA[nd][1] + DELTA[d][1]
            if diag_x < 0 or diag_x >= r or diag_y < 0 or diag_y >= c:
                continue

            if visited[diag_x][diag_y]:
                continue
            if nd in walls.get((x, y), []):
                continue
            if OPPOSITE_D[d] in walls.get((diag_x, diag_y), []):
                continue
            visited[diag_x][diag_y] = True
            dfs(diag_x, diag_y, d, tem - 1)

        nx, ny = x + DELTA[d][0], y + DELTA[d][1]
        if nx < 0 or nx >= r or ny < 0 or ny >= c:
            return
        if visited[nx][ny] or d in walls.get((x, y), []):
            return
        visited[nx][ny] = True
        dfs(nx, ny, d, tem - 1)

    x, y = sx + DELTA[d][0], sy + DELTA[d][1]
    if 0 <= x < r and 0 <= y < c:
        visited[x][y] = True
        dfs(x, y, d, 5)


def adjust_temperature():
    increments = [[0] * c for _ in range(r)]

    # 상하
    for i in range(r - 1):
        for j in range(c):
            if 3 in walls.get((i, j), []):
                continue
            ni, nj = i + 1, j
            diff = abs(matrix[ni][nj] - matrix[i][j]) // 4
            if matrix[i][j] > matrix[ni][nj]:
                diff *= -1
            increments[i][j] += diff
            increments[ni][nj] -= diff

    # 좌우
    for i in range(r):
        for j in range(c - 1):
            if 0 in walls.get((i, j), []):
                continue
            ni, nj = i, j + 1
            diff = abs(matrix[ni][nj] - matrix[i][j]) // 4
            if matrix[i][j] > matrix[ni][nj]:
                diff *= -1
            increments[i][j] += diff
            increments[ni][nj] -= diff

    for i in range(r):
        for j in range(c):
            matrix[i][j] += increments[i][j]

    # 최외곽 온도 하락
    for i in range(r):
        if matrix[i][0] > 0:
            matrix[i][0] -= 1
        if matrix[i][c - 1] > 0:
            matrix[i][c - 1] -= 1
    for j in range(1, c - 1):
        if matrix[0][j] > 0:
            matrix[0][j] -= 1
        if matrix[r - 1][j] > 0:
            matrix[r - 1][j] -= 1


def end_check():
    for x, y in check_points:
        if matrix[x][y] < k:
            return False
    return True


def simulate():
    for chocolate in range(1, 101):
        for x, y, d in heaters:
            heat_blow(x, y, d)

        adjust_temperature()

        if end_check():
            return chocolate

    return 101


print(simulate())
