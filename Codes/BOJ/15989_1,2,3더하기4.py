import sys

input = sys.stdin.readline


def dp(k):
    if k == 0:
        return 0
    if memo[k]:
        return memo[k]

    result = 0
    i = 0  # 3을 사용하는 횟수
    while 3 * i <= k:
        result += count_with_1or2(k - 3 * i)
        i += 1

    memo[k] = result
    return result


def count_with_1or2(k):
    return k // 2 + 1


memo = [0] * 10001
memo[1] = 1
memo[2] = 2
memo[3] = 3


t = int(input())
for _ in range(t):
    tc = int(input())
    print(dp(tc))
