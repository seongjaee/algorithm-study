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
