import sys

sys.setrecursionlimit(100000)

input = sys.stdin.readline


def backtrack(level, now):
    global answer
    if level == n:
        answer = max(answer, now)
        return

    if now + min(n - level, n - now) * 2 <= answer:
        return

    if healths[level] <= 0:
        backtrack(level + 1, now)
        return

    flag = True
    for i in range(n):
        if i == level or healths[i] <= 0:
            continue

        flag = False
        healths[level] -= weights[i]
        healths[i] -= weights[level]

        backtrack(level + 1, now + int(healths[i] <= 0) + int(healths[level] <= 0))

        healths[level] += weights[i]
        healths[i] += weights[level]

    if flag:
        backtrack(n, now)


n = int(input())

visited = [False] * n
healths = []
weights = []
for _ in range(n):
    d, w = map(int, input().split())
    healths.append(d)
    weights.append(w)

answer = 0
backtrack(0, 0)
print(answer)
