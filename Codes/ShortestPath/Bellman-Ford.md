# Bellman-Ford algorithm 벨만-포드 알고리즘

## 설명 :bread:

[Bellman–Ford algorithm - 위키피디아](https://en.wikipedia.org/wiki/Bellman%E2%80%93Ford_algorithm)

가중치와 방향성이 있는 그래프에서 최단 경로 문제를 푸는 알고리즘이다.

다익스트라 알고리즘의 경우 음의 간선이 있다면 사용할 수 없지만, 

벨만-포드 알고리즘은 음의 간선에서도 사용할 수 있다.

시간복잡도는 O(V * E) 이다.



최단 경로를 찾을 때 벨만 포드 알고리즘을 사용하면, 음의 사이클이 문제가 될 수 있다.

음의 사이클을 계속 돌면 거리가 -무한대로 갈 수 도 있기 때문에 음의 사이클을 만나면 

종료되어야한다.

따라서 탐색을 간선 수보다 많이 진행했음에도 거리가 줄어든다면 음수 사이클이라고 판단하고 종료한다.

이런 점에서 벨만 포드 알고리즘을 음의 사이클의 존재 여부를 찾는데도 사용할 수 있다.

### 과정

1. 시작 정점 결정
2. 시작 정점에서 다른 모든 정점까지의 거리는 무한대로 초기화(시작 정점은 0)
3. 다음 과정을 V 번 반복
   1. 전체 간선을 탐색
   2. 현재 간선을 거쳐 다른 노드로 가는 거리가 더 짧다면 최단 거리 갱신
4. 마지막 반복(V번째) 시에 최단 거리가 갱신됐다면 음수 사이클 존재



## 코드 :cookie:

 ```python
 # V : 정점 개수, E : 간선 개수, 방향 그래프
 
 # 간선 정보 입력받아 간선 배열 만들기
 edges = []
 for _ in range(E):
     s, e, cost = map(int, input().split())
 	edges.append((s, e, cost))
     
 # 거리 배열 초기화
 dist = [INF] * (V + 1)
 ```

```python
# 벨만-포드 알고리즘
def bellman_ford(edges, start):
    dist[start] = 0
    # 총 n번 반복
    for i in range(V):
        # 반복마다 모든 간선을 탐색
        for j in range(E):
            cur, nxt, cost = edges[j]
            # 현재 간선을 거쳐가는 nxt정점까지의 거리가 더 짧으면 갱신
            if dist[cur] != INF and dist[nxt] > dist[cur] + cost:
                dist[nxt] = dist[cur] + cost
                if i == V - 1:
                    return True
    return False

# 실행
has_negative_cycle = bellman_ford(edges, start)

if has_negative_cycle:
    print('음수 사이클 존재')
else:
    print(dist)
```





## BOJ :doughnut:

[BOJ 11657 타임머신](https://www.acmicpc.net/problem/11657)

[BOJ 1865 웜홀](https://www.acmicpc.net/problem/1865)

