import sys

sys.setrecursionlimit(20000)


class Node:
    def __init__(self, num):
        self.num = num
        self.left = None
        self.right = None

    def __repr__(self):
        return str(self.num)


def post(node):
    if node:
        post(node.left)
        post(node.right)
        print(node)


def init_tree(start, end):
    if start > end:
        return
    if start == end:
        return Node(numbers[start])

    mid = start + 1
    for j in range(start + 1, end + 1):
        if numbers[j] > numbers[start]:
            mid = j
            break

    left_root = init_tree(start + 1, mid - 1)
    right_root = init_tree(mid, end)

    node = Node(numbers[start])
    node.left = left_root
    node.right = right_root

    return node


lines = sys.stdin.readlines()
numbers = list(map(int, lines))

root = init_tree(0, len(numbers) - 1)
post(root)
