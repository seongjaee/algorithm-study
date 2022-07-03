# (y, x)에서 시작하는 k 크기 패턴그리기
def solution(y, x, k):
    if k == 1:
        matrix[y][x] = "*"
        return

    nk = k // 3
    for i in range(3):
        for j in range(3):
            if (i, j) != (1, 1):
                solution(y + i * nk, x + j * nk, nk)


n = int(input())
matrix = [[" "] * n for _ in range(n)]
solution(0, 0, n)
for row in matrix:
    print("".join(row))
