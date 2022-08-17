import sys

input = sys.stdin.readline


def solution(A, B):
    cnt = 0
    for i in range(n - 2):
        for j in range(m - 2):
            if A[i][j] != B[i][j]:
                cnt += 1
                for k in range(i, i + 3):
                    for l in range(j, j + 3):
                        A[k][l] = (A[k][l] + 1) % 2

    return cnt if A == B else -1


n, m = map(int, input().split())
A = [[*map(int, list(input().rstrip()))] for _ in range(n)]
B = [[*map(int, list(input().rstrip()))] for _ in range(n)]


print(solution(A, B))
