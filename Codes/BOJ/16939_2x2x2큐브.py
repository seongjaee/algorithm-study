import sys

input = sys.stdin.readline


def check_side(surface):
    return all(num == surface[0] for num in surface[1:])


def check_all(surface_list):
    return all(check_side(surface) for surface in surface_list)


def spin_r_cc(cube):
    u, f, d, l, r, b = [cube[i : i + 4] for i in range(0, 24, 4)]
    f[1], f[3], d[1], d[3], b[0], b[2], u[1], u[3] = (
        u[1],
        u[3],
        f[1],
        f[3],
        d[1],
        d[3],
        b[0],
        b[2],
    )
    return u, f, d, l, r, b


def spin_r(cube):
    u, f, d, l, r, b = [cube[i : i + 4] for i in range(0, 24, 4)]
    u[1], u[3], f[1], f[3], d[1], d[3], b[0], b[2] = (
        f[1],
        f[3],
        d[1],
        d[3],
        b[0],
        b[2],
        u[1],
        u[3],
    )
    return u, f, d, l, r, b


def spin_t(cube):
    u, f, d, l, r, b = [cube[i : i + 4] for i in range(0, 24, 4)]
    f[0], f[1], l[0], l[1], b[0], b[1], r[0], r[1] = (
        r[0],
        r[1],
        f[0],
        f[1],
        l[0],
        l[1],
        b[0],
        b[1],
    )
    return u, f, d, l, r, b


def spin_t_cc(cube):
    u, f, d, l, r, b = [cube[i : i + 4] for i in range(0, 24, 4)]
    r[0], r[1], f[0], f[1], l[0], l[1], b[0], b[1] = (
        f[0],
        f[1],
        l[0],
        l[1],
        b[0],
        b[1],
        r[0],
        r[1],
    )
    return u, f, d, l, r, b


def spin_f(cube):
    u, f, d, l, r, b = [cube[i : i + 4] for i in range(0, 24, 4)]
    u[2], u[3], r[0], r[2], d[0], d[1], l[1], l[3] = (
        l[1],
        l[3],
        u[2],
        u[3],
        r[0],
        r[2],
        d[0],
        d[1],
    )
    return u, f, d, l, r, b


def spin_f_cc(cube):
    u, f, d, l, r, b = [cube[i : i + 4] for i in range(0, 24, 4)]
    l[1], l[3], u[2], u[3], r[0], r[2], d[0], d[1] = (
        u[2],
        u[3],
        r[0],
        r[2],
        d[0],
        d[1],
        l[1],
        l[3],
    )
    return u, f, d, l, r, b


def solution(cube):
    funcs = [spin_r, spin_f, spin_t, spin_r_cc, spin_f_cc, spin_t_cc]
    return any(check_all(f(cube)) for f in funcs)


cube = [*map(int, input().split())]
print(int(solution(cube)))
