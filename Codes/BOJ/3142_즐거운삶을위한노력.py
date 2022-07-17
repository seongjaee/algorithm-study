import sys

input = sys.stdin.readline

min_factor = [i for i in range(1000001)]
for i in range(2, 1001):
    if min_factor[i] == i:
        for j in range(i**2, 1000001, i):
            if min_factor[j] == j:
                min_factor[j] = i


def factorizing(num, min_f):
    global odd_cnt
    while num > 1:
        if now[min_f] == 1:
            now[min_f] = 0
            odd_cnt -= 1
        else:
            now[min_f] += 1
            odd_cnt += 1
        num //= min_f
        min_f = min_factor[num]


now = [0] * 1000001
odd_cnt = 0

n = int(input())
for _ in range(n):
    cur = int(input())
    min_f = min_factor[cur]
    factorizing(cur, min_f)

    if odd_cnt == 0:
        print("DA")
    else:
        print("NE")
