import sys

input = sys.stdin.readline

n = int(input())
m = int(input())

INF = 1e10

m1 = [[INF] * (n + 1) for _ in range(n + 1)]
m2 = [[INF] * (n + 1) for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split())
    m1[a][b] = 1
    m2[b][a] = 1

for i in range(n + 1):
    m1[i][i] = 0
    m2[i][i] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            m1[i][j] = min(m1[i][j], m1[i][k] + m1[k][j])
            m2[i][j] = min(m2[i][j], m2[i][k] + m2[k][j])

for i in range(1, n + 1):
    cnt = 0
    for j in range(1, n + 1):
        if m1[i][j] == INF and m2[i][j] == INF:
            cnt += 1

    print(cnt)
