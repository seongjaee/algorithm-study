import sys

input = sys.stdin.readline

n = int(input())
numbers = input().split()
numbers.sort(reverse=True)

for j in range(n - 1, 0, -1):
    for i in range(j):
        now = numbers[i]
        nxt = numbers[i + 1]
        if now + nxt < nxt + now:
            numbers[i], numbers[i + 1] = numbers[i + 1], numbers[i]

print(int("".join(numbers)))
