import sys


class Node:
    def __init__(self, data):
        self.data = data
        self.children = {}


class Tree:
    def __init__(self):
        self.head = Node("")

    def insert(self, foods):
        node = self.head

        for food in foods:
            if food not in node.children:
                node.children[food] = Node(food)

            node = node.children[food]

    def dfs(self):
        stack = [(self.head, 0)]
        while stack:
            node, level = stack.pop()
            if node.data:
                print("-" * (level - 2) + node.data)
            for key in sorted(node.children.keys(), reverse=True):
                stack.append((node.children[key], level + 2))


input = sys.stdin.readline

n = int(input())
tree = Tree()
for _ in range(n):
    info = input().split()
    foods = info[1:]
    tree.insert(foods)

tree.dfs()
