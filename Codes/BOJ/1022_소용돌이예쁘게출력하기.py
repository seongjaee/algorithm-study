from cmath import e
import sys

input = sys.stdin.readline

# 우 상 좌 하
DELTA = [(0, 1), (-1, 0), (0, -1), (1, 0)]


def get_num(y, x):
    k = max(abs(y), abs(x))
    right_bottom = (2 * k + 1) ** 2

    # 하
    if k == y:
        return right_bottom - (k - x)
    # 좌
    elif k == -x:
        return right_bottom - (2 * k) - (k - y)
    # 상
    elif k == -y:
        return right_bottom - (4 * k) - (k + x)
    # 우
    elif k == x:
        return right_bottom - (6 * k) - (k + y)
    else:
        print("내가 뭐라고 했더라...")


r1, c1, r2, c2 = map(int, input().split())

n = r2 - r1
m = c2 - c1

max_length = 0
result = []
for r in range(r1, r2 + 1):
    temp = []
    for c in range(c1, c2 + 1):
        num = get_num(r, c)
        max_length = max(max_length, len(str(num)))
        temp.append(num)
    result.append(temp)


for i in range(n + 1):
    for j in range(m + 1):
        print(f"{result[i][j]:>{max_length}}", end=" ")
    print()
