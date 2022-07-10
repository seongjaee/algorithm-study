import sys

input = sys.stdin.readline

# x번째 사람이 할 일이 있나
def dfs(x):
    if visited[x]:
        return False

    visited[x] = True
    for nxt in graph[x]:
        # nxt 일을 차지한 사람이 없거나, 현재 nxt를 차지한 사람이 할 수 있는 다른 일이 있거나
        if matches[nxt] == -1 or dfs(matches[nxt]):
            matches[nxt] = x
            return True
    return False


n, m = map(int, input().split())

graph = [[]]
for _ in range(n):
    graph.append([*map(int, input().split()[1:])])

matches = [-1] * (m + 1)  # matches[i] : i번째 일을 차지한 사람 번호

cnt = 0
for i in range(1, n + 1):
    visited = [False] * (n + 1)
    if dfs(i):
        cnt += 1

print(cnt)
