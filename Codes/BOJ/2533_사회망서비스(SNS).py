import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9)

def dfs(i):
    visited[i] = True
    memo[i] = [1, 0]
    for nxt in graph[i]:
        if not visited[nxt]:
            dfs(nxt)
            memo[i][1] += memo[nxt][0]
            memo[i][0] += min(memo[nxt])
    

n = int(input())
graph = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)
memo = [None] * (n + 1)
for _ in range(n - 1):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

dfs(1)
print(min(memo[1]))