from collections import deque
import sys

input = sys.stdin.readline

DELTA = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def melt_ice(waters):
    result = set()

    while waters:
        y, x = waters.popleft()

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c and not water_visited[ny][nx]:
                water_visited[ny][nx] = True
                if matrix[ny][nx] == "X":
                    result.add((ny, nx))
                    matrix[ny][nx] = "."
                else:
                    waters.append((ny, nx))

    return result


def make_swan(swans, is_big):
    result = set()
    swan = "L" if is_big else "l"
    other_swan = "l" if is_big else "L"

    while swans:
        y, x = swans.popleft()
        swan_visited[y][x] = True

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if 0 <= ny < r and 0 <= nx < c:
                if matrix[ny][nx] == other_swan:
                    return 0
                if swan_visited[ny][nx]:
                    continue
                if matrix[ny][nx] == ".":
                    swan_visited[ny][nx] = True
                    matrix[ny][nx] = swan
                    swans.append((ny, nx))
                else:
                    result.add((y, x))

    return result


r, c = map(int, input().split())

matrix = [[*input().rstrip()] for _ in range(r)]
water_visited = [[False] * c for _ in range(r)]
swan_visited = [[False] * c for _ in range(r)]

waters = deque()
big_swans = deque()
little_swans = deque()
for i in range(r):
    for j in range(c):
        if matrix[i][j] == "L":
            if not big_swans:
                big_swans.append((i, j))
            else:
                matrix[i][j] = "l"
                little_swans.append((i, j))
            waters.append((i, j))
        elif matrix[i][j] == ".":
            waters.append((i, j))

cnt = 0
while True:
    cnt += 1
    next_waters = melt_ice(waters)
    next_big_swans = make_swan(big_swans, True)
    next_little_swans = make_swan(little_swans, False)

    if not next_big_swans or not next_little_swans:
        break
    waters = deque(next_waters)
    big_swans = deque(next_big_swans)
    little_swans = deque(next_little_swans)

print(cnt)
