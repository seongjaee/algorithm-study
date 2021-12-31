# 다익스트라 알고리즘, Dijkstra

## 설명 :bread:

- 그래프의 한 정점으로부터 다른 모든 정점까지의 최단거리를 구하는 알고리즘이다.
- 애츠허르 데이크스트라 선생님이 20분동안 연필이랑 종이없이 그냥 고안해냈다고 한다.
- 시간복잡도 : O(V ^ 2) 인데, 힙을 이용하면 O(V log V)

### 과정

1. 모든 정점까지의 거리를 무한대로 초기화한다.

2. 미방문 정점 중에 가장 가까운 노드를 선택한다.
3. 2번에서 선택한 노드를 거쳐서 다른 노드들로 가는 거리를 계산한다.
4. 3번에서 계산한 거리가 기존 거리보다 짧다면 각 노드까지의 최단 거리를 갱신한다.
5. 2, 3, 4번을 반복한다.



- 2번에서 가장 가까운 노드를 선택할 때 힙을 이용한다.



## 코드 :cookie:

```python
# 입력받아 그래프 만들기
# n : 정점 개수, m : 간선 개수

# 1. 딕셔너리와 리스트로 그래프 만들기
graph = {}
for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s] = graph.get(s, []) + [(e, cost)]
    
    
# 2. 이중 리스트로 그래프 만들기
graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    s, e, cost = map(int, input().split())
    graph[s][e] = min(graph[s][e], cost)
```



```python
# 다익스트라 알고리즘
# graph: 그래프, start: 출발 정점, distance: 반환할 거리 배열

import heapq
INF = 1e8  # 무한대

def dijkstra(graph, start, distance):
    distance[start] = 0
    
    # (cost, node) 순으로 저장해서 cost 기준으로 정렬되도록 함.
    heap = [(0, start)]

    while heap:
        cur_dist, cur_node = heapq.heappop(heap)
        
        # 기존 거리가 더 짧으면 스킵.
        if distance[cur_node] < cur_dist:
            continue
            
        for nxt_node, cost in graph.get(node, []):
            dist = cur_dist + cost
            
            # cur_node를 거쳐 nxt_node까지 가는게 기존거리보다 짧으면 갱신
            if dist < distance[nxt_node]:
                distance[nxt_node] = dist
                heapq.heappush(heap, (dist, nxt_node))
```



## BOJ :cake:

[BOJ 1753 - 최단경로](https://www.acmicpc.net/problem/1753)

[BOJ 11779 - 최소 비용 구하기 2](https://www.acmicpc.net/problem/11779)

