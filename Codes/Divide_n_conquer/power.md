# 분할 정복을 이용한 거듭제곱

a의 n제곱을 구할 때, `a**n` 으로 계산하면 O(N)이다.

분할 정복을 이용해 O(logN)으로 구할 수 있다.

n이 짝수일 땐, a^n = a^(n/2) * a^(n/2),

n이 홀수일 땐, a^n = a^((n-1)/2) * a^((n-1)/2) * a

임을 이용한다.

반복문을 이용한 방법
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

재귀를 이용한 방법
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
