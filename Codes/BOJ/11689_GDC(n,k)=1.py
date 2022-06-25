n = int(input())

is_primes = [True] * (10**6 + 1)
for i in range(2, 10**6):
    if is_primes[i]:
        for j in range(2 * i, 10**6 + 1, i):
            is_primes[j] = False

divs = []
m = n
for i in range(2, int(n**0.5) + 1):
    if m % i == 0:
        if is_primes[i]:
            divs.append(i)
            while m % i == 0:
                m //= i

if n == 1:
    print(1)

elif divs:
    answer = n
    for p in divs:
        answer *= p - 1
    for p in divs:
        answer //= p
    if m != 1:
        answer *= m - 1
        answer //= m
    print(answer)

else:
    print(n - 1)
