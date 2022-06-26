from collections import deque
import sys

input = sys.stdin.readline


DELTA = [
    (0, 1),
    (1, 0),
    (-1, 0),
    (0, -1),
]

knight = [
    (2, 1),
    (1, 2),
    (2, -1),
    (1, -2),
    (-1, 2),
    (-2, 1),
    (-1, -2),
    (-2, -1),
]


def bfs():
    visited = [[-1] * w for _ in range(h)]
    queue = deque([(0, 0, 0, k)])

    while queue:
        y, x, cnt, knight_cnt = queue.popleft()
        if (y, x) == (h - 1, w - 1):
            return cnt

        for dy, dx in DELTA:
            ny, nx = dy + y, dx + x
            if 0 <= ny < h and 0 <= nx < w and not matrix[ny][nx]:
                if visited[ny][nx] < knight_cnt:
                    visited[ny][nx] = knight_cnt
                    queue.append((ny, nx, cnt + 1, knight_cnt))

        if knight_cnt > 0:
            for dy, dx in knight:
                ny, nx = dy + y, dx + x
                if 0 <= ny < h and 0 <= nx < w and not matrix[ny][nx]:
                    if visited[ny][nx] < knight_cnt - 1:
                        visited[ny][nx] = knight_cnt - 1
                        queue.append((ny, nx, cnt + 1, knight_cnt - 1))

    return -1


k = int(input())
w, h = map(int, input().split())

matrix = [[*map(int, input().split())] for _ in range(h)]
print(bfs())
