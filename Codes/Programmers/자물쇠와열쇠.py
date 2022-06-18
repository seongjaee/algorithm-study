# 반시계 방향 회전
def rotate(matrix):
    m = len(matrix)
    new_matrix = [[0] * m for _ in range(m)]
    for i in range(m):
        for j in range(m):
            new_matrix[i][j] = matrix[j][m - 1 - i]
    return new_matrix


# key를 이동시킨 뒤 맞는지 확인
def check(key, lock, right, down):
    m = len(key)
    n = len(lock)
    for i in range(n):
        for j in range(n):
            if 0 <= i - right < m and 0 <= j - down < m:
                now = key[i - right][j - down]
            else:
                now = 0
            if lock[i][j] + now != 1:
                return False
    return True


def solution(key, lock):
    m = len(key)
    n = len(lock)

    for _ in range(4):
        key = rotate(key)
        for right in range(-m + 1, n):
            for down in range(-m + 1, n):
                if check(key, lock, right, down):
                    return True

    return False
