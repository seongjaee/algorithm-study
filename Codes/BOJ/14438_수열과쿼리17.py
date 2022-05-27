import sys
input = sys.stdin.readline


# tree[node]에 start ~ end 까지 저장
def init_tree(start, end, node):
    if start == end:
        tree[node] = numbers[start]
    else:
        mid = (start + end) // 2
        tree[node] = min(init_tree(start, mid, node * 2), init_tree(mid + 1, end, node * 2 + 1))
    return tree[node]


# start: 현재 노드 시작 인덱스
# end: 현재 노드 끝 인덱스
# node: 현재 노드
# left: 원하는 구간 시작 인덱스
# right: 원하는 구간 끝 인덱스
def get_min(start, end, node, left, right):
    # 목표를 아예 벗어난 경우
    if (left > end) or (right < start):
        return 1e10
    
    # 목표 구간에 아예 포함되는 경우
    if (left <= start) and (end <= right):
        return tree[node]

    mid = (start + end) // 2
    result = min(get_min(start, mid, node * 2, left, right), get_min(mid + 1, end, node * 2 + 1, left, right))
    return result

# start: 현재 노드 시작 인덱스
# end: 현재 노드 끝 인덱스
# node: 현재 노드
# index: 바꾸려는 인덱스
# x: 변경 값
def update(start, end, node, index, x):
    if not (start <= index <= end):
        return tree[node]

    if start == end == index:
        tree[node] = x
        return x

    mid = (start + end) // 2
    result = min(update(start, mid, node * 2, index, x), update(mid + 1, end, node * 2 + 1, index, x))
    tree[node] = result
    return result


n = int(input())
numbers = [*map(int, input().split())]
m = int(input())

tree = [1e10] * (4 * n)
init_tree(0, n-1, 1)

for _ in range(m):
    cmd, i, j = map(int, input().split())
    if cmd == 1:
        update(0, n - 1, 1, i - 1, j)
    elif cmd == 2:
        print(get_min(0, n-1, 1, i - 1, j - 1))

