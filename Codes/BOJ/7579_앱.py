# PyPy3 4332ms
# 각 메모리별 확보하는데 드는 최소 비용 배열
INF = 1e10

n, m = map(int, input().split())
memories = list(map(int, input().split()))
costs = list(map(int, input().split()))

dp = [INF] * (1 + m)
dp[0] = 0
    
for i in range(n):
    for j in range(m, 0, -1):
        dp[j] = min(dp[max(0, j - memories[i])] + costs[i], dp[j])

print(dp[-1])


# Python3 648ms, 비용 기준
# 각 비용별 확보할 수 있는 최대 메모리 배열
n, m = map(int, input().split())
memories = [0] + list(map(int, input().split()))
costs = [0] + list(map(int, input().split()))
total_cost = sum(costs)

dp = [0] * (total_cost + 1)
result = sum(costs)

for i in range(1, n + 1):
    for j in range(total_cost, 0, -1):
        if j - costs[i] >= 0:
            dp[j] = max(dp[j - costs[i]] + memories[i], dp[j])
        if dp[j] >= m:
            result = min(result, j)

if m != 0:
    print(result)
else:
    print(0)
