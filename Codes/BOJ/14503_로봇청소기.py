import sys

sys.setrecursionlimit(10000)
input = sys.stdin.readline


LEFT = {0: (0, -1), 1: (-1, 0), 2: (0, 1), 3: (1, 0)}

DELTA = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def go(y, x, d, a_cnt):
    global result
    # 현재 위치 청소
    if matrix[y][x] == "0":
        matrix[y][x] = "2"
        result += 1

    # 왼쪽 회전
    d = (d - 1) % 4

    # 왼쪽 위치
    ly, lx = y + DELTA[d][0], x + DELTA[d][1]

    if matrix[ly][lx] == "0":
        go(ly, lx, d, 0)
    else:
        a_cnt += 1
        if a_cnt == 4:
            by, bx = y + DELTA[(d + 2) % 4][0], x + DELTA[(d + 2) % 4][1]
            if matrix[by][bx] == "1":
                return
            else:
                go(by, bx, d, 0)
        else:
            go(y, x, d, a_cnt)


n, m = map(int, input().split())
r, c, d = map(int, input().split())

matrix = [list(input().split()) for _ in range(n)]
result = 0
go(r, c, d, 0)
print(result)
