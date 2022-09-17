import sys

input = sys.stdin.readline


def solution(numbers):
    left = sum(numbers[:-1])
    if left <= numbers[-1]:
        return numbers[-1] - left
    return (left + numbers[-1]) % 2


n = int(input())
numbers = sorted([int(input()) for _ in range(n)])
print(solution(numbers))
