from math import log2, floor
import sys

input = sys.stdin.readline


def inorder(x):
    if x <= n:
        inorder(2 * x)
        inorder_list.append(tree[x])
        height_list.append(floor(log2(x)))
        inorder(2 * x + 1)


n = int(input())
tree = [None] + list(map(int, input().split()))
inorder_list = []
height_list = []
inorder(1)
height = floor(log2(n + 1))

max_v = -1e9 * n
for top in range(height):
    for bottom in range(top, height):
        dp = []
        for i in range(n):
            if height_list[i] < top or height_list[i] > bottom:
                continue
            if not dp:
                dp.append(inorder_list[i])
            else:
                dp.append(max(0, dp[-1]) + inorder_list[i])
            max_v = max(max_v, dp[-1])

print(max_v)
