from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n = int(input())

lessons = []
for _ in range(n):
    _, s, e = map(int, input().split())
    lessons.append((s, e))
lessons.sort()

now = 0
answer = 0

heap = []
for s, e in lessons:
    if heap and heap[0] <= s:
        heappop(heap)
        heappush(heap, e)
    else:
        heappush(heap, e)
    answer = max(answer, len(heap))
print(answer)
