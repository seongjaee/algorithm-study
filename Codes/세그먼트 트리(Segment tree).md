# 세그먼트 트리(Segment tree)

## 세그먼트 트리란

**구간에 대한 정보를 저장**하는 트리 자료구조.

세그먼트 트리는

1. 배열의 구간 합 구하기
2. 배열의 특정 인덱스 수정하기

1, 2 번 연산을 M번 반복하는 문제에 대해서 빠르게 답을 내놓을 수 있는 자료구조이다.

보통 구간 합은 O(N), 인덱스 수정은 O(1)이 걸리므로, 총 시간 복잡도는 O(NM)이 된다.

세그먼트 트리를 이용하면 1번 연산을 O(log N), 2번 연산도 O(log N)만에 수행할 수 있게 된다.

## 세그먼트 트리 구조

세그먼트 트리의 노드는 다음의 의미를 갖는다.

- 리프 노드 : 배열에 담긴 숫자.

- 다른 노드 : 왼쪽 자식과 오른쪽 자식의 합.

  > 보통 루트 노드의 번호를 1로 저장해, 왼쪽 자식이 2 * x, 오른쪽 자식이 2 * x + 1

`Arr = [6, 3, 2, 7, 1, 5]` 인 배열에 대해 세그먼트 트리는 아래 그림과 같이 나타낼 수 있다.

<img src="세그먼트 트리(Segment tree).assets/tree1.png" alt="tree1" style="zoom:22%;" />

각 노드에 인덱스 i-j까지 해당하는 숫자들의 합이 저장된다.

주어진 배열을 반으로 나누어 나눈 배열의 합을 저장하게 된다.

<img src="세그먼트 트리(Segment tree).assets/tree2.png" alt="tree2" style="zoom:22%;" />

실제 트리는 아래와 같이 그릴 수 있다.

<img src="세그먼트 트리(Segment tree).assets/tree3.png" alt="tree3" style="zoom:22%;" />



배열을 반씩 나누어 구간을 저장하게 되므로 

- 트리의 높이는 `ceil( log2(배열의 크기) )+ 1`이 된다.

- $$
  2^{m-1} < \text{배열의 크기} \leq 2^{m}
  $$

  라고 하면 트리의 높이는 `m + 1` 이다.

따라서 전체 트리의 크기는 
$$
1 + 2 + 4 + \cdots + 2^{m} = 2^{m+1}-1
$$
이다.

보통 트리를 위해 4*n의 공간을 마련하는 방법을 사용하기도 한다.

- 왜냐면
  $$
  2^{m-1} < n \Rightarrow 2^{m+1} < 4n
  $$

## 세그먼트 트리 생성

세그먼트 트리의 생성은 재귀로 구현할 수 있다.

```python
# n: 배열의 크기
# arr: 배열

# 세그먼트 트리 생성
# 트리의 node번째 노드에 start부터 end까지의 구간 정보를 저장.
def init_tree(start, end, node):
    if start == end:
        tree[node] = arr[start]
        return tree[node]
    
    mid = (start + end) // 2
    tree[node] = init(start, mid, node * 2) + init(mid + 1, end, node * 2 + 1)
    return tree[node]

tree = [None] * (4 * n)
init_tree(0, n - 1, 1)
```



## 구간 합 구하기

위의 배열 `Arr = [6, 3, 2, 7, 1, 5]`에서 2번째 인덱스부터 4번째 인덱스의 합을 구한다고 생각해보자.

즉, 2 + 7 + 1을 구하고 싶다면, 아래 그림과 같이 세그먼트 트리의 5번 노드와 6번 노드를 더해야 한다는 사실을 알 수 있다. 

 <img src="세그먼트 트리(Segment tree).assets/tree4.png" alt="tree4" style="zoom:22%;" />

5번, 6번 노드를 찾는 방법은 **목표 구간에 포함되는 구간만을 찾으면 된다.**

위 그림의 총 11개의 노드 중 노드에 저장되어 있는 구간이 목표 구간인 [2, 7, 1] 에 포함되는 구간은 5번과 6번 노드의 구간뿐이다.

좀 더 구체적으로는 아래와 같다.

목표 구간을 들고 루트 노드부터 찾아간다. 그리고 아래를 반복한다.

- 만약 노드에 저장되어 있는 구간이 목표 구간에 포함된다면, ( `노드 저장 구간 ⊂ 목표 구간` )
  - 해당 노드에 저장되어있는 구간의 합을 반환한다.
- 만약 노드에 저장되어 있는 구간과 목표 구간이 겹치지 않는다면, (`노드 저장 구간 ∩ 목표 구간 = 0` )
  - 0을 반환한다.
- 위의 두 경우가 아니라면, 즉 노드에 저장되어 있는 구간의 일부가 목표 구간에 포함된다면, 
  - 목표 구간을 들고 노드의 왼쪽 자식과 오른쪽 자식을 찾아간다.

요약하자면, 트리를 탐색하면서 트리의 노드에 저장되어 있는 구간이 목표 구간에 포함될 때까지 탐색을 진행하면 된다.

구간 합도 마찬가지로 재귀로 구현할 수 있다.

```python
# n: 배열의 크기
# arr: 배열

# start: 현재 노드에 저장되어 있는 구간의 시작 인덱스
# end : 현재 노드에 저장되어 있는 구간의 끝 인덱스
# node: 현재 노드 번호
# left: 구간 합을 찾고자 하는 구간의 시작 인덱스
# right : 구간 합을 찾고자 하는 구간의 끝 인덱스
def sum_segment(start, end, node, left, right):
    if (left > end) or (right < start):  # 목표 구간을 아예 벗어난 경우
        return 0
    if (left <= start) and (end <= right):  # 목표 구간에 포함되는 경우
        return tree[node]
    
    mid = (start + end) // 2
    result = sum_segment(start, mid, node * 2, left, right) +\
         sum_segment(mid + 1, end, node * 2 + 1, left, right)
        
    return result
```



## 배열의 일부 변경하기

도중에 배열의 어떤 수를 변경한다면, 그 숫자가 포함된 구간을 저장한 노드를 모두 변경해주면 된다.

위와 비슷하게 목표 인덱스가 노드에 저장되어있는 구간에 포함되어 있다면 변경하면 된다.

마찬가지로 재귀로 구현할 수 있다.

```python
# arr: 배열
# tree: 세그먼트 트리

# start: 현재 노드에 저장되어 있는 구간의 시작 인덱스
# end: 현재 노드에 저장되어 있는 구간의 끝 인덱스
# node: 현재 노드
# index: 바꾸고자 하는 인덱스
# diff: 변경되는 값, (목표값) - (원래 값)
def update(start, end, node, index, diff):
    if not (start <= index <= end):
        return
    tree[node] += diff
    if start == end:
        return
    mid = (start + end) // 2
    update(start, mid, node * 2, index, dif)
    update(mid + 1, end, node * 2 + 1, index, dif)
```

