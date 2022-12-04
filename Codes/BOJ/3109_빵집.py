import sys

input = sys.stdin.readline


def dfs(y, x):
    global answer
    visited[y][x] = True
    if x == c - 1:
        answer += 1
        return True

    for ny in [y - 1, y, y + 1]:
        if ny < 0 or ny >= r:
            continue
        if visited[ny][x + 1]:
            continue
        if matrix[ny][x + 1] == "x":
            continue
        if dfs(ny, x + 1):
            return True

    return False


r, c = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(r)]
visited = [[False] * c for _ in range(r)]
answer = 0

for i in range(r):
    dfs(i, 0)

print(answer)
