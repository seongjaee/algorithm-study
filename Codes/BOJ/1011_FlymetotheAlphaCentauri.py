import sys, math

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    x, y = map(int, input().split())
    k = y - x
    m = int(math.sqrt(k))

    if k <= m**2 - m:
        print(2 * m - 2)
    elif k <= m**2:
        print(2 * m - 1)
    elif k <= m**2 + m:
        print(2 * m)
    else:
        print(2 * m + 1)
