import sys

input = sys.stdin.readline


def ccw(u, v, w):
    return (
        u[0] * v[1]
        + v[0] * w[1]
        + w[0] * u[1]
        - v[0] * u[1]
        - w[0] * v[1]
        - u[0] * w[1]
    )


u = tuple(map(int, input().split()))
v = tuple(map(int, input().split()))
w = tuple(map(int, input().split()))

result = ccw(u, v, w)
if result > 0:
    print(1)
elif result == 0:
    print(0)
else:
    print(-1)
