# 이분 탐색(Binary search)

오름차순으로 정렬된 리스트에서 특정한 값의 위치를 찾는 알고리즘.

처음 중간의 값(`mid`)을 임의의 값으로 선택하여, 그 값과 찾고자 하는 값의 크고 작음을 비교하는 방식.

중간값(`mid`) 이 찾고자 하는 값보다 크면 `mid` 가 새로운 `right`가 되고,

중간값(`mid`) 이 찾고자 하는 값보다 작으면 `mid` 가 새로운 `left`가 된다.

정렬되어있을 때만 사용할 수 있다는 단점이 있다.

O(log N)

## 코드

### 재귀로 구현한 이분 탐색

```python
def binarySearch(array, value, left, right):
    if left > right:
        return False
    mid = (left+right) // 2
    if array[mid] > value:
        return binarySearch(array, value, left, mid-1)
    elif array[mid] < value:
        return binarySearch(array, value, mid+1, right)
    else:
        return mid
```



### 반복문으로 구현한 이분 탐색

```python
def binarySearch(array, value, left, right):
    while left <= right:
        mid = (left+right) // 2
        if array[mid] > value:
            right = mid - 1
        elif array[mid] < value:
            left = mid + 1
        else:
            return mid
    return False
```



## 좀 더 

찾고자 하는 값이 리스트에 여러 개 존재하는데,

1. 그 중 **가장 작은 index**를 구해야하는 경우와

2. 그 중 **가장 큰 index**를 구해야하는 경우가

있을 수 있다.



위의 코드는 찾고자 하는 값이 여러 개 있으면 그 중 어떤 index를 가져올 지 알 수 없고,

리스트 내에 찾고자 하는 값이 없으면 `False` 를 반환한다.



### 가장 큰 index를 구해야하는 경우

- 찾고자 하는 값 중 가장 오른쪽에 있는 index를 반환
- 만약 찾고자 하는 값이 없으면 찾고자 하는 값보다 작으면서 가장 오른쪽에 있는 index를 반환

```python
def binarySearch(array, value, left, right):
    while left < right:
        mid = (left+right) // 2
        if array[mid] > value:
            right = mid
        else:
            left = mid + 1
    return left - 1
```

위와 같이 `array[mid]` 와 `value` 가 같을 때도 `left`를 키워서 오른쪽을 더 탐색해본다.

 최종적으로 `left == right`가 됐을 때,  `left - 1`을 반환한다.





### 가장 작은 index를 구해야하는 경우

- 찾고자 하는 값 중 가장 왼쪽에 있는 index를 반환
- 만약 찾고자 하는 값이 없으면 찾고자 하는 값보다 크면서 가장 왼쪽에 있는 index를 반환

```python
def binarySearch(array, value, left, right):
    while left < right:
        mid = (left+right+1) // 2
        if array[mid] >= value:
            right = mid - 1
        else:
            left = mid
    return right + 1
```

`mid`를 `(left+right+1)//2`로 잡아서 만약 `left`와 `right`가 1 차이가 났을 때 `mid = right`로 구하게 만들었다.

최종적으로 `left == right`가 됐을 때, `right + 1`을 반환한다.



