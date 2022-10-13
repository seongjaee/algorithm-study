from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n = int(input())
numbers = [int(input()) for _ in range(n)]

dasom = numbers[0]
heap = []
for i in range(1, n):
    heappush(heap, -numbers[i])

cnt = 0
while heap:
    big = -heappop(heap)
    if dasom > big:
        break
    dasom += 1
    big -= 1
    heappush(heap, -big)
    cnt += 1

print(cnt)
