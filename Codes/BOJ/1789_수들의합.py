s = int(input())

def sum1tok(k):
    return k * (k + 1) // 2

now = 1
while True:
    if sum1tok(now) > s:
        break
    now += 1
print(now - 1)
