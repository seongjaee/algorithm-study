from copy import deepcopy
import sys

input = sys.stdin.readline


def add1_to_min(numbers):
    min_value = 3001
    min_indices = []
    res = numbers[:]
    for i in range(len(numbers)):
        if numbers[i] < min_value:
            min_value = numbers[i]
            min_indices = [i]
        elif numbers[i] == min_value:
            min_indices.append(i)

    for i in min_indices:
        res[i] += 1
    return res


def roll(numbers):
    left_mass = [[numbers[0]]]
    start, k = 1, 1
    while len(left_mass) + 1 <= len(numbers) - start - k:
        left_mass.append(numbers[start : start + k])
        start = start + k
        left_mass = rotate(left_mass)
        k = len(left_mass[0])

    return left_mass + [numbers[start:]]


def rotate(matrix):
    n, m = len(matrix), len(matrix[0])
    new_matrix = [[0] * n for _ in range(m)]
    for i in range(m):
        for j in range(n):
            new_matrix[i][j] = matrix[n - 1 - j][i]
    return new_matrix


def push_down(matrix):
    new_matrix = deepcopy(matrix)
    for i, row in enumerate(matrix):
        for j, num in enumerate(row):
            for di, dj in DELTA:
                ni, nj = i + di, j + dj
                if ni < 0 or nj < 0 or ni >= len(matrix) or nj >= len(matrix[ni]):
                    continue
                d = abs(num - matrix[ni][nj]) // 5
                if num > matrix[ni][nj]:
                    d *= -1
                new_matrix[i][j] += d
                new_matrix[ni][nj] -= d

    arr = []
    for j in range(len(new_matrix[-1])):
        for i in range(len(new_matrix) - 1, -1, -1):
            try:
                arr.append(new_matrix[i][j])
            except:
                continue
    return arr


def fold(arr):
    matrix = []
    mid = len(arr) // 2
    matrix.append(arr[mid - 1 :: -1])
    matrix.append(arr[mid:])

    midmid = mid // 2
    left_half = [row[:midmid] for row in matrix]
    right_half = [row[midmid:] for row in matrix]
    return rotate(rotate(left_half)) + right_half


def work(arr):
    return push_down(fold(push_down(roll(add1_to_min(arr)))))


def diff_max_min(arr):
    return max(arr) - min(arr)


DELTA = [(0, 1), (1, 0)]
n, k = map(int, input().split())
arr = list(map(int, input().split()))
cnt = 0

while diff_max_min(arr) > k:
    arr = work(arr)
    cnt += 1

print(cnt)
