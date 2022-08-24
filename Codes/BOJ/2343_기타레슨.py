import sys

input = sys.stdin.readline


def check(mid):
    cnt = 0
    now = 0
    for i in range(1, n + 1):
        if presum[i] - now > mid:
            now = presum[i - 1]
            cnt += 1
            if cnt >= m:
                return False

    return cnt < m


n, m = map(int, input().split())
numbers = [*map(int, input().split())]
presum = [0]
for i in range(n):
    presum.append(presum[i] + numbers[i])

left, right = max(numbers) - 1, presum[-1] + 1

while left + 1 < right:
    mid = (left + right) // 2
    if check(mid):
        right = mid
    else:
        left = mid

print(right)
