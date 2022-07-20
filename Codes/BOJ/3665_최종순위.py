from collections import deque
import sys

input = sys.stdin.readline


def topology_sort(graph, in_degree):
    queue = deque()
    for i in range(1, n + 1):
        if in_degree[i] == 0:
            queue.append(i)

    res = []
    while queue:
        node = queue.popleft()
        res.append(node)

        for nxt in graph[node]:
            in_degree[nxt] -= 1
            if in_degree[nxt] == 0:
                queue.append(nxt)

    return res if len(res) == n else ["IMPOSSIBLE"]


t = int(input())

for _ in range(t):
    n = int(input())
    numbers = list(map(int, input().split()))
    m = int(input())
    in_degree = [0] * (n + 1)
    graph = [set() for _ in range(n + 1)]
    for i in range(n):
        for j in range(i + 1, n):
            graph[numbers[i]].add(numbers[j])

    for i in range(1, n):
        in_degree[numbers[i]] = i

    for _ in range(m):
        a, b = map(int, input().split())
        # a => b
        if b in graph[a]:
            in_degree[b] -= 1
            in_degree[a] += 1
            graph[a].remove(b)
            graph[b].add(a)
        # b => a
        else:
            in_degree[a] -= 1
            in_degree[b] += 1
            graph[b].remove(a)
            graph[a].add(b)

    result = topology_sort(graph, in_degree)
    print(*result)
