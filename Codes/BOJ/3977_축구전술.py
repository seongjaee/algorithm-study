import sys

sys.setrecursionlimit(100000)
input = sys.stdin.readline


def dfs(x):
    global cnt
    cnt += 1
    d[x] = cnt
    parent = d[x]
    stack.append(x)

    for nxt in graph[x]:
        if d[nxt] == 0:
            parent = min(parent, dfs(nxt))
        elif not finished[nxt]:
            parent = min(parent, d[nxt])

    if parent == d[x]:
        scc = []
        while True:
            top = stack.pop()
            scc.append(top)
            finished[top] = True
            if top == x:
                break

        SCC.append(scc)

    return parent


def check():
    def has_in_edge(scc):
        for x in scc:
            for y in in_graph[x]:
                if y not in scc:
                    return True
        return False

    if len(SCC) == 1:
        return True

    if has_in_edge(SCC[-1]):
        return False

    for i in range(len(SCC) - 2, -1, -1):
        if not has_in_edge(SCC[i]):
            return False

    return True


t = int(input())
for tc in range(t):
    n, m = map(int, input().split())

    cnt = 0
    d = [0] * n
    finished = [False] * n

    in_graph = [[] for _ in range(n)]
    graph = [[] for _ in range(n)]
    for _ in range(m):
        a, b = map(int, input().split())
        graph[a].append(b)
        in_graph[b].append(a)

    stack = []
    SCC = []

    for i in range(n):
        if d[i] == 0:
            dfs(i)

    if not check():
        print("Confused")
    else:
        for i in sorted(SCC[-1]):
            print(i)

    if tc != t - 1:
        input()
        print()
