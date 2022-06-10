from bisect import bisect_left
import sys
input = sys.stdin.readline

n = int(input())
d = {}  # key: 오른쪽 전봇대, value: 왼쪽 전봇대

for _ in range(n):
    a, b = map(int, input().split())
    d[b] = a

sorted_keys = sorted(d.keys(), key=lambda x: d[x])

L = [0]
index_list = []

for b in sorted_keys:
    if b > L[-1]:
        index_list.append(len(L))
        L.append(b)
    else:
        idx = bisect_left(L, b)
        L[idx] = b
        index_list.append(idx)


print(n - len(L) + 1)

now = len(L) - 1

result = []
for i in range(n-1, -1, -1):
    if index_list[i] == now:
        now -= 1
    else:
        result.append(d[sorted_keys[i]])  # LIS에 포함되지 않는 수

for r in sorted(result):
    print(r)


