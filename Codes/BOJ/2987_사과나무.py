import sys, math

input = sys.stdin.readline


# 양수 => v기준 u는 반시계
def cross_product(v, u):
    return v[0] * u[1] - v[1] * u[0]


def length_of_vector(u):
    return (u[0] ** 2 + u[1] ** 2) ** 0.5


def ccw(u, v, t):
    return cross_product(u, t) * cross_product(v, t)


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())

u = (x2 - x1, y2 - y1)
v = (x3 - x1, y3 - y1)
w = (x3 - x2, y3 - y2)

pd = cross_product(v, u)

# 땅 넓이
print(f"{abs(pd) * 0.5:.1f}")

n = int(input())

cnt = 0
for _ in range(n):
    tx, ty = map(int, input().split())
    t1 = (tx - x1, ty - y1)
    t2 = (tx - x2, ty - y2)

    c = ccw(u, v, t1)
    neg_u = (-u[0], -u[1])
    if c < 0 and ccw(neg_u, w, t2) <= 0:
        cnt += 1
    elif c == 0:
        if (
            cross_product(u, t1) == 0
            and min(x1, x2) <= tx <= max(x1, x2)
            and min(y1, y2) <= ty <= max(y1, y2)
        ):
            cnt += 1
        elif (
            cross_product(v, t1) == 0
            and min(x1, x3) <= tx <= max(x1, x3)
            and min(y1, y3) <= ty <= max(y1, y3)
        ):
            cnt += 1

print(cnt)
