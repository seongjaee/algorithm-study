import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(x):
    global cnt
    cnt += 1
    d[x] = cnt
    stack.append(x)
    parent = d[x]

    for y in graph[x]:
        if d[y] == 0:
            parent = min(parent, dfs(y))
        elif not finished[y]:
            parent = min(parent, d[y])

    if parent == d[x]:
        scc = []
        while True:
            top = stack.pop()
            finished[top] = True
            scc.append(top)
            if top == x:
                break
        SCC.append(scc)

    return parent


def check(scc):
    for x in scc:
        for y in in_graph[x]:
            if y not in scc:
                return False
    return True


t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    d = [0] * (n + 1)
    finished = [False] * (n + 1)
    cnt = 0
    stack = []
    SCC = []

    in_graph = [[] for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]
    for _ in range(m):
        x, y = map(int, input().split())
        graph[x].append(y)
        in_graph[y].append(x)

    for i in range(1, n + 1):
        if d[i] == 0:
            dfs(i)

    answer = 0
    for scc in SCC:
        if check(scc):
            answer += 1

    print(answer)
