n = int(input())
cars = [*map(int, input().split())]
print(len(list(filter(lambda i: i == n, cars))))
