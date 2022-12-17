import sys

input = sys.stdin.readline

n, m = map(int, input().split())
tall = [[0] * (n + 1) for _ in range(n + 1)]  # 1 : a < b, -1: a > b
for _ in range(m):
    a, b = map(int, input().split())
    tall[a][b] = 1
    tall[b][a] = -1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if tall[i][k] == 1 and tall[k][j] == 1:
                tall[i][j] = 1
            elif tall[i][k] == -1 and tall[k][j] == -1:
                tall[i][j] = -1

answer = 0
for i in range(1, n + 1):
    if tall[i].count(0) == 2:
        answer += 1

print(answer)
