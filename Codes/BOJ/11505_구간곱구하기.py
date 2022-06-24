import sys

input = sys.stdin.readline


# node에 start ~ end정보 저장
def init_tree(node, start, end):
    if start == end:
        tree[node] = numbers[start]
        return tree[node] % 1000000007
    else:
        mid = (start + end) // 2
        tree[node] = init_tree(node * 2, start, mid) * init_tree(
            node * 2 + 1, mid + 1, end
        )
        return tree[node] % 1000000007


# node: 현재 노드, start, end: 현재 노드 구간, l, r: 구하고자 하는 구간
def segment(node, start, end, l, r):
    if start > r or end < l:
        return 1
    if l <= start and end <= r:
        return tree[node] % 1000000007

    mid = (start + end) // 2
    return (
        segment(node * 2, start, mid, l, r)
        * segment(node * 2 + 1, mid + 1, end, l, r)
        % 1000000007
    )


# node: 현재 노드, start, end: 현재 노드 구간, index : 변경하고자 하는 인덱스, value: 변경하고자 하는 목표값
def update(node, start, end, index, value):
    if not (start <= index <= end):
        return

    if start == end:
        tree[node] = value
        return

    mid = (start + end) // 2
    update(node * 2, start, mid, index, value)
    update(node * 2 + 1, mid + 1, end, index, value)

    tree[node] = (tree[node * 2] * tree[node * 2 + 1]) % 1000000007


n, m, k = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

tree = [None] * (4 * n)
init_tree(1, 0, n - 1)

for _ in range(m + k):
    a, b, c = map(int, input().split())
    if a == 1:
        # b번째 수 c로 바꾸기
        update(1, 0, n - 1, b - 1, c)
        numbers[b - 1] = c
    elif a == 2:
        # b부터 c까지의 곱 구하기
        print(segment(1, 0, n - 1, b - 1, c - 1))
