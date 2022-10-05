from copy import deepcopy
import sys

input = sys.stdin.readline

FISH_DELTA = [(0, -1), (-1, -1), (-1, 0), (-1, 1), (0, 1), (1, 1), (1, 0), (1, -1)]
SHARK_DELTA = [(-1, 0), (0, -1), (1, 0), (0, 1)]


def all_fish_move():
    def fish_next_pos(i, j, d):
        for k in range(8):
            nd = (d - k) % 8
            ni, nj = i + FISH_DELTA[nd][0], j + FISH_DELTA[nd][1]
            if ni < 0 or ni >= 4 or nj < 0 or nj >= 4:
                continue
            if shark == [ni, nj] or scent_matrix[ni][nj]:
                continue
            return ni, nj, nd

        return i, j, d

    new_matrix = [[[] for _ in range(4)] for _ in range(4)]
    for i in range(4):
        for j in range(4):
            fishes = matrix[i][j]
            for fish_d in fishes:
                ni, nj, nd = fish_next_pos(i, j, fish_d)
                new_matrix[ni][nj].append(nd)

    return new_matrix


def shark_move_three_time():
    def dfs(x, y, level, points, fish_cnt):
        nonlocal max_fish_cnt, ate_points
        if level == 3:
            if fish_cnt > max_fish_cnt:
                max_fish_cnt = fish_cnt
                ate_points = points[:]
            return

        for dx, dy in SHARK_DELTA:
            nx, ny = x + dx, y + dy
            if nx < 0 or nx >= 4 or ny < 0 or ny >= 4:
                continue

            if visited[nx][ny]:
                dfs(nx, ny, level + 1, points + [(nx, ny)], fish_cnt)

            else:
                visited[nx][ny] = True
                dfs(
                    nx,
                    ny,
                    level + 1,
                    points + [(nx, ny)],
                    fish_cnt + len(matrix[nx][ny]),
                )
                visited[nx][ny] = False

    max_fish_cnt = -1
    ate_points = []
    visited = [[False] * 4 for _ in range(4)]
    dfs(*shark, 0, [], 0)

    for i, j in ate_points:
        if matrix[i][j]:
            scent_matrix[i][j] = 3
            matrix[i][j] = []

    shark[0] = ate_points[-1][0]
    shark[1] = ate_points[-1][1]


def scent_descending():
    for i in range(4):
        for j in range(4):
            if scent_matrix[i][j] > 0:
                scent_matrix[i][j] -= 1


def simulate():
    global matrix
    copyed_matrix = deepcopy(matrix)
    matrix = all_fish_move()

    shark_move_three_time()
    scent_descending()

    for i in range(4):
        for j in range(4):
            matrix[i][j] += copyed_matrix[i][j]


m, s = map(int, input().split())

matrix = [[[] for _ in range(4)] for _ in range(4)]
scent_matrix = [[0] * 4 for _ in range(4)]

for _ in range(m):
    x, y, d = map(lambda num: int(num) - 1, input().split())
    matrix[x][y].append(d)


shark = list(map(lambda num: int(num) - 1, input().split()))

for _ in range(s):
    simulate()

answer = 0

for i in range(4):
    for j in range(4):
        answer += len(matrix[i][j])
print(answer)
