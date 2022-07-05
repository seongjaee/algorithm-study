from copy import deepcopy
import sys

input = sys.stdin.readline

# 상 우 하 좌
DELTA = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def power(level):
    global answer
    if level == len(cctvs):
        answer = min(answer, simulation(now))
        return

    for i in range(4):
        now.append(i)
        power(level + 1)
        now.pop()


def simulation(now):
    def go(y, x, d):
        matrix[y][x] = "#"
        ny, nx = y + DELTA[d][0], x + DELTA[d][1]
        if 0 <= ny < n and 0 <= nx < m and matrix[ny][nx] != 6:
            go(ny, nx, d)

    matrix = deepcopy(graph)
    for cctv, d in zip(cctvs, now):
        y, x, num = cctv
        if num == 1:
            go(y, x, d)
        elif num == 2:
            go(y, x, d)
            go(y, x, (d + 2) % 4)
        elif num == 3:
            go(y, x, d)
            go(y, x, (d + 1) % 4)
        elif num == 4:
            go(y, x, d)
            go(y, x, (d + 1) % 4)
            go(y, x, (d + 2) % 4)

    cnt = 0
    for i in range(n):
        for j in range(m):
            if matrix[i][j] == 0:
                cnt += 1
    return cnt


def go(y, x, d):
    graph[y][x] = "#"
    ny, nx = y + DELTA[d][0], x + DELTA[d][1]
    if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] != 6:
        go(ny, nx, d)


n, m = map(int, input().split())
graph = [[*map(int, input().split())] for _ in range(n)]

cctvs = []
good_cctvs = []
for i in range(n):
    for j in range(m):
        if 0 < graph[i][j] < 5:
            cctvs.append((i, j, graph[i][j]))
        elif graph[i][j] == 5:
            good_cctvs.append((i, j))

visited = [[False] * m for _ in range(n)]

for y, x in good_cctvs:
    for i in range(4):
        go(y, x, i)

answer = n * m + 1
now = []
power(0)
print(answer)
