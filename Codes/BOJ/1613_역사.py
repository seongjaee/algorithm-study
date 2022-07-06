import sys

input = sys.stdin.readline

INF = 1e9
n, k = map(int, input().split())
forward = [[INF] * (n + 1) for _ in range(n + 1)]
backward = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    forward[i][i] = 0
    backward[i][i] = 0

for _ in range(k):
    a, b = map(int, input().split())
    forward[a][b] = 0
    backward[b][a] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            forward[i][j] = min(forward[i][j], forward[i][k] + forward[k][j])
            backward[i][j] = min(backward[i][j], backward[i][k] + backward[k][j])


s = int(input())
for _ in range(s):
    a, b = map(int, input().split())
    if forward[a][b] == 0:
        print(-1)
    elif backward[a][b] == 0:
        print(1)
    else:
        print(0)
