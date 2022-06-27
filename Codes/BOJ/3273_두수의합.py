import sys

input = sys.stdin.readline

n = int(input())
numbers = [*map(int, input().split())]
numbers.sort()
x = int(input())

cnt = 0
left, right = 0, n - 1
while left < right:
    now = numbers[left] + numbers[right]
    if now > x:
        right -= 1
    elif now == x:
        cnt += 1
        left += 1
    else:
        left += 1

print(cnt)
