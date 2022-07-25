from collections import deque
import sys

input = sys.stdin.readline

#  위쪽, 왼쪽, 아래쪽, 오른쪽
DELTA = [(-1, 0), (0, -1), (1, 0), (0, 1)]

# (y, x)의 구슬을 d 방향으로 쭉 옮기기
def move(y, x, d):
    i, j = y, x
    di, dj = DELTA[d]
    while True:
        ni, nj = i + di, j + dj
        if matrix[ni][nj] == "O":
            return (ni, nj)

        if matrix[ni][nj] != ".":
            return (i, j)

        i, j = ni, nj


# d 방향으로 기울이기
def lean(red, blue, d):
    ry, rx = move(*red, d)
    by, bx = move(*blue, d)

    if (ry, rx) == (by, bx):
        if (ry, rx) == hole:
            return (ry, rx), (by, bx)
        if d == 0:
            if red[0] > blue[0]:
                ry += 1
            else:
                by += 1

        elif d == 1:
            if red[1] > blue[1]:
                rx += 1
            else:
                bx += 1

        elif d == 2:
            if red[0] > blue[0]:
                by -= 1
            else:
                ry -= 1

        elif d == 3:
            if red[1] > blue[1]:
                bx -= 1
            else:
                rx -= 1

    return (ry, rx), (by, bx)


def bfs(sred, sblue):
    queue = deque([(sred, sblue, 0)])

    while queue:
        now_red, now_blue, cnt = queue.popleft()
        if cnt >= 10:
            return -1

        for d in range(4):
            nxt_red, nxt_blue = lean(now_red, now_blue, d)
            if now_red == nxt_red and now_blue == nxt_blue:
                continue

            if nxt_blue == hole:
                continue

            if nxt_red == hole:
                return cnt + 1

            queue.append((nxt_red, nxt_blue, cnt + 1))

    return -1


n, m = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "R":
            red = (i, j)
            matrix[i][j] = "."
        elif matrix[i][j] == "B":
            blue = (i, j)
            matrix[i][j] = "."
        elif matrix[i][j] == "O":
            hole = (i, j)

print(bfs(red, blue))

################################

# 2번째 풀이
from collections import deque
import sys

input = sys.stdin.readline


def bfs(red, blue):
    visited = set()
    queue = deque([(*red, *blue, 0)])
    visited.add((*red, *blue))

    while queue:
        ry, rx, by, bx, cnt = queue.popleft()
        if cnt == 10:
            return -1

        for dy, dx in DELTA:
            nry, nrx = ry, rx
            nby, nbx = by, bx

            flag = True
            while matrix[nby][nbx] != "#":
                nby, nbx = nby + dy, nbx + dx
                if matrix[nby][nbx] == "O":
                    flag = False
                    break
            if not flag:
                continue
            nby, nbx = nby - dy, nbx - dx

            while matrix[nry][nrx] != "#":
                nry, nrx = nry + dy, nrx + dx
                if matrix[nry][nrx] == "O":
                    return cnt + 1
            nry, nrx = nry - dy, nrx - dx

            if (nry, nrx) == (nby, nbx):
                # 움직이는 방향에 더 가까운 구슬: 빨강
                if (ry - by) * dy + (rx - bx) * dx > 0:
                    nby, nbx = nby - dy, nbx - dx
                else:
                    nry, nrx = nry - dy, nrx - dx

            if (nry, nrx, nby, nbx) in visited:
                continue
            visited.add((nry, nrx, nby, nbx))
            queue.append((nry, nrx, nby, nbx, cnt + 1))

    return -1


DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]
n, m = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if matrix[i][j] == "R":
            red = (i, j)
            matrix[i][j] = "."
        elif matrix[i][j] == "B":
            blue = (i, j)
            matrix[i][j] = "."

print(bfs(red, blue))
