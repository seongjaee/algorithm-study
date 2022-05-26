from collections import deque
import sys
input = sys.stdin.readline

def bfs(mid):
    queue = deque([start])
    visited = [False] * (n + 1)
    while queue:
        node = queue.popleft()

        for nxt_node, nxt_cost in graph.get(node, {}).items():
            if visited[nxt_node]:
                continue
            if nxt_cost < mid:
                continue
            if nxt_node == end:
                return True
                
            visited[nxt_node] = True
            queue.append(nxt_node)

    return False


n, m = map(int, input().split())

left, right = 1e9, 1

# 가장 튼튼한 다리들만 남겨놔야함.
graph = {}
for _ in range(m):
    a, b, c = map(int, input().split())
    if a in graph:
        if b in graph[a]:
            graph[a][b] = max(c, graph[a][b])
        else:
            graph[a][b] = c
    else:
        graph[a] = {b: c}

    if b in graph:
        if a in graph[b]:
            graph[b][a] = max(c, graph[b][a])
        else:
            graph[b][a] = c
    else:
        graph[b] = {a: c}

    left = min(left, c)
    right = max(right, c)

start, end = map(int, input().split())

# left, right가 답이 될 수도 있으므로 범위 밖으로 내쫓음
left -= 1
right += 1

while left + 1 < right:
    mid = (left + right) // 2
    if bfs(mid):
        left = mid
    else:
        right = mid

print(left)
    