import sys

input = sys.stdin.readline


def compare(v):
    return (v[0] / (v[0] ** 2 + v[1] ** 2) ** 0.5, v[1], v[0])


def ccw(u, v, w):
    return (
        u[0] * v[1]
        + v[0] * w[1]
        + w[0] * u[1]
        - v[0] * u[1]
        - w[0] * v[1]
        - u[0] * w[1]
    ) > 0


def convex_hull(points):
    stack = []
    for point in points:
        while len(stack) >= 2:
            first, second = stack[-2], stack[-1]
            # 좌회전 할때까지 stack에서 pop
            if ccw(first, second, point):
                break
            stack.pop()
        stack.append(point)

    return stack


n = int(input())
answer = 0
points = [tuple(map(int, input().split())) for _ in range(n)]
points.sort(key=lambda arr: (arr[1], arr[0]))
answer += len(convex_hull(points))
points.reverse()
answer += len(convex_hull(points))

print(answer - 2)
