n = int(input())
for i in range(n - 1, -1, -1):
    print(" " * (n - 1 - i) + "*" * (2 * i + 1))
