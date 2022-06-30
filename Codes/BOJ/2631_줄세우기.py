from bisect import bisect_left
import sys

input = sys.stdin.readline

n = int(input())

LIS = [0]

for _ in range(n):
    num = int(input())
    if LIS[-1] < num:
        LIS.append(num)
    else:
        idx = bisect_left(LIS, num)
        LIS[idx] = num


print(n - len(LIS) + 1)
