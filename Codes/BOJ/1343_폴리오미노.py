import sys


def backtrack(level):
    if level > n:
        return

    if level == n:
        print("".join(now))
        sys.exit()
        return

    if board[level] == ".":
        now.append(".")
        backtrack(level + 1)
        now.pop()

    if level + 4 <= n:
        for i in range(level, level + 4):
            if board[i] == ".":
                break
        else:
            now.append("AAAA")
            backtrack(level + 4)
            now.pop()

    if level + 2 <= n:
        for i in range(level, level + 2):
            if board[i] == ".":
                break
        else:
            now.append("BB")
            backtrack(level + 2)
            now.pop()


board = input()
n = len(board)
now = []

backtrack(0)
print(-1)
