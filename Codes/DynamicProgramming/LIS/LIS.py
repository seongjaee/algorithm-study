import bisect

n = int(input())
A = list(map(int, input().split()))

dp = [A[0]]

for i in range(n):
    if A[i] > dp[-1]:
        dp.append(A[i])
    else:
        idx = bisect.bisect_left(dp, A[i])
        dp[idx] = A[i]
print(len(dp))