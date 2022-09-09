import sys

input = sys.stdin.readline

n, k = map(int, input().split())
coins = set()
for _ in range(n):
    coins.add(int(input()))

coins = list(coins)
n = len(coins)
dp = [0] + [1000000] * k
for i in range(n):
    coin = coins[i]
    for j in range(1, k + 1):
        if j - coin >= 0:
            dp[j] = min(dp[j], dp[j - coin] + 1)

print(dp[-1] if dp[-1] != 1000000 else -1)
