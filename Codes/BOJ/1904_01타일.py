def solution(k):
    if k == 1:
        return 1
    elif k == 2:
        return 2

    dp = [1, 2]
    for i in range(k - 2):
        dp[0], dp[1] = dp[1] % 15746, (dp[0] + dp[1]) % 15746

    return dp[1] % 15746


n = int(input())
print(solution(n))
