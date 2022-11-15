import sys

input = sys.stdin.readline

visited = [[False] * 100 for _ in range(100)]

n = int(input())

for _ in range(n):
    y, x = map(int, input().split())
    for i in range(y, y + 10):
        for j in range(x, x + 10):
            visited[i][j] = True

answer = 0
for i in range(100):
    for j in range(100):
        if visited[i][j]:
            answer += 1
print(answer)
