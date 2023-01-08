from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n = int(input())

problems = [tuple(map(int, input().split())) for _ in range(n)]
problems.sort(key=lambda tup: (tup[0], tup[1]))

heap = []
answer = 0
for day in range(n, 0, -1):
    while problems:
        deadline, score = problems[-1]
        if deadline == day:
            heappush(heap, -score)
            problems.pop()
        else:
            break
    if heap:
        answer -= heappop(heap)

print(answer)
