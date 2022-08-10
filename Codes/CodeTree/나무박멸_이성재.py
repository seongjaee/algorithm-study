import sys

input = sys.stdin.readline

DELTA = [(1, 0), (-1, 0), (0, 1), (0, -1)]
DIAGONAL = [(1, 1), (1, -1), (-1, 1), (-1, -1)]


def grow_tree():
    for i in range(n):
        for j in range(n):
            if matrix[i][j] <= 0:
                continue
            for di, dj in DELTA:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n:
                    continue
                if matrix[ni][nj] > 0:
                    matrix[i][j] += 1


def spread_tree(matrix, time):
    new_matrix = [[0] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            new_matrix[i][j] += matrix[i][j]
            if matrix[i][j] <= 0:
                continue

            empty_arounds = []
            for di, dj in DELTA:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n:
                    continue
                if matrix[ni][nj] != 0:
                    continue
                if jecho_matrix[ni][nj] >= time:
                    continue
                empty_arounds.append((ni, nj))

            empty_cnt = len(empty_arounds)
            for y, x in empty_arounds:
                new_matrix[y][x] += matrix[i][j] // empty_cnt

    return new_matrix


def jecho(matrix, time):
    max_cnt = 0
    max_point = (0, 0)
    # 가장 많이 박멸되는 칸 찾기
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0:
                tree_cnt = matrix[i][j]
                for di, dj in DIAGONAL:
                    for d in range(1, k + 1):
                        ni, nj = i + di * d, j + dj * d
                        if ni < 0 or ni >= n or nj < 0 or nj >= n:
                            break
                        if matrix[ni][nj] <= 0:
                            break
                        tree_cnt += matrix[ni][nj]
                if max_cnt < tree_cnt:
                    max_point = (i, j)
                    max_cnt = tree_cnt

    # 찾은 칸에 뿌리기
    i, j = max_point
    for di, dj in DIAGONAL:
        for d in range(1, k + 1):
            ni, nj = i + di * d, j + dj * d
            if ni < 0 or ni >= n or nj < 0 or nj >= n:
                break
            jecho_matrix[ni][nj] = c + time
            if matrix[ni][nj] <= 0:
                break
            matrix[ni][nj] = 0

    matrix[i][j] = 0
    jecho_matrix[i][j] = c + time

    return max_cnt


n, m, k, c = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]
jecho_matrix = [[-1] * n for _ in range(n)]
total_count = 0

for time in range(m):
    grow_tree()
    matrix = spread_tree(matrix, time)
    total_count += jecho(matrix, time)

print(total_count)
