from collections import deque
import sys
input = sys.stdin.readline

def bfs():
    queue = deque([(1, 0)])
    visited = [False] * 101
    while queue:
        now, cnt = queue.popleft()
        for i in range(1, 7):
            nxt = now + i
            if visited[nxt]:
                continue
            if nxt > 100:
                continue
            elif nxt == 100:
                return cnt + 1
            visited[nxt] = True
            queue.append((graph[nxt], cnt + 1))

n, m = map(int, input().split())

ladders = {}
for _ in range(n):
    x, y = map(int, input().split())
    ladders[x] = y

snakes = {}
for _ in range(m):
    u, v = map(int, input().split())
    snakes[u] = v

graph = {}
for i in range(2, 100):
    nxt = i
    while nxt in ladders or nxt in snakes:
        nxt = ladders.get(nxt, nxt)
        nxt = snakes.get(nxt, nxt)
    graph[i]= nxt

print(bfs())
