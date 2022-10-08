import sys

input = sys.stdin.readline
n, m = map(int, input().split())
for _ in range(n):
    row = input().rstrip()
    print(row[::-1])
