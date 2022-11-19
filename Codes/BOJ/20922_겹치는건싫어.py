import sys

input = sys.stdin.readline

n, k = map(int, input().split())
numbers = [*map(int, input().split())]
answer = 1

counter = {numbers[0]: 1}
left, right = 0, 1
while right < n:
    now = numbers[right]
    counter[now] = counter.get(now, 0) + 1

    if counter[now] <= k:
        answer = max(answer, right - left + 1)
    else:
        while counter[now] > k:
            counter[numbers[left]] -= 1
            left += 1

    right += 1

print(answer)
