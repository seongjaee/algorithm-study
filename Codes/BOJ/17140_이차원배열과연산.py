from functools import reduce
import sys

input = sys.stdin.readline


def sort_matrix(matrix):
    # 한 줄 정렬
    def sort_by_count(arr, length):
        counter = {}
        for num in arr:
            if num:
                counter[num] = counter.get(num, 0) + 1

        sorted_items = sorted(counter.items(), key=lambda tup: (tup[1], tup[0]))
        result = reduce(lambda t1, t2: [*t1, *t2], sorted_items, [])

        if len(result) > length:
            return result[:length]
        else:
            return result + [0] * (length - len(result))

    def R_sort(matrix):
        max_length = 0
        for row in matrix:
            s = set(row)
            s.discard(0)
            max_length = max(max_length, len(s) * 2)
        max_length = min(100, max_length)
        return [sort_by_count(row, max_length) for row in matrix]

    def C_sort(matrix):
        transposed = list(zip(*matrix))
        return list(zip(*R_sort(transposed)))

    row_length = len(matrix)
    col_length = len(matrix[0])

    if row_length >= col_length:
        return R_sort(matrix)
    else:
        return C_sort(matrix)


r, c, k = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(3)]

for i in range(101):
    try:
        if matrix[r - 1][c - 1] == k:
            print(i)
            break
    except:
        pass
    matrix = sort_matrix(matrix)

else:
    print(-1)
