import sys


input = sys.stdin.readline

n = int(input())
numbers = [*map(int, input().split())]

xor_presum = [0]
for num in numbers:
    xor_presum.append(xor_presum[-1] ^ num)

bit_cnt = [0] * 30
for num in xor_presum:
    i = 0
    while num > 0:
        num, r = divmod(num, 2)
        if r:
            bit_cnt[i] += 1
        i += 1

f = lambda k, i, cnt: cnt * (k - cnt) * (2**i)
answer = sum([f(len(xor_presum), i, cnt) for i, cnt in enumerate(bit_cnt)])

print(answer)
