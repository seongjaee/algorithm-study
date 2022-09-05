from functools import reduce
import sys

input = sys.stdin.readline


def arr_sort(arr):
    counter = {}
    for num in arr:
        if num:
            counter[num] = counter.get(num, 0) + 1
    sorted_items = sorted(counter.items(), key=lambda item: (item[1], item[0]))
    result = reduce(lambda item1, item2: [*item1, *item2], sorted_items, [])
    return result[:100]


def r_operate(matrix):
    new_matrix = []
    max_length = 0
    for row in matrix:
        new_row = arr_sort(row)
        max_length = max(max_length, len(new_row))
        new_matrix.append(new_row)

    for i, _ in enumerate(matrix):
        new_matrix[i] += [0] * (max_length - len(new_matrix[i]))

    return new_matrix


def c_operate(matrix):
    transposed = list(zip(*matrix))
    return list(zip(*r_operate(transposed)))


def operate(matrix):
    r_length = len(matrix)
    c_length = len(matrix[0])
    return r_operate(matrix) if r_length >= c_length else c_operate(matrix)


r, c, k = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(3)]

for time in range(100):
    try:
        if matrix[r - 1][c - 1] == k:
            print(time)
            break
    except:
        pass
    matrix = operate(matrix)

else:
    print(-1)
