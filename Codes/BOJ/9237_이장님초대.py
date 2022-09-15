import sys

input = sys.stdin.readline

n = int(input())
times = list(map(int, input().split()))
times.sort(reverse=True)

answer = 0
for i, time in enumerate(times):
    answer = max(answer, i + 2 + time)

print(answer)
