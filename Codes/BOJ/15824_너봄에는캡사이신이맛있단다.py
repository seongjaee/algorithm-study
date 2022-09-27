import sys

input = sys.stdin.readline


P = 1000000007


def power(a, k):
    result = 1
    while k > 0:
        if k % 2:
            result *= a
            result %= P
        a *= a
        a %= P
        k //= 2
    return result % P


n = int(input())
numbers = list(map(int, input().split()))
numbers.sort()

cache = [power(2, i) for i in range(n)]

answer = 0
for i in range(n // 2):
    answer += (numbers[n - 1 - i] - numbers[i]) * (cache[n - 1 - i] - cache[i])
    answer %= P

print(answer)
