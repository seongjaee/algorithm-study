import sys
input = sys.stdin.readline

def solution(y, x):
    if dp[y][x] != -1:
        return dp[y][x]

    result = 0
    for i in range(y - 1, -1, -1):
        if matrix[i][x] + i == y:
            result += solution(i, x)
    for i in range(x - 1, -1, -1):
        if matrix[y][i] + i == x:
            result += solution(y, i)
    
    dp[y][x] = result
    return result

n = int(input())
matrix = [[*map(int, input().split())] for _ in range(n)]

dp = [[-1] * n for _ in range(n)]
dp[0][0] = 1

print(solution(n - 1, n - 1))
