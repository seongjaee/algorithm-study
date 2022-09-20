code = [*map(int, input())]


def solution(code):
    n = len(code)
    if code[0] == 0:
        return [0]
    if n == 1:
        return [1]

    dp = [0] * (n + 1)
    dp[0] = 1
    dp[1] = 1
    for i in range(2, n + 1):
        if code[i - 1] == 0:
            if code[i - 2] > 2 or code[i - 2] == 0:
                return [0]
            dp[i - 1] = dp[i - 2]
            dp[i] = dp[i - 1]
        elif code[i - 2] == 1 or (code[i - 2] == 2 and code[i - 1] < 7):
            dp[i] = (dp[i - 1] + dp[i - 2]) % 1000000
        else:
            dp[i] = dp[i - 1]

    return dp


print(solution(code)[-1])
