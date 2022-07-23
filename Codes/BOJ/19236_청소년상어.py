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
