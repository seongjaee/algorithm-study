def solution(y, x, k):
    if k == 3:
        matrix[y][x] = "*"
        matrix[y + 1][x - 1] = "*"
        matrix[y + 1][x + 1] = "*"
        for j in range(x - 2, x + 3):
            matrix[y + 2][j] = "*"
        return

    nk = k // 2
    solution(y, x, nk)
    solution(y + nk, x - nk, nk)
    solution(y + nk, x + nk, nk)


n = int(input())

matrix = [[" "] * (2 * n) for _ in range(n)]
solution(0, n - 1, n)

for row in matrix:
    print("".join(row))
