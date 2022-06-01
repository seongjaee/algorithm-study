from collections import deque
import sys
input = sys.stdin.readline

def d(k):
    return (2 * k) % 10000

def s(k):
    return (k - 1) % 10000

def l(k):
    d1 = k // 1000
    d2 = (k // 100) % 10
    d3 = (k // 10) % 10
    d4 = k % 10
    return d2 * 1000 + d3 * 100 + d4 * 10 + d1

def r(k):
    d1 = k // 1000
    d2 = (k // 100) % 10
    d3 = (k // 10) % 10
    d4 = k % 10
    return d4 * 1000 + d1 * 100 + d2 * 10 + d3

f = {'D': d, 'S': s, 'L': l, 'R': r}

def bfs():
    queue = deque([(a, '')])
    visited = [False] * 10000

    while queue:
        num, now = queue.popleft()

        if num == b:
            return now
    
        for key, func in f.items():
            nxt = func(num)
            if not visited[nxt]:
                visited[nxt] = True
                queue.append((nxt, now + key))


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    visited = [False] * 10000
    print(bfs())
