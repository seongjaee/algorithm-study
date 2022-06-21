# 이 기둥 얼마나 안전한가요?
def get_pillar_safety(x, y, pillar_matrix, bo_matrix):
    n = len(pillar_matrix)
    result = [0, 0, 0]  # 바닥?, 아래 기둥?, 아래 보?
    # 바닥에 있나
    if y == 0:
        result[0] = 1
    # 아래에 기둥이 있나
    if y > 0:
        result[1] = pillar_matrix[y - 1][x]
    # 보가 있나
    if x > 0:
        result[2] += bo_matrix[y][x - 1]
    if x < n:
        result[2] += bo_matrix[y][x]
    return result


# 이 보가 얼마나 안전한가요?
def get_bo_safety(x, y, pillar_matrix, bo_matrix):
    n = len(pillar_matrix)
    result = [0, 0]  # 아래 기둥?, 양쪽 보?

    # 기둥이 있나
    result[0] += pillar_matrix[y - 1][x]
    result[0] += pillar_matrix[y - 1][x + 1]

    # 양쪽 보가 둘다 있나
    if 0 < x < n - 1 and bo_matrix[y][x - 1] and bo_matrix[y][x + 1]:
        result[1] = 1
    return result


def check_pillar_install(x, y, pillar_matrix, bo_matrix):
    return sum(get_pillar_safety(x, y, pillar_matrix, bo_matrix)) > 0


def check_pillar_delete(x, y, pillar_matrix, bo_matrix):
    n = len(pillar_matrix)
    # 왼쪽 보가 있음
    if x > 0 and bo_matrix[y + 1][x - 1]:
        if sum(get_bo_safety(x - 1, y + 1, pillar_matrix, bo_matrix)) == 1:
            return False

    # 오른쪽 보가 있음
    if bo_matrix[y + 1][x]:
        if sum(get_bo_safety(x, y + 1, pillar_matrix, bo_matrix)) == 1:
            return False

    # 위쪽 기둥이 있음
    if y < n - 1 and pillar_matrix[y + 1][x]:
        if sum(get_pillar_safety(x, y + 1, pillar_matrix, bo_matrix)) == 1:
            return False

    return True


def check_bo_install(x, y, pillar_matrix, bo_matrix):
    return sum(get_bo_safety(x, y, pillar_matrix, bo_matrix)) > 0


def check_bo_delete(x, y, pillar_matrix, bo_matrix):
    n = len(pillar_matrix)
    # 왼쪽 보 있음
    if x > 0 and bo_matrix[y][x - 1]:
        if get_bo_safety(x - 1, y, pillar_matrix, bo_matrix) == [0, 1]:
            return False
    # 오른쪽 보 있음
    if x < n - 2 and bo_matrix[y][x + 1]:
        if get_bo_safety(x + 1, y, pillar_matrix, bo_matrix) == [0, 1]:
            return False
    # 왼쪽 위 기둥 있음
    if y < n and pillar_matrix[y][x]:
        if sum(get_pillar_safety(x, y, pillar_matrix, bo_matrix)) == 1:
            return False
    # 오른쪽 위 기둥 있음
    if y < n and pillar_matrix[y][x + 1]:
        if sum(get_pillar_safety(x + 1, y, pillar_matrix, bo_matrix)) == 1:
            return False

    return True


def solution(n, build_frame):
    answer = []
    pillar_matrix = [[0] * (n + 1) for _ in range(n)]
    bo_matrix = [[0] * n for _ in range(n + 1)]
    ftn_matrix_d = {
        (0, 0): (check_pillar_delete, pillar_matrix),
        (0, 1): (check_pillar_install, pillar_matrix),
        (1, 0): (check_bo_delete, bo_matrix),
        (1, 1): (check_bo_install, bo_matrix),
    }

    for x, y, a, b in build_frame:
        ftn, matrix = ftn_matrix_d[(a, b)]
        # 설치 가능
        if b and ftn(x, y, pillar_matrix, bo_matrix):
            matrix[y][x] = 1
        # 삭제 가능
        elif b == 0 and ftn(x, y, pillar_matrix, bo_matrix):
            matrix[y][x] = 0

    for i in range(n + 1):
        for j in range(n + 1):
            if i != n and pillar_matrix[i][j]:
                answer.append([j, i, 0])
            if j != n and bo_matrix[i][j]:
                answer.append([j, i, 1])
    answer.sort(key=lambda arr: (arr[0], arr[1], arr[2]))

    return answer
