import sys

input = sys.stdin.readline


def get_points_in_direction(y, x, direction):
    result = []
    dy, dx = DELTA[direction]
    while True:
        y, x = y + dy, x + dx
        if y < 0 or y >= n or x < 0 or x >= m or matrix[y][x] == 6:
            break
        result.append((y, x))
    return result


def pawn(y, x, d):
    return get_points_in_direction(y, x, d)


def knight(y, x, d):
    result = []
    result += get_points_in_direction(y, x, d)
    result += get_points_in_direction(y, x, d + 2)
    return result


def rook(y, x, d):
    result = []
    result += get_points_in_direction(y, x, d)
    result += get_points_in_direction(y, x, (d + 1) % 4)
    return result


def king(y, x, d):
    result = []
    result += get_points_in_direction(y, x, d)
    result += get_points_in_direction(y, x, (d + 1) % 4)
    result += get_points_in_direction(y, x, (d + 2) % 4)
    return result


def queen(y, x):
    result = []
    for d in range(4):
        result += get_points_in_direction(y, x, d)
    return result


def backtrack(level):
    global answer
    if level == len(pieces):
        checked = [[False] * m for _ in range(n)]
        for points in visited:
            for y, x in points:
                checked[y][x] = True

        cnt = 0
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0 and not checked[i][j]:
                    cnt += 1
        answer = min(answer, cnt)
        return

    piece_num, y, x = pieces[level]
    get_points = get_points_func_for_piece_num[piece_num]
    if piece_num == 2:
        for d in range(2):
            visited.append(knight(y, x, d))
            backtrack(level + 1)
            visited.pop()

    elif piece_num == 5:
        visited.append(queen(y, x))
        backtrack(level + 1)
        visited.pop()

    else:
        for d in range(4):
            visited.append(get_points(y, x, d))
            backtrack(level + 1)
            visited.pop()


DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]

n, m = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]
get_points_func_for_piece_num = {1: pawn, 2: knight, 3: rook, 4: king, 5: queen}
visited = []
answer = n * m
pieces = []  # (말번호, y, x)
for i in range(n):
    for j in range(m):
        if 0 < matrix[i][j] < 6:
            pieces.append((matrix[i][j], i, j))

backtrack(0)

print(answer)
