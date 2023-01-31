def solution(n, count):
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    dp[1][1] = 1
    for i in range(2, n + 1):
        for j in range(1, i + 1):
            dp[i][j] = dp[i - 1][j - 1]
            if j < i:
                dp[i][j] += dp[i - 1][j] * (2 * i - 2)
            dp[i][j] %= 1000000007

    return dp[n][count]
