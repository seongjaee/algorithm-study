# DFS
import sys
input = sys.stdin.readline

direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

def go(sy, sx, y, x):
    global cnt
    parents[y][x] = (sy, sx)

    dy, dx = direction[matrix[y][x]]
    ny, nx = y + dy, x + dx
    if not parents[ny][nx]:
        go(sy, sx, ny, nx)
    elif parents[ny][nx] == (sy, sx):
        cnt += 1


n, m = map(int, input().split())
matrix = [input().rstrip() for _ in range(n)]
parents = [[None] * m for _ in range(n)]
cnt = 0
for i in range(n):
    for j in range(m):
        if not parents[i][j]:
            go(i, j, i, j)
print(cnt)


# Union-Find
import sys
input = sys.stdin.readline


def find(x):
    if x == parents[x[0]][x[1]]:
        return x
    else:
        parents[x[0]][x[1]] = find(parents[x[0]][x[1]])
        return parents[x[0]][x[1]]

def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if x[0] < y[0]:
        parents[y[0]][y[1]] = x
    elif x[0] > y[0]:
        parents[x[0]][x[1]] = y
    else:
        if x[1] < y[1]:
            parents[y[0]][y[1]] = x
        else:
            parents[x[0]][x[1]] = y

n, m = map(int, input().split())
matrix = [input().rstrip() for _ in range(n)]
parents = [[(i, j) for j in range(m)] for i in range(n)]
direction = {'U': (-1, 0), 'D': (1, 0), 'L': (0, -1), 'R': (0, 1)}

for i in range(n):
    for j in range(m):
        di, dj = direction[matrix[i][j]]
        ni, nj = i + di, j + dj
        union((i, j), (ni, nj))

cnt = 0
for i in range(n):
    for j in range(m):
        if (i, j) == parents[i][j]:
            cnt += 1

print(cnt)