from collections import deque

n = int(input())
queue = deque(range(1, n + 1))
try:
    while queue:
        print(queue.popleft(), end=" ")
        queue.append(queue.popleft())
except:
    pass
