import sys

input = sys.stdin.readline


def find(x):
    if parents[x] != x:
        parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    x = find(x)
    y = find(y)

    if x == y:
        return
    if x < y:
        parents[y] = x
    else:
        parents[x] = y


g = int(input())
p = int(input())

# 1 ~ i 중 도킹할 수 있는 가장 큰 번호의 게이트
parents = [i for i in range(1 + g)]

answer = 0
flag = True
for _ in range(p):
    num = int(input())
    nxt = find(num)
    if nxt:
        if flag:
            answer += 1
            union(nxt, nxt - 1)
    else:
        flag = False

print(answer)
