from collections import deque
import sys

input = sys.stdin.readline


def bfs():
    visited = [False] * (n + 2)
    visited[0] = True
    queue = deque([0])

    while queue:
        now = queue.popleft()
        y, x = points[now]

        for nxt, pt in enumerate(points):
            ny, nx = pt
            if not visited[nxt] and abs(y - ny) + abs(x - nx) <= 1000:
                visited[nxt] = True
                queue.append(nxt)
                if (ny, nx) == (ey, ex):
                    return True
    return False


t = int(input())
for _ in range(t):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n + 2)]
    ey, ex = points[-1]
    print("happy" if bfs() else "sad")
