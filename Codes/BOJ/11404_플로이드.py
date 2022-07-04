import sys

input = sys.stdin.readline

INF = 1e10


def floyd():
    for k in range(1, n + 1):
        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if i == j:
                    dists[i][j] = 0
                else:
                    dists[i][j] = min(dists[i][j], dists[i][k] + dists[k][j])


n = int(input())
m = int(input())

dists = [[INF] * (1 + n) for _ in range(1 + n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    dists[a][b] = min(dists[a][b], c)

floyd()
for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(dists[i][j] if dists[i][j] != INF else 0, end=" ")
    print()
