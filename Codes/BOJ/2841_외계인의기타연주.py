from heapq import heappop, heappush
import sys

input = sys.stdin.readline

n, p = map(int, input().split())

heaps = [None, [], [], [], [], [], []]
cnt = 0
for _ in range(n):
    string_num, fret_num = map(int, input().split())

    while heaps[string_num] and -heaps[string_num][0] > fret_num:
        cnt += 1
        heappop(heaps[string_num])

    if heaps[string_num] and -heaps[string_num][0] == fret_num:
        continue
    heappush(heaps[string_num], -fret_num)
    cnt += 1

print(cnt)
