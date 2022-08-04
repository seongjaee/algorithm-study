import sys

input = sys.stdin.readline

n = int(input())
balls = list(input().rstrip())
answer = n

# red right
flag = True
red_right = 0
for i in range(n - 1, -1, -1):
    if not flag and balls[i] == "R":
        red_right += 1
        if red_right >= answer:
            break
    if flag and balls[i] == "B":
        flag = False

answer = min(answer, red_right)

# red left
flag = True
red_left = 0
for i in range(n):
    if not flag and balls[i] == "R":
        red_left += 1
        if red_left >= answer:
            break
    if flag and balls[i] == "B":
        flag = False

answer = min(answer, red_left)

# blue right
flag = True
blue_right = 0
for i in range(n - 1, -1, -1):
    if not flag and balls[i] == "B":
        blue_right += 1
        if blue_right >= answer:
            break
    if flag and balls[i] == "R":
        flag = False

answer = min(answer, blue_right)

# blue left
flag = True
blue_left = 0
for i in range(n):
    if not flag and balls[i] == "B":
        blue_left += 1
        if blue_left >= answer:
            break
    if flag and balls[i] == "R":
        flag = False

answer = min(answer, blue_left)

print(answer)
