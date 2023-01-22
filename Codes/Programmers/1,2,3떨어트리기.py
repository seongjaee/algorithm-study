from collections import deque


def init_tree(graph):
    tree = [[] for _ in range(len(graph))]
    visited = [False] * len(graph)
    visited[1] = True
    stack = [1]
    while stack:
        node = stack.pop()
        for nxt in graph[node]:
            if visited[nxt]:
                continue
            visited[nxt] = True
            stack.append(nxt)
            tree[node].append(nxt)

    for idx, children in enumerate(tree):
        tree[idx] = deque(sorted(children))

    return tree


# 숫자 떨어트리기
def drop(tree):
    now = 1
    while True:
        children = tree[now]
        if len(children) == 0:
            return now
        now = children[0]
        children.append(children.popleft())


def solution(edges, target):
    target = [0] + target
    n = len(edges) + 1
    graph = [[] for _ in range(n + 1)]
    for x, y in edges:
        graph[x].append(y)
        graph[y].append(x)

    tree = init_tree(graph)

    # target의 각 숫자를 만드려면 최소 몇 번 거기로 떨어트려야하나?
    min_count = {}
    for i, num in enumerate(target):
        if num == 0:
            continue
        min_count[i] = (num // 3) + (1 if num % 3 > 0 else 0)

    # 각 노드에 떨어지는 횟수
    drop_count = {}
    # 각 노드에 떨어지는 순서
    drop_order = []

    while True:
        leaf_node = drop(tree)
        drop_order.append(leaf_node)
        drop_count[leaf_node] = drop_count.get(leaf_node, 0) + 1

        if min_count[leaf_node] > 0:
            min_count[leaf_node] -= 1

        if sum(min_count.values()) == 0:
            break

    # 불가능한지 판단
    for leaf_node, cnt in drop_count.items():
        if target[leaf_node] < cnt:
            return [-1]

    # 가장 사전순 빠른 result 만들기
    result = [1] * len(drop_order)
    for leaf_node, cnt in drop_count.items():
        target[leaf_node] -= cnt

    for i in range(len(drop_order) - 1, -1, -1):
        leaf_node = drop_order[i]
        remain = target[leaf_node]
        if remain == 0:
            continue
        elif remain == 1:
            target[leaf_node] -= 1
            result[i] += 1
        else:
            target[leaf_node] -= 2
            result[i] += 2

    return result


edges = [[2, 4], [1, 2], [6, 8], [1, 3], [5, 7], [2, 5], [3, 6], [6, 10], [6, 9]]
target = [0, 0, 0, 3, 0, 0, 5, 1, 2, 3]

print(solution(edges, target))
