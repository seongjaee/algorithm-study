from collections import deque
import sys

input = sys.stdin.readline

# 시계방향, 상 우 하 좌
DELTA = [(-1, 0), (0, 1), (1, 0), (0, -1)]


def main():
    def f(sy, sx):
        queue = deque([(sy, sx, 0, 3)])
        visited = [[False] * 6 for _ in range(6)]
        visited[sy][sx] = True
        cube = [0, 0, 0, 0, 0, 0]  # 앞 오른쪽 왼쪽 위쪽 아래쪽 뒤쪽

        while queue:
            y, x, side, up = queue.popleft()
            num = matrix[y][x]
            cube[side] = num

            for i, d in enumerate(DELTA):
                ny, nx = y + d[0], x + d[1]
                if ny >= 6 or ny < 0 or nx >= 6 or nx < 0:
                    continue
                if matrix[ny][nx] == 0:
                    continue
                if visited[ny][nx]:
                    continue
                visited[ny][nx] = True

                if i == 0:
                    nxt_up = oppsite[side]
                elif i == 2:
                    nxt_up = side
                else:
                    nxt_up = up

                nxt_side = side_urld[side][(side_urld[side].index(up) + i) % 4]
                queue.append((ny, nx, nxt_side, nxt_up))

        return cube

    matrix = [[*map(int, input().split())] for _ in range(6)]

    # 앞0 오른쪽1 왼쪽2 위쪽3 아래쪽4 뒤쪽5
    # 상0 우1 하2 좌3
    side_urld = (
        (3, 1, 4, 2),
        (3, 5, 4, 0),
        (3, 0, 4, 5),
        (5, 1, 0, 2),
        (0, 1, 5, 2),
        (3, 2, 4, 1),
    )
    oppsite = [5, 2, 1, 4, 3, 0]

    for i in range(6):
        for j in range(6):
            if matrix[i][j] == 1:
                return f(i, j)


result = main()
if sum(result) != 21:
    print(0)
else:
    print(result[5])
