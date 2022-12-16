import sys

input = sys.stdin.readline

n, s = map(int, input().split())
numbers = [*map(int, input().split())]


def solution():
    if sum(numbers) < s:
        return 0
    result = n
    now = numbers[0]
    left, right = 0, 1
    while left < right <= n:
        if now < s:
            if right == n:
                break
            now += numbers[right]
            right += 1
        else:
            result = min(result, right - left)
            now -= numbers[left]
            left += 1

    return result


print(solution())
