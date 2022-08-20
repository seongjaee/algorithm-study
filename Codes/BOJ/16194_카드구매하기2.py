import sys

input = sys.stdin.readline

n = int(input())
numbers = list(map(int, input().split()))
dp = [0] * (n + 1)

for j in range(n + 1):
    dp[j] = j * numbers[0]

for i in range(1, len(numbers)):  # 카드
    for j in range(1, n + 1):  # 금액
        if j - i - 1 >= 0:
            dp[j] = min(dp[j], dp[j - i - 1] + numbers[i])

print(dp[-1])
