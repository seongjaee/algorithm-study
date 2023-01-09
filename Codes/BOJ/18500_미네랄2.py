import sys

input = sys.stdin.readline
DELTA = [(1, 0), (0, 1), (0, -1), (-1, 0)]


def throw_stick(height, order):
    if order % 2 == 0:
        for j in range(c):
            if matrix[height][j] == "x":
                matrix[height][j] = "."
                return
    else:
        for j in range(c - 1, -1, -1):
            if matrix[height][j] == "x":
                matrix[height][j] = "."
                return


def find_cluster():
    is_float = [[True] * c for _ in range(r)]
    # 바닥 찾기
    floors = []
    for j in range(c):
        if matrix[r - 1][j] == "x":
            floors.append((r - 1, j))

    # 바닥과 이어진 미네랄들 체크
    stack = floors
    while stack:
        y, x = stack.pop()

        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if matrix[ny][nx] == "." or not is_float[ny][nx]:
                continue
            is_float[ny][nx] = False
            stack.append((ny, nx))

    # 공중에 떠있는 클러스터가 있는지 체크
    si, sj = r - 1, c - 1
    for i in range(r):
        for j in range(c):
            if matrix[i][j] == "x" and is_float[i][j]:
                si, sj = i, j
                break

    # 없으면 리턴
    if (si, sj) == (r - 1, c - 1):
        return []

    cluster = [(si, sj)]
    stack = [(si, sj)]
    visited = [[False] * c for _ in range(r)]
    visited[si][sj] = True
    while stack:
        y, x = stack.pop()
        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if ny < 0 or ny >= r or nx < 0 or nx >= c:
                continue
            if matrix[ny][nx] == "." or visited[ny][nx]:
                continue
            visited[ny][nx] = True
            stack.append((ny, nx))
            cluster.append((ny, nx))

    return cluster


def drop_cluster(cluster):
    if not cluster:
        return
    dy, dx = DELTA[0]
    while True:
        for y, x in cluster:
            matrix[y][x] = "."

        next_cluster = []
        for y, x in cluster:
            ny, nx = y + dy, x + dx
            if ny == r or matrix[ny][nx] == "x":
                for y, x in cluster:
                    matrix[y][x] = "x"
                return
            next_cluster.append((ny, nx))

        for y, x in next_cluster:
            matrix[y][x] = "x"

        cluster = next_cluster


r, c = map(int, input().split())
matrix = [list(input().rstrip()) for _ in range(r)]

n = int(input())
stick_heights = [*map(int, input().split())]
stick_heights = [r - h for h in stick_heights]

for idx, h in enumerate(stick_heights):
    throw_stick(h, idx)
    float_cluster = find_cluster()
    drop_cluster(float_cluster)

for row in matrix:
    print("".join(row))
