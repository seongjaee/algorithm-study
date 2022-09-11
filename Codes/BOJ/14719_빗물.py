import sys

input = sys.stdin.readline


def is_left_closed(i, j):
    if matrix[i][j] == 1:
        return True
    if j == 0:
        return False
    return is_left_closed(i, j - 1)


def is_right_closed(i, j):
    if matrix[i][j] == 1:
        return True
    if j == W - 1:
        return False
    return is_right_closed(i, j + 1)


def is_filled(i, j):
    return is_left_closed(i, j) and is_right_closed(i, j)


H, W = map(int, input().split())
heights = [*map(int, input().split())]

matrix = [[0] * W for _ in range(H)]
for j, height in enumerate(heights):
    for i in range(height):
        matrix[H - 1 - i][j] = 1

cnt = 0
for i in range(H):
    for j in range(W):
        if matrix[i][j] == 0 and is_filled(i, j):
            cnt += 1

print(cnt)
