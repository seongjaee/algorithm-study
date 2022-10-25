import sys

input = sys.stdin.readline


def simulate():
    time = 1

    while time < n:
        # 폭탄 설치
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][j] = 3
                else:
                    matrix[i][j] -= 1

        time += 1
        if time >= n:
            break

        # 폭탄 터짐
        booms = []
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 1:
                    booms.append((i, j))
                    for dy, dx in DELTA:
                        ny, nx = i + dy, j + dx
                        if ny < 0 or ny >= r or nx < 0 or nx >= c:
                            continue
                        booms.append((ny, nx))

        for y, x in booms:
            matrix[y][x] = 0

        for i in range(r):
            for j in range(c):
                if matrix[i][j]:
                    matrix[i][j] -= 1

        time += 1


DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
r, c, n = map(int, input().split())
matrix = [[0] * c for _ in range(r)]

for i in range(r):
    for j, char in enumerate(input().rstrip()):
        if char == "O":
            matrix[i][j] = 2

simulate()

for row in matrix:
    print("".join(map(lambda num: "O" if num else ".", row)))


# 두번째 풀이
import sys

input = sys.stdin.readline
r, c, n = map(int, input().split())

matrix = [[0] * c for _ in range(r)]
for i in range(r):
    for j, char in enumerate(input().rstrip()):
        if char == "O":
            matrix[i][j] = 2


def simulate():
    time = 1
    while time < n:
        for i in range(r):
            for j in range(c):
                if matrix[i][j] == 0:
                    matrix[i][j] = 3
                else:
                    matrix[i][j] -= 1

        time += 1
        if time == n:
            break

        booms = []
        for i in range(r):
            for j in range(c):
                if matrix[i][j] > 1:
                    matrix[i][j] -= 1
                elif matrix[i][j] == 1:
                    booms.append((i, j))

        for i, j in booms:
            matrix[i][j] = 0
            for ni, nj in [(i + 1, j), (i - 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= ni < r and 0 <= nj < c:
                    matrix[ni][nj] = 0

        time += 1
        if time == n:
            break


simulate()


for row in matrix:
    for num in row:
        print("O" if num else ".", end="")
    print()
