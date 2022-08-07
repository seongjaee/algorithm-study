n = int(input())
x_blank = " " * (n - 2)

print("*" * n + " " * (2 * n - 3) + "*" * n)
for i in range(1, n - 1):
    side_blank = " " * i
    center_blank = " " * (2 * (n - i) - 3)
    print(side_blank + "*" + x_blank + "*" + center_blank + "*" + x_blank + "*")

print(" " * (n - 1) + "*" + x_blank + "*" + x_blank + "*")

for i in range(n - 2, 0, -1):
    side_blank = " " * i
    center_blank = " " * (2 * (n - i) - 3)
    print(side_blank + "*" + x_blank + "*" + center_blank + "*" + x_blank + "*")

print("*" * n + " " * (2 * n - 3) + "*" * n)
