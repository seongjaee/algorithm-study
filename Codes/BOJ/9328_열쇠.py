from collections import deque
import sys
input = sys.stdin.readline

DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]

def bfs():
    queue = deque([(0, 0)])
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    visited_doors = {}  # 알파벳: (위치y, 위치x)
    cnt = 0
    while queue:
        y, x = queue.popleft()

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h+2 and 0 <= nx < w+2 and not visited[ny][nx] and matrix[ny][nx] != '*':
                visited[ny][nx] = True
                nxt = matrix[ny][nx]
                if nxt == '.':
                    queue.append((ny, nx))

                elif nxt == '$':
                    cnt += 1
                    queue.append((ny, nx))

                elif nxt.isupper():
                    if nxt.lower() in keys:
                        queue.append((ny, nx))    
                    else:
                        visited_doors[nxt.lower()] = visited_doors.get(nxt.lower(), []) + [(ny, nx)]
                    
                elif nxt.islower():
                    keys.add(nxt)
                    queue.append((ny, nx))

                    for i, j in visited_doors.get(nxt, []):
                        queue.append((i, j))

    return cnt

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())

    matrix = ['.' * (w + 2)] + ['.' + input().rstrip() + '.'  for _ in range(h)] + ['.' * (w + 2)]
    keys = set(input().rstrip())
    
    print(bfs())

