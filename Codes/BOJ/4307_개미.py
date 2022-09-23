import sys

input = sys.stdin.readline

t = int(input())
for _ in range(t):
    l, n = map(int, input().split())
    ants = [int(input()) for _ in range(n)]
    min_value = max([min(ant, l - ant) for ant in ants])
    max_value = max([max(ant, l - ant) for ant in ants])
    print(min_value, max_value)
