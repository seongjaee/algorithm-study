def check(x1, y1, x2, y2, x3, y3, x4, y4):
    if x2 <= x3 or x4 <= x1 or y2 <= y3 or y4 <= y1:
        if x2 < x3 or x4 < x1 or y2 < y3 or y4 < y1:
            return "d"
        res = 0
        if x2 == x3:
            res += 1
        if x4 == x1:
            res += 1
        if y2 == y3:
            res += 1
        if y4 == y1:
            res += 1
        if res == 2:
            return "c"
        else:
            return "b"

    return "a"


for _ in range(4):
    x1, y1, x2, y2, x3, y3, x4, y4 = map(int, input().split())
    print(check(x1, y1, x2, y2, x3, y3, x4, y4))
