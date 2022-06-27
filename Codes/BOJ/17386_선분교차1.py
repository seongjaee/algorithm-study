def ccw(u, v, w):
    return (
        u[0] * v[1]
        + v[0] * w[1]
        + w[0] * u[1]
        - v[0] * u[1]
        - w[0] * v[1]
        - u[0] * w[1]
    )


def is_cross(u, v, w, z):
    d1 = ccw(u, v, w) * ccw(u, v, z)
    d2 = ccw(w, z, u) * ccw(w, z, v)

    if d1 > 0 or d2 > 0:
        return 0

    elif d1 == 0 and d2 == 0:
        if (
            min(u[0], v[0]) <= max(w[0], z[0])
            and min(w[0], z[0]) <= max(u[0], v[0])
            and min(u[1], v[1]) <= max(w[1], z[1])
            and min(w[1], z[1]) <= max(u[1], v[1])
        ):
            return 1
        else:
            return 0

    else:
        return 1


x1, y1, x2, y2 = map(int, input().split())
x3, y3, x4, y4 = map(int, input().split())

print(is_cross((x1, y1), (x2, y2), (x3, y3), (x4, y4)))
