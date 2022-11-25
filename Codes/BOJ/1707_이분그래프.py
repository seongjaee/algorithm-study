import sys

input = sys.stdin.readline


def solution():
    def dfs(start):
        set_number = [0] * (v + 1)
        set_number[start] = 1
        visited[start] = True

        stack = [start]
        while stack:
            node = stack.pop()
            for nxt in graph[node]:
                if set_number[nxt] == set_number[node]:
                    return False
                set_number[nxt] = -set_number[node]
                if visited[nxt]:
                    continue
                visited[nxt] = True
                stack.append(nxt)

        return True

    visited = [False] * (v + 1)
    for i in range(1, v + 1):
        if not visited[i]:
            if not dfs(i):
                return False
    return True


k = int(input())
for _ in range(k):
    v, e = map(int, input().split())
    graph = [[] for _ in range(v + 1)]
    for _ in range(e):
        a, b = map(int, input().split())
        graph[a].append(b)
        graph[b].append(a)

    print("YES" if solution() else "NO")
