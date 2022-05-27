from collections import deque
import sys
input = sys.stdin.readline
DELTA = [(-1, 0), (0, -1), (1, 0), (0, 1)]

def find(sy, sx):
    matrix[sy][sx] = 0
    queue = deque([(sy, sx, 0)])
    visited = [[False] * n for _ in range(n)]

    fishes = []
    while queue:
        y, x, level = queue.popleft()
        flag = True
        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if 0 <= ny < n and 0 <= nx < n and not visited[ny][nx]:
                visited[ny][nx] = True
                if matrix[ny][nx] > shark_size:
                    continue
                if matrix[ny][nx] != 0 and matrix[ny][nx] < shark_size:
                    fishes.append((level + 1, ny, nx, matrix[ny][nx]))
                    flag = False
                    continue

                if flag:
                    queue.append((ny, nx, level + 1))
    if fishes:
        fishes.sort(key=lambda arr: (arr[0], arr[1], arr[2]))
        return fishes[0]
    else:
        return (-1, -1, -1, -1)


n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]
shark_size = 2
levelup_cnt = 0
remain_fish = 0
total_time = 0

for i in range(n):
    for j in range(n):
        if matrix[i][j] == 9:
            shark = (i, j)
        elif matrix[i][j] != 0:
            remain_fish += 1


while remain_fish > 0:
    time, y, x, size = find(*shark)
    if time == -1:
        break
    matrix[y][x] = 0
    remain_fish -= 1
    levelup_cnt += 1
    total_time += time
    shark = (y, x)
    if levelup_cnt == shark_size:
        shark_size += 1
        levelup_cnt = 0

print(total_time)

