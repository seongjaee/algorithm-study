from collections import deque
import sys

input = sys.stdin.readline


def bfs(sy, sx):
    visited = [[1e10] * w for _ in range(h)]
    queue = deque([(sy, sx, -1, -1)])
    matrix[sy][sx] = "."
    visited[sy][sx] = 0

    while queue:
        y, x, cnt, d = queue.popleft()
        if matrix[y][x] == "C":
            return cnt

        for idx in range(4):
            ny, nx = y + DELTA[idx][0], x + DELTA[idx][1]
            if ny < 0 or ny >= h or nx < 0 or nx >= w:
                continue
            if matrix[ny][nx] == "*":
                continue

            if d == idx:
                if visited[ny][nx] < cnt:
                    continue
                visited[ny][nx] = cnt
                queue.appendleft((ny, nx, cnt, idx))
            else:
                if visited[ny][nx] < cnt + 1:
                    continue
                visited[ny][nx] = cnt + 1
                queue.append((ny, nx, cnt + 1, idx))


def solution():
    for i in range(h):
        for j in range(w):
            if matrix[i][j] == "C":
                return bfs(i, j)


DELTA = [(0, 1), (0, -1), (1, 0), (-1, 0)]
w, h = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(h)]
print(solution())
