import sys

input = sys.stdin.readline

while True:
    line = input().rstrip()
    if line == "END":
        break
    print(line[::-1])
