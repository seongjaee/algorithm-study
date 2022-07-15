from collections import deque
import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, k = map(int, input().split())
    delays = [0] + [*map(int, input().split())]

    graph = [[] for _ in range(1 + n)]
    degrees = [0] * (n + 1)
    build_times = [0] * (n + 1)

    for _ in range(k):
        x, y = map(int, input().split())
        degrees[y] += 1
        graph[x].append(y)

    w = int(input())

    queue = deque([])
    for i in range(1, n + 1):
        if degrees[i] == 0:
            queue.append((i, delays[i]))
            build_times[i] = delays[i]

    while queue:
        node, time = queue.popleft()
        if node == w:
            print(time)
            break

        for nxt in graph[node]:
            degrees[nxt] -= 1
            build_times[nxt] = max(build_times[nxt], time + delays[nxt])
            if degrees[nxt] == 0:
                queue.append((nxt, build_times[nxt]))
