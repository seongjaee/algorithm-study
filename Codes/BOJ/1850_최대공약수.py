def gcd(a, b):
    a, b = max(a, b), min(a, b)

    while True:
        _, r = divmod(a, b)
        if r == 0:
            return b
        a, b = b, r


a, b = map(int, input().split())

print(gcd(a, b) * "1")
