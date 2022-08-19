import sys

input = sys.stdin.readline


def get_best_seat(student_num):
    result = (0, 0)
    max_value = -1
    for i in range(n):
        for j in range(n):
            if matrix[i][j]:
                continue
            temp = 0
            for di, dj in DELTA:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n:
                    continue
                if matrix[ni][nj] == 0:
                    temp += 1
                elif matrix[ni][nj] in student_like[student_num]:
                    temp += 10

            if temp > max_value:
                max_value = temp
                result = (i, j)

    return result


def get_total_score():
    result = 0
    for i in range(n):
        for j in range(n):
            num = matrix[i][j]
            like_cnt = 0
            for di, dj in DELTA:
                ni, nj = i + di, j + dj
                if ni < 0 or ni >= n or nj < 0 or nj >= n:
                    continue
                if matrix[ni][nj] in student_like[num]:
                    like_cnt += 1
            if like_cnt:
                result += 10 ** (like_cnt - 1)
    return result


DELTA = [(0, 1), (1, 0), (0, -1), (-1, 0)]
n = int(input())

student_like = {}
students = []
for _ in range(n * n):
    a, b, c, d, e = map(int, input().split())
    student_like[a] = {b, c, d, e}
    students.append(a)

matrix = [[0] * n for _ in range(n)]

for num in students:
    i, j = get_best_seat(num)
    matrix[i][j] = num

print(get_total_score())
