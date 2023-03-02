from collections import deque

DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]


def solution(maps):
    answer = 0
    n = len(maps)
    m = len(maps[0])

    def bfs(start, end):
        sy, sx = start
        queue = deque([(sy, sx, 0)])
        visited = [[False] * m for _ in range(n)]
        visited[start[0]][start[1]] = True
        while queue:
            y, x, cnt = queue.popleft()
            if (y, x) == end:
                return cnt
            for dy, dx in DELTA:
                ny = y + dy
                nx = x + dx
                if ny < 0 or ny >= n or nx < 0 or nx >= m:
                    continue
                if visited[ny][nx] or maps[ny][nx] == "X":
                    continue
                visited[ny][nx] = True
                queue.append((ny, nx, cnt + 1))

        return -1

    start = (None, None)
    end = (None, None)
    lever = (None, None)
    for i in range(n):
        for j in range(m):
            if maps[i][j] == "S":
                start = (i, j)
            elif maps[i][j] == "E":
                end = (i, j)
            elif maps[i][j] == "L":
                lever = (i, j)

    dist1 = bfs(start, lever)
    if dist1 == -1:
        return -1

    dist2 = bfs(lever, end)
    if dist2 == -1:
        return -1

    return dist1 + dist2
