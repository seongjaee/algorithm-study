import sys

input = sys.stdin.readline

DELTA = [(0, 0), (0, 1), (0, -1), (-1, 0), (1, 0)]


def roll(d):
    global x, y
    dx, dy = DELTA[d]
    nx, ny = x + dx, y + dy
    if 0 > nx or nx >= n or 0 > ny or ny >= m:
        return

    # 동
    if d == 1:
        temp = dice[0]
        dice[0] = dice[3]
        dice[3] = dice[5]
        dice[5] = dice[2]
        dice[2] = temp

    # 서
    elif d == 2:
        temp = dice[0]
        dice[0] = dice[2]
        dice[2] = dice[5]
        dice[5] = dice[3]
        dice[3] = temp

    # 북
    elif d == 3:
        temp = dice[0]
        dice[0] = dice[4]
        dice[4] = dice[5]
        dice[5] = dice[1]
        dice[1] = temp

    # 남
    elif d == 4:
        temp = dice[0]
        dice[0] = dice[1]
        dice[1] = dice[5]
        dice[5] = dice[4]
        dice[4] = temp

    map_number = matrix[nx][ny]

    if map_number:
        dice[5] = map_number
        matrix[nx][ny] = 0
    else:
        matrix[nx][ny] = dice[5]

    x, y = nx, ny
    print(dice[0])


n, m, x, y, k = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]
commands = [*map(int, input().split())]

# 상 북 동 서 남 하
dice = [0] * 6
for command in commands:
    roll(command)
