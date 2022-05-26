from collections import deque
import sys, math
input = sys.stdin.readline

def bfs(max_gas):
    queue = deque([(0, 0, 0)])
    visited= set()

    while queue:
        x, y, cnt = queue.popleft()
        
        for nx, ny in points:
            if (nx, ny) in visited:
                continue
            if (math.dist((x, y), (nx, ny))) > max_gas * 10:
                continue
            if (nx, ny) == (10000, 10000):
                return True

            if cnt + 1 >= k + 1:  # (nx, ny)에 도착하는 게 k + 1이면 안돼!
                continue

            visited.add((nx, ny))
            queue.append((nx, ny, cnt + 1))

    return False


n, k = map(int, input().split())

points = [list(map(int, input().split())) for _ in range(n)]
points.append([10000, 10000])
left, right = 0, 1500  # 넉넉하게 잡아도 됨

while left + 1 < right:
    mid = (left + right) // 2
    if bfs(mid):
        right = mid
    else:
        left = mid

print(right)
