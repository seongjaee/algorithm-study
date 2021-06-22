## LIS

### 최장 증가 부분 수열의 길이

수열 arr가 주어졌을 때, 가장 긴 증가하는 부분 수열의 길이를 구하는 프로그램을 작성하시오.

#### 동적 프로그래밍만을 이용하는 방법

L(i) 를 arr[i]를 마지막 원소로 하는 증가 부분 수열의 길이라고 했을 때, 다음과 같은 점화식을 얻을 수 있다.

L(i) = 1 +max ( L( j ) ) , where j < i & arr[ j ] < arr[ i ]
or  
L(i) = 1, if no such j exists.

```
n = int(input())                       # 수열의 길이
arr = list(map(int, input().split()))  # 주어진 수열

L = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if arr[j] < arr[i]:
            L[i] = max(L[i], L[j]+1)
           
print(max(L))
```


#### 이분 탐색을 이용하는 방법

arr를 탐색하면서 증가 수열 L을 만들어 나간다.

arr[i]를 수열의 뒤에 붙일 수 있다면(L의 마지막값보다 크다면) 뒤에 붙인다.

뒤에 붙일 수 없다면 이분 탐색을 통해 arr[i]의 적당한 인덱스를 구하고 기존값과 바꾸어 넣는다.

최종적으로 얻는 L의 길이가 LIS의 길이지만, L이 부분 수열이 아닐 수도 있다.

```
import bisect

n = int(input())                        # 수열의 길이
arr = list(map(int, input().split()))   # 주어진 수열

L = [arr[0]]

for i in range(n):
    if arr[i] > L[-1]:
        L.append(arr[i])
    else:
        idx = bisect.bisect_left(L, arr[i])
        L[idx] = arr[i]
        
print(len(dp))
```
