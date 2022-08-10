def triangle(s, e):  # e가 뾰족한 쪽
    l = abs(e - s) + 1

    for j in range(N // 2 - l + 1, N // 2 + l):
        matrix[s][j] = "*"

    if s < e:
        for i in range(s + 1, e):
            matrix[i][N // 2 - l + 1 + (i - s)] = "*"
            matrix[i][N // 2 + l - 1 - (i - s)] = "*"

    else:
        for i in range(e + 1, s):
            matrix[i][N // 2 - (i - e)] = "*"
            matrix[i][N // 2 + (i - e)] = "*"

    matrix[e][N // 2] = "*"


n = int(input())
N = 2 ** (n + 1) - 3

matrix = [[" "] * N for _ in range((N + 1) // 2)]

if n % 2:
    s, e = (N + 1) // 2 - 1, 0
else:
    s, e = 0, (N + 1) // 2 - 1
while True:
    triangle(s, e)
    if s < e:
        s, e = (s + e) // 2, s + 1
    elif s > e:
        s, e = (s + e) // 2, s - 1
    else:
        break

for row in matrix:
    print("".join(row).rstrip())
