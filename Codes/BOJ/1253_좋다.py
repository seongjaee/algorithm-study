import sys

input = sys.stdin.readline


def is_good(idx):
    left = 0
    right = n - 1

    while left < right:
        if left == idx:
            left += 1
        elif right == idx:
            right -= 1
        else:
            now = numbers[left] + numbers[right]
            if now < numbers[idx]:
                left += 1
            elif now > numbers[idx]:
                right -= 1
            else:
                return True
    return False


n = int(input())
numbers = [*map(int, input().split())]
numbers.sort()

answer = 0
for i in range(n):
    answer += int(is_good(i))
print(answer)
