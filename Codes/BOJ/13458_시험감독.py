import sys

input = sys.stdin.readline

n = int(input())
numbers = [*map(int, input().split())]
b, c = map(int, input().split())

answer = n
for num in numbers:
    q, r = divmod(max(0, num - b), c)
    answer += q
    answer += int(r > 0)

print(answer)
