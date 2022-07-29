import sys

input = sys.stdin.readline


def dfs(sy, sx):
    visited = [[False] * m for _ in range(n)]
    visited[sy][sx] = True
    stack = [(sy, sx)]
    res = 1
    while stack:
        y, x = stack.pop()

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                continue
            if visited[ny][nx]:
                continue
            visited[ny][nx] = True
            if matrix[ny][nx] == matrix[sy][sx]:
                stack.append((ny, nx))
                res += 1

    return res * matrix[sy][sx]


def roll():
    global y, x, d, answer
    dy, dx = DELTA[d]
    ny, nx = y + dy, x + dx
    if ny < 0 or ny >= n or nx < 0 or nx >= m:
        ny, nx = y - dy, x - dx
        d = (d + 2) % 4

    # 동
    if d == 0:
        dice[0], dice[4], dice[2], dice[5] = dice[4], dice[2], dice[5], dice[0]

    # 남
    elif d == 1:
        dice[0], dice[3], dice[2], dice[1] = dice[3], dice[2], dice[1], dice[0]

    # 서
    elif d == 2:
        dice[0], dice[5], dice[2], dice[4] = dice[5], dice[2], dice[4], dice[0]

    # 북
    elif d == 3:
        dice[0], dice[1], dice[2], dice[3] = dice[1], dice[2], dice[3], dice[0]

    A = dice[2]
    B = matrix[ny][nx]

    if A > B:
        d = (d + 1) % 4
    elif A < B:
        d = (d - 1) % 4

    y, x = ny, nx
    answer += dfs(y, x)


# 동 남 서 북
DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n, m, k = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]
answer = 0
y, x = 0, 0
# 위 앞 밑 뒤 왼 오
dice = [1, 5, 6, 2, 4, 3]
d = 0
for _ in range(k):
    roll()
print(answer)
