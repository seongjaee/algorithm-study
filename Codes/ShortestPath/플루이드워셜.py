import sys
input = sys.stdin.readline
INF = 1e8

v, e = map(int ,input().split())
start = int(input().rstrip())
graph = [[INF]*(v+1) for _ in range(v+1)]

for x in range(1, v+1):
    for y in range(1, v+1):
        if x == y:
            graph[x][y] = 0

for _ in range(e):
    a, b, c = map(int ,input().split())
    graph[a][b] = min(c, graph[a][b])

for k in range(1, v+1):
    for a in range(1, v+1):
        if a == k: continue # 계산 불필요
        if graph[a][k] == INF: continue # a->k 길이 없으면 어차피 a->k->b도 없음
        for b in range(1, v+1):
            if b == k or a == b : continue # 계산 불필요
            if graph[k][b] == INF : continue # k->b 길이 없으면 어차피 a->k->b도 없음
            graph[a][b] = min(graph[a][b] ,graph[a][k]+ graph[k][b])

for res in graph[start][1:]:
    if res == INF:
        print('INF')
    else:
        print(res)