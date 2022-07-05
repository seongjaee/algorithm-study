import sys

input = sys.stdin.readline


def is_pelindrome(string):
    for i in range(len(string) // 2):
        if string[i] != string[len(string) - 1 - i]:
            return False
    return True


t = int(input())

for _ in range(t):
    n = int(input())
    num = int(input())
    x1 = int("1" + "0" * (n - 1) + "1")
    x2 = int("1" * (n + 1))

    if len(str(x1 - num)) == n:
        print(str(x1 - num))
        continue

    if len(str(x2 - num)) == n:
        print(str(x2 - num))
        continue
