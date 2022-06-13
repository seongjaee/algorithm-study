import sys


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
        parents[x] = y
    else:
        parents[y] = x


input = sys.stdin.readline
n = int(input())
m = int(input())

parents = [i for i in range(n + 1)]

for i in range(n):
    row = list(map(int, input().split()))
    for j in range(n):
        if row[j]:
            union(i + 1, j + 1)

cities = list(map(int, input().split()))
now = find(cities[0])

flag = True
for city in cities[1:]:
    if now != find(city):
        flag = False
        break

if flag:
    print("YES")
else:
    print("NO")
