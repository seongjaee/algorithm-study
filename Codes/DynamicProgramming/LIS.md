# LIS, Longest Increasing Subsequence

## :bread: 설명​

>  [최장 증가 부분 수열](https://ko.wikipedia.org/wiki/%EC%B5%9C%EC%9E%A5_%EC%A6%9D%EA%B0%80_%EB%B6%80%EB%B6%84_%EC%88%98%EC%97%B4)

수열 arr가 주어졌을 때, 가장 긴 증가하는 부분 수열의 길이를 구하는 문제.

부분 수열 : 수열의 일부 항을 **원래 순서대로** 나열하여 얻을 수 있는 수열



## :cookie: 코드

### 동적 프로그래밍만을 이용하는 방법

L(i) 를 arr[i]를 마지막 원소로 하는 최장 증가 부분 수열의 길이라고 했을 때, 다음과 같은 점화식을 얻을 수 있다.

$$
L(i) = 
\begin{cases}
1 + \text{max}(L(j)), \text{  where } j < i & arr[j] < arr[i]\\
1, \text{  if no such j exists}
\end{cases}
$$
L(i) 는 arr[j] < arr[i] 이고 j < i 인 j들에 대해, 1 + max(L(j)) 이다.

점화식을 이해해보자.

arr[i]를 마지막 원소로 하는 증가 수열이므로 i보다 앞에 있는 값들은 모두 arr[i]보다 작아야한다.

그러니 i보다 앞에 있고, arr[i]보다 작은 값을 갖는 인덱스  j들 중에 arr[j]를 마지막 원소로 하는 최장 증가 부분 수열을 찾아준 다음, 뒤에 arr[i]를 붙여주면 된다.

점화식을 코드로 옮기면 다음과 같다.

```python
# n : 수열의 길이
# arr :주어진 수열

L = [1 for _ in range(n)]  # LIS 저장 배열, 모두 1로 초기화

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            L[i] = max(L[i], L[j]+1)
           
print(max(L))
```

### 이분 탐색을 이용하는 방법

> 완벽하게 이해 못함 :face_with_thermometer:

arr를 탐색하면서 증가 수열 L을 만들어 나간다.

arr[i]를 수열의 뒤에 붙일 수 있다면(L의 마지막값보다 크다면) 뒤에 붙인다.

뒤에 붙일 수 없다면 이분 탐색을 통해 arr[i]의 적당한 인덱스를 구하고 기존값과 "바꾸어" 넣는다.

최종적으로 얻는 L의 길이가 LIS의 길이지만, L이 부분 수열이 아닐 수도 있다.

우리가 얻는 L은 정렬이 된 상태이기 때문에 원래 arr에서 순서가 바뀌어 있을 수 있다.

 밑의 코드에서는 이분 탐색을 위해 [bisect 모듈](https://docs.python.org/ko/3/library/bisect.html)을 이용한다.

```python
import bisect

# n : 수열의 길이
# arr :주어진 수열

L = [arr[0]]

for i in range(n):
    if arr[i] > L[-1]:
        L.append(arr[i])
    else:
        idx = bisect.bisect_left(L, arr[i])
        L[idx] = arr[i]
        
print(len(L))
```

## BOJ

### BOJ 11053 : 가장 긴 증가하는 부분 수열

[BOJ 11053 : 가장 긴 증가하는 부분 수열](https://www.acmicpc.net/problem/11053)

