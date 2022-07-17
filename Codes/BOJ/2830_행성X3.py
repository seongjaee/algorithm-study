import sys

input = sys.stdin.readline

n = int(input())
bit_cnt = [0] * 20
for _ in range(n):
    num = int(input())
    i = 0
    while num > 0:
        num, r = divmod(num, 2)
        if r == 1:
            bit_cnt[i] += 1
        i += 1

f = lambda n, i, cnt: cnt * (n - cnt) * (2**i)
answer = sum([f(n, i, cnt) for i, cnt in enumerate(bit_cnt)])
print(answer)
