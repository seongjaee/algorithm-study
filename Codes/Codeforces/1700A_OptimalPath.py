import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    result = 0
    for i in range(1, m):
        result += i
    for j in range(m, n * m + 1, m):
        result += j
    print(result)
