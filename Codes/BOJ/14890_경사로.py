import sys

input = sys.stdin.readline

# i번째 행 검사
def check_row(i):
    visited = [False] * n  # 경사로를 놓은 곳
    for j in range(n - 1):
        d = matrix[i][j] - matrix[i][j + 1]
        if abs(d) > 1:
            return False

        # 오른쪽이 한칸 높음
        elif d == -1:
            if j + 1 - l < 0:
                return False
            for k in range(j + 1 - l, j + 1):
                if visited[k]:
                    return False
                if matrix[i][k] != matrix[i][j]:
                    return False
                visited[k] = True

        # 왼쪽이 한칸 높음
        elif d == 1:
            if j + l + 1 > n:
                return False
            for k in range(j + 1, j + l + 1):
                if visited[k]:
                    return False
                if matrix[i][k] != matrix[i][j + 1]:
                    return False
                visited[k] = True

    return True


n, l = map(int, input().split())
matrix = [[*map(int, input().split())] for _ in range(n)]

cnt = 0
for i in range(n):
    cnt += check_row(i)

# 전치
matrix = list(zip(*matrix))
for i in range(n):
    cnt += check_row(i)

print(cnt)
