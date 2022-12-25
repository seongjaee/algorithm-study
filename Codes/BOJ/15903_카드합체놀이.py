from heapq import heappush, heappop
import sys

input = sys.stdin.readline

n, m = map(int, input().split())
numbers = [*map(int, input().split())]

heap = []
for num in numbers:
    heappush(heap, num)

for _ in range(m):
    x = heappop(heap)
    y = heappop(heap)
    heappush(heap, x + y)
    heappush(heap, x + y)

print(sum(heap))
