import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline

DELTA = [(-1, 0), (0, -1), (0, 1), (1, 0)]

def solution(y, x):
    if dp[y][x] != -1:
        return dp[y][x]

    result = 0
    for dy, dx in DELTA:
        ny, nx = y + dy, x + dx
        if 0 <= ny < m and 0 <= nx < n and matrix[y][x] < matrix[ny][nx]:
            result += solution(ny, nx)

    dp[y][x] = result
    return result


m, n = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(m)]

dp = [[-1] * n for _ in range(m)]
dp[0][0] = 1

print(solution(m - 1, n - 1))
