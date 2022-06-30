import sys

input = sys.stdin.readline

n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]

min_value = 1e20

# i, j : 포함하지 않을 두 점
for i in range(n):
    for j in range(i):
        min_x, min_y, max_x, max_y = 1e10, 1e10, -1e10, -1e10
        for k in range(n):
            if k != i and k != j:
                min_x = min(min_x, points[k][0])
                min_y = min(min_y, points[k][1])
                max_x = max(max_x, points[k][0])
                max_y = max(max_y, points[k][1])

        min_value = min(min_value, max(max_x - min_x, max_y - min_y))

print((min_value + 2) ** 2)
