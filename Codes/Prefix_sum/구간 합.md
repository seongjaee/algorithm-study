# 구간 합



주어진 수열에서 i번째 값부터 j번째 값까지의 합을 구간 합(Prefix sum)이라고 한다.

반복문을 이용해 i부터 j까지 더하는 건 O(N)이다.

가능한 모든 구간 합을 구해야 한다면 O(N^2)이 걸린다.



따라서 구간 합을 여러번 구해야하는 경우는 구간 합 알고리즘을 이용한다.



## 구간 합 알고리즘

- 주어진 수열의 누적 합을 미리 계산해둔다.

  예를 들어, seq = [3, -2, -4, -9, 0, 3, 7, 13, 8, -3] 와 같은 수열이 있다면,

  psum = [0, 3, 1, -3, -12, -12, -9, -2, 11, 19, 16]을 구한다.

  

- i번째 값부터 j번째 값 까지의 합을 구하려면,

  psum[j+1] - psum[i] 으로 한 번에 계산할 수 있다.

  예를 들어 seq의 2번째 인덱스인 -4 부터 6번째 인덱스인 7까지의 합을 구하려면

  psum[6+1] - psum[2] = -2 - 1 = -3 이다.



## BOJ 2559번 : 수열

[BOJ 2559번 : 수열](https://www.acmicpc.net/problem/2559)

```python
import sys
input = sys.stdin.readline

n, k = map(int, input().split())
temper = list(map(int, input().split()))

psum = [0]
now = 0
for i in range(n):
    now += temper[i]
    psum.append(now)

result = -10000001
for j in range(n-k+1):
    result = max(result, psum[j+k]-psum[j])

print(result)
```

