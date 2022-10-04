import sys

sys.setrecursionlimit(20000)

input = sys.stdin.readline


def init_tree(i):
    visited[i] = True
    for nxt in graph[i]:
        if visited[nxt]:
            continue
        children[i].append(nxt)
        init_tree(nxt)


def dp(i):
    temp = []
    for child in children[i]:
        temp.append(dp(child))

    if not temp:
        return (numbers[i], 0)

    return (numbers[i] + sum([tup[1] for tup in temp]), sum([max(tup) for tup in temp]))


n = int(input())
numbers = [0] + list(map(int, input().split()))
graph = [[] for _ in range(1 + n)]
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [False] * (n + 1)
children = [[] for _ in range(n + 1)]
init_tree(1)
print(max(dp(1)))
