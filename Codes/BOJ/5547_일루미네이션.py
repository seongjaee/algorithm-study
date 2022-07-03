import sys

input = sys.stdin.readline


y_even_delta = [(0, 1), (0, -1), (-1, -1), (-1, 0), (1, -1), (1, 0)]
y_odd_delta = [(0, 1), (0, -1), (-1, 0), (-1, 1), (1, 0), (1, 1)]

delta = {0: y_even_delta, 1: y_odd_delta}


def dfs():
    result = 0
    visited = [[False] * (w + 2) for _ in range(h + 2)]
    stack = [(0, 0)]
    visited[0][0] = True
    while stack:
        y, x = stack.pop()
        for dy, dx in delta[y % 2]:
            ny, nx = y + dy, x + dx
            if 0 <= ny < h + 2 and 0 <= nx < w + 2 and not visited[ny][nx]:
                if matrix[ny][nx]:
                    result += 1
                else:
                    visited[ny][nx] = True
                    stack.append((ny, nx))

    return result


w, h = map(int, input().split())
matrix = [[0] * (w + 2) for _ in range(h + 2)]

for i in range(1, h + 1):
    for j, value in enumerate(map(int, input().split())):
        matrix[i][j + 1] = value

print(dfs())
