def f(k):
    if memo[k]:
        return memo[k]
    if k == 2:
        return (0, 1)
    if k == 1:
        return (1, 0)

    temp1 = f(k - 1)
    temp2 = f(k - 2)
    memo[k] = (temp1[0] + temp2[0], temp1[1] + temp2[1])
    return memo[k]


d, k = map(int, input().split())
memo = [0] * (d + 1)
a, b = f(d)

for i in range(k // b, -1, -1):
    A, B = (k - b * i) // a, i
    if (k - b * i) % a == 0 and 0 < A <= B:
        print(A)
        print(B)
        break
