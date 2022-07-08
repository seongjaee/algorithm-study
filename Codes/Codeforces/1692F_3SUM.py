import sys

input = sys.stdin.readline


def check():
    A = [
        (0, 1, 2),
        (0, 4, 9),
        (0, 5, 8),
        (0, 6, 7),
        (1, 3, 9),
        (1, 4, 8),
        (1, 5, 7),
        (2, 3, 8),
        (2, 4, 7),
        (2, 5, 6),
        (3, 4, 6),
        (6, 8, 9),
    ]
    B = [
        (0, 3),
        (6, 1),
        (2, 9),
        (3, 7),
        (5, 3),
        (4, 5),
        (9, 5),
        (7, 9),
        (8, 7),
    ]

    for a, b, c in A:
        if counter.get(a, 0) >= 1 and counter.get(b, 0) >= 1 and counter.get(c, 0) >= 1:
            return True

    for a, b in B:
        if counter.get(a, 0) >= 2 and counter.get(b, 0) >= 1:
            return True

    if counter.get(1, 0) >= 3:
        return True

    return False


t = int(input())
for _ in range(t):
    n = int(input())
    numbers = [*map(int, input().split())]
    counter = {}
    for num in numbers:
        x = num % 10
        counter[x] = counter.get(x, 0) + 1

    print("YES" if check() else "NO")
