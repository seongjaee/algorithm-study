import sys

input = sys.stdin.readline

n, l = map(int, input().split())
numbers = [*map(int, input().split())]
numbers.sort()

now = 0
cnt = 0
for num in numbers:
    if num >= now:
        now = num + l
        cnt += 1

print(cnt)
