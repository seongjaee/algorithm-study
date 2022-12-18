import sys

input = sys.stdin.readline


def is_square(sy, sx, k):
    if sy + k >= 11 or sx + k >= 11:
        return False

    for i in range(sy, sy + k):
        for j in range(sx, sx + k):
            if matrix[i][j] == 0:
                return False
    return True


def fill_area(sy, sx, k, flag):
    for y in range(sy, sy + k):
        for x in range(sx, sx + k):
            matrix[y][x] = flag


def backtrack(level, cnt, remain_cnt):
    global answer
    if answer <= cnt:
        return

    y, x = divmod(level, 10)

    if remain_cnt == 0:
        answer = cnt
        return

    if y == 10:
        return

    if matrix[y][x] == 0:
        backtrack(level + 1, cnt, remain_cnt)

    for size in range(5, 0, -1):
        if papers[size] == 0:
            continue

        if is_square(y, x, size):
            fill_area(y, x, size, 0)
            papers[size] -= 1

            backtrack(level + 1, cnt + 1, remain_cnt - size * size)

            fill_area(y, x, size, 1)
            papers[size] += 1


matrix = [[*map(int, input().split())] for _ in range(10)]

remain_cnt = 0
for i in range(10):
    for j in range(10):
        if matrix[i][j]:
            remain_cnt += 1

papers = [0, 5, 5, 5, 5, 5]

answer = 26
backtrack(0, 0, remain_cnt)
print(answer if answer != 26 else -1)
