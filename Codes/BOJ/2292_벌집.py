n = int(input())

i = 0
while True:
    if n <= 3 * i * i + 3 * i + 1:
        break
    i += 1

print(i + 1)

# 두번째 풀이
n = int(input())

i = 1
x = 1

while x < n:
    x += i * 6
    i += 1

print(i)
