from re import S
import sys

input = sys.stdin.readline

DELTA = [(-1, 0), (1, 0), (0, -1), (0, 1)]


def get_seat_score(i, j, likes):
    score = [0, 0]  # [인접 좋아하는 학생 수, 인접 빈 자리 수]
    for dy, dx in DELTA:
        ny, nx = i + dy, j + dx
        if ny < 0 or ny >= n or nx < 0 or nx >= n:
            continue
        if matrix[ny][nx] == 0:
            score[1] += 1
        elif matrix[ny][nx] in likes:
            score[0] += 1

    return score


def seat(likes):
    best_score = [-1, -1]
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                continue
            score = get_seat_score(i, j, likes)
            if score[0] > best_score[0]:
                best_score = score
                best_seat = (i, j)
            elif score[0] == best_score[0] and score[1] > best_score[1]:
                best_score = score
                best_seat = (i, j)

    return best_seat


def get_satisfaction(matrix):
    result = 0
    for i in range(n):
        for j in range(n):
            student = matrix[i][j]
            num = 0
            for dy, dx in DELTA:
                ny, nx = i + dy, j + dx
                if ny < 0 or ny >= n or nx < 0 or nx >= n:
                    continue
                if matrix[ny][nx] in student_likes[student]:
                    num += 1
            result += 10 ** (num - 1) if num else 0
    return result


n = int(input())

matrix = [[0] * n for _ in range(n)]
student_likes = {}

for _ in range(n**2):
    temp = [*map(int, input().split())]
    student, likes = temp[0], temp[1:]
    student_likes[student] = likes
    y, x = seat(likes)
    matrix[y][x] = student

print(get_satisfaction(matrix))
