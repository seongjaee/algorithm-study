import sys

input = sys.stdin.readline

# 좌하우상
DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]

answer = 0


def left_and_right(y, x, d):
    d1 = (d + 1) % 4
    d2 = (d - 1) % 4
    left = (y + DELTA[d1][0], x + DELTA[d1][1])
    right = (y + DELTA[d2][0], x + DELTA[d2][1])
    return left, right


def two_left_and_right(y, x, d):
    d1 = (d + 1) % 4
    d2 = (d - 1) % 4
    two_left = (y + DELTA[d1][0] * 2, x + DELTA[d1][1] * 2)
    two_right = (y + DELTA[d2][0] * 2, x + DELTA[d2][1] * 2)
    return two_left, two_right


n = int(input())
matrix = [list(map(int, input().split())) for _ in range(n)]


def sand_move(sy, sx, ey, ex, amount):
    global answer
    matrix[sy][sx] -= amount
    if 0 <= ey < n and 0 <= ex < n:
        matrix[ey][ex] += amount
    else:
        answer += amount


def tornado_move(sy, sx, d):
    yy, yx = sy + DELTA[d][0], sx + DELTA[d][1]
    ay, ax = yy + DELTA[d][0], yx + DELTA[d][1]

    percents_1_poses = left_and_right(sy, sx, d)
    percents_2_poses = two_left_and_right(yy, yx, d)
    percents_5_pos = ay + DELTA[d][0], ax + DELTA[d][1]
    percents_7_poses = left_and_right(yy, yx, d)
    percents_10_poses = left_and_right(ay, ax, d)

    percent_positions = [
        (1, percents_1_poses[0]),
        (1, percents_1_poses[1]),
        (2, percents_2_poses[0]),
        (2, percents_2_poses[1]),
        (5, percents_5_pos),
        (7, percents_7_poses[0]),
        (7, percents_7_poses[1]),
        (10, percents_10_poses[0]),
        (10, percents_10_poses[1]),
    ]

    sand_amount = matrix[yy][yx]

    for percent, (ey, ex) in percent_positions:
        sand_move(yy, yx, ey, ex, sand_amount * percent // 100)

    sand_move(yy, yx, ay, ax, matrix[yy][yx])


y, x = n // 2, n // 2
d = 0
for k in range(1, n):
    # 왼쪽 or 오른쪽
    for _ in range(k):
        tornado_move(y, x, d)
        x += DELTA[d][1]

    # 아래 or 위
    d += 1
    for _ in range(k):
        tornado_move(y, x, d)
        y += DELTA[d][0]

    d = (d + 1) % 4

for _ in range(n - 1):
    tornado_move(y, x, 0)
    x -= 1

print(answer)
