A = input()
B = input()

n = len(A)
m = len(B)

# dp = [[0] * (n + 1) for _ in range(m + 1)]

# for i in range(1, m+1):
#     for j in range(1, n+1):
#         if B[i - 1] == A[j - 1]:
#             dp[i][j] = dp[i - 1][j - 1] + 1
#         else:
#             dp[i][j] = max(dp[i-1][j], dp[i][j-1])

# print(dp[-1][-1])

dp = [0] * (n + 1)

for i in range(1, m+1):
    for j in range(1, n+1):
        if B[i - 1] == A[j - 1]:
            dp[j] = dp[j - 1] + 1
        else:
            dp[j] = max(dp[j], dp[j-1])

print(dp[-1])