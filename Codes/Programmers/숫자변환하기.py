from collections import deque


def solution(x, y, n):
    visited = [False] * 1000001
    queue = deque([(x, 0)])
    visited[x] = True
    while queue:
        now, cnt = queue.popleft()
        if now == y:
            return cnt

        for nxt in [now + n, now * 2, now * 3]:
            if nxt > y:
                continue
            if visited[nxt]:
                continue
            visited[nxt] = True
            queue.append((nxt, cnt + 1))

    return -1
