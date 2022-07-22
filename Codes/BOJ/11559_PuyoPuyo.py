import sys

input = sys.stdin.readline


DELTA = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def boom():
    def dfs(sy, sx):
        cnt = 0
        res = [(sy, sx)]
        stack = [(sy, sx)]
        visited[sy][sx] = True

        while stack:
            y, x = stack.pop()
            cnt += 1
            for dy, dx in DELTA:
                ny, nx = y + dy, x + dx
                if ny >= 12 or ny < 0 or nx >= 6 or nx < 0:
                    continue
                if visited[ny][nx]:
                    continue
                if matrix[ny][nx] == matrix[sy][sx]:
                    visited[ny][nx] = True
                    res.append((ny, nx))
                    stack.append((ny, nx))

        return res if cnt >= 4 else []

    visited = [[False] * 6 for _ in range(12)]
    boomed = []
    for i in range(12):
        for j in range(6):
            if matrix[i][j] != "." and not visited[i][j]:
                boomed += dfs(i, j)

    for y, x in boomed:
        matrix[y][x] = "."

    return boomed


def down():
    for j in range(6):
        for i in range(11, 0, -1):
            if matrix[i][j] != ".":
                continue
            for k in range(i - 1, -1, -1):
                if matrix[k][j] == ".":
                    continue
                matrix[i][j], matrix[k][j] = matrix[k][j], matrix[i][j]
                break


matrix = [list(input().rstrip()) for _ in range(12)]

answer = 0
while True:
    if not boom():
        break
    down()
    answer += 1

print(answer)
