## Union find

주어진 노드들에 대해서, 두 노드가 같은 그래프에 속하는지(연결되어있는지?) 알아내는 알고리즘이다.

같은 그래프에 속하는지를 표현하기 위해 리스트에 각 노드들의 루트 노드를 저장한다. 

여기서는 서로 연결되어있는 노드들 중 가장 작은 노드를 루트 노드로 정한다.

Union(두 노드가 속한 집합을 합집합)과 Find(두 노드의 루트 노드를 찾아 같은 집합인지 확인) 두 가지 알고리즘을 사용한다.

- Find : 재귀적으로 자신의 루트 노드를 찾는다.

- Union : 두 노드를 합치는데, 두 노드의 루트 노드를 찾아서 루트 노드가 서로 다르다면(연결되어 있지 않다면) 더 작은 쪽을 루트 노드로 한다.

```
def find(index):
    # index의 루트노드를 재귀적으로 찾음
    if parent[index] == index: 
        return index
    parent[index] = find(parent[index])
    return parent[index]

def union(x, y):
    # x와 y를 같은 집합으로
    x = find(x)
    y = find(y)

    if x== y:
        return

    if parent[x] > parent[y]:
        parent[x] = y
    else:
        parent[y] = x


n = 10
parent = [i for i in range(n)]

union(0,2)
union(2,3)
union(4,5)
union(5,6)
union(7,8)
union(9,7)

print(parent) # [0, 1, 0, 0, 4, 4, 4, 7, 7, 7]
```
