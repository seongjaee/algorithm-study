import sys

input = sys.stdin.readline
min_num, max_num = map(int, input().split())

is_sqaure_nono = [True] * (max_num - min_num + 1)
i = 2
while i**2 <= max_num:
    start = (min_num // (i**2)) * (i**2)
    for j in range(start, max_num + 1, i**2):
        if min_num <= j <= max_num:
            is_sqaure_nono[j - min_num] = False
    i += 1

print(sum(is_sqaure_nono))
