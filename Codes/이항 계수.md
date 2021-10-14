# 이항 계수

## 이항 계수란

$$
{n \choose k} :  (1 + x)^n \text{ 를 전개했을 때  } x^{k} \text{의 계수}
$$

라서 이항 계수.

계산하는 방법은
$$
{n \choose k} =\cfrac{n!}{k!(n-k)!}= \cfrac{n(n-1)\cdots(n-k+1)}{1\cdot2\cdot\cdots k}
$$
로 계산할 수 있지만, 보통 n이나 k가 너무 크면 팩토리얼 계산이 힘들다.

그래서 동적 계획법, 메모이제이션 등을 활용한다.

이때 이항 계수의 성질을 활용하는데, 다음과 같다.
$$
{n \choose k} =  {n-1 \choose k} + {n-1 \choose k-1}
$$

> 숫자 1 ~ n 중에서 k개의 숫자를 고르는 방법의 수는, 
>
> n을 안 고르고 1 ~ n-1 중 k개를 고르는 방법 +
>
> n을 고르고 나머지 1 ~ n-1 중 k - 1개를 고르는 방법
>
> 과 같다.





## 계산

### 1. 재귀 함수

```python
def combination(n, k):
    k = min(k, n - k)
    if k == 0: return 1
    return combination(n - 1, k) + combination(n - 1 , k - 1)
```

여기에 메모이제이션을 활용하면,

```python
memo = {(1, 0): 1, (1, 1): 1}

def combination(n, k):
    if (n, k) in memo: return memo[(n, k)]
    k = min(k, n - k)
    if k == 0: return 1
    memo[(n, k)] = combination(n - 1, k) + combination(n - 1 , k - 1)
    return memo[(n, k)]
```



### 2. 반복문

```python
memo = [[0] * (k + 1) for _ in range(n + 1)]

def combination(n, k):
    if memo[n][k]: return memo[n][k]
    for i in range(n + 1):
        for j in range(min(i, k) + 1):
            if j == 0 or j == i:
                memo[i][j] = 1
            else:
                memo[i][j] = memo[i - 1][j] + memo[i - 1][j - 1]
    return memo[n][k]
```

``` python
def combination(n, k):
    k = min(k, n - k)
    if k == 0: return 1
    denom = n
    numer = 1
    for i in range(1, k):
        denom *= n - i
        numer *= i + 1
    return denom // numer
```



### 3. 모듈러

- 보통 n이 커지면 이항 계수가 많이 커지면서 모듈러 연산을 해야할 때가 있는데,

  이 때 소수로 나눈 나머지를 구해야하는 경우 페르마의 작은 정리를 쓸 수 있다.

- `pow(a, n, mod)` : a의 n제곱을 mod로 나눈 나머지 반환

```python
def combination(n, k, p):  # p: n C r을 p로 나눈 나머지를 구한다!
    k = min(k, n - k)
    if k == 0: return 1
    denom = n
    numer = 1
    for i in range(1, k):
        denom = denom * (n - i) % p
        numer = numer * (i + 1) % p
    return denom * pow(numer, p - 2, p) % p
```



- [뤼카 정리](https://ko.wikipedia.org/wiki/%EB%A4%BC%EC%B9%B4%EC%9D%98_%EC%A0%95%EB%A6%AC)도 이용할 수 있다!

```python
def combination(n, k, p):  # p: n C r을 p로 나눈 나머지를 구한다!
    k = min(k, n - k)
    if k == 0: return 1
    denom = n
    numer = 1
    for i in range(1, k):
        denom = denom * (n - i) % p
        numer = numer * (i + 1) % p
    return denom * pow(numer, p - 2, p) % p


def lucas(n, k):
    # 숫자 n을 p진법으로 나타냄
    np = []
    while n > 0:
        np.append(n % p)
        n //= p
    # 숫자 k를 p진법으로 나타냄
    kp = []
    while k > 0:
        kp.append(k % p)
        k //= p
    # 길이를 맞춰줌
    kp = kp + [0] * (len(np) - len(kp))
    
    # 각 자리마다 이항 계수를 구해 곱해줌
    result = 1
    for i in range(len(np)):
        result =  result * combination(np[i], kp[i], p) % p
    return result
```



