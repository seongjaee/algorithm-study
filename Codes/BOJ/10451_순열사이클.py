from collections import deque
import sys

input = sys.stdin.readline


def bfs(start):
    queue = deque([start])
    while queue:
        node = queue.popleft()
        nxt = numbers[node]
        if visited[nxt]:
            return
        visited[nxt] = True
        queue.append(nxt)


t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [0] + [*map(int, input().split())]
    visited = [False] * (n + 1)
    cnt = 0
    for i in range(1, n + 1):
        if not visited[i]:
            cnt += 1
            bfs(i)

    print(cnt)
