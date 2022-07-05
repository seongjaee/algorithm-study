import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [*map(int, input().split())]

    for i in range(n):
        result = 0
        for j in range(n):
            if i != j:
                result ^= numbers[j]
        if result == numbers[i]:
            print(result)
            break
