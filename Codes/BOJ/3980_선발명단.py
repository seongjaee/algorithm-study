import sys

input = sys.stdin.readline


def backtrack(level, result, visited):
    global answer
    if level == 11:
        answer = max(answer, result)
        return

    cnt = 0
    for idx, num in enumerate(matrix[level]):
        if cnt == 5:
            break
        if num and not visited & (1 << idx):
            cnt += 1
            backtrack(level + 1, result + num, visited | (1 << idx))


t = int(input())
for _ in range(t):
    answer = 0
    matrix = [[*map(int, input().split())] for _ in range(11)]
    backtrack(0, 0, 0)
    print(answer)
