# 최소 스패닝 트리

## 스패닝 트리

스패닝 트리란 그래프의 모든 정점을 포함하고 있는 트리이다.

그 중 최소 스패닝 트리는 스패닝 트리 중 가중치의 총합이 최소인 스패닝 트리이다.

즉 주어진 그래프에 대해, **가장 적은 비용으로 모든 노드를 연결한 그래프**이다.

![tree01](C:\Users\seongjaee\algorithm-study\Codes\Minimum_Spanning_Tree.assets\tree01.png)

위와 같은 트리가 있을 때 최소 스패닝 트리는 가중치가 1, 2, 3인 간선만을 골라 만드는 트리다.

![tree02](C:\Users\seongjaee\algorithm-study\Codes\Minimum_Spanning_Tree.assets\tree02.png)



최소 스패닝 트리를 찾는 알고리즘으로

- 프림 알고리즘 (Prim's algorithm)
- 크루스칼 알고리즘 (Kruskal Algorithm)

이 있다.



## [프림 알고리즘](https://ko.wikipedia.org/wiki/%ED%94%84%EB%A6%BC_%EC%95%8C%EA%B3%A0%EB%A6%AC%EC%A6%98)

### 수행 순서

1. 하나의 꼭짓점을 선택해 새로운 트리를 만든다.

2. 모든 꼭짓점이 트리에 포함되어있지 않는 동안

   트리에 속하지 않은 정점들 중 트리에 가장 가까운 정점을 골라 트리에 추가한다. (이 과정에서 우선순위 큐를 이용한다.)

### 코드

```python
# v: 정점의 개수

INF = 1e10  # 무한

def prim(start):
    visited = [False] * (v+1)   # 트리에 추가한 정점 표시
    heap = [(0, start, -1)]  # 가중치, 노드, 부모 저장
    weight = 0  # 총 가중치
    tree = []   # 트리
    while heap:
        dist, node, parent = heapq.heappop(heap)
        
        # 이미 트리에 포함됐으면 건너뜀
        if visited[node]:                 
            continue
            
        visited[node] = True              
        weight += dist                    
        tree.append((parent, node))       # 트리에 간선 (부모, 노드) 저장

        for nxt, cost in graph[node]:     # 현재 정점과 이웃한 정점 중
            if visited[nxt]:              # 트리에 포함되었으면 건너뜀
                continue
            heapq.heappush(heap, (cost, nxt, node))
    
    return weight, tree
```

### 그림으로 확인하기

- 시작 정점을 heap에 넣는다.
  - `heap = [(0, 0, 0)]`

#### Step1.

- heap에서 가중치가 최소인 정점 정보 `(0, 0, 0)` 을 꺼내고 방문 처리.

  - `heap = []`

  

![tree03](C:\Users\seongjaee\algorithm-study\Codes\Minimum_Spanning_Tree.assets\tree03.png)

- 정점 0과 인접한 모든 정점 정보를 heap에 넣는다.
  - `heap = [(1, 2, 0), (2, 3, 0), (3, 1, 0)]`

#### Step2.

- heap에 담긴 정점 중 가중치가 최소인 정점 정보 `(1, 2, 0)` 를 꺼내고 트리에 추가
  - `heap = [(2, 3, 0), (3, 1, 0)]`



![tree04](C:\Users\seongjaee\algorithm-study\Codes\Minimum_Spanning_Tree.assets\tree04.png)

- 꺼낸 정점 2와 인접한 모든 정점 정보를 heap에 넣는다.
  - `heap = [(2, 3, 0), (3, 1, 0), (5, 1, 2), (7, 3, 2)]`

#### Step3.

- heap에 담긴 정점 중 가중치가 최소인 정점 정보 `(2, 3, 0)`을 꺼내고 트리에 추가

  - `heap = [(3, 1, 0), (5, 1, 2), (7, 3, 2)]`

    

![tree05](C:\Users\seongjaee\algorithm-study\Codes\Minimum_Spanning_Tree.assets\tree05.png)

- 꺼낸 정점 3과 인접한 모든 정점 정보를 heap에 넣는다.
  - `heap = [(3, 1, 0), (5, 1, 2), (7, 3, 2)]`

#### Step4.

- heap에 담긴 정점 중 가중치가 최소인 정점 정보 `(3, 1, 0)`을 꺼내고 트리에 추가

![tree06](C:\Users\seongjaee\algorithm-study\Codes\Minimum_Spanning_Tree.assets\tree06.png)



## 크루스칼 알고리즘

`추가 해야함.`