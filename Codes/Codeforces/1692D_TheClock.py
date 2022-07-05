import sys

input = sys.stdin.readline


def add_x_minute(hhmm):
    h, m = map(int, hhmm.split(":"))
    time = h * 60 + m
    time += x
    h, m = divmod(time, 60)
    h %= 24
    return f"{h:02}:{m:02}"


def is_pelindrome(string):
    for i in range(2):
        if string[i] != string[4 - i]:
            return False
    return True


t = int(input())
for _ in range(t):
    s, x = input().split()
    x = int(x)
    now = s
    answer = 0
    while True:
        now = add_x_minute(now)
        if is_pelindrome(now):
            answer += 1
        if now == s:
            break

    print(answer)
