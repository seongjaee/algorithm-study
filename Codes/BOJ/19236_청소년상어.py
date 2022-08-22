from copy import deepcopy
import sys

input = sys.stdin.readline

DELTA = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]


def backtrack(matrix, fish_pos, cnt):
    global answer
    answer = max(answer, cnt)

    # 물고기 움직이기
    for i in range(1, 17):
        if fish_pos[i][0] == -1:
            continue
        y, x = fish_pos[i]
        d = matrix[y][x][1]

        for k in range(8):
            dy, dx = DELTA[(d + k) % 8]
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
                continue
            if matrix[ny][nx][0] == 17:
                continue

            nxt_fish, nxt_d = matrix[ny][nx]
            if nxt_fish:
                fish_pos[nxt_fish] = (y, x)
                fish_pos[i] = (ny, nx)
                matrix[ny][nx] = [i, (d + k) % 8]
                matrix[y][x] = [nxt_fish, nxt_d]
            else:
                fish_pos[i] = (ny, nx)
                matrix[ny][nx] = [i, (d + k) % 8]
                matrix[y][x] = [0, 0]
            break

    # 상어 이동하기
    sy, sx = fish_pos[17]
    d = matrix[sy][sx][1]

    for k in range(1, 4):
        dy, dx = DELTA[d]
        ny, nx = sy + dy * k, sx + dx * k

        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            break
        if matrix[ny][nx][0] == 0:
            continue

        fish_num, fish_d = matrix[ny][nx]

        matrix[sy][sx] = [0, 0]
        matrix[ny][nx] = [17, fish_d]
        fish_pos[fish_num] = (-1, -1)
        fish_pos[17] = (ny, nx)

        backtrack(deepcopy(matrix), fish_pos[:], cnt + fish_num)

        fish_pos[17] = (sy, sx)
        fish_pos[fish_num] = (ny, nx)
        matrix[ny][nx] = [fish_num, fish_d]
        matrix[sy][sx] = [17, d]


matrix = [[None] * 4 for _ in range(4)]  # [물고기 번호, 방향], 상어 번호 17
fish_pos = [(-1, -1) for _ in range(18)]
for i in range(4):
    row = [*map(int, input().split())]
    for j in range(4):
        matrix[i][j] = [row[2 * j], row[2 * j + 1] - 1]
        fish_pos[row[2 * j]] = (i, j)

fish_num, fish_d = matrix[0][0]
fish_pos[17] = (0, 0)
matrix[0][0] = [17, fish_d]
fish_pos[fish_num] = (-1, -1)

answer = 0
backtrack(deepcopy(matrix), fish_pos[:], fish_num)
print(answer)


## 2번째 풀이
from copy import deepcopy
import sys


input = sys.stdin.readline


def backtrack(matrix, fish_d, sy, sx, res):
    global answer
    copy_matrix = deepcopy(matrix)
    copy_fish_d = fish_d[:]

    # 먹기
    ate_fish_num = copy_matrix[sy][sx]
    copy_matrix[sy][sx] = None
    sd = copy_fish_d[ate_fish_num][2]
    copy_fish_d[ate_fish_num] = None

    # 물고기 움직임
    for fish_num in range(1, 17):
        if copy_fish_d[fish_num] == None:
            continue

        y, x, d = copy_fish_d[fish_num]
        for k in range(8):
            now_d = (d + k) % 8
            dy, dx = DELTA[now_d]
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= 4 or nx < 0 or nx >= 4 or (ny, nx) == (sy, sx):
                continue

            nxt_fish_num = copy_matrix[ny][nx]
            copy_matrix[ny][nx], copy_matrix[y][x] = (
                copy_matrix[y][x],
                copy_matrix[ny][nx],
            )
            copy_fish_d[fish_num] = (ny, nx, now_d)
            if nxt_fish_num != None:
                copy_fish_d[nxt_fish_num] = (y, x, copy_fish_d[nxt_fish_num][2])

            break

    # 상어 움직임
    dy, dx = DELTA[sd]
    for k in range(1, 4):
        ny, nx = sy + dy * k, sx + dx * k
        if ny < 0 or ny >= 4 or nx < 0 or nx >= 4:
            break
        if copy_matrix[ny][nx] == None:
            continue
        backtrack(copy_matrix, copy_fish_d, ny, nx, res + ate_fish_num)

    answer = max(answer, res + ate_fish_num)


DELTA = [(-1, 0), (-1, -1), (0, -1), (1, -1), (1, 0), (1, 1), (0, 1), (-1, 1)]

matrix = [[None] * 4 for _ in range(4)]
fish_d = [None] * 17
for i in range(4):
    a1, b1, a2, b2, a3, b3, a4, b4 = map(int, input().split())
    matrix[i][0] = a1
    matrix[i][1] = a2
    matrix[i][2] = a3
    matrix[i][3] = a4
    fish_d[a1] = (i, 0, b1 - 1)
    fish_d[a2] = (i, 1, b2 - 1)
    fish_d[a3] = (i, 2, b3 - 1)
    fish_d[a4] = (i, 3, b4 - 1)

answer = 0
backtrack(matrix, fish_d, 0, 0, 0)

print(answer)
