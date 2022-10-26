from collections import deque
import sys

input = sys.stdin.readline
DELTA = [(1, 0, 0), (0, 1, 0), (0, 0, 1), (-1, 0, 0), (0, -1, 0), (0, 0, -1)]


def bfs(building, l, r, c, start):
    visited = [[[False for _ in range(c)] for _ in range(r)] for _ in range(l)]
    sx, sy, sz = start
    queue = deque([(sx, sy, sz, 0)])
    visited[sx][sy][sz] = True
    while queue:
        x, y, z, time = queue.popleft()
        if (x, y, z) == end:
            return time

        for dx, dy, dz in DELTA:
            nx, ny, nz = x + dx, y + dy, z + dz
            if nx < 0 or ny < 0 or nz < 0:
                continue
            if nx >= l or ny >= r or nz >= c:
                continue
            if building[nx][ny][nz] == "#":
                continue
            if visited[nx][ny][nz]:
                continue
            visited[nx][ny][nz] = True
            queue.append((nx, ny, nz, time + 1))

    return False


while True:
    l, r, c = map(int, input().split())
    if 0 == l == r == c:
        break
    building = []
    for _ in range(l):
        floor = [input().rstrip() for _ in range(r)]
        building.append(floor)
        input()

    for i in range(l):
        for j in range(r):
            for k in range(c):
                if building[i][j][k] == "S":
                    start = (i, j, k)
                elif building[i][j][k] == "E":
                    end = (i, j, k)

    result = bfs(building, l, r, c, start)
    if result:
        print(f"Escaped in {result} minute(s).")
    else:
        print("Trapped!")
