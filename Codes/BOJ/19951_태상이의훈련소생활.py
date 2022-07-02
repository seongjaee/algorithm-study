import sys

input = sys.stdin.readline

n, m = map(int, input().split())

numbers = [*map(int, input().split())]

todo = [0] * (n + 1)
for _ in range(m):
    a, b, k = map(int, input().split())
    a -= 1
    b -= 1
    todo[a] += k
    todo[b + 1] -= k

for i in range(n):
    todo[i + 1] += todo[i]

for i in range(n):
    print(numbers[i] + todo[i], end=" ")
