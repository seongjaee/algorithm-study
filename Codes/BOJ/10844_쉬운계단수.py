n = int(input())
dp = [0] + [1] * 9  # 끝자리가 k인 계단수의 개수

for i in range(n - 1):
    new_dp = [0] * 10
    new_dp[0] = dp[1]
    new_dp[9] = dp[8]
    for j in range(1, 9):
        new_dp[j] = dp[j-1] + dp[j+1]
    dp = new_dp

print(sum(dp) % 1000000000)
