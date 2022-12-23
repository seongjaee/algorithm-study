import sys

input = sys.stdin.readline


def mhtn_dist(pt1, pt2):
    return abs(pt1[0] - pt2[0]) + abs(pt1[1] - pt2[1])


n = int(input())
points = [tuple(map(int, input().split())) for _ in range(n)]


max_value = 0
max_index = -1
for i in range(n - 2):
    now_value = (
        mhtn_dist(points[i], points[i + 1])
        + mhtn_dist(points[i + 1], points[i + 2])
        - mhtn_dist(points[i], points[i + 2])
    )
    if now_value > max_value:
        max_value = now_value
        max_index = i


answer = 0
i = 0
while i < n - 1:
    if i == max_index:
        answer += mhtn_dist(points[i], points[i + 2])
        i += 2
        continue
    answer += mhtn_dist(points[i], points[i + 1])
    i += 1

print(answer)
