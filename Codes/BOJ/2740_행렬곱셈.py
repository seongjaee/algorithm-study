import sys

input = sys.stdin.readline


def product(v, w):
    res = 0
    for i in range(len(v)):
        res += v[i] * w[i]
    return res


n, m = map(int, input().split())
A = [[*map(int, input().split())] for _ in range(n)]

m, k = map(int, input().split())
B = [[*map(int, input().split())] for _ in range(m)]

C = [[0] * k for _ in range(n)]

for i in range(n):
    for j in range(k):
        C[i][j] = product(A[i], [x[j] for x in B])

for row in C:
    print(*row)
