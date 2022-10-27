from collections import deque
import sys

input = sys.stdin.readline

operation = {
    "push": lambda num: queue.append(num),
    "pop": lambda: print(queue.popleft() if queue else -1),
    "size": lambda: print(len(queue)),
    "empty": lambda: print(0 if queue else 1),
    "front": lambda: print(queue[0] if queue else -1),
    "back": lambda: print(queue[-1] if queue else -1),
}

n = int(input())
queue = deque()
for _ in range(n):
    cmd = input().split()
    f = operation[cmd[0]]
    if len(cmd) == 1:
        f()
    else:
        f(cmd[1])
