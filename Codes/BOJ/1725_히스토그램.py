import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline

# 각 구간의 최소 높이 인덱스 저장
def init(start, end, node):
    if start == end:
        tree[node] = start
        return

    mid = (start + end) // 2
    init(start, mid, node * 2)
    init(mid + 1, end, node * 2 + 1)
    left, right = tree[node * 2], tree[node * 2 + 1]
    tree[node] = left if numbers[left] < numbers[right] else right


# start, end : 현재 노드의 구간. left, right: 구하고자 하는 구간
# left, right까지의 최소 높이 인덱스
def find_min_index(start, end, node, left, right):
    if right < start or left > end:
        return -1
    if left <= start and end <= right:
        return tree[node]

    mid = (start + end) // 2
    left_min_index = find_min_index(start, mid, node * 2, left, right)
    right_min_index = find_min_index(mid + 1, end, node * 2 + 1, left, right)

    if left_min_index == -1:
        return right_min_index
    if right_min_index == -1:
        return left_min_index

    if numbers[left_min_index] < numbers[right_min_index]:
        return left_min_index
    else:
        return right_min_index


# left, right 까지의 최대 넓이
def get_max_area(left, right):
    min_index = find_min_index(0, n - 1, 1, left, right)
    res = numbers[min_index] * (right - left + 1)

    if min_index < right:
        right_area = get_max_area(min_index + 1, right)
        res = max(res, right_area)

    if left < min_index:
        left_area = get_max_area(left, min_index - 1)
        res = max(res, left_area)

    return res


n = int(input())
numbers = [int(input()) for _ in range(n)]

tree = [None] * (4 * n)
init(0, n - 1, 1)

print(get_max_area(0, n - 1))
