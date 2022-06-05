import sys
input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort(key=lambda arr: arr[0])
result = 0
prev = points[0][0]
now = points[0][0]

for s, e in points:
    if now < s:
        result += now - prev
        prev = s
    now = max(now, e)

result += now - prev
print(result)
