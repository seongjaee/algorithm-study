from bisect import bisect_left

n = int(input())
numbers = [*map(int, input().split())]

# 가장 긴 증가하는 부분 수열
L = [0]
for num in numbers:
    if L[-1] < num:
        L.append(num)
    else:
        idx = bisect_left(L, num)
        L[idx] = num

print(len(L) - 1)