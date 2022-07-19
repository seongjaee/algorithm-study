import sys

input = sys.stdin.readline


def next_permutation(numbers):
    for i in range(n - 1, 0, -1):
        if numbers[i - 1] < numbers[i]:
            for j in range(n - 1, 0, -1):
                if numbers[i - 1] < numbers[j]:
                    numbers[i - 1], numbers[j] = numbers[j], numbers[i - 1]
                    numbers = numbers[:i] + sorted(numbers[i:])
                    return numbers

    return -1


n = int(input())
numbers = list(map(int, input().split()))
result = next_permutation(numbers)
if result == -1:
    print(result)
else:
    print(*result)
