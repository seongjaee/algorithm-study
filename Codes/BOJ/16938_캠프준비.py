import sys

input = sys.stdin.readline


def backtrack(level):
    global answer
    if level == n:
        if len(now) >= 2:
            if l <= sum(now) <= r and (now[-1] - now[0]) >= x:
                answer += 1
        return

    now.append(problems[level])
    backtrack(level + 1)
    now.pop()
    backtrack(level + 1)

    pass


n, l, r, x = map(int, input().split())
problems = list(map(int, input().split()))
problems.sort()
now = []
answer = 0
backtrack(0)

print(answer)
