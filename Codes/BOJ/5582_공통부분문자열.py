A = input()
B = input()
answer = 0
dp = [0] * (len(B) + 1)
for i in range(1, len(A) + 1):
    for j in range(len(B), 0, -1):
        if A[i - 1] == B[j - 1]:
            dp[j] = dp[j - 1] + 1
            answer = max(answer, dp[j])
        else:
            dp[j] = 0

print(answer)


## 두번째 풀이
import sys

input = sys.stdin.readline

s1 = input().rstrip()
s2 = input().rstrip()

n = len(s1)
m = len(s2)
matrix = [[0] * (m + 1) for _ in range(n + 1)]
result = 0
for i in range(1, n + 1):
    for j in range(1, m + 1):
        if s1[i - 1] == s2[j - 1]:
            matrix[i][j] = matrix[i - 1][j - 1] + 1
            result = max(result, matrix[i][j])

print(result)
