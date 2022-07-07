import sys

input = sys.stdin.readline


def solution():
    left, right = 0, 0
    result = n
    now = numbers[0]
    while left <= right < n:
        if now < s:
            right += 1
            if right < n:
                now += numbers[right]
        elif now == s:
            result = min(result, left + (n - 1 - right))
            right += 1
            if right < n:
                now += numbers[right]
        else:
            now -= numbers[left]
            left += 1

    return result if result != n else -1


t = int(input())

for tc in range(t):
    n, s = map(int, input().split())
    numbers = [*map(int, input().split())]
    print(solution())
