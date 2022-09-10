import sys

input = sys.stdin.readline


def bruteforce(level, day_works, night_works):
    global answer
    if level == n:
        day_score = 0
        for i in day_works:
            for j in day_works:
                day_score += matrix[i][j]

        night_score = 0
        for i in night_works:
            for j in night_works:
                night_score += matrix[i][j]

        answer = min(answer, abs(day_score - night_score))
        return

    if len(day_works) < n // 2:
        bruteforce(level + 1, [*day_works, level], night_works)
    if len(night_works) < n // 2:
        bruteforce(level + 1, day_works, [*night_works, level])


n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]
answer = 1e10
bruteforce(1, [0], [])
print(answer)
