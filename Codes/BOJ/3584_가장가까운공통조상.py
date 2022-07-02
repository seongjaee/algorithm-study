import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    parents = [i for i in range(n + 1)]
    for _ in range(n - 1):
        parent, child = map(int, input().split())
        parents[child] = parent

    x, y = map(int, input().split())
    parents_of_x = set()
    now = x
    while True:
        parents_of_x.add(now)
        if now == parents[now]:
            break
        now = parents[now]

    now = y
    while True:
        if now in parents_of_x:
            break
        now = parents[now]

    print(now)
