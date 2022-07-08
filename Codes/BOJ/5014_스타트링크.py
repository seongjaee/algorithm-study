from collections import deque


def bfs(start, goal):
    if start == goal:
        return 0
    visited = [False] * (f + 1)
    queue = deque([(start, 0)])
    visited[start] = True

    while queue:
        floor, cnt = queue.popleft()

        if floor + u <= f and not visited[floor + u]:
            if floor + u == goal:
                return cnt + 1

            visited[floor + u] = True
            queue.append((floor + u, cnt + 1))

        if floor - d >= 1 and not visited[floor - d]:
            if floor - d == goal:
                return cnt + 1

            visited[floor - d] = True
            queue.append((floor - d, cnt + 1))

    return "use the stairs"


f, start, goal, u, d = map(int, input().split())


print(bfs(start, goal))
