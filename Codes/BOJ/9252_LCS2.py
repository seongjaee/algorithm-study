A = input()
B = input()

n = len(A)
m = len(B)
dp = [[0] * (n + 1) for _ in range(m + 1)]

lcs = {}

for j in range(m):
    for i in range(n):
        if A[i] == B[j]:
            temp = dp[j][i] + 1
            dp[j + 1][i + 1] = temp
        else:
            dp[j + 1][i + 1] = max(dp[j][i + 1], dp[j + 1][i])

result = dp[-1][-1]
print(result)


if result:
    now = result
    nb, na = m + 1, n + 1
    lcs = ''
    for j in range(m, 0, -1):
        for i in range(n, 0, -1):
            if dp[j][i] == now and dp[j - 1][i] == dp[j][i - 1] == now - 1 and i < na and j < nb:
                lcs += A[i - 1]
                now -= 1
                nb, na = j, i

    print(lcs[::-1])