import sys

input = sys.stdin.readline
sys.setrecursionlimit(100000)

def dfs(node, cost):
    visited.add(node)
    for nxt in graph[node]:
        if nxt[0] in visited: continue
        nxt_cost = nxt[1] + cost
        distance[nxt[0]] = nxt_cost
        dfs(nxt[0], nxt_cost)

v = int(input().rstrip())

graph = {}
for i in range(v):
    cmd = list(map(int, input().split()))
    a = cmd[0]
    graph[a] = []
    l = len(cmd)-2
    for j in range(l//2):
        graph[a].append((cmd[1+j*2],cmd[2+j*2]))

visited = set()
distance = [0]*(v+1)
dfs(1,0)
y = max(range(v+1), key = lambda x : distance[x])

visited = set()
distance = [0]*(v+1)
dfs(y,0)
print(max(distance))