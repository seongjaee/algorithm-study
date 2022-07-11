import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline


def dfs(i):
    global cnt
    cnt += 1
    d[i] = cnt
    stack.append(i)
    parent = d[i]

    for j in graph[i]:
        if d[j] == 0:  # 방문 하지 않은 이웃이면 방문해보자
            parent = min(parent, dfs(j))
        elif not finished[j]:  # 처리중인 이웃이면
            parent = min(parent, d[j])

    if parent == d[i]:  # 자신이 부모라면
        scc = []
        while True:  # 스택에서 자신이 나올때까지 scc
            top = stack.pop()
            scc.append(top)
            finished[top] = True
            if top == i:
                break
        SCC.append(scc)

    return parent


v, e = map(int, input().split())
visited = [False] * (v + 1)
finished = [False] * (v + 1)
graph = [[] for _ in range(v + 1)]
cnt = 0
d = [0] * (v + 1)
for _ in range(e):
    a, b = map(int, input().split())
    graph[a].append(b)

stack = []
SCC = []
for i in range(1, v + 1):
    if d[i] == 0:
        dfs(i)

print(len(SCC))
SCC.sort(key=lambda arr: min(arr))
for scc in SCC:
    print(*sorted(scc), -1)
