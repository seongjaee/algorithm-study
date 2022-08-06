import sys

sys.setrecursionlimit(100000)


def solution():
    def go(y, x, d):
        matrix[y][x] = "*"
        if (y, x) == (N // 2 + 1, M // 2):
            return

        dy, dx = DELTA[d]
        ny, nx = y + dy, x + dx
        if ny < 0 or ny >= N or nx < 0 or nx >= M:
            # 방향 바꾸기
            d = (d + 1) % 4
            dy, dx = DELTA[d]
            ny, nx = y + dy, x + dx

        elif 0 <= ny + dy < N and 0 <= nx + dx < M and matrix[ny + dy][nx + dx] == "*":
            # 방향 바꾸기
            d = (d + 1) % 4
            dy, dx = DELTA[d]
            ny, nx = y + dy, x + dx

        go(ny, nx, d)

    DELTA = [(0, -1), (1, 0), (0, 1), (-1, 0)]

    n = int(input())
    if n == 1:
        print("*")
        return

    M = 4 * n - 3
    N = 4 * n - 1

    matrix = [[" "] * M for _ in range(N)]

    go(0, M - 1, 0)
    for row in matrix:
        print("".join(row).strip())


solution()
