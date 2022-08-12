import sys

input = sys.stdin.read()

qwerty = "`1234567890-=QWERTYUIOP[]\\ASDFGHJKL;'ZXCVBNM,./"
for char in input.rstrip():
    if char == " ":
        print(" ", end="")
    elif char == "\n":
        print("")
    else:
        print(qwerty[qwerty.index(char) - 1], end="")
