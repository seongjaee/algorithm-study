from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

queue = deque(range(1, n + 1))
numbers = list(map(int, input().split()))

answer = 0
for num in numbers:
    i = queue.index(num)
    if i <= len(queue) - i:
        answer += i
        for _ in range(i):
            queue.append(queue.popleft())
    else:
        answer += len(queue) - i
        for _ in range(len(queue) - i):
            queue.appendleft(queue.pop())
    queue.popleft()

print(answer)
