n = int(input())
memo = [1] * 10

for _ in range(n - 1):
    for i in range(10):
        memo[i] = sum(memo[i:])
print(sum(memo) % 10007)
