from itertools import permutations as pmts
import sys

input = sys.stdin.readline
INF = 1e10

N, K = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(N)]

for k in range(N):
    for i in range(N):
        for j in range(N):
            matrix[i][j] = min(matrix[i][j], matrix[i][k] + matrix[k][j])

answer = 1e10

pos = [i for i in range(N) if i != K]
permuations = list(pmts(pos, N - 1))
for p in permuations:
    result = 0
    now = K
    for nxt in p:
        result += matrix[now][nxt]
        now = nxt

    answer = min(answer, result)

print(answer)
