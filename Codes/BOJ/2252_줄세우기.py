from collections import deque
import sys

input = sys.stdin.readline

n, m = map(int, input().split())

in_degrees = [0] * (n + 1)

graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    in_degrees[b] += 1

queue = deque()
for i in range(1, n + 1):
    if in_degrees[i] == 0:
        queue.append(i)

answer = []
while queue:
    node = queue.popleft()
    answer.append(node)

    for nxt in graph[node]:
        in_degrees[nxt] -= 1
        if in_degrees[nxt] == 0:
            queue.append(nxt)

print(*answer)
