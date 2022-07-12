from collections import deque
import sys

input = sys.stdin.readline
l, r = 6, 2


def spin(num, d):
    if num > 0 and not visited[num - 1] and gears[num - 1][r] != gears[num][l]:
        visited[num - 1] = True
        spin(num - 1, not d)
    if num < 3 and not visited[num + 1] and gears[num + 1][l] != gears[num][r]:
        visited[num + 1] = True
        spin(num + 1, not d)

    if d:
        gears[num].appendleft(gears[num].pop())
    else:
        gears[num].append(gears[num].popleft())


gears = []
for _ in range(4):
    gears.append(deque(input().rstrip()))

k = int(input())
for _ in range(k):
    num, d = map(int, input().split())
    visited = [False] * 4
    visited[num - 1] = True
    spin(num - 1, d > 0)

answer = ""
for gear in gears:
    answer += gear[0]
print(int(answer[::-1], 2))
