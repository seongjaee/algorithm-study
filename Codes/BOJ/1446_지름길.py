import sys

input = sys.stdin.readline


def backtrack(level, now, dist):
    global answer
    if now == d:
        answer = min(answer, dist)
        return

    if level == len(roads):
        answer = min(answer, dist + d - now)
        return

    answer = min(answer, dist + d - now)

    if dist >= answer:
        return

    for i in range(level, len(roads)):
        s, e, cost = roads[i]
        if now > s:
            continue
        backtrack(i + 1, e, dist + s - now + cost)


n, d = map(int, input().split())
roads = []
for _ in range(n):
    a, b, c = map(int, input().split())
    if b > d:
        continue
    if b - a <= c:
        continue
    roads.append((a, b, c))

roads.sort(key=lambda arr: arr[0])

answer = 1e5
backtrack(0, 0, 0)
print(answer)
