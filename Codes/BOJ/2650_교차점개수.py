import sys

input = sys.stdin.readline

n = int(input())

# 양수 : 반시계, 음수: 시계, 0: 평행
def ccw(u, v, t):
    return (
        u[0] * v[1]
        + v[0] * t[1]
        + t[0] * u[1]
        - v[0] * u[1]
        - t[0] * v[1]
        - u[0] * t[1]
    )


def is_cross(line1, line2):
    a, b = line1
    c, d = line2
    res1 = ccw(a, b, c) * ccw(a, b, d)
    res2 = ccw(c, d, a) * ccw(c, d, b)

    if res1 == 0 and res2 == 0:
        a, b = min(a, b), max(a, b)
        c, d = min(c, d), max(c, d)
        if b < c or d < a or a < c < d < b or c < a < b < d:
            return False

        return True

    return res1 <= 0 and res2 <= 0


def convert(a, b):
    if a == 1:
        return (b, 0)
    elif a == 2:
        return (b, 100)
    elif a == 3:
        return (0, b)
    elif a == 4:
        return (100, b)


lines = []
for _ in range(n // 2):
    a, b, c, d = map(int, input().split())
    lines.append((convert(a, b), convert(c, d)))

crossed = [0] * (n // 2)
result = 0
for i in range(n // 2 - 1):
    for j in range(i + 1, n // 2):
        if is_cross(lines[i], lines[j]):
            result += 1
            crossed[i] += 1
            crossed[j] += 1

print(result)
print(max(crossed))
