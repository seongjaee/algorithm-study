import sys

input = sys.stdin.readline


def dp_in(i):
    if memo_in[i]:
        return memo_in[i]
    result = 0
    for j in range(i):
        if numbers[i] > numbers[j]:
            result = max(dp_in(j), result)
    memo_in[i] = result + 1
    return result + 1


def dp_out(i):
    if memo_de[i]:
        return memo_de[i]

    result = 0
    for j in range(i + 1, n):
        if numbers[i] > numbers[j]:
            result = max(dp_out(j), result)
    memo_de[i] = result + 1
    return result + 1


n = int(input())
numbers = list(map(int, input().split()))

memo_in = [0] * n
memo_de = [0] * n
for i in range(n):
    dp_in(i)

for i in range(n - 1, -1, -1):
    dp_out(i)

max_value = 0
for i in range(n):
    max_value = max(max_value, memo_in[i] + memo_de[i])

print(max_value - 1)
