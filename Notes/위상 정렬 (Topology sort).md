# 위상 정렬 (Topology sort)

## 설명 :bread:

- 위상 정렬은 사이클이 없는 유향 그래프의 꼭짓점들을 변의 방향을 거스르지 않고 나열하는 것이다. 대학 선수과목을 생각하면 좋다. 주로 업무 일정 순서를 배치하기 위한 것.
- 정렬 순서는 선후 관계에 따라 여러 개의 종류가 나올 수 있다.



## 동작 :cookie:

1. 자신을 가리키는 간선이 없는 정점을 찾는다. 즉, 진입 차수가 0인 정점을 찾는다.

2. 찾은 정점을 출력하고, 해당 정점에서 출발하는 간선을 삭제한다.

3. 위 과정을 반복한다. 모든 정점을 방문했다면 종료한다.



### 큐를 이용한 위상 정렬

1. 진입 차수가 0인 정점들을 모두 큐에 넣는다.
2. 큐가 빌 때까지 다음을 반복한다.
   1. 큐에서 정점을 꺼내 출력하고 해당 정점에서 출발하는 간선을 삭제한다.
   2. 진입 차수가 0이 된 정점들을 큐에 넣는다.

- 만약 모든 정점을 방문하기 전에 큐가 비게 된다면 사이클이 존재한다.



## 코드 :cake:

```python
# n: 정점 수, m: 간선 수
# degrees[n] : 진입 차수 리스트
# graph : key=정점, value=인접 정점 리스트

# 그래프 입력 받기
degrees = [0] * (n + 1)
graph = {}
for _ in range(m):
    a, b = map(int, input().split())
    graph[a] = graph.get(a, []) + [b]
    degrees[b] += 1


# 위상 정렬
def topology_sort():
    queue = deque([])
    
    # 차수가 0인 정점 큐에 삽입
    for i in range(1, n+1):
        if degrees[i] == 0:
            queue.append(i)

    while queue:
        node = queue.popleft()
        print(node, end=' ')  # 정점 출력
		
        for nxt in graph.get(node, []):
            degrees[nxt] -= 1  # 간선 삭제

            if degrees[nxt] == 0:  # 진입 차수 0이면 큐에 삽입
                queue.append(nxt)
```