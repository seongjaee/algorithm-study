import sys, math
input = sys.stdin.readline


def length_sum_vector(selected):
    left_vector = [0, 0]
    right_vector = [0, 0]
    for i in range(n):
        if selected[i]:
            lx, ly = points[i]
            left_vector[0] += lx
            left_vector[1] += ly

        else:
            rx, ry = points[i]
            right_vector[0] += rx
            right_vector[1] += ry

    return math.dist(left_vector, right_vector)
        
def backtrack(level, now, k):
    global answer
    if k == n // 2:
        dist = length_sum_vector(now)
        answer = min(answer, dist)
        return

    for i in range(level, n // 2 + k + 1):
        now[i] = True
        backtrack(i + 1, now, k + 1)
        now[i] = False


t = int(input())

for _ in range(t):
    n = int(input())
    points = [tuple(map(int, input().split())) for _ in range(n)]
    answer = 1e10
    backtrack(0, [False] * (n), 0)
    print(answer)