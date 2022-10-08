import sys

input = sys.stdin.readline
a, b, c = map(int, input().split())
time = int(input())

now = a * 3600 + b * 60 + c
now += time

h = now // 3600
m = (now - h * 3600) // 60
s = now % 60
print(h % 24, m, s)
