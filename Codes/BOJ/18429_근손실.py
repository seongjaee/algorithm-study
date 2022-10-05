import sys

input = sys.stdin.readline


def simulate(numbers):
    now = 500
    for num in numbers:
        now += num
        now -= k
        if now < 500:
            return False
    return True


def permutation(level):
    global answer
    if level == n:
        if simulate(numbers):
            answer += 1
        return

    for nxt in range(level, n):
        numbers[nxt], numbers[level] = numbers[level], numbers[nxt]
        permutation(level + 1)
        numbers[nxt], numbers[level] = numbers[level], numbers[nxt]


n, k = map(int, input().split())
numbers = list(map(int, input().split()))
answer = 0

permutation(0)
print(answer)
