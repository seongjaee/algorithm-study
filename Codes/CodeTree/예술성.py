from copy import deepcopy
import sys


def init_groups(matrix):
    def dfs(sy, sx):
        group = [(sy, sx)]
        stack = [(sy, sx)]
        visited[sy][sx] = True
        while stack:
            y, x = stack.pop()
            for dy, dx in DELTA:
                ny, nx = y + dy, x + dx
                if ny < 0 or nx < 0 or ny >= n or nx >= n:
                    continue
                if visited[ny][nx] or matrix[ny][nx] != matrix[sy][sx]:
                    continue
                visited[ny][nx] = True
                stack.append((ny, nx))
                group.append((ny, nx))

        return group

    groups = []
    visited = [[False] * n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                continue
            groups.append(dfs(i, j))

    return groups


def indexing(groups):
    indexed = [[None] * n for _ in range(n)]
    for i, group in enumerate(groups):
        for y, x in group:
            indexed[y][x] = i
    return indexed


def get_arounds_count(indexed, group):
    arounds = {}
    for y, x in group:
        for dy, dx in DELTA:
            ny, nx = y + dy, x + dx
            if ny < 0 or nx < 0 or ny >= n or nx >= n:
                continue
            if indexed[ny][nx] == indexed[y][x]:
                continue
            nxt_idx = indexed[ny][nx]
            arounds[nxt_idx] = arounds.get(nxt_idx, 0) + 1

    return arounds


def get_art_score(matrix):
    groups = init_groups(matrix)
    indexed = indexing(groups)
    group_sizes = []  # 그룹에 속한 칸의 수
    group_nums = []  # 그룹을 이루고 있는 숫자
    for group in groups:
        group_sizes.append(len(group))

        y, x = group[0]
        group_nums.append(matrix[y][x])

    score = 0
    for now_idx, group in enumerate(groups):
        arounds_counter = get_arounds_count(indexed, group)

        for nxt_idx, count in arounds_counter.items():
            score += (
                (group_sizes[now_idx] + group_sizes[nxt_idx])
                * group_nums[now_idx]
                * group_nums[nxt_idx]
                * count
            )

    return score // 2


def spin_cross(matrix):
    def spin(i):
        # (i, n // 2) => (n // 2, i) => (n - i, n // 2) => (n // 2, n - i)
        (
            matrix[n // 2][i],
            matrix[n - 1 - i][n // 2],
            matrix[n // 2][n - 1 - i],
            matrix[i][n // 2],
        ) = (
            matrix[i][n // 2],
            matrix[n // 2][i],
            matrix[n - 1 - i][n // 2],
            matrix[n // 2][n - 1 - i],
        )

    for i in range(n // 2):
        spin(i)


def spin_square(matrix):
    new_matrix = deepcopy(matrix)

    mid = n // 2
    for sy, sx, ey, ex in [
        (0, 0, mid - 1, mid - 1),
        (0, mid + 1, mid - 1, n - 1),
        (mid + 1, 0, n - 1, mid - 1),
        (mid + 1, mid + 1, n - 1, n - 1),
    ]:
        for y in range(sy, ey + 1):
            for x in range(sx, ex + 1):
                new_matrix[y][x] = matrix[ey - x + sx][sx + y - sy]

    return new_matrix


def simulate():
    global answer, matrix
    score = get_art_score(matrix)
    answer += score
    spin_cross(matrix)
    matrix = spin_square(matrix)


input = sys.stdin.readline
n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]
DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]

answer = 0

for _ in range(4):
    simulate()

print(answer)
