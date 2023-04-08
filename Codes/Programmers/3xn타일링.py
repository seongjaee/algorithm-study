def solution(n):
    if n % 2:
        return 0
    if n == 2:
        return 3
    if n == 4:
        return 11

    dp = [3, 11]
    for i in range(0, n - 4, 2):
        temp = 2
        for i in range(len(dp) - 1):
            temp += 2 * dp[i]
        temp += dp[-1] * 3
        dp.append(temp % 1000000007)

    return dp[-1] % 1000000007
