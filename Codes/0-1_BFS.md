# 0-1 BFS 알고리즘

그래프의 가중치가 **0 또는 1**뿐일 때, 그래프에서 **최단 경로**를 찾는 알고리즘.



BFS는 가중치가 없는 그래프에서 최단 경로를 구하는 데 쓸 수 있다.  출발점으로부터 도착점까지 몇 개의 간선을 지나는지만 세면 된다. 가중치가 없는 그래프는 그냥 모든 간선의 가중치가 1인 그래프라고 생각할 수 있는데, 만약 몇몇 가중치가 1이 아니라면?

이런식으로 가중치가 있는 그래프에서는 다익스트라 알고리즘을 사용할 수 있다. 하지만 가중치가 0과 1밖에 없다면 시간 복잡도가 O(E log V) 인 다익스트라 대신 더 빨리 풀 수 있는 0-1 BFS 알고리즘을 사용할 수 있다.



## :bread: 설명

다익스트라 알고리즘은 

1. 현재 정점에서 가장 가까운 정점을 찾고
2. 그 정점을 거쳐 가는 특정 정점들까지의 최단 경로를 갱신

하는 식이다.

가장 가까운 정점을 찾기위해 우선순위 큐를 사용한다. 즉 정렬을 계속 해야한다.



그런데 그래프의 가중치가 0 또는 1뿐이므로, u와 인접한 정점 v는 둘 중 하나다.

1. v는 u와 같은 레벨이다. (가중치가 0일때)
2. v는 u보다 1레벨 아래다. (가중치가 1일때)



이를 이용해 큐 안에 담긴 모든 정점을 정렬할 수 있다.

v까지의 간선의 가중치가 0이라면 v를 큐의 앞쪽에 삽입하고,

v까지의 간선의 가중치가 1이라면 v를 큐의 뒷쪽에 삽입한다.



이러면 큐에서 정점을 꺼내올 때, 언제나 출발점으로부터 가까운 정점순으로 먼저 꺼내게 된다.


## :cookie: 코드
의사 코드

```python
# vertices: 정점 리스트
# adjacent_vertices : 인접 리스트, {key: 정점 u, value: (인접한 정점 v, 가중치)}

for v in vertices:
    dist[v] = inf
    
dist[start] = 0
q = deque([(0, start)])
while q:
    cost, v = q.popleft()
    for next_vertex, next_cost in adjacent_vertices[v]:
        if dist[v] + cost < dist[next_vertex]:
            dist[next_vertex] = dist[v] + cost
            if cost == 1:
                q.append(next_vertex)
            else:
                q.appendleft(next_vertex)
```


다익스트라와 BFS가 섞인 느낌이다.





## :hamburger: BOJ 13549 숨바꼭질 3

[BOJ 13549 숨바꼭질 3](https://www.acmicpc.net/problem/13549), 0-1 BFS을 이용해 풀 수 있는 문제다!

```python
from collections import deque

def bfs(start):
    q = deque([(start, 0)])
    while q:
        for _ in range(len(q)):
            node, level = q.popleft()
            if node in visited: continue  # 방문했으면 건너 뜀
            if node < 0 or node > 200000: continue  # 너무 많이 갔으면 건너뜀
            if node == end: return level  # 찾으면 리턴
            
            visited.add(node)  # 방문 처리
            
            q.append((node+1, level+1))  # x+1은 1초 걸림
            q.append((node-1, level+1))  # x-1은 1초 걸림
            q.appendleft((node*2, level))  # 2x는 0초 걸림

n, end = map(int ,input().split())
visited = set()

print(bfs(n))
```

