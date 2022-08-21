from collections import deque
import sys

input = sys.stdin.readline
n, d, k, c = map(int, input().split())

left = deque([int(input()) for _ in range(k)])
right = deque([int(input()) for _ in range(n - k)])

max_value = 0
for _ in range(n):
    max_value = max(max_value, len(set(list(left) + [c])))
    left.append(right.popleft())
    right.append(left.popleft())

print(max_value)
