def solution(k):
    start, end = 2 * k, 4 * n - 3 - 2 * k
    for i in range(start, end):
        matrix[start][i] = "*"
        matrix[i][start] = "*"
        matrix[4 * n - 3 - start - 1][i] = "*"
        matrix[i][4 * n - 3 - start - 1] = "*"


n = int(input())

matrix = [[" "] * (4 * n - 3) for _ in range(4 * n - 3)]

for i in range(n):
    solution(i)

for row in matrix:
    print("".join(row))
