from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
numbers = [*map(int, input().split())]

L = [0]

for num in numbers:
    if num > L[-1]:
        L.append(num)
    else:
        idx = bisect_left(L, num)
        L[idx] = num

print(len(L) - 1)