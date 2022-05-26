# 분할 정복을 이용한 거듭제곱

a의 n제곱을 구할 때, `a**n` 으로 계산하면 O(N)이다.

분할 정복을 이용해 O(logN)으로 구할 수 있다.

n이 짝수일 땐, a^n = a^(n/2) * a^(n/2),

n이 홀수일 땐, a^n = a^((n-1)/2) * a^((n-1)/2) * a

임을 이용한다.

## :cookie: 코드

### 반복문을 이용한 방법

```python
def power(a, k):
    ans = 1
    while k >0:
        if k%2 ==1:
            ans *= a
        a *= a
        k //= 2
    return ans
```

### 재귀를 이용한 방법

```python
def power(a, k):
    if k == 1:
        return C
    x = power(a, k//2)
    if n % 2 == 0:
        return x * x
    else:
        return x * x * C
```



## 행렬 제곱

```python
# 같은 크기의 정사각행렬 A, B 곱셈 정의
def matrix_product(A, B):
    n = len(A)
    result = [[0]*n for _ in range(n)]
    for i in range(n):
        for j in range(n):
            A_ith_row = [x for x in A[i]]  # 행렬 A의 i번째 행
            B_jth_col = [y[j] for y in B]  # 행렬 B의 j번째 열
            for idx in range(n):
                result[i][j] += A_ith_row[idx] * B_jth_col[idx]
	return result

# 정사각행렬 A의 m 제곱
def matrix_square(A, m):
    I = [[int(i == j) for i in range(n)] for j in range(n)]  # 단위행렬
    while m > 0:
        if m % 2 == 1:
            I = matrix_product(I, A)
        A = matrix_product(A, A)
        m //= 2
        
   return I
```
