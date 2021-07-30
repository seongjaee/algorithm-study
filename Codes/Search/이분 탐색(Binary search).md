# 이분 탐색, Binary search

## 설명

**정렬**(오름차순)된 리스트에서 특정한 값의 위치를 찾을 때 사용하는 알고리즘

중간에 있는 값(`mid`)와 찾고자 하는 값의 크기를 비교해서 찾아가는 방식이다.

`left = 0`, `right = len(array)-1`로 두고 `mid = (left + right) // 2`로 정한다.

중간에 있는 값(`mid`)이 찾고자 하는 값보다 크면 `mid` 가 새로운 `right`가 되고,

중간에 있는 값(`mid`) 이 찾고자 하는 값보다 작으면 `mid` 가 새로운 `left`가 된다.

## 주의할 점

시간 복잡도 : O(log N)

리스트가 정렬되어있을 때만 사용할 수 있다!

## 코드

### 재귀로 구현한 이분 탐색

```python
def binarySearch(array, value, left, right):
    if left > right:
        return False
    mid = (left + right) // 2
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
        mid = (left + right) // 2
        if array[mid] > value:
            right = mid - 1
        elif array[mid] < value:
            left = mid + 1
        else:
            return mid
    return False
```

#### 그림으로 살펴보기

`array = [1, 2, 5, 8, 9, 12, 15, 23, 27]`, 찾고자 하는 값이 `8`인 경우.

처음의 `mid = 4`고, `array[mid] = 3` 이다.

![image](이분 탐색(Binary search).assets/그림8-16276454076121.png)

`array[mid]`가 `8`보다 크므로 `right = mid - 1`이 되고, 다시 `mid`를 계산하면 아래 그림과 같다.

![image](이분 탐색(Binary search).assets/그림9-16276454241722.png)

`mid = 1`고, `array[mid] = 2`이다.

`array[mid]`가 `8`보다 작으므로 `left = mid + 1`이 되고, 다시 `mid`를 계산하면 아래 그림과 같다.

![image](이분 탐색(Binary search).assets/그림10-16276454296253.png)

`mid = 2`고, `array[mid] = 5`이다. 

`array[mid]`가 `8`보다 작으므로 `left = mid + 1`이 되고, `left == right`이 된다.



![image](이분 탐색(Binary search).assets/그림12-16276454351564.png)

`mid = 3`이고 `array[mid] = 8` 이므로 원하는 값을 찾았다!

따라서 인덱스 3이 반환된다.





---

<br/>

---

## Moreover

찾고자 하는 값이 리스트에 여러 개 존재하는데,

1. 그 중 **가장 작은 index**를 구해야하는 경우와

2. 그 중 **가장 큰 index**를 구해야하는 경우가

있을 수 있다.



위에 써놓은 코드는 찾고자 하는 값이 여러 개 있으면 그 중 어떤 index를 가져올 지 알 수 없고,

리스트 내에 찾고자 하는 값이 없으면 `False` 를 반환한다.



### 가장 큰 index를 구해야하는 경우

- 찾고자 하는 값 중 가장 오른쪽에 있는 index를 반환
- 만약 찾고자 하는 값이 없으면 찾고자 하는 값보다 작으면서 가장 오른쪽에 있는 index를 반환

```python
def binarySearch(array, value, left, right):
    while left < right:
        mid = (left + right) // 2
        if array[mid] > value:
            right = mid
        else:
            left = mid + 1
    return left - 1
```

위와 같이 `array[mid]` 와 `value` 가 같을 때도 `left`를 키워서 오른쪽을 더 탐색해본다.

최종적으로 `left == right`가 됐을 때,  `left - 1`을 반환한다.

찾고자 하는 값이 여러 개 있을 때, 찾고자 하는 값의 인덱스 중 하나를 찾고 `right`는 고정해두고

`left`를 조금씩 오른쪽으로 옮겨보면서 "이래도 찾고자 하는 값이야?" 하는 느낌이다.

#### 그림으로 살펴보기

`array = [1, 2, 2, 3, 3, 3, 4, 4, 5]`, 찾고자 하는 값이 `3`인 경우.

처음의 `mid = 4`고, `array[mid] = 3` 이다.

![image](이분 탐색(Binary search).assets/그림1-16276454421415.png)

`array[mid]`의 값이 더 작거나 같으니까 `right = mid - 1` 이고, 다음 `mid`까지 구해보면 밑의 그림과 같다.

![image](이분 탐색(Binary search).assets/그림5-16276454473576.png)

`mid = 6`이고 `array[mid] = 4`이다.

 `array[mid]`값이 `3`보다 크므로 `right = mid`가 되고, `mid`를 계산하면 `mid`는 `left`와 같아진다.

![image](이분 탐색(Binary search).assets/그림6-16276454525087.png)

`mid = 5`이고 `array[mid] = 3`이다.

 `array[mid]`이  `3`보다 작거나 같으므로 `left = mid + 1`이 되서 `left == right`가 된다.

![image](이분 탐색(Binary search).assets/그림7-16276454571468.png)

이제 반복문의 종료 조건이므로 `left - 1`이 반환된다. 즉 인덱스 `5`가 반환된다.





### 가장 작은 index를 구해야하는 경우

- 찾고자 하는 값 중 가장 왼쪽에 있는 index를 반환
- 만약 찾고자 하는 값이 없으면 찾고자 하는 값보다 크면서 가장 왼쪽에 있는 index를 반환

```python
def binarySearch(array, value, left, right):
    while left < right:
        mid = (left + right + 1) // 2
        if array[mid] >= value:
            right = mid - 1
        else:
            left = mid
    return right + 1
```

바로 위의 코드랑 살짝 다른 점은 `mid`를 `(left + right + 1)//2`로 잡았다.

만약 `left`와 `right`가 1 차이가 났을 때 `mid = right`로 구하게 만들었다.



#### 그림으로 살펴보기

`array = [1, 2, 2, 3, 3, 3, 4, 4, 5]`, 찾고자 하는 값이 `3`인 경우.

처음의 `mid = 4`고, `array[mid] = 3` 이다.

![image](이분 탐색(Binary search).assets/그림1-16276454626119.png)

 `array[mid]`의 값이 더 크거나 같으니까 `right = mid - 1` 이고, 다음 `mid`까지 구해보면 밑의 그림과 같다.



![image](이분 탐색(Binary search).assets/그림2-162764546752310.png)

이번엔 `mid = 2` 이고 `array[mid] = 2`이다.

`array[mid]`의 값이 더 작으니까 `left = mid`가 된다.

![image](이분 탐색(Binary search).assets/그림3-162764547249111.png)

`mid = (left + right + 1) // 2`를 계산하면 `mid`는 `right`와 같아진다.

 `array[mid]`의 값이 더 크거나 같으니까 `right = mid - 1` 이고, 그럼 `left == right`가 된다.

![image](이분 탐색(Binary search).assets/그림4-162764547665212.png)



이제 반복문의 종료 조건을 만족하므로 `right + 1`, 즉 인덱스 `3`이 반환된다.