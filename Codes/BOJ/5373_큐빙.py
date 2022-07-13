import sys

input = sys.stdin.readline


def spin(side, d):
    spin_func_dict[side](d)


# 한쪽면 행렬 90도 회전, i: 면 번호, d: 방향 ('+': 시계, '-': 반시계)
def spin_oneside(i, d):
    if d == "+":
        cube[i][0][0], cube[i][2][0], cube[i][2][2], cube[i][0][2] = (
            cube[i][2][0],
            cube[i][2][2],
            cube[i][0][2],
            cube[i][0][0],
        )

        cube[i][1][2], cube[i][0][1], cube[i][1][0], cube[i][2][1] = (
            cube[i][0][1],
            cube[i][1][0],
            cube[i][2][1],
            cube[i][1][2],
        )
    else:
        cube[i][0][0], cube[i][0][2], cube[i][2][2], cube[i][2][0] = (
            cube[i][0][2],
            cube[i][2][2],
            cube[i][2][0],
            cube[i][0][0],
        )

        cube[i][1][2], cube[i][2][1], cube[i][1][0], cube[i][0][1] = (
            cube[i][2][1],
            cube[i][1][0],
            cube[i][0][1],
            cube[i][1][2],
        )


def spin_twice(i):
    spin_oneside(i, "+")
    spin_oneside(i, "+")


def spin_U(d):
    spin_oneside(0, d)
    if d == "+":
        cube[3][0], cube[2][0], cube[1][0], cube[4][0] = (
            cube[2][0],
            cube[1][0],
            cube[4][0],
            cube[3][0],
        )
    else:
        cube[3][0], cube[4][0], cube[1][0], cube[2][0] = (
            cube[4][0],
            cube[1][0],
            cube[2][0],
            cube[3][0],
        )


def spin_D(d):
    # 앞뒤를 축으로 180도 회전
    cube[0], cube[5], cube[2], cube[4] = cube[5], cube[0], cube[4], cube[2]

    for i in range(6):
        spin_twice(i)

    spin_U(d)

    # 돌려놓기
    for i in range(6):
        spin_twice(i)

    cube[0], cube[5], cube[2], cube[4] = cube[5], cube[0], cube[4], cube[2]


def spin_F(d):
    # 좌우를 축으로 위쪽으로 90도 회전
    # 앞 -> 위, 위 -> 뒤, 뒤 -> 아래, 아래 -> 앞
    cube[0], cube[3], cube[5], cube[1] = cube[3], cube[5], cube[1], cube[0]
    # 뒤, 아래 : 180도 회전
    spin_twice(1)
    spin_twice(5)
    # 오른쪽: 시계, 왼쪽: 반시계
    spin_oneside(2, "+")
    spin_oneside(4, "-")

    spin_U(d)

    spin_oneside(4, "+")
    spin_oneside(2, "-")
    spin_twice(1)
    spin_twice(5)
    cube[0], cube[1], cube[5], cube[3] = cube[1], cube[5], cube[3], cube[0]


def spin_B(d):
    # 상하를 축으로 180도 회전
    cube[1], cube[3], cube[2], cube[4] = cube[3], cube[1], cube[4], cube[2]
    spin_twice(0)
    spin_twice(5)

    spin_F(d)

    spin_twice(0)
    spin_twice(5)
    cube[1], cube[3], cube[2], cube[4] = cube[3], cube[1], cube[4], cube[2]


def spin_L(d):
    # 상하를 중심축으로 90도 회전
    cube[3], cube[4], cube[1], cube[2] = cube[4], cube[1], cube[2], cube[3]
    spin_oneside(0, "-")
    spin_oneside(5, "+")

    spin_F(d)

    spin_oneside(5, "-")
    spin_oneside(0, "+")
    cube[3], cube[2], cube[1], cube[4] = cube[2], cube[1], cube[4], cube[3]


def spin_R(d):
    # 상하를 중심축으로 90도 회전
    cube[3], cube[2], cube[1], cube[4] = cube[2], cube[1], cube[4], cube[3]
    spin_oneside(5, "-")
    spin_oneside(0, "+")

    spin_F(d)

    spin_oneside(0, "-")
    spin_oneside(5, "+")
    cube[3], cube[4], cube[1], cube[2] = cube[4], cube[1], cube[2], cube[3]


# def pretty_print(cube):
#     D = ["위", "뒤", "오른쪽", "앞", "왼쪽", "아래"]
#     for i in range(6):
#         print(D[i])
#         for row in cube[i]:
#             print("".join(row))


spin_func_dict = {
    "U": spin_U,
    "D": spin_D,
    "F": spin_F,
    "B": spin_B,
    "L": spin_L,
    "R": spin_R,
}

t = int(input())
for _ in range(t):
    n = int(input())
    arr = input().split()
    # 위, 뒤, 오른, 앞, 왼, 아래
    cube = [[[color, color, color] for _ in range(3)] for color in "wobrgy"]
    for cmd in arr:
        spin(*cmd)
        # pretty_print(cube)

    for row in cube[0]:
        print("".join(row))
