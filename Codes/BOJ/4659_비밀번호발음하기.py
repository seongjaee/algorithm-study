import sys

input = sys.stdin.readline

vowels = {"a", "e", "i", "o", "u"}


def check1(word):
    flag = False
    for char in word:
        if char in vowels:
            flag = True

    return flag


def check2(word):
    stack = []
    for char in word:
        if char in vowels:
            stack.append(1)
        else:
            stack.append(-1)
        if sum(stack[-3:]) == 3 or sum(stack[-3:]) == -3:
            return False
    return True


def check3(word):
    for idx, char in enumerate(word[:-1]):
        if char == word[idx + 1]:
            if char != "e" and char != "o":
                return False
    return True


while True:
    word = input().rstrip()
    if word == "end":
        break

    if check1(word) and check2(word) and check3(word):
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
