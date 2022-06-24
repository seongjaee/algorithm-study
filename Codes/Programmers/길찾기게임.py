import sys

sys.setrecursionlimit(100000)


class Node:
    def __init__(self, x):
        self.x = x
        self.left = None  # 왼쪽 노드 키값
        self.right = None  # 오른쪽 노드 키값

    def __repr__(self):
        return f"[{self.left}, {self.x}, {self.right}]"


class Tree:
    def __init__(self, n):
        self.tree = [None] * (n + 1)  # Node
        self.head = -1

    def insert(self, x, index):
        if self.head == -1:
            self.tree[index] = Node(x)
            self.head = index
            return

        node = self.tree[self.head]
        while True:
            if node.x > x:  # 왼쪽
                if node.left:
                    node = self.tree[node.left]
                else:
                    node.left = index
                    self.tree[index] = Node(x)
                    break
            else:
                if node.right:
                    node = self.tree[node.right]
                else:
                    node.right = index
                    self.tree[index] = Node(x)
                    break


def solution(nodeinfo):
    def preorder(tree, now):
        if now:
            preorder_result.append(now)
            preorder(tree, tree.tree[now].left)
            preorder(tree, tree.tree[now].right)

    def postorder(tree, now):
        if now:
            postorder(tree, tree.tree[now].left)
            postorder(tree, tree.tree[now].right)
            postorder_result.append(now)

    preorder_result = []
    postorder_result = []
    n = len(nodeinfo)

    indexed_nodeinfo = []
    for i in range(n):
        x, y = nodeinfo[i]
        indexed_nodeinfo.append((x, y, i + 1))
    indexed_nodeinfo.sort(key=lambda arr: -arr[1])

    tree = Tree(n)
    for x, y, index in indexed_nodeinfo:
        tree.insert(x, index)

    preorder(tree, tree.head)
    postorder(tree, tree.head)

    return [preorder_result, postorder_result]
