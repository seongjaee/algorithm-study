import sys

input = sys.stdin.readline


def get_time(i):
    if not children[i]:
        return 1

    times = [get_time(child) for child in children[i]]
    times.sort(reverse=True)

    return max([time + idx for idx, time in enumerate(times)]) + 1


n = int(input())
parents = [*map(int, input().split())]

children = [[] for _ in range(n)]
for i in range(1, n):
    children[parents[i]].append(i)

print(get_time(0) - 1)
