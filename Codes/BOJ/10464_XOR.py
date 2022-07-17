import sys


def get_xor_sum(k):
    r = k % 4
    if r == 0:
        return k
    elif r == 1:
        return k ^ (k - 1)
    elif r == 2:
        return k ^ (k - 1) ^ (k - 2)
    else:
        return 0


input = sys.stdin.readline

t = int(input())
for _ in range(t):
    s, f = map(int, input().split())
    left_sum = get_xor_sum(s - 1)
    right_sum = get_xor_sum(f)

    print(left_sum ^ right_sum)
