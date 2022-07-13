from math import gcd
import sys

input = sys.stdin.readline


# (k, p)의 개수 * 2 : k >= p and gcd(p, k) = 1
def solution(k):
    if k == 1:
        return 3
    result = 0
    for i in range(1, k):
        if gcd(k, i) == 1:
            result += 1
    return result * 2


A = [solution(i) for i in range(1, 1001)]
presum = [0]
for i in range(1000):
    presum.append(presum[-1] + A[i])

c = int(input())

for _ in range(c):
    n = int(input())
    print(presum[n])
